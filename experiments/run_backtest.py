from squid.data import load_fred_data
from squid.optimizer import optimize

# Load real FRED data
df = load_fred_data()

# Candidate features
df["y_raw"] = df["10Y_3M"]
df["y_smooth"] = df["10Y_3M"].rolling(5).mean()
df["y_vol_adj"] = df["10Y_3M"] / (df["10Y_3M"].rolling(5).std() + 1e-5)
df = df.dropna()

# Run optimizer
results = optimize(
    df,
    y_candidates=["y_raw", "y_smooth", "y_vol_adj", "10Y_5Y", "10Y_3M"],
    slope_thresholds=[0.01, 0.02, 0.03, 0.05]
)

print("\n=== TOP STRATEGIES ===")
print(results.head())
