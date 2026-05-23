import numpy as np

class DurationAnalyzer:
    """
    Evaluates tradeoffs between different Treasury durations.
    Focuses on Carry, Duration Risk, and Reinvestment Risk.
    """
    
    def __init__(self):
        # Simplified duration multipliers (Years)
        self.maturity_map = {
            "3M": 0.25,
            "6M": 0.5,
            "1Y": 1.0,
            "2Y": 2.0,
            "5Y": 5.0,
            "10Y": 10.0,
            "30Y": 30.0
        }

    def calculate_metrics(self, yield_a, yield_b, label_a, label_b):
        """
        Compares two securities. 
        Security A is typically the shorter duration.
        """
        dur_a = self.maturity_map.get(label_a, 0.25)
        dur_b = self.maturity_map.get(label_b, 0.5)
        
        # 1. Carry (Yield differential in bps)
        carry = (yield_b - yield_a) * 100
        
        # 2. Duration Sensitivity (Price impact of 100bps move)
        # Simplified: Pct Change ~ -Duration * Change in Yield
        price_impact_a = -dur_a * 0.01 * 100 # In percent
        price_impact_b = -dur_b * 0.01 * 100
        
        # 3. Reinvestment Risk Proxy
        # Shorter duration has higher reinvestment risk (more frequent rolls)
        reinvest_risk_a = 1.0 / dur_a
        reinvest_risk_b = 1.0 / dur_b
        
        return {
            "carry_bps": carry,
            "dur_sensitivity_a": price_impact_a,
            "dur_sensitivity_b": price_impact_b,
            "reinvest_risk_a": reinvest_risk_a,
            "reinvest_risk_b": reinvest_risk_b
        }

    def compare(self, security_a, security_b, yield_a, yield_b, regime, entropy, confidence):
        """
        Generates a recommendation based on market context.
        """
        metrics = self.calculate_metrics(yield_a, yield_b, security_a, security_b)
        
        preference = "neutral"
        reason = ""
        
        # Logic: 
        # If entropy is high or regime is inflationary tightening, prefer SHORTER duration (defensive)
        if entropy > 1.5 or regime == "inflationary_tightening":
            preference = security_a
            reason = f"Elevated entropy ({entropy:.2f}) or tightening regime favors defensive {security_a} duration."
        
        # If entropy is low and carry is positive, prefer LONGER duration
        elif entropy < 0.8 and metrics["carry_bps"] > 10:
            preference = security_b
            reason = f"Low entropy and positive carry ({metrics['carry_bps']:.0f} bps) favor {security_b} yield capture."
            
        else:
            # Default to shorter if confidence is low
            if confidence < 0.4:
                preference = security_a
                reason = "Low confidence environment; defaulting to shorter duration for safety."
            else:
                preference = security_a if yield_a > yield_b else security_b
                reason = "Yield-driven preference in moderate stability environment."
                
        return {
            "metrics": metrics,
            "preference": preference,
            "reason": reason
        }
