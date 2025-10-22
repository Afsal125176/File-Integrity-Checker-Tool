# # 🧩 CODTECH Internship Task 1 — File Integrity Checker

## 📘 Overview
This project is part of the **CODTECH Internship Task - 1**, where the goal is to build a **File Integrity Checker** tool.  
It monitors changes in files by calculating and comparing **hash values** using Python’s `hashlib` library.

The tool helps ensure that files remain **unaltered, secure, and authentic** by detecting modifications, deletions, or additions.

---

## 🧠 Features
- ✅ Calculates **SHA256 hash values** for all files in a folder  
- ✅ Detects if any file is **added**, **modified**, or **deleted**  
- ✅ Stores file hashes in a JSON file (`file_hashes.json`)  
- ✅ Works on **Linux, Windows, and macOS**  
- ✅ Simple **command-line interface**

---

## ⚙️ Requirements
Make sure you have:
- **Python 3.x** installed  
- Standard Python libraries:  
  - `os`
  - `hashlib`
  - `json`

No extra installations are required.

---

## 🧩 Installation and Setup (Kali Linux Example)

### 1️⃣ Clone or Download the Project
```bash
mkdir ~/codtech_task1
cd ~/codtech_task1
