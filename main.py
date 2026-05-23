import pandas as pd
import argparse
from squid.data import load_fred_data
from squid.features import build_features
from squid.optimizer import optimize
from squid.engine import EpistemicEngine
from squid.viz import plot_yield_curve, plot_relevance_surface, plot_entropy_dashboard

def run_interpretive_mode(df):
    """
    Runs the Epistemic Engine on the latest data and generates interpretive outputs.
    """
    print("\n--- SQUID INTERPRETIVE MODE ---")
    engine = EpistemicEngine()
    
    # Warm up engine with historical data to build states
    print("Warming up engine...")
    for i in range(len(df) - 1):
        engine.process_step(df.iloc[i])
        
    # Generate report for the latest data point
    latest_row = df.iloc[-1]
    report = engine.generate_interpretive_report(latest_row)
    
    # Output Report
    print(report.generate_summary())
    
    # Generate Visualizations
    print("\nGenerating visualizations...")
    plot_yield_curve(df)
    plot_relevance_surface(engine.belief.relevance_map)
    plot_entropy_dashboard(df)
    print("Visualizations saved to outputs/ folder.")

def main():
    parser = argparse.ArgumentParser(description="Squid System: Adaptive Epistemic Engine")
    parser.add_argument("--interpret", action="store_true", help="Run in interpretive navigation mode")
    parser.add_argument("--start", type=str, default="2018-01-01", help="Start date for data fetching")
    args = parser.parse_args()

    print(f"Fetching data from FRED starting {args.start}...")
    df_raw = load_fred_data(start=args.start)
    
    if df_raw.empty:
        print("No data fetched. Check your internet connection or FRED status.")
        return

    print(f"Fetched {len(df_raw)} rows. Building features...")
    df = build_features(df_raw)

    if args.interpret:
        run_interpretive_mode(df)
        return

    print(f"Features built. Running Optimization...")
    
    # Run optimization for Billygoat
    print("\n--- Billygoat Agent Results ---")
    results_bg = optimize(df, agent_type="billygoat")
    if not results_bg.empty: print(results_bg.head(3))
    
    # Run optimization for Thermodynamic Agent (Fixed Exit)
    print("\n--- Thermodynamic Agent (Fixed Exit) ---")
    results_th_fixed = optimize(df, agent_type="thermodynamic", use_dynamic_exit=False)
    if not results_th_fixed.empty: print(results_th_fixed.head(3))

    # Run optimization for Thermodynamic Agent (Dynamic Exit)
    print("\n--- Thermodynamic Agent (Dynamic Exit: Decay/Spikes) ---")
    results_th_dyn = optimize(df, agent_type="thermodynamic", use_dynamic_exit=True)
    if not results_th_dyn.empty: print(results_th_dyn.head(3))

    # Run optimization for Commodity Shock Agent
    print("\n--- Commodity Shock Agent Results ---")
    results_cs = optimize(df, agent_type="commodity_shock")
    if not results_cs.empty: print(results_cs.head(3))

    # Run optimization for Integrated Agent
    print("\n--- Integrated Agent Results ---")
    results_int = optimize(df, agent_type="integrated")
    if not results_int.empty: print(results_int.head(3))

    # Run optimization for Epistemic Agent
    print("\n--- Epistemic (Adaptive) Agent Results ---")
    results_epi = optimize(df, agent_type="epistemic")
    if not results_epi.empty: print(results_epi.head(3))
    
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

if __name__ == "__main__":
    main()
