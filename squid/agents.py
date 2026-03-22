import pandas as pd

def billygoat(slope, threshold=0.03):
    if slope > threshold:
        return 1
    elif slope < -threshold:
        return -1
    return 0

def squid(entropy_diff):
    if pd.isna(entropy_diff):
        return 0
    return 1 if entropy_diff > 0 else (-1 if entropy_diff < 0 else 0)

def apply_agents(df, slope_thresh=0.03):
    df = df.copy()
    df["Billygoat"] = df["Slope"].apply(lambda x: billygoat(x, slope_thresh))
    df["Squid"] = df["Entropy"].diff().apply(squid)
    df["Accum"] = df["Billygoat"].rolling(3).sum()
    df["TradeSignal"] = df["Accum"].apply(lambda x: 1 if x >= 2 else 0)
    return df
