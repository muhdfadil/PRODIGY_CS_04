# Simple Keylogger

This project implements a simple keylogger in Python. The keylogger records all keystrokes made by the user and stores them in a log file for later review. This tool is developed for ethical use, such as monitoring personal devices, and should not be used for malicious purposes.

## Features

- **Keystroke Logging**: Captures all keyboard inputs and saves them to a log file.
- **Time Stamping**: Records the timestamp of when each key was pressed.
- **Configurable Logging Interval**: Allows you to set how often the log file is updated.
- **Cross-Platform Support**: The keylogger works on major operating systems like Windows, Linux, and macOS (with appropriate permissions).

## How It Works

1. The keylogger runs in the background, recording every keypress.
2. The recorded keystrokes are periodically written to a log file.
3. The log file can be reviewed later to see the keystrokes.

## Example Usage

1. **Start Keylogger**:
   ```bash
   $ python3 keylogger.py
