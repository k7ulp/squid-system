# Squid System: Fed Data Entropy Evaluator

This system evaluates entropy and other features in Federal Reserve (FRED) data to generate trading signals for Treasury yields.

## Features
- **Data Source**: Fetches live data from FRED (DGS10, DGS5, DGS3MO).
- **Entropy**: Calculates Shannon Entropy on a rolling window of yield slopes.
- **Agents**: 
  - `Billygoat`: Signal based on yield slope thresholds.
  - `Squid`: Signal based on changes in entropy.
- **Optimization**: Brute-force search for optimal yield spreads and thresholds.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main optimization script:
```bash
python main.py
```

## Structure
- `squid/data.py`: Data ingestion from FRED.
- `squid/features.py`: Feature engineering (Entropy, Slope, Curvature).
- `squid/agents.py`: Signal generation logic.
- `squid/backtest.py`: Backtesting engine.
- `squid/optimizer.py`: Parameter optimization.
