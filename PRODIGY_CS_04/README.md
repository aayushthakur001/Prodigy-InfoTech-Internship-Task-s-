# 🖥️ Simple Keylogger

A lightweight and feature-rich keylogger developed in Python by **Ayush Thakur (Hunter001x)**. This tool logs keystrokes, supports email notifications, log rotation, stealth mode, and customizable hotkeys.

---

## ✨ Features

1. **🖊️ Keystroke Logging**: Logs all keystrokes to a specified file.
2. **📧 Email Notifications**: Automatically sends the log file to a specified email address.
3. **🕵️ Stealth Mode**: Hides the console window for discreet operation (Windows only).
4. **🎛️ Customizable Hotkey**: Allows users to define a hotkey to stop the keylogger.
5. **⏰ Timestamps**: Adds timestamps to each logged keystroke.
6. **⚙️ Error Handling**: Handles errors gracefully during logging.
7. **🌐 Cross-Platform**: Works on Windows, macOS, and Linux.
8. **🔄 Log Rotation**: Automatically rotates the log file when it exceeds 1 MB.
9. **🚫 Excluded Keys**: Skips logging of specific keys like `Shift`, `Ctrl`, `Alt`, and `Cmd`.

---

## 📋 Requirements

- **Python**: Version 3.6 or higher
- **Required Libraries**:
  - `pynput`
  - `argparse`
  - `smtplib`

Install dependencies using:
```bash
pip install pynput
```

---

## 🚀 Usage

### 🏁 Running the Keylogger

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aayushthakur001/Simple-Keylogger.git
   cd Simple-Keylogger
   ```

2. **Run the Script**:
   ```bash
   python keylogger.py
   ```

   ## Banner
The tool displays the following banner upon execution:
 ```
_  __          _                                      
| |/ /___ _   _| | ___  ___ ___  _ __   ___ _ __  _   _ 
| ' // _ \ | | | |/ _ \/ __/ _ \| '_ \ / _ \ '_ \| | | |
| . \  __/ |_| | |  __/ (_| (_) | | | |  __/ | | | |_| |
|_|\_\___|\__,_|_|\___|\___\___/|_| |_|\___|_| |_|\__,_|
=================================================================
    Simple Keylogger – Developed by: Ayush Thakur (Hunter001x)
            GitHub: https://github.com/aayushthakur001
=================================================================
```
3. **Customize Behavior**: Use the available arguments to modify the keylogger's functionality.

---

### ⚙️ Command-Line Arguments

| Argument             | Description                                                                                  | Default Value       |
|-----------------------|----------------------------------------------------------------------------------------------|---------------------|
| `--output`           | Output file to save keystrokes.                                                              | `key_log.txt`       |
| `--email`            | Recipient email to send logs.                                                                | None                |
| `--sender_email`     | Sender email for sending logs.                                                               | None                |
| `--sender_password`  | Sender email password.                                                                       | None                |
| `--hotkey`           | Hotkey to stop the keylogger.                                                                | `<esc>`             |
| `--stealth`          | Run in stealth mode (no console output).                                                     | Disabled            |

---

### 🛠️ Example Commands

1. **Basic Usage**:
   ```bash
   python keylogger.py
   ```

2. **Send Logs via Email**:
   ```bash
   python keylogger.py --email recipient@example.com --sender_email sender@example.com --sender_password yourpassword
   ```

3. **Run in Stealth Mode**:
   ```bash
   python keylogger.py --stealth
   ```

4. **Custom Hotkey**:
   ```bash
   python keylogger.py --hotkey "<ctrl>+<alt>+s"
   ```

---

### 🛑 Stopping the Keylogger

Press the defined hotkey (default: `<esc>`) to stop the keylogger. Upon stopping, the log file will be sent via email (if configured).

---

## 🛡️ How It Works

1. **Keystroke Logging**: Captures keystrokes using the `pynput` library and writes them to a log file.
2. **Email Notifications**: Sends the log file to the recipient email using the `smtplib` library.
3. **Stealth Mode**: Hides the console window on Windows using the `ctypes` library.
4. **Log Rotation**: Renames the log file with a timestamp when it exceeds 1 MB.
5. **Custom Hotkey**: Uses `keyboard.GlobalHotKeys` to listen for a user-defined hotkey to stop the keylogger.

---

## 🔒 Security and Privacy

This tool is intended for **educational purposes only**. Use it responsibly and ensure you have proper authorization before deploying it on any system.

---

## ⚠️ Disclaimer

The author is **not responsible** for any misuse of this tool. Use it at your own risk.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed by **Ayush Thakur (Hunter001x)**  
GitHub: [https://github.com/aayushthakur001](https://github.com/aayushthakur001)

---
