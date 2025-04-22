import argparse
import os

def show_banner():
    print(r"""
  ____                                ____  _       _           
 / ___|__ _ _ __ ___   ___  ___ ___  |  _ \| |_   _(_)_ __  ___ 
| |   / _` | '_ ` _ \ / _ \/ __/ __| | |_) | | | | | | '_ \/ __|
| |__| (_| | | | | | |  __/\__ \__ \ |  __/| | |_| | | | | \__ \
 \____\__,_|_| |_| |_|\___||___/___/ |_|   |_|\__,_|_|_| |_|___/

=====================================================================
                Caesar Cipher Tool - Prodigy Infotech Internship
                         Developed by: Ayush Thakur(Hunter001x 💻)
=====================================================================
    """)

# Call this right before your menu or argparse logic

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def save_to_file(filename, mode, text, result, shift):
    with open(filename, 'w') as file:
        file.write(f"Mode     : {mode}\n")
        file.write(f"Shift    : {shift}\n")
        file.write(f"Input    : {text}\n")
        file.write(f"Result   : {result}\n")
    print(f"\n📁 Result saved to: {filename}")

def interactive_menu():
    print("🔐 Caesar Cipher Tool")
    print("----------------------")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter an integer for the shift value.")
    
    output = input("Enter output filename (press Enter for default): ").strip() or "cipher_output.txt"

    return mode, text, shift, output

def main():
    parser = argparse.ArgumentParser(description="🔐 Caesar Cipher CLI Tool")
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], help='Choose: encrypt or decrypt')
    parser.add_argument('--text', help='Message to encrypt/decrypt')
    parser.add_argument('--shift', type=int, help='Shift value (integer)')
    parser.add_argument('--output', default='cipher_output.txt', help='Output filename (default: cipher_output.txt)')

    args = parser.parse_args()

    # If not all CLI arguments are given, fall back to menu
    if not args.mode or not args.text or args.shift is None:
        print("\n🧠 Switching to interactive mode...")
        mode, text, shift, output = interactive_menu()
    else:
        mode = args.mode
        text = args.text
        shift = args.shift
        output = args.output

    # Process
    result = encrypt(text, shift) if mode == 'encrypt' else decrypt(text, shift)
    print(f"\n🔁 {mode.title()}ed Text: {result}")
    save_to_file(output, mode, text, result, shift)

if __name__ == "__main__":
    main()
