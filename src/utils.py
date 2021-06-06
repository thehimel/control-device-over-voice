import sys
import pyautogui


def screenshot():
    try:
        # Hold the windows left, press the print screen, and
        # release the windows left.
        pyautogui.keyDown('winleft')
        pyautogui.press('printscreen')
        pyautogui.keyUp('winleft')
        print("Taken screenshot.")
    except Exception as e:
        print(e)
        print("Screenshot could not be taken.")


def exit_program():
    # Exit the program.
    print("See you soon!")
    sys.exit()


def process_text(text):
    if "capture" in text:
        print("Taking screenshot.")
        screenshot()

    if "exit now" in text:
        exit_program()
