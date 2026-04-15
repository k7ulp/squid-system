import numpy as np
from scipy.stats import entropy

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
    
    return df.dropna()
