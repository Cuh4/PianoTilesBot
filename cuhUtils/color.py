# --------------------------------------------
# ---- // [Module] Color
# --------------------------------------------

# ---- // Classes
class rgb:
    def __init__(self, r: float = 255, g: float = 255, b: float = 255):
        self.r = r
        self.g = g
        self.b = b
        
    def unpack(self):
        return self.r, self.g, self.b
    
    def __eq__(self, color: "rgb"):
        return self.unpack() == color.unpack()