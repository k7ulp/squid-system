# Squid System: Adaptive Epistemic Engine

Squid is a physics-inspired trading system that has evolved from deterministic forecasting toward **Adaptive Epistemology**. It moves away from asking "What will happen?" to continuously asking "**What matters right now?**"

## 🧠 Core Philosophy: Adaptive Epistemology
The system operates on a 7-layer hierarchy designed to handle market complexity through navigation rather than prediction:
1. **Perception**: Raw data ingestion from FRED and energy markets.
2. **State Physics**: Computation of Shannon Entropy, intrinsic decay ($\lambda$), and systemic injection ($\beta$).
3. **Regime Detection**: Contextual identification of operating environments (e.g., Commodity Shock, Low-Vol Compression).
4. **Episodic Memory**: Recording and recalling historical analogs to inform current beliefs.
5. **Attention Allocation**: Selective computational focus based on uncertainty, novelty, and systemic importance.
6. **Interpretation**: Generating "Relevance Maps" (Attention Surfaces) that distinguish observation from belief.
7. **Execution**: Signal generation via adaptive agents that scale size by confidence.

## 🚀 Features
- **Data Source**: Fetches live data from FRED (Treasury Yields) and WTI Oil Prices.
- **Thermodynamic Modeling**: Estimates market "disorder" and energy decay rates.
- **Stateful Features**: Features carry memory, confidence, and regime context.
- **Evolving Topology**: Models market variables as dynamic influence graphs.

## 🤖 Agents
- `Epistemic`: **(Primary)** Adaptive agent using the full 7-layer engine to navigate via consensus belief.
- `Billygoat`: Signal based on yield spread Z-scores and entropy baseline.
- `Thermodynamic`: Signal based on decay-dominance (lambda/beta ratio).
- `Commodity Shock`: Signal based on extreme oil price volatility.
- `Integrator`: Consensus-weighted module for legacy signals.

## 🛠 Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Usage
Run the main optimization and comparison script:
```bash
python main.py
```

## 📂 Structure
- `squid/engine.py`: The central **Epistemic Engine** orchestrator.
- `squid/memory.py`: Stateful features, episodic memory, and belief states.
- `squid/regimes.py`: Regime definitions and detection heuristics.
- `squid/topology.py`: Graph-based influence modeling and MarketNodes.
- `squid/thermodynamics.py`: Physics-inspired $\lambda$ and $\beta$ estimation.
- `squid/agents.py`: Adaptive and legacy signal generators.
- `squid/backtest.py`: Backtesting engine with dynamic, decay-based exits.
