import sys
import pyautogui
import os


def action(button, name):
    """
    Action for pyautogui.
    :param button: str
    :param name: str
    :return: void
    """
    try:
        pyautogui.press(button)
        print(f"{name} performed.")
    except Exception as e:
        print(e)
        print(f"{name} could not be performed.")


def screenshot():
    """
    Take screenshot.
    :return: void
    """
    try:
        # Hold the windows left, press the print screen, and
        # release the windows left.
        pyautogui.hotkey('winleft', 'printscreen')
        print("Screenshot taken.")
    except Exception as e:
        print(e)
        print("Screenshot could not be taken.")


def shell_script(command):
    """
    Run a shell script.
    :param command: str
    :return: void
    """
    os.system(command)


def open_app(text):
    """
    Open an app.
    :param text: str
    :return: void
    """
    if 'chrome' in text:
        command = 'start chrome'
        shell_script(command=command)

    if 'notepad' in text:
        command = 'start notepad'
        shell_script(command=command)


def go_to(text):
    """
    Go to a url.
    :param text: str
    :return: void
    """
    # Remove the spaces
    text = text.replace(" ", "")

    # Keep everything after 'goto'
    url = text.partition('goto')[2]

    if url:
        command = f'start chrome {url}'
        shell_script(command=command)


def search(text):
    """
    Search for the keywords.
    :param text: str
    :return: void
    """

    # Keep everything after 'goto'
    kw = text.partition('search')[2]

    if kw:
        command = f'start chrome "?{kw}"'
        shell_script(command=command)


def exit_program():
    """
    Exit the program.
    :return: void
    """
    # Exit the program.
    print("See you soon!")
    sys.exit()


def process_text(text):
    """
    Process the text.
    :param text: str
    :return: void
    """
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

    elif 'open' in text:
        try:
            open_app(text)
        except Exception as e:
            print(e)

    elif 'go to' in text:
        try:
            go_to(text)
        except Exception as e:
            print(e)

    elif 'search' in text:
        try:
            search(text)
        except Exception as e:
            print(e)

    elif "exit now" in text:
        exit_program()
