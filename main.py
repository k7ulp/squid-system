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

    print(f"Fetched {len(df)} rows. Running Optimization...")
    
    # Run optimization for Billygoat
    print("\n--- Billygoat Agent Results ---")
    results_bg = optimize(df, agent_type="billygoat")
    print(results_bg.head(3))
    
    # Run optimization for Thermodynamic Agent (Fixed Exit)
    print("\n--- Thermodynamic Agent (Fixed Exit) ---")
    results_th_fixed = optimize(df, agent_type="thermodynamic", use_dynamic_exit=False)
    print(results_th_fixed.head(3))

    # Run optimization for Thermodynamic Agent (Dynamic Exit)
    print("\n--- Thermodynamic Agent (Dynamic Exit: Decay/Spikes) ---")
    results_th_dyn = optimize(df, agent_type="thermodynamic", use_dynamic_exit=True)
    print(results_th_dyn.head(3))
    
    # Compare
    if not results_th_dyn.empty and not results_bg.empty:
        best_bg = results_bg.iloc[0]["total_pnl"]
        best_th = results_th_dyn.iloc[0]["total_pnl"]
        print(f"\nBillygoat Best PnL: {best_bg:.4f}")
        print(f"Thermodynamic (Dynamic) Best PnL: {best_th:.4f}")
        winner = "Thermodynamic" if best_th > best_bg else "Billygoat"
        print(f"Overall Winner: {winner}")

if __name__ == "__main__":
    main()
