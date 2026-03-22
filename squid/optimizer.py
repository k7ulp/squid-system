import pandas as pd
from squid.features import build_features
from squid.agents import apply_agents
from squid.backtest import run_backtest

def optimize(df, y_candidates=None, slope_thresholds=None):
    if y_candidates is None:
        y_candidates = ["10Y_3M", "10Y_5Y", "10Y_3M"]  # can include spreads
    if slope_thresholds is None:
        slope_thresholds = [0.01, 0.02, 0.03, 0.05]

    results = []

    for y in y_candidates:
        for slope in slope_thresholds:
            temp = build_features(df, y)
            temp = apply_agents(temp, slope)
            trades = run_backtest(temp)
            if trades.empty:
                continue
            results.append({
                "y_col": y,
                "slope_thresh": slope,
                "trades": len(trades),
                "total_pnl": trades["PnL"].sum(),
                "avg_pnl": trades["PnL"].mean()
            })

    return pd.DataFrame(results).sort_values("total_pnl", ascending=False)
