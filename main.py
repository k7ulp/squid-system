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

    # Run optimization for Commodity Shock Agent
    print("\n--- Commodity Shock Agent Results ---")
    results_cs = optimize(df, agent_type="commodity_shock")
    print(results_cs.head(3))

    # Run optimization for Integrated Agent
    print("\n--- Integrated Agent Results ---")
    results_int = optimize(df, agent_type="integrated")
    print(results_int.head(3))

    # Run optimization for Epistemic Agent
    print("\n--- Epistemic (Adaptive) Agent Results ---")
    results_epi = optimize(df, agent_type="epistemic")
    print(results_epi.head(3))
    
    # Compare
    comparison = []
    if not results_bg.empty: comparison.append(("Billygoat", results_bg.iloc[0]["total_pnl"]))
    if not results_th_dyn.empty: comparison.append(("Thermodynamic", results_th_dyn.iloc[0]["total_pnl"]))
    if not results_cs.empty: comparison.append(("Commodity Shock", results_cs.iloc[0]["total_pnl"]))
    if not results_int.empty: comparison.append(("Integrated", results_int.iloc[0]["total_pnl"]))
    if not results_epi.empty: comparison.append(("Epistemic", results_epi.iloc[0]["total_pnl"]))

    if comparison:
        print("\n--- Final Comparison (Best Total PnL) ---")
        for name, pnl in comparison:
            print(f"{name}: {pnl:.4f}")
        
        winner = max(comparison, key=lambda x: x[1])
        print(f"\nOverall Winner: {winner[0]} with PnL {winner[1]:.4f}")

if __name__ == "__main__":
    main()
