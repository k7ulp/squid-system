# Squid System: Adaptive Epistemic Engine

Squid is a physics-inspired trading system that has evolved from deterministic forecasting toward **Adaptive Epistemology**. It moves away from asking "What will happen?" to continuously asking "**What matters right now?**"

## 🧠 Core Philosophy: Adaptive Epistemology
The system operates on a 7-layer hierarchy designed to handle market complexity through navigation rather than prediction:
1. **Perception**: Raw data ingestion from FRED and energy markets.
2. **State Physics**: Computation of Shannon Entropy, intrinsic decay ($\lambda$), and systemic injection ($\beta$).
3. **Regime Detection**: Contextual identification of operating environments using **ZFC Set-Theoretic** formalization.
4. **Episodic Memory**: Recording and recalling historical analogs to inform current beliefs.
5. **Alignment & Selection**: Evaluating trajectories via the **Alignment Layer** (Coherent vs. Entropic) and the **Coherence Filter** (Ultrafilter).
6. **Interpretation**: Generating "Relevance Maps" (Attention Surfaces) and analytical **Alignment Reports**.
7. **Execution**: Signal generation via adaptive agents that scale size by confidence.

## 🌌 Compound Regime Interpretation Engine (v0.3)
The engine has been upgraded to include formal mathematical foundations:

### 1. ZFC Set-Theoretic Regimes
Regimes are no longer just labels; they are formalized as **Sets** ($R$) with explicit **Membership Relation** ($x \in R$). This enables rigorous modeling of regime overlap and nesting using set operations:
- **Intersection ($\cap$)**: Identifying the precise compound state of active forces.
- **Union ($\cup$)**: Mapping the entire reachable macro state space.

### 2. Alignment Layer (Coherent vs. Entropic)
An analytical framework that evaluates market forces based on their contribution to systemic stability. It replaces subjective terminology with an objective **Alignment Gradient**:
- **Coherent**: Trajectories that contribute to resilience, productivity, and institutional stability.
- **Destabilizing**: Forces that amplify entropy and decay trust.
- **Neutral**: Trajectories with balanced or negligible systemic impact.

### 3. Coherence Selection (The Ultrafilter)
Inspired by the **Gödel Ultrafilter**, this mechanism selects which subsets of regime trajectories belong to a "stable coherent future set." It acts as a high-order selection process for market navigation.

## 📉 The Role of Entropy
Squid monitors **Global Entropy** as a proxy for market "disorder." In the 2020s era, we have observed a structural increase in entropy driven by:
- **Narrative Volatility**: The transition from Social Media to Synthetic (AI) Media regimes.
- **Institutional Decay**: Declining synchronization between monetary policy and fiscal reality.
- **Reflexivity**: AI-accelerated feedback loops that compress signal half-life.

## 📄 Sample Output Report
The engine generates a comprehensive **Compound Regime Interpretation Report**. Below is a sample from the current 2026 environment:

```text
====================================================================
 SQUID SYSTEM :: COMPOUND REGIME INTERPRETATION ENGINE v0.3
====================================================================
CONFIDENCE: 1.00          GLOBAL ENTROPY: ELEVATED (2.09)
--------------------------------------------------------------------
 PRIMARY MARKET STATE: AI ACCELERATION
 DURATION RECOMMENDATION: 3M DEFENSIVE
--------------------------------------------------------------------
 ALIGNMENT ANALYSIS (Coherent vs Entropic)
--------------------------------------------------------------------
 FORCE: COMPUTE_DEMAND
  Status:       COHERENT
  Metrics:
    resilience                +0.50
    productivity              +0.30
    entropy_effect            -0.50
    long_term_stability       +0.40

 FORCE: NARRATIVE_FRAGMENTATION
  Status:       DESTABILIZING (Threshold Analysis Applied)
--------------------------------------------------------------------
 COMPOUND REGIME STACK (ZFC Sets)
--------------------------------------------------------------------
 [MONETARY]      Neutral (Stable)
 [LIQUIDITY]     Adequate (Stable)
 [INFORMATION]   Synthetic Media Transition {meme_volatility, narrative_fragmentation}
 [TECHNOLOGICAL] AI Acceleration {capex_concentration, compute_demand, labor_displacement}
 [SOCIAL]        Fragmentation {polarization, trust_decay}
--------------------------------------------------------------------
 REGIME INTERFERENCE MATRIX:
  [AI Productivity] x [Demographic Aging] -> Structural labor contraction offset
--------------------------------------------------------------------
 RELEVANCE WEIGHTS:
  Monetary Policy: 0.84    AI Acceleration: 0.79    Liquidity: 0.81
====================================================================
```

## 🚀 Features
- **Data Source**: Fetches comprehensive Treasury data from FRED and WTI Oil Prices.
- **ZFC Regime Mapping**: Formal set-theoretic identification of overlapping market drivers.
- **Alignment Layer**: Analytical evaluation of coherence vs. entropy for all active forces.
- **Ultrafilter Selection**: Selection of stable trajectories for long-horizon navigation.
- **Treasury Duration Module**: Analyzes carry vs. risk tradeoffs based on multi-axis regime state.

## 🤖 Agents
- `Epistemic`: **(Primary)** Adaptive agent using the full 7-layer engine to navigate via consensus belief and alignment.
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
- `squid/alignment.py`: **(New)** Alignment Layer and Coherence Filter (Ultrafilter).
- `squid/regimes.py`: ZFC Set-theoretic regime definitions and detection.
- `squid/reporting.py`: Enhanced Human-readable Relevance Report generator.
- `squid/memory.py`: Belief state management including alignment analysis.
- `squid/topology.py`: Graph-based influence modeling and MarketNodes.
- `squid/thermodynamics.py`: Physics-inspired $\lambda$ and $\beta$ estimation.
- `squid/agents.py`: Adaptive and legacy signal generators.
- `squid/backtest.py`: Backtesting engine with dynamic, decay-based exits.
