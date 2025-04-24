# 🖼️ Pixel Image Encryptor Tool

Pixel Image Encryptor is a Python-based tool that allows you to encrypt and decrypt images using XOR-based encryption. This tool was developed as part of the Prodigy Infotech Internship by **Ayush Thakur (Hunter001x💻)**.

## 🚀 Features

- **Encrypt Images**: Secure your images by encrypting their pixel data.
- **Decrypt Images**: Restore encrypted images back to their original form.
- **Interactive Mode**: User-friendly prompts for input, output, and encryption key.
- **Command-Line Support**: Use arguments for automation and scripting.
- **Progress Bar**: Visual feedback during processing using `tqdm`.
- **Grayscale and RGB Support**: Works with both grayscale and color images.

## 🛠️ Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `Pillow`
  - `argparse`
  - `tqdm`

Install the dependencies using:
```bash
pip install pillow tqdm
```

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pixel-image-encryptor.git
   cd pixel-image-encryptor
   ```
2. Install the required dependencies:
   ```bash
   pip install pillow tqdm
   ```
3. Ensure you have Python 3.6 or higher installed.

## 📖 Usage

### 1. Interactive Mode
If you don't provide all the required arguments, the tool will switch to an interactive menu:
1. Enter the image path.
2. Choose the mode (encrypt or decrypt).
3. Specify the encryption key (0-255).
4. Provide an output filename (or press Enter for the default).
Run the script without arguments to enter interactive mode:
```bash
python image_encryptor.py
```
Follow the prompts to encrypt or decrypt an image.

### 2. Command-Line Mode
Use the following arguments for automation:
- `--mode`: Operation mode (`encrypt` or `decrypt`).
- `--input`: Path to the input image.
- `--output`: Path to save the output image.
- `--key`: Encryption key (integer between 0 and 255).
- `--verbose`: Enable verbose logging.

Run the script with the following arguments:
```bash
python image_encryptor.py --mode [encrypt|decrypt] --input [input_path] --output [output_path] --key [0-255]
```

Example:
```bash
python image_encryptor.py --mode encrypt --input image.png --output encrypted_image.png --key 42
```

Example:
```bash
python image_encryptor.py --mode encrypt --input input.png --output encrypted.png --key 123
```

### Example Workflow
1. Encrypt an image:
   ```bash
   python image_encryptor.py --mode encrypt --input image.png --output encrypted_image.png --key 42
   ```
2. Decrypt the image:
   ```bash
   python image_encryptor.py --mode decrypt --input encrypted_image.png --output decrypted_image.png --key 42
   ```

## 🔑 How It Works

The tool uses XOR encryption to modify the pixel values of the image. XOR is a reversible operation, meaning the same key can be used for both encryption and decryption.

### Encryption Logic
- For grayscale images: `pixel_value = pixel_value ^ key`
- For RGB images: `(r, g, b) = (r ^ key, g ^ key, b ^ key)`

### Decryption Logic
Decryption is identical to encryption since XOR is reversible.

## 📁 Output

The tool saves the processed image to the specified output path. If no output path is provided, it defaults to:
- `encrypted_output.png` for encryption.
- `decrypted_output.png` for decryption.

## 🖼️ Banner

```
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
```

## 🛡️ Error Handling

- **Invalid Image Format**: Displays an error if the input image is unsupported or corrupted.
- **Invalid Key**: Ensures the key is an integer between 0 and 255.
- **File Not Found**: Prompts the user if the input file does not exist.
- **Save Errors**: Handles issues when saving the output image.

## 📂 Project Structure

```
PRODIGY_CS_02/
├── image_encryptor.py  # Main script
├── README.md           # Documentation
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs 🐛
- Suggest features ✨
- Submit pull requests 🔧
  
## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgments

- **Prodigy Infotech Internship** for the opportunity to work on this project.
- **Pillow** and **tqdm** libraries for simplifying image processing and progress tracking.

## 📧 Contact

For any queries or suggestions, feel free to reach out:
- **Developer**: Ayush Thakur (Hunter001x💻)
- **GitHub**: [https://github.com/aayushthakur001]

---
Happy Encrypting! 🔒
