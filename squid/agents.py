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

def apply_commodity_shock_agent(df, shock_thresh=2.0):
    """
    Commodity Shock Agent:
    - Signals based on extreme oil price moves (Oil_Shock).
    - Large positive shock -> inflation expectation up -> yields likely up.
    """
    df = df.copy()
    
    # ENTRY logic
    df["Entry_Long"] = df["Oil_Shock"] > shock_thresh
    df["Entry_Short"] = df["Oil_Shock"] < -shock_thresh
    
    # Trade direction
    df["ShockSignal"] = np.where(df["Entry_Long"], 1, np.where(df["Entry_Short"], -1, 0))
    
    # Signal for backtester
    df["TradeSignal"] = (df["Entry_Long"] | df["Entry_Short"]).astype(int)
    
    return df

def apply_integrated_agent(df):
    """
    Integrator Agent (Weighted):
    - Compiles signals from Billygoat, Thermodynamic, and Commodity Shock.
    - Any agent can trigger a trade.
    - Position size is scaled by consensus.
    """
    df = df.copy()
    
    # Get individual signals
    # Billygoat
    df = apply_agents(df, agent_type="billygoat")
    df["BG_Dir"] = df["Billygoat"]
    
    # Thermodynamic
    df = apply_thermodynamic_agent(df)
    df["TH_Dir"] = df["Thermostat"]
    
    # Commodity Shock
    df = apply_commodity_shock_agent(df)
    df["CS_Dir"] = df["ShockSignal"]
    
    # Integrated Direction: 
    # If they conflict, the majority wins or they cancel out.
    df["Sum_Dir"] = df["BG_Dir"] + df["TH_Dir"] + df["CS_Dir"]
    
    # ENTRY logic: Trigger if ANY agent has a signal
    df["Entry_Long"] = df["Sum_Dir"] > 0
    df["Entry_Short"] = df["Sum_Dir"] < 0
    
    # Final Integrated Direction
    df["Integrated_Dir"] = np.where(df["Entry_Long"], 1, np.where(df["Entry_Short"], -1, 0))
    
    # Position Sizing: Base size 1.0, +1.0 for each additional agreeing agent
    # If Sum_Dir is 2, it means 2 agents agree (or 3 agree and 1 conflicts, etc.)
    # Let's just use absolute Sum_Dir as a simple multiplier.
    df["PositionSize"] = np.abs(df["Sum_Dir"]).clip(1, 3).astype(float)
    
    # Signal for backtester
    df["TradeSignal"] = (df["Entry_Long"] | df["Entry_Short"]).astype(int)
    
    return df

def apply_epistemic_agent(df, engine):
    """
    Epistemic Agent:
    - Uses the EpistemicEngine to generate a BeliefState for every step.
    - Decisions are based on consensus relevance and confidence.
    """
    df = df.copy()
    signals = []
    directions = []
    sizes = []
    
    for _, row in df.iterrows():
        belief = engine.process_step(row)
        
        # Logic: If confidence is high and a relevant feature is stretched
        # This is a simplified version of the epistemic reasoning
        relevance = belief.relevance_map
        oil_rel = relevance.get("Oil_Shock", 0)
        z_rel = relevance.get("Z_Score", 0)
        
        signal = 0
        direction = 0
        size = 1.0
        
        if belief.confidence > 0.6:
            # If Oil is highly relevant (Commodity Shock regime)
            if oil_rel > 0.7:
                if row.get("Oil_Shock", 0) > 2.0:
                    signal = 1
                    direction = 1
                elif row.get("Oil_Shock", 0) < -2.0:
                    signal = 1
                    direction = -1
            
            # If Z_Score is highly relevant (Low Vol regime)
            elif z_rel > 0.6:
                if row.get("Z_Score", 0) < -2.0:
                    signal = 1
                    direction = 1
                elif row.get("Z_Score", 0) > 2.0:
                    signal = 1
                    direction = -1
                    
        signals.append(signal)
        directions.append(direction)
        sizes.append(belief.confidence * 2.0) # Size scales with confidence
        
    df["TradeSignal"] = signals
    df["Epistemic_Dir"] = directions
    df["PositionSize"] = sizes
    
    return df

def apply_agents(df, slope_thresh=0.03, agent_type="billygoat", engine=None):
    df = df.copy()
    
    if agent_type == "epistemic" and engine is not None:
        return apply_epistemic_agent(df, engine)
    
    if agent_type == "thermodynamic":
        return apply_thermodynamic_agent(df)
    
    if agent_type == "commodity_shock":
        return apply_commodity_shock_agent(df)
    
    if agent_type == "integrated":
        return apply_integrated_agent(df)
    
    # Default: Billygoat logic
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
