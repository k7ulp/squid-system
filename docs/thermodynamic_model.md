# A Thermodynamic Market Model for Statistical Arbitrage
## Intrinsic Decay (lambda) and Systemic Entropy Injection (beta)

### System Overview
Markets are modeled as open thermodynamic systems. Mispricing represents structured deviation. Arbitrage represents correction. External events act as entropy injections.

### Core Variables
*   **lambda ($\lambda$):** Intrinsic decay rate. Mispricing decays according to $E(t) = E_0 \cdot e^{-\lambda t}$. High $\lambda$ implies fast correction.
*   **beta ($\beta$):** Systemic volatility and external perturbations (macro shocks, liquidity events, etc.).

### Dynamic System Model
$dE/dt = -\lambda \cdot E + \beta \cdot \xi(t)$

### Trading Rules
*   **Entry:** Enter when Z-score threshold is exceeded and $\lambda$ is high relative to $\beta$.
*   **Sizing:** Position sizing proportional to $\lambda / \beta$.
*   **Exit:** Exit on decay completion or $\beta$ spikes.
