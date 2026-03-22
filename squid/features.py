def build_features(df, y_col="10Y_3M"):
    df = df.copy()
    df["y"] = df[y_col]
    df["Slope"] = df["y"].diff()
    df["Curvature"] = df["Slope"].diff()
    df["Entropy"] = df["y"].rolling(5).std()
    return df.dropna()
