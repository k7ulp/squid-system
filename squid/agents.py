import pandas as pd
import numpy as np

def apply_thermodynamic_agent(df, lambda_beta_min=0.05):
    """
    Thermodynamic Agent:
    - Enter when Z-score is extreme AND lambda/beta ratio is high (decay-dominant).
    - Position sizing proportional to lambda/beta.
    """
    df = df.copy()
    
    # Ratio of decay to injection
    df["lb_ratio"] = df["lambda"] / (df["beta"] + 1e-6)
    
    # ENTRY logic: 
    # lambda > 0 means decay has started.
    # lb_ratio > 0.05 is a conservative threshold given lambda is often small.
    df["Entry_Long"] = (df["Z_Score"] < -2.0) & (df["lb_ratio"] > lambda_beta_min)
    df["Entry_Short"] = (df["Z_Score"] > 2.0) & (df["lb_ratio"] > lambda_beta_min)
    
    # Trade direction
    df["Thermostat"] = np.where(df["Entry_Long"], 1, np.where(df["Entry_Short"], -1, 0))
    
    # Signal for backtester
    df["TradeSignal"] = (df["Entry_Long"] | df["Entry_Short"]).astype(int)
    
    # Position Sizing: Capped to avoid extreme leverage
    df["PositionSize"] = np.clip(df["lb_ratio"] * 10, 0.1, 5.0)
    
    return df

def apply_agents(df, slope_thresh=0.03, agent_type="billygoat"):
    df = df.copy()
    
    if agent_type == "thermodynamic":
        return apply_thermodynamic_agent(df)
    
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
