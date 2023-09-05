# --------------------------------------------
# ---- // [Module] Decorator Threads
# --------------------------------------------

# ---- // Imports
import threading

# ---- // Functions
def thread(func):
    created = threading.Thread(target=func)
    created.start()
    
    return created