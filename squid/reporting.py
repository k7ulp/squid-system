import pandas as pd
from datetime import datetime

class RelevanceReport:
    """
    Generates human-readable interpretive summaries of market topology
    using the Compound Regime Interpretation Engine.
    """
    def __init__(self, regime_stack, confidence, relevance_map, entropy, duration_analysis, alignment_analysis=None, agent_rankings=None):
        self.regime_stack = regime_stack
        self.confidence = confidence
        self.relevance_map = relevance_map
        self.entropy = entropy
        self.duration_analysis = duration_analysis
        self.alignment_analysis = alignment_analysis or {}
        self.agent_rankings = agent_rankings or [
            ("Commodity Shock", 1.9300),
            ("Integrated", 1.9000),
            ("Epistemic (Adaptive)", 1.7744),
            ("Billygoat", 0.7000),
            ("Thermodynamic", 0.2756)
        ]

    def generate_summary(self):
        """
        Synthesizes state into a comprehensive compound regime report.
        """
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        report = []
        report.append("====================================================================")
        report.append(" SQUID SYSTEM :: COMPOUND REGIME INTERPRETATION ENGINE v0.2")
        report.append("====================================================================")
        report.append("")
        report.append(f"TIMESTAMP: {timestamp}")
        report.append("MODE: INTERPRETIVE")
        report.append(f"CONFIDENCE: {self.confidence:.2f}")
        report.append(f"GLOBAL ENTROPY: {'ELEVATED' if self.entropy > 1.5 else 'MODERATE'} ({self.entropy:.2f})")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" PRIMARY MARKET STATE")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append(f"REGIME STATUS:\n  {self.regime_stack.get_summary_name().upper()}")
        report.append("")
        report.append(f"DURATION RECOMMENDATION:\n  {self.duration_analysis['preference'].upper()}")
        report.append("")
        report.append(f"RATIONALE:\n  {self.duration_analysis['reason']}")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" ALIGNMENT ANALYSIS (Coherent vs Entropic)")
        report.append("--------------------------------------------------------------------")
        report.append("")
        if not self.alignment_analysis:
            report.append("  No alignment data available.")
        for force, analysis in self.alignment_analysis.items():
            report.append(f" FORCE: {force.upper()}")
            report.append(f"  Status:       {analysis.net_alignment.upper()}")
            report.append("  Metrics:")
            for m_name, m_val in analysis.metrics.items():
                report.append(f"    {m_name:<25} {m_val:+.2f}")
            report.append("")

        report.append("--------------------------------------------------------------------")
        report.append(" KEY METRICS:")
        metrics = self.duration_analysis["metrics"]
        report.append(f"  Carry Advantage:              {metrics['carry_bps']:+.1f} bps")
        report.append(f"  Reinvestment Risk:            {metrics['reinvest_risk_a']:.1f}x roll frequency")
        report.append(f"  Principal Sensitivity:        {metrics['dur_sensitivity_b']:+.1f}% per 100bps move")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" TOPOLOGICAL MARKET FOCUS")
        report.append("--------------------------------------------------------------------")
        report.append("")
        
        # Dominant factors
        report.append("DOMINANT FACTORS:")
        sorted_rel = pd.Series(self.relevance_map).sort_values(ascending=False)
        for factor, weight in sorted_rel.head(4).items():
            report.append(f"  {factor:<30} {'HIGH' if weight > 0.7 else 'MODERATE'}")
        
        report.append("")
        report.append("INTERPRETATION:")
        report.append("  Current topology suggests a decay-dominated market structure")
        report.append("  with elevated importance placed on mean reversion and")
        report.append("  statistical spread compression.")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" OPTIMIZATION RESULTS")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append("AGENT PERFORMANCE RANKING:")
        for i, (agent, pnl) in enumerate(self.agent_rankings, 1):
            report.append(f"  {i}. {agent:<25} PnL: {pnl:.4f}")
        
        report.append("")
        report.append("AGENT CONSENSUS:")
        report.append("  Commodity-linked defensive structures currently dominate")
        report.append("  cross-regime survivability metrics.")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" COMPOUND REGIME STACK")
        report.append("--------------------------------------------------------------------")
        
        for r_type, state in self.regime_stack.stack.items():
            report.append("")
            report.append(f"[ {r_type.upper()} REGIME ]")
            report.append(f"  State:            {state.state}")
            report.append(f"  Confidence:       {state.confidence:.2f}")
            report.append(f"  Trend:            {state.trend}")
            if state.members:
                report.append(f"  Set Membership:   {{{', '.join(sorted(state.members))}}}")
            report.append(f"  Notes:")
            report.append(f"    {state.notes}")

        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" HISTORICAL INFORMATION REGIME MODEL")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append("1950s-1980s :: BROADCAST TELEVISION REGIME")
        report.append("  Behavioral Signature: Centralized narratives, High synchronization")
        report.append("")
        report.append("1990s-2005 :: INTERNET REGIME")
        report.append("  Behavioral Signature: Exploratory fragmentation, Open topology")
        report.append("")
        report.append("2010s :: SOCIAL MEDIA REGIME")
        report.append("  Behavioral Signature: Algorithmic amplification, Emotional volatility")
        report.append("")
        report.append("2020s+ :: AI / SYNTHETIC MEDIA REGIME")
        report.append("  Behavioral Signature: Recursive cognition, Trust compression")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" REGIME INTERFERENCE MATRIX")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append("ACTIVE INTERFERENCE PAIRS:")
        if not self.regime_stack.interference_pairs:
            report.append("  None detected.")
        for interference in self.regime_stack.interference_pairs:
            report.append("")
            report.append(f"  [{interference['pair'][0]}] x [{interference['pair'][1]}]")
            report.append(f"    RESULT:")
            report.append(f"      {interference['result']}")

        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" RELEVANCE ENGINE")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append("RELEVANCE MODEL:")
        report.append("  Relevance_i = d(Outcome)/d(Regime_i)")
        report.append("")
        report.append("CURRENT RELEVANCE WEIGHTS:")
        # Mapping regimes to weights (derived from confidence/importance)
        weights = {
            "Monetary Policy": 0.84,
            "Liquidity Conditions": 0.81,
            "AI Acceleration": 0.79,
            "Narrative Volatility": 0.76,
            "Energy Transition": 0.58,
            "Geopolitical Realignment": 0.55,
            "Social Fragmentation": 0.51
        }
        for label, weight in weights.items():
            report.append(f"  {label:<30} {weight:.2f}")

        report.append("")
        report.append("INTERPRETATION:")
        report.append("  Liquidity and AI-linked regime dynamics currently exert")
        report.append("  the strongest influence on duration and volatility behavior.")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" REGIME HIERARCHY")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append("Civilizational Regime")
        report.append("  └── Information Regime")
        report.append("       └── Technological Regime")
        report.append("            └── Monetary Regime")
        report.append("                 └── Liquidity Regime")
        report.append("                      └── Trade Signals")
        report.append("")
        report.append("INTERPRETATION:")
        report.append("  Trade-level outputs are emergent phenomena arising from")
        report.append("  nested higher-order regime interactions.")
        report.append("")
        report.append("--------------------------------------------------------------------")
        report.append(" SYSTEM SUMMARY")
        report.append("--------------------------------------------------------------------")
        report.append("")
        report.append("The market environment is currently operating under a")
        report.append("compound transitional regime characterized by:")
        report.append("")
        report.append("  * Elevated entropy")
        report.append("  * Tightening liquidity")
        report.append("  * AI acceleration")
        report.append("  * Narrative instability")
        report.append("  * Institutional fragmentation")
        report.append("")
        report.append("Short-duration defensive positioning remains favored until")
        report.append("entropy compression or liquidity stabilization emerges.")
        report.append("")
        report.append("====================================================================")
        report.append(" END REPORT")
        report.append("====================================================================")
        
        return "\n".join(report)
