import numpy as np
from scipy.stats import entropy
from squid.thermodynamics import estimate_lambda, estimate_beta

def calculate_shannon_entropy(series, bins=10):
    """Calculate Shannon Entropy of a series by binning values"""
    if series.isnull().any():
        return np.nan
    counts, _ = np.histogram(series, bins=bins)
    probs = counts / counts.sum()
    return entropy(probs)

def build_features(df, y_col="10Y_3M"):
    df = df.copy()
    df["y"] = df[y_col]
    df["Slope"] = df["y"].diff()
    df["Curvature"] = df["Slope"].diff()
    
    # Entropy: Measuring market "disorder"
    df["Entropy"] = df["Slope"].rolling(20).apply(calculate_shannon_entropy)
    
    # Z-Score: Measuring how "stretched" the spread is
    df["MA"] = df["y"].rolling(50).mean()
    df["STD"] = df["y"].rolling(50).std()
    df["Z_Score"] = (df["y"] - df["MA"]) / df["STD"]
    
    # Thermodynamic Features
    df["lambda"] = estimate_lambda(df["Z_Score"])
    df["beta"] = estimate_beta(df)
    
    # Oil Shock Features
    if "Oil" in df.columns:
        df["Oil_Return"] = df["Oil"].pct_change()
        df["Oil_5D_Change"] = df["Oil"].pct_change(5)
        df["Oil_Vol"] = df["Oil_Return"].rolling(20).std()
        df["Oil_Shock"] = (df["Oil_5D_Change"] - df["Oil_5D_Change"].rolling(50).mean()) / (df["Oil_5D_Change"].rolling(50).std() + 1e-6)
    
    return df.dropna()
