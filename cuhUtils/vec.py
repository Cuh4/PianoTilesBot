# --------------------------------------------
# ---- // [Module] Vector
# --------------------------------------------

# no idea why i made this i don't know vector math whatsoever

# ---- // Classes
class vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        
    def __add__(self, vec: "vector2"):
        return vector2(self.x + vec.x, self.y + vec.y)
    
    def __sub__(self, vec: "vector2"):
        return vector2(self.x - vec.x, self.y - vec.y)
    
    def __truediv__(self, vec: "vector2"):
        return vector2(self.x / vec.x, self.y / vec.y)
    
    def __mul__(self, vec: "vector2"):
        return vector2(self.x * vec.x, self.y * vec.y)