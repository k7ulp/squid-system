import pandas as pd
from squid.data import load_fred_data
from squid.features import build_features
from squid.optimizer import optimize

def main():
    print("Fetching data from FRED...")
    df = load_fred_data(start="2018-01-01")
    
    if df.empty:
        print("No data fetched. Check your internet connection or FRED status.")
        return

    print(f"Fetched {len(df)} rows. Building features and optimizing...")
    
    # Run optimization across different spreads and thresholds
    results = optimize(df)
    
    print("\nOptimization Results (Top 5):")
    print(results.head(5))
    
    if not results.empty:
        best = results.iloc[0]
        print(f"\nBest configuration:")
        print(f"Target Column: {best['y_col']}")
        print(f"Slope Threshold: {best['slope_thresh']}")
        print(f"Total PnL: {best['total_pnl']:.4f}")

if __name__ == "__main__":
    main()
