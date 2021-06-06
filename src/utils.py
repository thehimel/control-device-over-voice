import sys
import pyautogui


def action(button, name):
    try:
        pyautogui.press(button)
        print(f"{name} performed.")
    except Exception as e:
        print(e)
        print(f"{name} could not be performed.")


def screenshot():
    try:
        # Hold the windows left, press the print screen, and
        # release the windows left.
        pyautogui.hotkey('winleft', 'printscreen')
        print("Screenshot taken.")
    except Exception as e:
        print(e)
        print("Screenshot could not be taken.")


def exit_program():
    # Exit the program.
    print("See you soon!")
    sys.exit()


def process_text(text):
    if "capture" in text:
        screenshot()

    elif 'play' in text or 'pause' in text:
        action(button='playpause', name="Play / Pause")

    elif 'next' in text:
        action(button='nexttrack', name="Next")

    elif 'previous' in text:
        action(button='prevtrack', name="Previous")

    elif 'volume up' in text:
        action(button='volumeup', name="Volume Up")

    elif 'volume down' in text:
        action(button='volumedown', name="Volume Down")

    elif 'volume mute' in text:
        action(button='volumemute', name="Volume Mute")

    elif "exit now" in text:
        exit_program()
