Markdown

# Python Codelets

A collection of small, self-contained Python scripts ("codelets") for exploring Python concepts, testing ideas, and building utilities. This repository serves as a personal learning space and a central place to organize various Python experiments.

---

## Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Codelet Descriptions](#codelet-descriptions)
4. [How to Use](#how-to-use)
5. [License](#license)

---

## Overview

This repository contains Python scripts that demonstrate a variety of programming concepts, utilities, and tools. Each script is self-contained and focuses on a specific task or idea. The project is organized into directories based on functionality, such as encoding, networking, hardware interaction, and Python basics.

---

## Directory Structure

The repository is organized as follows:

Python-Codelets/
├── API-Calls/
│   └── bitcoin_trader.py
├── Encoding/
│   ├── Binary-Hex/
│   │   └── binary_hex_converter.py
│   ├── Ceaser-Cypher/
│   │   ├── Ceaser Cypher.py
│   │   └── data.txt
│   └── Password Generator/
├── Hardware/
│   ├── PID/
│   │   └── pid_test.py
│   └── Uart-Tester/
│       └── uart_test.py
├── Networking/
│   ├── Protocols/
│   │   └── icmp_packet.py
│   └── Requests/
│       ├── request_checker.py
│       └── understanding_requests.py
└── Python-Basics/
    ├── class.py
    └── decorator.py


---

## Codelet Descriptions

### API-Calls
- **`bitcoin_trader.py`**: Simulates a cryptocurrency trading bot using the Coinbase API. It fetches real-time Bitcoin prices, executes buy/sell trades based on thresholds, and tracks portfolio performance.

---

### Encoding
- **Binary-Hex Converter (`binary_hex_converter.py`)**: Converts input (numbers or characters) to their binary and hexadecimal representations.
- **Ceaser Cypher (`Ceaser Cypher.py`)**: Encrypts text using the Caesar cipher method. Reads input from `data.txt` and outputs the encrypted text.
- **Password Generator**: A folder for generating strong, random passwords with customizable lengths.

---

### Hardware
- **PID Controller Test (`pid_test.py`)**: Simulates a Proportional-Integral-Derivative (PID) controller, often used in hardware systems like temperature control.
- **UART Tester (`uart_test.py`)**: Listens to UART communication and processes serial data.

---

### Networking
- **Protocols**:
  - **ICMP Packet (`icmp_packet.py`)**: Demonstrates low-level networking using ICMP (e.g., ping functionality).
- **Requests**:
  - **Request Checker (`request_checker.py`)**: Demonstrates HTTP requests and response headers using the `requests` library.
  - **Understanding Requests (`understanding_requests.py`)**: Explores the basics of making HTTP calls with the `requests` library.

---

### Python Basics
- **Class Demonstration (`class.py`)**: Demonstrates object-oriented programming concepts, including inheritance and method overriding.
- **Decorator Example (`decorator.py`)**: Shows how to use Python decorators to measure and print the execution time of a function.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/Python-Codelets.git](https://github.com/your-username/Python-Codelets.git)
   cd Python-Codelets
   ```

2. Navigate to the desired script's directory:
   ```bash
   cd Encoding/Binary-Hex
   ```

3. Run the script:
   ```bash
   python3 binary_hex_converter.py
   ```

4. Follow any on-screen instructions or observe the output.

---

## License

This repository is for educational purposes. Unless otherwise specified, the code is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use and modify the scripts as needed.