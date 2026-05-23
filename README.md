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
- **Data Source**: Fetches comprehensive Treasury data from FRED (3M, 6M, 1Y, 2Y, 5Y, 10Y, 30Y) and WTI Oil Prices.
- **Interpretive Navigation**: Moves beyond signal generation to explain market topology and "what matters right now."
- **Treasury Duration Module**: Analyzes carry vs. risk tradeoffs to recommend optimal duration (e.g., 3M vs 6M) based on entropy and regime.
- **Thermodynamic Modeling**: Estimates market "disorder" and energy decay rates ($\lambda$, $\beta$).
- **Graphical Reporting**: Generates automated dashboards for yield curve topology, attention surfaces, and entropy metrics.

## 🤖 Agents
- `Epistemic`: **(Primary)** Adaptive agent using the full 7-layer engine to navigate via consensus belief.
- `Duration Navigator`: Specialized module for Treasury duration comparison and risk-adjusted positioning.
- `Thermodynamic`: Signal based on decay-dominance (lambda/beta ratio).
- `Commodity Shock`: Signal based on extreme oil price volatility.
- `Integrator`: Consensus-weighted module for legacy signals.

## 🛠 Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Usage
### 1. Interpretive Mode (Navigation Terminal)
Run the engine on the latest data to generate a human-readable **Relevance Report** and graphical dashboard:
```bash
python main.py --interpret
```
Outputs are saved to the `outputs/` directory.

### 2. Optimization Mode (Backtesting)
Run the main optimization and signal comparison script:
```bash
python main.py
```

## 📂 Structure
- `squid/engine.py`: The central **Epistemic Engine** orchestrator.
- `squid/analysis.py`: **(New)** Treasury Duration Analyzer and risk-reward logic.
- `squid/reporting.py`: **(New)** Human-readable Relevance Report generator.
- `squid/viz.py`: **(New)** Visualization layer for graphical macro navigation.
- `squid/memory.py`: Stateful features, episodic memory, and belief states.
- `squid/regimes.py`: Regime definitions and detection heuristics.
- `squid/topology.py`: Graph-based influence modeling and MarketNodes.
- `squid/thermodynamics.py`: Physics-inspired $\lambda$ and $\beta$ estimation.
- `squid/agents.py`: Adaptive and legacy signal generators.
- `squid/backtest.py`: Backtesting engine with dynamic, decay-based exits.
