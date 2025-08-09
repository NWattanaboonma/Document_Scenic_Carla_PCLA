# Scenic + CARLA + PCLA Setup Guide

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
```

**Documentation**:  
[Scenic Quickstart](https://docs.scenic-lang.org/en/latest/quickstart.html)  
[Scenic GitHub](https://github.com/BerkeleyLearnVerify/Scenic)

---

## 2️⃣ Installing CARLA

We use **CARLA v0.9.15** (Unreal Engine 4.26).

**Requirements**:
- Windows/Linux
- GPU ≥ 6GB (8GB recommended)
- Disk space ≥ 20GB
- Python 3.x
- `pygame`, `numpy` (install before starting)

**Installation**:
1. Download [CARLA 0.9.15 Release](https://github.com/carla-simulator/carla/releases/tag/0.9.15)
2. Extract both the main CARLA package and additional files.
3. Replace files in CARLA with those from the "Additional" folder.
4. Launch `CarlaUE4.exe` before running scenarios.

**Check Scenic Integration**:
```bash
scenic examples/carla/Carla_Challenge/carlaChallenge1.scenic --2d --model scenic.simulators.carla.model --simulate
```

**Documentation**:  
[CARLA Quickstart](https://carla.readthedocs.io/en/latest/start_quickstart/)

---

## 3️⃣ Installing PCLA

PCLA lets you run pretrained CARLA leaderboard agents independently.

**Windows Setup**:
- Install [Anaconda](https://www.anaconda.com/)
- Install dependencies from `requirements.txt`  
  *(Ensure correct CUDA/cuDNN versions, e.g. `nvidia-cudnn-cu11==9.0.0.312`)*

---

## 4️⃣ Running the Full Integration

Example script provided in `main.py`:

```bash
python main.py
```

The script:
- Loads a Scenic scenario (`Case1.scenic`)
- Connects to CARLA
- Spawns all actors (including the ego vehicle)
- Initializes PCLA AI agent
- Runs the simulation loop with live camera feed

---

## 🛠 File Structure

```
.
├── Part1_Setup_Scenic.md
├── Part2_Setup_Carla.md
├── Part3_Setup_PCLA.md
├── main.py            # Full integration script
├── scenic/            # Scenic source
├── carla/             # CARLA files and configs
└── README.md
```

---

## ⚠ Common Issues

- **Pygame window not responding**: Ensure GPU drivers are updated and CARLA is running before executing Scenic scripts.
- **Spawn failures**: Check map availability and spawn point clearance in CARLA.
- **Missing dependencies**: Install from `requirements.txt` using the correct Python environment.

---

## 📚 References

- [Scenic Documentation](https://docs.scenic-lang.org/en/latest/quickstart.html)
- [CARLA Simulator](https://carla.org)
- [PCLA Project](https://github.com/carla-simulator/leaderboard) *(for agent reference)*

---

## 📄 License

This repository follows the licensing terms of Scenic, CARLA, and PCLA. See individual project licenses for details.
