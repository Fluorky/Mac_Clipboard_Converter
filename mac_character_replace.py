import keyboard
import pyperclip

def replace_hyphen_with_colon():
    clipboard_text = pyperclip.paste()
    new_text = clipboard_text.replace('-', ':')
    pyperclip.copy(new_text)

keyboard.add_hotkey('ctrl+shift+1', replace_hyphen_with_colon)
keyboard.wait()