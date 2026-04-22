import pandas as pd
import numpy as np

def run_backtest(df, holding_period=10, use_dynamic_exit=False):
    """
    Backtest with optional dynamic exit logic.
    - Decay completion: Z-score returns to near-zero.
    - Beta spike: External entropy injection disrupts the trade.
    """
    trades = []
    in_trade = False
    entry_price = 0
    entry_date = None
    entry_idx = 0
    direction = 0 
    pos_size = 1.0

    # Determine direction column
    dir_col = "Billygoat"
    if "Thermostat" in df.columns:
        dir_col = "Thermostat"

    # For beta spike detection (rolling mean of beta)
    beta_ma = df["beta"].rolling(50).mean() if "beta" in df.columns else None

    for i in range(len(df)):
        row = df.iloc[i]

        # ENTRY logic
        if not in_trade and row["TradeSignal"] == 1:
            direction = row[dir_col]
            entry_price = row["y"]
            entry_date = row["Date"]
            entry_idx = i
            in_trade = True
            pos_size = row.get("PositionSize", 1.0)
            continue

        # EXIT logic
        if in_trade:
            exit_trigger = False
            exit_reason = "Fixed Time"

            if use_dynamic_exit:
                # 1. Decay Completion: Z-score moves back towards 0
                if abs(row["Z_Score"]) < 0.5:
                    exit_trigger = True
                    exit_reason = "Decay Completion"
                
                # 2. Beta Spike: beta significantly higher than its average
                elif beta_ma is not None and row["beta"] > (beta_ma.iloc[i] * 2.0):
                    exit_trigger = True
                    exit_reason = "Beta Spike"
            
            # 3. Fixed time exit (fallback)
            if not exit_trigger and (i - entry_idx) >= holding_period:
                exit_trigger = True
                exit_reason = "Fixed Time"

            if exit_trigger:
                exit_price = row["y"]
                exit_date = row["Date"]
                pnl = (exit_price - entry_price) * direction * pos_size
                
                trades.append({
                    "Entry_Date": entry_date,
                    "Exit_Date": exit_date,
                    "Entry_Price": entry_price,
                    "Exit_Price": exit_price,
                    "Direction": "Long" if direction == 1 else "Short",
                    "PnL": pnl,
                    "PosSize": pos_size,
                    "Duration": i - entry_idx,
                    "Exit_Reason": exit_reason
                })
                in_trade = False

    return pd.DataFrame(trades)
