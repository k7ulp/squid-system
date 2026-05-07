# Squid System: Fed Data Entropy Evaluator

This system evaluates entropy, thermodynamic decay, and commodity shocks in Federal Reserve (FRED) data to generate trading signals for Treasury yields.

## Features
- **Data Source**: Fetches live data from FRED (DGS10, DGS5, DGS3MO) and WTI Oil Prices.
- **Entropy & Thermodynamics**: Calculates Shannon Entropy and estimates intrinsic decay (lambda) vs. systemic injection (beta).
- **Commodity Shocks**: Tracks oil price shocks to predict inflation-driven yield movements.
- **Agents**: 
  - `Billygoat`: Signal based on yield spread Z-scores and entropy.
  - `Thermodynamic`: Signal based on decay rates (lambda/beta ratio).
  - `Commodity Shock`: Signal based on extreme oil price moves.
  - `Integrator`: Compiles trades across all modules with weighted position sizing based on consensus.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main optimization and comparison script:
```bash
python main.py
```

## Structure
- `squid/data.py`: Data ingestion from FRED (Treasuries & Oil).
- `squid/features.py`: Feature engineering (Entropy, Z-Scores, Oil Shocks).
- `squid/agents.py`: Signal generation and module integration.
- `squid/thermodynamics.py`: Physics-inspired decay modeling.
- `squid/backtest.py`: Backtesting engine with dynamic exits.
- `squid/optimizer.py`: Parameter optimization.
