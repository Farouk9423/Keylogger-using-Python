Educational Keylogger - For Cybersecurity Awareness

This project is a simple keylogger created for educational purposes to demonstrate how keyloggers work and how to defend against them in the realm of cybersecurity.


🛠️ How It Works

The script listens for keyboard input and logs the keystrokes into a local file called log.txt.

It filters out special keys such as Shift, Ctrl, Alt, and Enter to keep the log clean.

The keystrokes are stored locally in a text file and sent to a configured server every hour.


🔗 Server Communication

This keylogger includes a feature to send logged keystrokes to a remote server every hour.

You need to specify your server URL in the script (SERVER_URL).

The script uses an HTTP POST request to send the logs as data={"logs": logs}.


⚠️ Legal & Ethical Disclaimer

This project is intended for educational purposes only and should not be used for any malicious activities.

Do not use this keylogger on any system without explicit permission.

Unauthorized use may violate privacy laws and ethical guidelines.

The author does not take responsibility for any misuse of this code.


🛡️ How to Protect Yourself

While keyloggers like this are a security concern, you can take measures to protect yourself:

Use reputable antivirus and endpoint protection software to detect and block keyloggers.

Be cautious with downloading and running unknown scripts or software from untrusted sources.

Monitor running processes and check for unusual background activity on your system.

Use on-screen keyboards for sensitive data entry (e.g., passwords) to avoid hardware keyloggers.

Keep your operating system and security tools up to date to ensure protection against new threats.

Note: This project is not intended for use in illegal activities. It is created to help individuals understand keylogger functionality and improve their security awareness.

