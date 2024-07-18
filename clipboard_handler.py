import sys
import pyperclip


def clipboard_input():
    try:
        return str(pyperclip.paste())
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        sys.exit(1)


def clipboard_output(results):
    pyperclip.copy(results)
