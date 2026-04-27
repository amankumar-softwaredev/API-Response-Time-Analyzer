# 🚀 API Response Time Analyzer

A Python-based benchmarking tool to measure REST API response times and perform statistical latency analysis using multiple samples.

---

## 📌 Overview

This project benchmarks an API endpoint by sending repeated HTTP requests and measuring the latency of each response.

It then performs statistical analysis on the collected data to determine the API's average performance, variability, and confidence interval.

This helps developers understand how fast and stable an API is under repeated requests.

---

## ✨ Features

- ⏱ Benchmarks API response time over multiple requests  
- 📊 Calculates Mean Response Time  
- 📈 Computes Variance  
- 📉 Calculates Standard Deviation  
- 🎯 Generates 95% Confidence Interval  
- 🏦 Displays API Response Data for Each Request  
- ⚡ Provides Statistical Performance Insights  

---

## 🛠 Tech Stack

- Python 3  
- Requests Library  

---

## 📂 Project Structure

API-Response-Time-Analyzer/
│
├── main.py  
└── README.md  

---

## 🚀 Installation

```bash
git clone https://github.com/amankumar-softwaredev/API-Response-Time-Analyzer.git
cd API-Response-Time-Analyzer
pip install requests
