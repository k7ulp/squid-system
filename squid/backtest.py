import pandas as pd

def run_backtest(df, holding_period=10):
    """
    Backtest with a fixed time-based exit.
    """
    trades = []
    in_trade = False
    entry_price = 0
    entry_date = None
    entry_idx = 0
    direction = 0 

    for i in range(len(df)):
        row = df.iloc[i]

        # ENTRY logic: Triggered by Z-Score extremes (Mean Reversion)
        if not in_trade and row["TradeSignal"] == 1:
            direction = row["Billygoat"]
            entry_price = row["y"]
            entry_date = row["Date"]
            entry_idx = i
            in_trade = True
            continue

        # EXIT logic: Fixed time-based exit
        if in_trade:
            # Exit after fixed number of days
            if (i - entry_idx) >= holding_period:
                exit_price = row["y"]
                exit_date = row["Date"]
                pnl = (exit_price - entry_price) * direction
                
                trades.append({
                    "Entry_Date": entry_date,
                    "Exit_Date": exit_date,
                    "Entry_Price": entry_price,
                    "Exit_Price": exit_price,
                    "Direction": "Long" if direction == 1 else "Short",
                    "PnL": pnl,
                    "Duration": i - entry_idx
                })
                in_trade = False

    return pd.DataFrame(trades)
