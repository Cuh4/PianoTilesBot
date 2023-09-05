# --------------------------------------------
# ---- // [Module] Logging
# --------------------------------------------

# ---- // Imports
import datetime
import colorama as tcolor

tcolor.init()

# ---- // Functions
def _setup(title: str, msg: str, style: str, color: str):
    return f"{style}{color}[{title}] [{datetime.datetime.now()}]{tcolor.Fore.RESET} {msg}{tcolor.Style.RESET_ALL}"

def warn(msg: str):
    print(_setup("WARNING", msg, tcolor.Style.DIM, tcolor.Fore.LIGHTYELLOW_EX))

def info(msg: str):
    print(_setup("INFO", msg, tcolor.Style.DIM, tcolor.Fore.LIGHTBLACK_EX))
    
def error(msg: str):
    print(_setup("ERROR", msg, tcolor.Style.DIM, tcolor.Fore.LIGHTRED_EX))

def success(msg: str):
    print(_setup("SUCCESS", msg, tcolor.Style.DIM, tcolor.Fore.LIGHTGREEN_EX))
    
def inputQuery(msg: str):
    return input(_setup("INPUT", msg, tcolor.Style.DIM, tcolor.Fore.LIGHTBLUE_EX))