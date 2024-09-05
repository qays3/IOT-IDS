

# IoT IDS - Security Monitoring System

Welcome to the **IoT IDS (Intrusion Detection System)** project! This platform keeps an eye on your IoT devices, looking for potential network security issues and notifying you via email when suspicious activities are spotted. The design is straightforward and scalable, making it ideal for anyone exploring how to secure their IoT environment.

## Table of Contents

1. [Core Functions](#core-functions)
2. [System Design](#system-design)
3. [Project Layout](#project-layout)
4. [Setup Guide](#setup-guide)
5. [Getting Started](#getting-started)
6. [API Interface](#api-interface)
7. [Data Resources](#data-resources)
8. [How to Contribute](#how-to-contribute)
9. [License Information](#license-information)
10. [Credits](#Credits)

## Core Functions

- **Live Threat Detection:** Monitors network interactions from IoT devices to identify potential risks.
- **Alert System:** Sends detailed email notifications when unusual activity is detected.
- **Easy API Access:** Each IoT device communicates with the monitoring script via a simple API.
- **Scalable Setup:** More devices can be added quickly by connecting them to the API.
- **Data-Driven Analysis:** Uses a detailed dataset for precise identification of threats.

## System Design

The system consists of two main parts:

1. **Core Monitoring Script (VPS):** Operates on a Virtual Private Server (VPS) to analyze network traffic and detect risks.
2. **IoT Devices:** Devices send alert data to the main script through an API when they detect potential threats.

![System Design Diagram](docs/architecture.png)

## Project Layout

Here’s a snapshot of the project folder structure:

```
IOT/
├── API/
│   └── api.php
├── archive/
│   ├── all.jsonl
│   ├── Cyber-Threat-Intelligence-Custom-Data_new_processed.csv
│   ├── test.jsonl
│   ├── train.jsonl
│   ├── validation.jsonl
├── results/
│   ├── 08-31-2024-21-01-32/
│   └── packets.json
├── logs/
│   ├── app.log
├── main.py
├── README.md
├── requirements.txt
```

### Detailed Explanation

- **API/**: Contains `api.php`, the script used by IoT devices to send data to the server.
- **archive/**: Holds datasets used for identifying security threats, including JSONL and CSV files.
- **results/**: Stores session results, with each folder organized by timestamps and containing analysis files like `packets.json`.
- **logs/**: Tracks system activity and errors through log files.
- **main.py**: The primary Python script that analyzes network activity and detects threats.
- **requirements.txt**: Lists all Python modules needed for the project.

## Setup Guide

### What You’ll Need

- **Python 3.8+**
- **PHP 7.4+**
- **Virtual Private Server (VPS)**
- **Permissions to Install Python Modules**

### Steps to Install

1. **Download the Repository**

   ```bash
   git clone https://github.com/qays3/IOT-IDS.git
   cd IOT-IDS
   ```

2. **Set Up a Python Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the API**

   - Go to the `API/` folder.
   - Deploy `api.php` on a PHP server or VPS.

5. **Prepare the Dataset**

   - Download the dataset from [Kaggle](https://www.kaggle.com/datasets/ramoliyafenil/text-based-cyber-threat-detection?resource=download).
   - Move the `cyber-threat-intelligence_all.csv` file into the `archive/` folder.

## Getting Started

1. **Start the Core Monitoring Script**

   ```bash
   python main.py
   ```

2. **Select a Mode**

   - **Live Capture:** Analyzes network traffic in real time.
   - **Capture File:** Reviews a previously saved `.pcap` file.

3. **Input the Necessary Data**

   - **Live Mode:** Enter the interface you wish to monitor (e.g., Wi-Fi, Ethernet).
   - **Capture Mode:** Supply the path to the `.pcap` file.

4. **Check the Results**

   - Reports are saved in the `results/` directory with timestamps.
   - Each folder contains `packets.json` and `threats.json`.

## API Interface

### `api.php`

The PHP script acts as the API endpoint for IoT devices to send alerts about detected threats.

#### API Call

- **Method:** POST
- **Endpoint:** `https://yourdomain.com/API/api.php`
- **Parameters:**
  - `ip` (string): Device’s IP address.
  - `threat_id` (string): Unique identifier for the threat.
  - `threat_name` (string): Name or description of the threat.
  - `secretkey` (string): Secret key for verification.

#### API Response

- **Success:** `{ "message": "Notification sent" }`
- **Error:** Appropriate HTTP error code with a message.

#### Example

```bash
curl -X POST https://yourdomain.com/API/ \
     -d "ip=192.168.1.10" \
     -d "threat_id=12345" \
     -d "threat_name=Malware" \
     -d "secretkey=c55d47f942c79e312982f60d1a584b46"
```

## Data Resources

The dataset is key to identifying network threats and can be downloaded from [Kaggle](https://www.kaggle.com/datasets/ramoliyafenil/text-based-cyber-threat-detection?resource=download).

### Dataset Contents

- **all.jsonl**: Dataset in JSON Lines format.
- **cyber-threat-intelligence_all.csv**: Combined data for detecting threats.
- **train.jsonl**: Training data in JSON Lines format.
- **test.jsonl**: Test data in JSON Lines format.
- **validation.jsonl**: Validation data in JSON Lines format.

## How to Contribute

If you'd like to contribute:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b new-feature
   ```

3. **Commit Your Work**

   ```bash
   git commit -m "Added new feature"
   ```

4. **Push the Branch**

   ```bash
   git push origin new-feature
   ```

5. **Submit a Pull Request**

## License Information

This project is distributed under the [MIT License](LICENSE).

---

## Additional Details

- **Contact Us:** Feel free to reach out via email at [qayssarayra.h@gmail.com](mailto:qayssarayra.h@gmail.com).

## Credits
[qays3](https://github.com/qays3) ([Support qays](https://buymeacoffee.com/hidden))
