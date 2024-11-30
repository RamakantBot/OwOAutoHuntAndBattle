import time
import pyautogui

# -------------------------------------------------------------------------------

def main():
    print("press 'Ctrl+c' to stop the code.")
    time.sleep(5)
    custom()
    time.sleep(5)
    hunt()
    time.sleep(5)
    battle()

# -------------------------------------------------------------------------------

def custom():
    pyautogui.write(str(":P"), interval = 0.1)
    pyautogui.press('enter')

def hunt():
    pyautogui.write(str("owo h"), interval = 0.1)
    pyautogui.press('enter')

def battle():
    pyautogui.write(str("owo b"), interval = 0.1)
    pyautogui.press('enter')

# -------------------------------------------------------------------------------

while True:
    main()
