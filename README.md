# 🏎️ Mini hackathon - F1 Predictor

This project uses the [Fast-F1](https://github.com/theOehrly/Fast-F1) package to ingest race data and build predictive models for Formula 1 outcomes, including qualifying results, lap times, and race finishes.

## 🔧 Features

- Ingest and cache live and historical race session data
- Extract driver telemetry, sector times, and lap performance
- Perform EDA on race conditions, strategies, and performance
- Predict outcomes using ML models (planned)

## 🚀 Setup

You can run this project using either **Docker (recommended)** or **Miniconda**.

---

### 🐳 Option 1: Docker (Recommended)

Run the project in a fully isolated environment using Docker.

To activate an interactive Ubuntu-based shell with the `f1` Conda environment preloaded, run the following line in any Unix-like terminal:

```bash
make run
```

#### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [GNU Make](https://www.gnu.org/software/make/) - already included on most Unix-like systems

> 🪟 **Windows users**:  
> Install WSL by running the following in **PowerShell**:
> ```powershell
> wsl --install
> ```
> Then reboot, and in your WSL terminal (e.g. Ubuntu), run:
> ```bash
> sudo apt-get install build-essential
> ```

---

### 🐍 Option 2: Miniconda (Local Dev)

If you prefer running Python natively on your system:

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)  
   [Reference guide](https://eduand-alvarez.medium.com/setting-up-anaconda-on-your-windows-pc-6e39800c1afb)

2. Open a terminal and create the environment:

   ```bash
   conda env create -f environment.yml --name f1
   ```

3. Activate the environment:

   ```bash
   conda activate f1
   ```

You’re now ready to run scripts and notebooks locally.