import pandas as pd
from squid.features import build_features
from squid.agents import apply_agents
from squid.backtest import run_backtest

def optimize(df, y_candidates=None, slope_thresholds=None, holding_periods=None):
    if y_candidates is None:
        y_candidates = ["10Y_5Y", "10Y_3M"]  
    if slope_thresholds is None:
        slope_thresholds = [0.03] # Simplified for this test
    if holding_periods is None:
        holding_periods = [5, 10, 20, 30, 40]

    results = []

    for y in y_candidates:
        for slope in slope_thresholds:
            for hold in holding_periods:
                temp = build_features(df, y)
                temp = apply_agents(temp, slope)
                trades = run_backtest(temp, holding_period=hold)
                
                if trades.empty:
                    continue
                
                results.append({
                    "y_col": y,
                    "slope_thresh": slope,
                    "holding_days": hold,
                    "trades": len(trades),
                    "total_pnl": trades["PnL"].sum(),
                    "avg_pnl": trades["PnL"].mean()
                })

    return pd.DataFrame(results).sort_values("total_pnl", ascending=False)
