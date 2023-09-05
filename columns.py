# --------------------------------------------
# ---- // [Module] Columns
# --------------------------------------------

# ---- // Imports
import cuhUtils

# ---- // Variables
recognisedColumns: list["column"] = []

# ---- // Classes
class column:
    def __init__(self, pos: cuhUtils.vec.vector2, targetColor: cuhUtils.color.rgb, key: str):
        self.pos = pos
        self.targetColor = targetColor
        self.key = key
        
        recognisedColumns.append(self)