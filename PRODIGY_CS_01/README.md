# 🔐 Caesar Cipher Tool

Welcome to the **Caesar Cipher Tool**! This Python-based tool allows you to encrypt and decrypt messages using the Caesar Cipher technique. It supports both command-line arguments and an interactive menu for ease of use.

---

## 🚀 Features

- **Encryption & Decryption**: Easily encrypt or decrypt messages with a specified shift value.
- **Interactive Mode**: User-friendly menu for those who prefer not to use command-line arguments.
- **CLI Support**: Pass arguments directly via the command line for quick operations.
- **File Output**: Save the results to a file for future reference.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/caesar-cipher-tool.git
   cd caesar-cipher-tool
   ```
2. Ensure you have Python installed (version 3.6 or higher).

---

## 🛠️ Usage

### **Command-Line Mode**
Run the script with the following arguments:
```bash
python "Caesar Cipher.py" --mode [encrypt|decrypt] --text "your message" --shift [integer] --output [filename]
```

Example:
```bash
python "Caesar Cipher.py" --mode encrypt --text "Hello World" --shift 3 --output result.txt
```

### **Interactive Mode**
If you don't provide all the required arguments, the tool will switch to an interactive menu:
1. Choose the mode (encrypt or decrypt).
2. Enter your message.
3. Specify the shift value.
4. Provide an output filename (or press Enter for the default).

---

## 📁 Output

The tool saves the results in a text file with the following format:
```
Mode     : encrypt
Shift    : 3
Input    : Hello World
Result   : Khoor Zruog
```

---

## 🖼️ Banner

The tool displays a cool ASCII banner when executed:
```
  ____                                ____  _       _           
 / ___|__ _ _ __ ___   ___  ___ ___  |  _ \| |_   _(_)_ __  ___ 
| |   / _` | '_ ` _ \ / _ \/ __/ __| | |_) | | | | | | '_ \/ __|
| |__| (_| | | | | | |  __/\__ \__ \ |  __/| | |_| | | | | \__ \
 \____\__,_|_| |_| |_|\___||___/___/ |_|   |_|\__,_|_|_| |_|___/
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs 🐛
- Suggest features ✨
- Submit pull requests 🔧

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👨‍💻 Developed By

**Ayush Thakur**  
GitHub: [Hunter001x](https://github.com/Hunter001x)  
Part of the **Prodigy Infotech Internship** program.

---