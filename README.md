# 🏎️ Mini hackathon - F1 Predictor

This project uses the [Fast-F1](https://github.com/theOehrly/Fast-F1) package to ingest race data and build predictive models for Formula 1 outcomes, including qualifying results, lap times, and race finishes.

## 🔧 Features

- Ingest and cache live and historical race session data
- Extract driver telemetry, sector times, and lap performance
- Perform EDA on race conditions, strategies, and performance
- Predict outcomes using ML models (planned)

## 📦 Setup environment

1. Install Miniconda
    - see https://eduand-alvarez.medium.com/setting-up-anaconda-on-your-windows-pc-6e39800c1afb

2. Open terminal, run `conda env create -f environment.yml --name ENV_NAME`
    - replace ENV_NAME with your choice

3. Use `conda activate ENV_NAME` to activate the environment