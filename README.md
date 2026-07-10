# Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing

## Project Description

The **Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing** is a Python-based application developed to collect, classify, and manage log data generated from multiple servers in real time. The system simulates servers located in different cities and continuously generates log messages such as **INFO**, **WARNING**, **ERROR**, and **DEBUG**. These logs are transmitted through socket communication, processed by a log harvester, and stored in separate binary files based on their log level.

The main objective of this project is to demonstrate how distributed systems can collect and organize logs from multiple sources while maintaining efficient storage and fast retrieval. The project also introduces the concept of binary log files, socket programming, and real-time monitoring.

---

# Project Objectives

- To simulate real-time log generation from multiple servers.
- To collect logs using socket communication.
- To classify logs into different categories.
- To store logs in binary (.bin) format.
- To read binary log files and display them in a readable format.
- To understand parallel log processing concepts.
- To provide a simple log monitoring system for educational purposes.

---

# Problem Statement

Large organizations generate thousands of log records every minute from different applications and servers. Managing these logs manually is difficult and time-consuming. Without proper organization, identifying errors, warnings, or debugging information becomes challenging.

This project provides an automated solution that collects logs from different servers, categorizes them, stores them in binary files, and allows users to read the stored logs whenever required.

---

# Technologies Used

- Python 3.x
- Socket Programming
- Binary File Handling
- Struct Module
- VS Code
- Windows Operating System

---

# Python Modules Used

- socket
- struct
- os
- random
- datetime
- time

---

# Project Structure

```
RealTimeLogEngine/

│
├── read_binary.py
├── log_server_simulator.py
├── log_harvester_daemon.py
│
├── mumbai_WARNING.bin
├── mumbai_ERROR.bin
├── mumbai_INFO.bin
├── mumbai_DEBUG.bin
│
├── chennai_WARNING.bin
├── chennai_ERROR.bin
├── chennai_INFO.bin
├── chennai_DEBUG.bin
│
├── bangalore_WARNING.bin
├── bangalore_ERROR.bin
├── bangalore_INFO.bin
├── bangalore_DEBUG.bin
│
└── README.md
```

---

# Project Workflow

1. Start the Log Harvester Server.
2. The server waits for incoming log messages.
3. Start the Log Server Simulator.
4. The simulator generates logs continuously.
5. Logs are transmitted through sockets.
6. The Log Harvester receives the logs.
7. Logs are classified into INFO, WARNING, ERROR, and DEBUG.
8. Classified logs are stored inside binary files.
9. The Binary Reader reads and displays the stored logs.

---

# Log Categories

## INFO

INFO logs represent normal system activities.

Examples:

- Server Started
- User Login Successful
- Configuration Loaded
- Backup Completed
- Service Running Normally

---

## WARNING

WARNING logs indicate situations that require attention.

Examples:

- High CPU Usage
- Low Disk Space
- High Memory Usage
- Network Delay
- Slow Response Time

---

## ERROR

ERROR logs indicate critical failures.

Examples:

- Database Connection Failed
- Authentication Failed
- Socket Timeout
- API Request Failed
- File Write Error

---

## DEBUG

DEBUG logs help developers during debugging.

Examples:

- Variable Initialized
- Cache Loaded
- Function Executed
- Thread Started
- Packet Parsed

---

# Cities Included

The project simulates servers located in three different cities.

- Mumbai
- Chennai
- Bangalore

Each city contains four binary log files.

Example:

Mumbai

- WARNING.bin
- ERROR.bin
- INFO.bin
- DEBUG.bin

The same structure is followed for Chennai and Bangalore.

---

# Binary File Format

Each log entry contains:

- Timestamp
- City Name
- Server Name
- Log Level
- Log Message

Example:

2026-07-09 10:20:35 | Mumbai | Server-01 | INFO | Server Started

---

# How to Run the Project

## Step 1

Open the project folder using VS Code.

---

## Step 2

Open Terminal.

Run:

```
python log_harvester_daemon.py
```

Output:

```
Waiting for Logs...
```

---

## Step 3

Open another terminal.

Run:

```
python log_server_simulator.py
```

Output:

```
2026-07-09 10:00:01 | Mumbai | INFO | Server Started
```

---

## Step 4

Open another terminal.

Run:

```
python read_binary.py
```

Output:

```
mumbai_INFO.bin

2026-07-09 10:00:01 | Mumbai | INFO | Server Started

mumbai_WARNING.bin

2026-07-09 10:00:05 | Mumbai | WARNING | CPU Usage High
```

---

# Advantages

- Real-time monitoring
- Organized log storage
- Easy log classification
- Faster troubleshooting
- Supports multiple cities
- Binary storage improves efficiency
- Easy to understand
- Beginner-friendly implementation

---

# Applications

- Data Centers
- Cloud Servers
- Banking Systems
- Hospital Management Systems
- E-Commerce Platforms
- IoT Devices
- Enterprise Monitoring
- Network Administration

---

# Future Enhancements

- Multi-threaded log processing
- AI-based anomaly detection
- Cloud storage integration
- Web dashboard using Flask
- Email notification for critical errors
- Database support
- User authentication
- Log search and filtering
- Log visualization using graphs
- REST API integration

---

# Limitations

- Uses simulated log data.
- Runs on a local machine.
- No database integration.
- Basic socket communication.
- Suitable mainly for educational purposes.

---

# Expected Output

The application continuously receives log messages, categorizes them, stores them into binary files, and displays the stored logs using the binary reader.

Sample Output:

```
Waiting for Logs...

Connected Successfully

2026-07-09 10:05:12 | Mumbai | INFO | Server Started

2026-07-09 10:05:15 | Chennai | WARNING | CPU Usage High

2026-07-09 10:05:20 | Bangalore | ERROR | Database Connection Failed

2026-07-09 10:05:24 | Mumbai | DEBUG | Variable Initialized
```

---


# project output#

<img width="960" height="604" alt="Screenshot 2026-07-10 135048" src="https://github.com/user-attachments/assets/2aaf5cec-0f51-497d-a5c6-fe296d22e875" />



# Conclusion

The **Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing** successfully demonstrates the process of collecting, transmitting, classifying, storing, and reading log data generated from multiple servers. The project combines socket programming with binary file handling to create an efficient log management system. It provides practical knowledge of real-time communication, structured data storage, and log processing concepts. This project can be further enhanced with cloud integration, databases, dashboards, and AI-based log analysis, making it suitable for enterprise-level monitoring systems.

---

# Author

**Name:** Nathiya

**Department:** Bachelor of Computer Application (BCA)

**Project Title:** Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing
