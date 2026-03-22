import pandas as pd

def run_backtest(df):
    trades = []
    in_trade = False

    for i in range(len(df)):
        row = df.iloc[i]

        # Entry: glass fills
        if not in_trade and row["TradeSignal"] == 1:
            entry_price = row["y"]
            entry_date = row["Date"]
            entry_idx = i
            in_trade = True
            continue

        # Exit: curvature flips negative
        if in_trade:
            if row["Curvature"] < 0:
                exit_price = row["y"]
                exit_date = row["Date"]
                trades.append({
                    "Entry_Date": entry_date,
                    "Exit_Date": exit_date,
                    "Entry_Price": entry_price,
                    "Exit_Price": exit_price,
                    "PnL": exit_price - entry_price,
                    "Duration": i - entry_idx
                })
                in_trade = False

    return pd.DataFrame(trades)
