import pandas as pd
import datetime

def load_fred_data(start="2020-01-01", end=None):
    """Fetch historical Treasury data from FRED via CSV URLs"""
    if end is None:
        end = datetime.date.today().strftime("%Y-%m-%d")
    
    # FRED series IDs
    series = {
        "DGS30": "30Y",
        "DGS10": "10Y",
        "DGS5": "5Y",
        "DGS2": "2Y",
        "DGS1": "1Y",
        "DGS6MO": "6M",
        "DGS3MO": "3M",
        "DCOILWTICO": "Oil"
    }
    
    dfs = []
    for s_id, label in series.items():
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s_id}"
        try:
            # Fetch CSV and parse dates
            df_s = pd.read_csv(url)
            df_s.columns = ["Date", label]
            df_s["Date"] = pd.to_datetime(df_s["Date"])
            # Filter by date
            df_s = df_s[df_s["Date"] >= pd.to_datetime(start)]
            dfs.append(df_s)
        except Exception as e:
            print(f"Error fetching {s_id} from FRED: {e}")
            continue

    if not dfs:
        return pd.DataFrame(columns=["Date", "30Y", "10Y", "5Y", "2Y", "1Y", "6M", "3M", "Oil"])

    # Merge all series on Date
    df = dfs[0]
    for next_df in dfs[1:]:
        df = df.merge(next_df, on="Date", how="outer")
    
    df = df.sort_values("Date").reset_index(drop=True)
    
    # Standardize types
    for col in ["30Y", "10Y", "5Y", "2Y", "1Y", "6M", "3M", "Oil"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    df = df.dropna()

    # Compute spreads
    if "10Y" in df.columns and "2Y" in df.columns:
        df["10Y_2Y"] = df["10Y"] - df["2Y"]
    if "10Y" in df.columns and "3M" in df.columns:
        df["10Y_3M"] = df["10Y"] - df["3M"]
    if "6M" in df.columns and "3M" in df.columns:
        df["6M_3M"] = df["6M"] - df["3M"]

    return df
