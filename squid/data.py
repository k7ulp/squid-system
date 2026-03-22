import pandas as pd

def load_fred_data():
    """Load historical Treasury CSVs from data folder"""
    dgs10 = pd.read_csv("data/DGS10.csv")
    dgs5 = pd.read_csv("data/DGS5.csv")
    dgs3m = pd.read_csv("data/DGS3MO.csv")

    # Standardize columns
    for df, name in zip([dgs10, dgs5, dgs3m], ["10Y","5Y","3M"]):
        df.columns = ["Date", name]
        df["Date"] = pd.to_datetime(df["Date"])
        df[name] = pd.to_numeric(df[name], errors="coerce")

    # Merge all tenors
    df = dgs10.merge(dgs5, on="Date").merge(dgs3m, on="Date")
    df = df.dropna()

    # Compute spreads
    df["10Y_5Y"] = df["10Y"] - df["5Y"]
    df["10Y_3M"] = df["10Y"] - df["3M"]

    return df
