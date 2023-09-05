# --------------------------------------------
# ---- // Piano Tiles Bot
# Made by @cuh6_ (Discord)

# Built for http://tanksw.com/piano-tiles/ (rush mode). Scroll to top of page with average zoom level.

# --------------------------------------------

# ------------------- // Imports
import cuhUtils
import columns
import pyautogui
import keyboard

import win32api, win32con, time # for clicking

# ------------------- Variables
keyToStartEnd = "q"

# ------------------- Functions
def click(pos: cuhUtils.vec.vector2): # unused, using keybinds instead of clicking (faster, more accurate)
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
    time.sleep(0.5) # wait some time for user to release keyToStartEnd key

    while True:
        # stop bot
        if keyboard.is_pressed(keyToStartEnd):
            cuhUtils.logging.success("Stopped.")
            return # stop the function, get gone
        
        # detection
        for column in columns.recognisedColumns:
            # tile is not in position, so check next
            if not pyautogui.pixelMatchesColor(column.pos.x, column.pos.y, column.targetColor.unpack()):
                continue
            
            # tile is in position, so press key responsible for tile
            cuhUtils.logging.info(f"Tile ({column.pos.x}, {column.pos.y}) in position, pressing '{column.key.upper()}'")
            pyautogui.press(column.key)
            # click(column.pos) # too slow
        
# start on key press
cuhUtils.logging.info(f"Process started, press '{keyToStartEnd}' to start.")
while True:
    if keyboard.is_pressed(keyToStartEnd):
        cuhUtils.logging.success("Started.")

        start() # yield (pauses) the loop until the function is completed. this is because of the while loop up in the 'start' function
        break # end this loop if function above is finished