from PIL import Image, UnidentifiedImageError
import argparse
import os
import logging
from tqdm import tqdm  # For progress bar

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def show_banner():
    print(r"""
   ____  _           _        ____                      
  |  _ \| |__   __ _| |_ __ _|  _ \ ___ _ __   ___ _ __ 
  | | | | '_ \ / _` | __/ _` | |_) / _ \ '_ \ / _ \ '__|
  | |_| | | | | (_| | || (_| |  _ <  __/ |_) |  __/ |   
  |____/|_| |_|\__,_|\__\__,_|_| \_\___| .__/ \___|_|   
                                       |_|              
===================================================================
    🖼️ Pixel Image Encryptor Tool – Prodigy Infotech Internship
            Developed by: Ayush Thakur (Hunter001x💻)
===================================================================
    """)

def encrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
    except UnidentifiedImageError:
        logging.error("Unsupported or corrupted image format.")
        return

    pixels = image.load()
    is_grayscale = len(image.getbands()) == 1  # Check if image is grayscale

    for i in tqdm(range(image.size[0]), desc="Processing", unit="column"):
        for j in range(image.size[1]):
            if is_grayscale:
                gray = pixels[i, j]
                pixels[i, j] = gray ^ key
            else:
                r, g, b = pixels[i, j]
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    try:
        image.save(output_path)
        logging.info(f"Encrypted and saved to: {output_path}")
    except IOError:
        logging.error("Failed to save the output image. Check the output path.")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)  # XOR is reversible

def interactive_mode():
    input_path = input("🖼️ Enter image path: ").strip()
    while not os.path.exists(input_path):
        logging.error("File not found.")
        input_path = input("🖼️ Enter image path: ").strip()

    mode = input("🔄 Mode (encrypt/decrypt): ").strip().lower()
    while mode not in ['encrypt', 'decrypt']:
        mode = input("🔄 Mode must be 'encrypt' or 'decrypt': ").strip().lower()

    try:
        key = int(input("🔑 Enter key (0-255): "))
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        logging.error("Invalid key. Must be an integer between 0 and 255.")
        return

    output_path = input("💾 Output image path (e.g., result.png): ").strip()
    if not output_path:
        output_path = "encrypted_output.png" if mode == "encrypt" else "decrypted_output.png"

    if mode == "encrypt":
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="Image Encryptor - by Ayush Thakur (Hunter001x)")
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], help='Mode of operation')
    parser.add_argument('--input', help='Path to input image')
    parser.add_argument('--output', help='Path to output image')
    parser.add_argument('--key', type=int, help='Key (0-255) for XOR encryption')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if not args.mode or not args.input or args.output is None or args.key is None:
        logging.info("Not enough arguments. Switching to interactive mode...\n")
        interactive_mode()
    else:
        if not os.path.exists(args.input):
            logging.error("Input file not found.")
            return

        if not (0 <= args.key <= 255):
            logging.error("Key must be between 0 and 255.")
            return

        if args.mode == 'encrypt':
            encrypt_image(args.input, args.output, args.key)
        else:
            decrypt_image(args.input, args.output, args.key)

if __name__ == "__main__":
    main()
