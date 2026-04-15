import pandas as pd
import numpy as np

def apply_agents(df, slope_thresh=0.03):
    df = df.copy()
    
    # 1. Calculate an "Entropy Baseline"
    df["Entropy_MA"] = df["Entropy"].rolling(50).mean()
    
    # 2. ENTRY SIGNAL:
    # - Spread is overstretched (Z_Score > 2.0 or < -2.0)
    # - Entropy is higher than average (Energy for a move)
    df["Entry_Long"] = (df["Z_Score"] < -2.0) & (df["Entropy"] > df["Entropy_MA"])
    df["Entry_Short"] = (df["Z_Score"] > 2.0) & (df["Entropy"] > df["Entropy_MA"])
    
    # 3. SET TradeSignal
    df["TradeSignal"] = (df["Entry_Long"] | df["Entry_Short"]).astype(int)
    
    # 4. SET Billygoat as the trade direction
    # If Entry_Long, direction is +1. If Entry_Short, direction is -1.
    df["Billygoat"] = np.where(df["Entry_Long"], 1, np.where(df["Entry_Short"], -1, 0))
    
    return df
