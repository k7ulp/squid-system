import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def plot_yield_curve(df, output_path="squid-system/outputs/yield_curve.png"):
    """
    Plots the current yield curve vs recent historical analogs.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    maturities = ["3M", "6M", "1Y", "2Y", "5Y", "10Y", "30Y"]
    available_mats = [m for m in maturities if m in df.columns]
    
    if not available_mats:
        return

    latest = df.iloc[-1][available_mats]
    prev_1m = df.iloc[-22][available_mats] if len(df) > 22 else None
    prev_6m = df.iloc[-126][available_mats] if len(df) > 126 else None
    
    plt.figure(figsize=(10, 6))
    plt.plot(available_mats, latest.values, marker='o', linestyle='-', label='Current', color='blue', linewidth=2)
    
    if prev_1m is not None:
        plt.plot(available_mats, prev_1m.values, marker='s', linestyle='--', label='1 Month Ago', color='gray', alpha=0.7)
    if prev_6m is not None:
        plt.plot(available_mats, prev_6m.values, marker='^', linestyle=':', label='6 Months Ago', color='lightgray', alpha=0.5)
        
    plt.title("Treasury Yield Curve Topology", fontsize=14)
    plt.xlabel("Maturity", fontsize=12)
    plt.ylabel("Yield (%)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig(output_path)
    plt.close()

def plot_relevance_surface(relevance_map, output_path="squid-system/outputs/relevance_surface.png"):
    """
    Visualizes what variables currently dominate attention.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    rel_series = pd.Series(relevance_map).sort_values()
    
    plt.figure(figsize=(8, 6))
    rel_series.plot(kind='barh', color='teal')
    plt.title("Attention Surface: What Matters Right Now?", fontsize=14)
    plt.xlabel("Attention Weight", fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_entropy_dashboard(df, output_path="squid-system/outputs/entropy_dashboard.png"):
    """
    Shows market disorder and thermodynamic metrics over time.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    if "Entropy" not in df.columns or "lambda" not in df.columns:
        return
        
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
    
    # Subplot 1: Entropy
    ax1.plot(df["Date"], df["Entropy"], color='purple', label='Shannon Entropy')
    ax1.axhline(y=df["Entropy"].mean(), color='r', linestyle='--', alpha=0.5, label='Mean Entropy')
    ax1.set_title("Systemic Entropy (Market Disorder)", fontsize=14)
    ax1.set_ylabel("Entropy Units")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Thermodynamics
    ax2.plot(df["Date"], df["lambda"], color='orange', label='Lambda (Decay)')
    ax2.plot(df["Date"], df["beta"], color='cyan', label='Beta (Injection)', alpha=0.6)
    ax2.set_title("Thermodynamic Stability Metrics", fontsize=14)
    ax2.set_ylabel("Rate")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
