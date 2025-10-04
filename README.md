# 🔐 WiFi Password Harvester

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**A stealthy Windows utility for extracting saved WiFi credentials and system information**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Disclaimer](#%EF%B8%8F-disclaimer)

</div>

---

## 📋 Overview

WiFi Password Harvester is a lightweight, **completely silent** Windows tool that extracts all saved WiFi passwords and system information without any visible interface. Perfect for penetration testing, security audits, or simply recovering your own forgotten WiFi passwords.

### ✨ Features

- 🔒 **WiFi Password Extraction** - Retrieves all saved WiFi SSIDs and passwords from Windows
- 💻 **System Information Collection** - Gathers hostname, IP address, and MAC address
- 👻 **Completely Silent** - Runs invisibly with zero console window flash
- ⚡ **Lightning Fast** - Multi-threaded execution for 3-5x faster password extraction
- 📝 **Persistent Logging** - Appends to existing logs instead of overwriting
- 🚀 **Portable** - Single standalone .exe, no installation required
- 🔧 **No Dependencies** - Runs on any Windows system without Python

## 🚀 Installation

### Option 1: Download Pre-built Executable
1. Download `wifi_pc_info.exe` from the [releases](../../releases) page
2. Place it anywhere on your Windows system
3. Run it - that's it!

### Option 2: Build from Source
```bash
# Clone the repository
git clone https://github.com/yourusername/wifi-password-harvester.git
cd wifi-password-harvester

# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --clean wifi_pc_info.spec
```

The compiled executable will be in the `dist/` folder.

## 💡 Usage

### Basic Usage
Simply double-click `wifi_pc_info.exe` or run it from command line:

```cmd
wifi_pc_info.exe
```

The program will:
1. Run completely invisibly (no windows)
2. Extract all saved WiFi passwords
3. Collect system information
4. Save everything to `data.txt` in the same directory

### Output Example
```
-----------------PC Info-----------------

PC Name: DESKTOP-ABC123
IP Address: 192.168.1.100
MAC Address: 00:1a:2b:3c:4d:5e

-----------------WIFI Info-----------------

Wi-Fi Name: HomeNetwork
Password: MySecurePassword123
====================
Wi-Fi Name: Office_WiFi
Password: CompanyPass456
====================
```

## 🔧 How It Works

### Technical Architecture

```
┌─────────────────────────────────────┐
│     WiFi Password Harvester         │
├─────────────────────────────────────┤
│  1. System Info Collection          │
│     └─ socket, uuid modules         │
├─────────────────────────────────────┤
│  2. WiFi Profile Enumeration        │
│     └─ netsh wlan show profiles     │
├─────────────────────────────────────┤
│  3. Multi-threaded Password Extract │
│     └─ ThreadPoolExecutor (10x)     │
│     └─ netsh show profile key=clear │
├─────────────────────────────────────┤
│  4. Silent Subprocess Execution     │
│     └─ CREATE_NO_WINDOW flag        │
├─────────────────────────────────────┤
│  5. Data Logging                    │
│     └─ Append to data.txt           │
└─────────────────────────────────────┘
```

### Key Technologies
- **Windows WLAN API** - Via `netsh` command-line utility
- **Threading** - `concurrent.futures.ThreadPoolExecutor` for parallel WiFi queries
- **Silent Execution** - `CREATE_NO_WINDOW` flag prevents console flash
- **PyInstaller** - Bundles Python script into standalone .exe with no console

### Why It's Fast
The tool uses multi-threading to query up to 10 WiFi profiles simultaneously instead of sequentially:
- **Sequential**: 10 profiles × 1 sec = 10 seconds
- **Parallel (10 threads)**: 10 profiles ÷ 10 = ~2 seconds ⚡

## 🛠️ Development

### Project Structure
```
wifi-password-harvester/
├── script.py              # Main Python source code
├── wifi_pc_info.spec      # PyInstaller build configuration
├── README.md              # This file
├── LICENSE                # MIT License
├── requirements.txt       # Python dependencies (none!)
└── dist/
    └── wifi_pc_info.exe   # Compiled executable
```

### Requirements
- **Python 3.7+** (for building only)
- **Windows OS** (target platform)
- Standard library only - no external dependencies!

### Building
```bash
# Standard build
pyinstaller --onefile --noconsole --name wifi_pc_info script.py

# Or use the spec file for customized build
pyinstaller --clean wifi_pc_info.spec
```

## 🔒 Security Considerations

### Antivirus Detection
Due to the nature of password extraction and silent execution, some antivirus software may flag this tool as potentially unwanted. This is a **false positive** - the source code is open for inspection.

To avoid detection:
- Add an exception in Windows Defender
- Code sign the executable (for professional use)
- Compile with custom PyInstaller bootloader

### Permissions
- Requires standard user privileges (no admin needed)
- Only extracts WiFi passwords that the current user has access to
- Uses legitimate Windows `netsh` commands

## ⚠️ Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED USE ONLY**

This tool is designed for:
- ✅ Security professionals conducting authorized penetration tests
- ✅ Recovering your own forgotten WiFi passwords
- ✅ Educational purposes and security research
- ✅ IT administrators managing network credentials

**DO NOT USE** for:
- ❌ Unauthorized access to networks or systems
- ❌ Stealing WiFi passwords without permission
- ❌ Any illegal or malicious activities

**The authors are not responsible for misuse of this tool. Always obtain explicit permission before testing on systems you don't own.**

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Have questions or suggestions? Open an issue or reach out!

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

Made with ❤️ for the cybersecurity community

</div>

