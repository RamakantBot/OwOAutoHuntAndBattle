import time
import pyautogui

# --------------------------------------------------------------------------------

def main():
    print( i, ". Press 'Ctrl+c' to stop the code.")
    time.sleep(t)
    custom()
    time.sleep(t)
    hunt()
    time.sleep(t)
    battle()

# -------------------------------------------------------------------------------

def custom():
    pyautogui.write(str("rp"), interval = 0.2)
    pyautogui.press('enter')

def hunt():
    pyautogui.write(str("owo h"), interval = 0.2)
    pyautogui.press('enter')

def battle():
    pyautogui.write(str("owo b"), interval = 0.2)
    pyautogui.press('enter')

# -------------------------------------------------------------------------------

i = 1
t = 5

while True:
    main()
    i = i + 1
