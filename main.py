# --------------------------------------------
# ---- // Piano Tiles Bot
# Made by @cuh5_ (Discord)

# Built for http://tanksw.com/piano-tiles/ (rush mode). Scroll to top of page with average zoom level.

# --------------------------------------------

# ------------------- // Imports
import cuhUtils
import columns
import pyautogui
import keyboard

import win32api, win32con, time # for clicking

# ------------------- Functions
def click(pos: cuhUtils.vec.vector2):
    # get cursor in position
    win32api.SetCursorPos((pos.x, pos.y))

    # click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# ------------------- // Main
# ---- // Construct Columns
# -- 1
columns.column(
    cuhUtils.vec.vector2(800, 740), cuhUtils.color.rgb(17, 17, 17), "a"
)

# -- 2
columns.column(
    cuhUtils.vec.vector2(900, 740), cuhUtils.color.rgb(17, 17, 17), "s"
)

# -- 3
columns.column(
    cuhUtils.vec.vector2(1000, 740), cuhUtils.color.rgb(17, 17, 17), "d"
)

# -- 4
columns.column(
    cuhUtils.vec.vector2(1100, 740), cuhUtils.color.rgb(17, 17, 17), "f"
)

# ---- // Bot
def start():
    while True:
        # fail-safe
        if keyboard.is_pressed("q"):
            return
        
        # detection
        for column in columns.recognisedColumns:
            # tile is not in position, so check next
            if not pyautogui.pixelMatchesColor(column.pos.x, column.pos.y, column.targetColor.unpack()):
                continue
            
            # tile is in position, so press key responsible for tile
            pyautogui.press(column.key)
            # click(column.pos) # too slow
        
# start on key press
while True:
    if keyboard.is_pressed("e"):
        start()
        break # end this loop if function above is finished