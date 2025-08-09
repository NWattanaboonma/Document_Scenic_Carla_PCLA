# Document_Scenic_Carla_PCLA
This repository provides step-by-step instructions and reference code for integrating the **Scenic** scenario description language with the **CARLA** autonomous driving simulator and **PCLA** (Pretrained CARLA Leaderboard Agent).

The setup is intended for **Windows** users but can be adapted for Linux.

---

## 📌 Overview

- **Scenic** – A domain-specific language for describing scenarios for autonomous systems.
- **CARLA** – An open-source simulator for autonomous driving research.
- **PCLA** – A framework to run pretrained CARLA leaderboard agents directly in custom scenarios.

This guide covers:
1. Installing Scenic
2. Installing CARLA (v0.9.15, UE4.26)
3. Installing and configuring PCLA
4. Running the full integration (Scenic + CARLA + PCLA)

---

## 1️⃣ Installing Scenic

**Requirements**: Python 3.8+

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate.bat   # Windows

# Upgrade pip
python -m pip install --upgrade pip

# Clone Scenic
git clone https://github.com/BerkeleyLearnVerify/Scenic
cd Scenic
python -m pip install -e .

# Verify installation
scenic --version
