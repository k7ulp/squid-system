import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def estimate_lambda(series, window=10):
    """
    Estimate lambda (intrinsic decay rate) using rolling regression.
    ln(E(t)) = ln(E0) - lambda * t
    """
    # Use absolute Z-score as mispricing energy
    E = np.abs(series).replace(0, 1e-6)
    ln_E = np.log(E)
    
    lambdas = np.zeros(len(series))
    
    for i in range(window, len(series)):
        window_data = ln_E[i-window:i]
        if window_data.isna().any() or np.isinf(window_data).any():
            continue
            
        y = window_data.values.reshape(-1, 1)
        X = np.arange(window).reshape(-1, 1)
        
        try:
            model = LinearRegression()
            model.fit(X, y)
            # lambda = -slope. We want to detect if it IS decaying.
            # If it's increasing, lambda is 0 (no decay).
            lambdas[i] = max(0, -model.coef_[0][0])
        except:
            continue
        
    return lambdas

def estimate_beta(df, window=20):
    """
    Estimate beta (systemic entropy injection rate).
    """
    # Proxy 1: Rolling volatility of the slope
    vol = df["Slope"].rolling(window).std()
    
    # Proxy 2: Shannon Entropy
    entropy_feat = df["Entropy"] if "Entropy" in df.columns else vol
        
    # Combine and normalize, with a floor to avoid explosion
    vol_norm = vol / (vol.rolling(100).mean() + 1e-6)
    ent_norm = entropy_feat / (entropy_feat.rolling(100).mean() + 1e-6)
    
    beta = (vol_norm.fillna(0) + ent_norm.fillna(0)) / 2
    # Cap beta to avoid extreme values and floor it
    return np.clip(beta, 0.1, 5.0)
