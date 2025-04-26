# 🚀 Ultimate Packet Sniffer

![Banner](https://via.placeholder.com/800x200.png?text=Ultimate+Packet+Sniffer)

## 📖 Introduction

The **Ultimate Packet Sniffer** is a Python-based network packet capturing tool designed to monitor and analyze network traffic in real-time. It provides detailed insights into network protocols such as TCP, UDP, ICMP, and HTTP. This tool is ideal for network administrators, cybersecurity professionals, and enthusiasts who want to understand network behavior or troubleshoot network issues.

---

## ✨ Features

- 🔍 **Real-time Packet Capture**: Captures packets on a specified network interface.
- 🎯 **Protocol Filtering**: Filter packets by protocol (TCP, UDP, ICMP, or all).
- 🌐 **HTTP Payload Detection**: Detects and displays HTTP payloads in TCP packets.
- 📝 **Detailed Logging**: Logs packet details, including source, destination, protocol, and payload.
- ⚙️ **Promiscuous Mode**: Configures the network interface to capture all traffic.
- 💻 **Cross-Platform**: Works on both Windows and Unix-like systems (requires admin privileges).

---

## 🛠️ Project Structure

```
Ultimate-Packet-Sniffer/
├── packet_sniffer.py       # Main script for packet capturing
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── LICENSE                 # License file
```


## ✅ Prerequisites

Before running the tool, ensure the following dependencies are installed:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Scapy**: Install Scapy using pip:
   ```bash
   pip install scapy
   ```
3. **Administrator Privileges**: The tool requires admin/root privileges to capture packets.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aayushthakur001/Ultimate-Packet-Sniffer.git
   cd Ultimate-Packet-Sniffer
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the script has execution permissions:
   ```bash
   chmod +x packet_sniffer.py
   ```

---

## 🚀 Usage

1. Run the script with administrator privileges:
   - **Windows**: Open Command Prompt as Administrator and execute:
     ```bash
     python packet_sniffer.py
     ```
   - **Linux/Mac**: Use `sudo` to run the script:
     ```bash
     sudo python3 packet_sniffer.py
     ```

2. Follow the prompts to configure the sniffer:
   - Enter the network interface (e.g., `eth0`).
   - Specify the number of packets to capture (0 for infinite).
   - Set the capture duration in seconds.
   - Choose the protocol to filter (tcp, udp, icmp, or 0 for all).
   - Provide a name for the log file.

3. View the captured packets in real-time and check the log file for detailed information.

---

## 📊 Example Output

```
* Enter the interface on which to run the sniffer (e.g., 'eth0'): eth0
* Enter the number of packets to capture (0 for infinite): 10
* Enter the number of seconds to run the capture: 30
* Enter the protocol to filter by (tcp|udp|icmp|0 for all): tcp
* Please give a name to the log file: capture_log.txt

Interface eth0 was set to PROMISC mode.

* Starting the capture...

[+] Time: 2023-03-15 14:23:45 Protocol: TCP Source: 192.168.1.2 Destination: 192.168.1.3 Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n'...
🌐 HTTP Payload Detected:
b'GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...'

📊 Capture Summary:
    - Total Packets Captured: 10
    - TCP Packets: 8
    - UDP Packets: 2
    - ICMP Packets: 0
    - HTTP Packets Detected: 1

* Please check the capture_log.txt file to see the captured packets.
```

---

## 🤝 Contribution

Contributions are welcome! If you have suggestions or want to improve the tool, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

---

## 🧑‍💻 Developer

- **Name**: Ayush Thakur (Hunter001x)  
- **GitHub**: [https://github.com/aayushthakur001](https://github.com/aayushthakur001)  
- **Email**: [ayush@example.com](mailto:ayush@example.com)

---

## ⚠️ Disclaimer

This tool is intended for educational and ethical purposes only. Unauthorized use of this tool to intercept or monitor network traffic without permission is illegal and unethical. The developer is not responsible for any misuse of this tool.

---