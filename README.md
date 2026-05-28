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

## 🌌 Compound Regime Interpretation Engine (v0.2)
The system has moved beyond "flat" regime detection to a **Multi-Axis Phase Space** model. Instead of identifying a single dominant state, Squid now identifies overlapping and nested regimes across seven dimensions:

1. **Monetary**: Policy framework transitions (e.g., Hawkish vs. Neutral).
2. **Liquidity**: Systemic refinancing stress and duration appetite.
3. **Information**: Evolution from legacy broadcast narratives to AI-generated synthetic consensus.
4. **Technological**: Structural productivity shifts (AI Acceleration).
5. **Energy**: Electrification transitions and grid stress sensitivity.
6. **Social**: Institutional synchronization vs. fragmentation.
7. **Geopolitical**: Multipolar realignment and supply chain volatility.

### 📉 The Role of Entropy
Squid monitors **Global Entropy** as a proxy for market "disorder." In the 2020s era, we have observed a structural increase in entropy driven by:
- **Narrative Volatility**: The transition from Social Media to Synthetic (AI) Media regimes.
- **Institutional Decay**: Declining synchronization between monetary policy and fiscal reality.
- **Reflexivity**: AI-accelerated feedback loops that compress signal half-life.

When Entropy is **ELEVATED (>1.5)**, the system automatically shifts to a defensive posture, prioritizing shorter durations (3M/6M) regardless of carry advantage, as historical pricing assumptions lose stability.

### 📄 Sample Output Report
The engine generates a comprehensive **Compound Regime Interpretation Report**. Below is a sample from the current 2026 environment:

```text
====================================================================
 SQUID SYSTEM :: COMPOUND REGIME INTERPRETATION ENGINE v0.2
====================================================================
CONFIDENCE: 0.92          GLOBAL ENTROPY: ELEVATED (2.09)
--------------------------------------------------------------------
 PRIMARY MARKET STATE: AI ACCELERATION
 DURATION RECOMMENDATION: 3M DEFENSIVE
--------------------------------------------------------------------
 COMPOUND REGIME STACK:
  [MONETARY]      Neutral (Stable)
  [LIQUIDITY]     Adequate (Stable)
  [INFORMATION]   Synthetic Media Transition (Accelerating)
  [TECHNOLOGICAL] AI Acceleration (Expansionary)
  [SOCIAL]        Fragmentation (Divergent)
--------------------------------------------------------------------
 REGIME INTERFERENCE MATRIX:
  [AI Productivity] x [Demographic Aging] -> Structural labor contraction offset
  [Liquidity Tightening] x [Narrative Volatility] -> Reduced pricing stability
--------------------------------------------------------------------
 RELEVANCE WEIGHTS:
  Monetary Policy: 0.84    AI Acceleration: 0.79    Liquidity: 0.81
====================================================================
```

## 🚀 Features
- **Data Source**: Fetches comprehensive Treasury data from FRED (3M, 6M, 1Y, 2Y, 5Y, 10Y, 30Y) and WTI Oil Prices.
- **Compound Regime Mapping**: Navigates 7-dimensional phase space to identify overlapping market drivers.
- **Regime Interference Matrix**: Models how conflicting or reinforcing regimes (e.g., AI boom vs. Demographic aging) impact systemic stability.
- **Interpretive Navigation**: Moves beyond signal generation to explain market topology and "what matters right now."
- **Treasury Duration Module**: Analyzes carry vs. risk tradeoffs to recommend optimal duration based on multi-axis regime state.
- **Thermodynamic Modeling**: Estimates market "disorder" and energy decay rates ($\lambda$, $\beta$).

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
