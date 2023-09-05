# --------------------------------------------
# ---- // [Module] Events
# --------------------------------------------

# ---- // Classes
class event:
    def __init__(self):
        self.events: dict[int, "handler"] = {}
        
    def attach(self, func):
        pos = len(self.events)

        attached = handler(
            pos,
            self,
            func
        )
        
        self.events[pos] = attached
        
    def fire(self, *args, **kwargs):
        returnValue = None

        for _, v in self.events.items():
            returnValue = v.call(*args, **kwargs)
            
        return returnValue
        
class handler:
    def __init__(self, pos: int, parent: event, callback):
        self.callback = callback
        self.pos = pos
        self.parent = parent
        
    def call(self, *args, **kwargs):
        return self.callback(*args, **kwargs)

    def detach(self):
        self.parent.events.pop(self.pos)