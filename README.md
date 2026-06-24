# Wireshark HTTP Traffic Analysis Project

## Project Information

This repository contains the final project for the Computer Networks course.

The goal of this project is to analyze web traffic using standard networking tools such as Wireshark and curl. In this project, HTTP traffic is generated with curl, captured with Wireshark, and then analyzed layer by layer based on the TCP/IP protocol stack.

## Student Information

* **Name:** Saro Hosseini
* **Course:** Computer Networks
* **Instructor:** Dr. Saadoun Azizi
* **Project Topic:** HTTP/TCP/IP Traffic Analysis using Wireshark and curl

## Project Goal

The main purpose of this project is to understand what happens behind the scenes when a client sends an HTTP request to a web server.

In normal usage, the user only sees the final web page or the server response. However, at the network level, several packets are exchanged between the client and the server. This project captures and analyzes those packets in order to understand the behavior of the HTTP, TCP, and IP protocols.

## Tools Used

* **Wireshark:** Used to capture and analyze network packets.
* **curl:** Used to send simple HTTP requests from the terminal.
* **Git and GitHub:** Used for version control and project submission.
* **Python:** Used for the optional automation phase.

## Why curl is Used Instead of a Browser

Modern browsers usually redirect HTTP traffic to HTTPS automatically. Since HTTPS traffic is encrypted, the HTTP headers and methods cannot be clearly seen in Wireshark.

For this reason, curl is used in this project. It allows us to send simple and clear HTTP requests without extra browser behavior.

Example command:

```bash
curl http://neverssl.com
```

## Why HTTP Websites are Used

In this project, websites that support plain HTTP are used so that the HTTP request and response can be visible in Wireshark.

Example target websites:

```text
http://example.com
http://neverssl.com
http://httpbin.org/ip
http://httpbin.org/status/404
```

## Project Structure

```text
Wireshark/
├── captures/
├── screenshots/
├── notes/
├── scripts/
└── README.md
```

## Folder Description

### captures

This folder contains the captured Wireshark traffic files.

The captured files are saved in `.pcap` or `.pcapng` format. These files are required because screenshots alone are not enough for project submission.

### screenshots

This folder contains screenshots taken from Wireshark.

The screenshots will show important packets and fields such as:

* HTTP GET request
* HTTP response
* Source and destination IP addresses
* Source and destination ports
* HTTP headers
* Status code
* Delta Time or RTT

### notes

This folder contains temporary notes and explanations written during the project.

### scripts

This folder is used for the optional phase of the project.

If the optional automation part is implemented, the Python script for analyzing captured packets will be placed in this folder.

## Project Phases

## Phase 1: Environment Setup and Packet Capture

In this phase, Wireshark is opened and the active network interface is selected. Then, curl is used to generate HTTP traffic.

After receiving the response in the terminal, the capture process is stopped and the captured packets are saved in `.pcapng` format.

Expected output of this phase:

```text
captures/phase1_http_capture.pcapng
```

## Phase 2: Header and Protocol Stack Analysis

In this phase, the captured packets are filtered in Wireshark using display filters such as:

```text
http
```

or:

```text
tcp.port == 80
```

Then, the first HTTP GET request is selected and analyzed.

The following information will be extracted:

### Application Layer

* HTTP method
* Host
* HTTP version
* User-Agent

### Transport Layer

* Transport protocol
* Source port
* Destination port

### Network Layer

* Source IP address
* Destination IP address

## Phase 3: Server Response and RTT Analysis

In this phase, the server response packet is analyzed.

The following information will be extracted:

* HTTP status code
* Meaning of the status code
* Delta Time between the HTTP request and the first server response
* Approximate RTT analysis

If the delay is high, possible reasons will be discussed, such as:

* Client-side network problem
* Low bandwidth
* Network congestion
* Server-side processing delay
* Long physical or routing distance between client and server

## Phase 4: Optional Automation

In the optional phase, a simple Python script may be written to read the captured packet file and print a summary of useful information such as:

* Source IP
* Destination IP
* HTTP packets
* HTTP status codes

This phase is optional and is done for extra credit.