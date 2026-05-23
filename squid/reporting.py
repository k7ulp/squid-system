import pandas as pd

class RelevanceReport:
    """
    Generates human-readable interpretive summaries of market topology.
    """
    def __init__(self, regime, confidence, relevance_map, entropy, duration_analysis):
        self.regime = regime
        self.confidence = confidence
        self.relevance_map = relevance_map
        self.entropy = entropy
        self.duration_analysis = duration_analysis

    def generate_summary(self):
        """
        Synthesizes state into a readable report.
        """
        # Get dominant variables
        sorted_rel = pd.Series(self.relevance_map).sort_values(ascending=False)
        dominant = sorted_rel.head(3).index.tolist()
        
        # Determine confidence level
        conf_str = "High" if self.confidence > 0.8 else "Medium" if self.confidence > 0.5 else "Low"
        
        # Entropy description
        ent_desc = "elevated" if self.entropy > 1.5 else "moderate" if self.entropy > 0.8 else "stable/low"
        
        report = []
        report.append("=== SQUID RELEVANCE REPORT ===")
        report.append(f"Regime: {self.regime.upper()}")
        report.append(f"Confidence: {conf_str} ({self.confidence:.2f})")
        report.append(f"Market Entropy: {ent_desc.upper()} ({self.entropy:.2f})")
        report.append("-" * 30)
        
        report.append("TOPOLOGICAL INTERPRETATION:")
        report.append(f"Current market topology is dominated by: {', '.join(dominant)}.")
        if "Oil_Shock" in dominant:
            report.append("- Energy volatility is a primary driver of systemic uncertainty.")
        if "Z_Score" in dominant:
            report.append("- Mean-reversion energy (yield stretch) is currently highly relevant.")
        if "Entropy" in dominant:
            report.append("- Systemic 'noise' and disorder are influencing attention allocation.")
        
        report.append("-" * 30)
        report.append("TREASURY DURATION NAVIGATOR:")
        pref = self.duration_analysis["preference"]
        reason = self.duration_analysis["reason"]
        metrics = self.duration_analysis["metrics"]
        
        report.append(f"Recommended Duration Preference: {pref.upper()}")
        report.append(f"RATIONALE: {reason}")
        report.append(f"Key Metrics:")
        report.append(f"  * Carry Advantage: {metrics['carry_bps']:.1f} bps")
        report.append(f"  * Reinvestment Risk (Short-end): {metrics['reinvest_risk_a']:.1f}x roll frequency")
        report.append(f"  * Principal Sensitivity: {metrics['dur_sensitivity_b']:.1f}% per 100bps yield move")
        
        report.append("=" * 30)
        
        return "\n".join(report)
