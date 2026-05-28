import numpy as np

REGIME_TYPES = [
    "monetary",
    "liquidity",
    "information",
    "technological",
    "energy",
    "social",
    "geopolitical"
]

class RegimeState:
    """
    Specific state for a single regime dimension.
    """
    def __init__(self, name, state="UNKNOWN", confidence=0.5, trend="STABLE", notes=""):
        self.name = name
        self.state = state
        self.confidence = confidence
        self.trend = trend
        self.notes = notes

    def __repr__(self):
        return f"RegimeState({self.name}: {self.state}, conf={self.confidence:.2f})"

class CompoundRegimeStack:
    """
    A collection of nested/overlapping regimes.
    """
    def __init__(self):
        self.stack = {r_type: RegimeState(r_type) for r_type in REGIME_TYPES}
        self.interference_pairs = []

    def set_regime(self, r_type, state, confidence, trend, notes=""):
        if r_type in self.stack:
            self.stack[r_type] = RegimeState(r_type, state, confidence, trend, notes)

    def add_interference(self, r_a, r_b, result):
        self.interference_pairs.append({
            "pair": (r_a, r_b),
            "result": result
        })

    def get_summary_name(self):
        # Heuristic for a single "dominant" regime name for backward compatibility
        dominant = max(self.stack.values(), key=lambda x: x.confidence)
        return dominant.state

class RegimeDetector:
    """
    Identifies multiple market regimes across different dimensions.
    """
    def __init__(self):
        # Traditional single-regime mapping for backward compatibility if needed
        self.legacy_regimes = {
            "commodity_shock": {"monetary": "Hawkish", "liquidity": "Tightening"},
            "low_vol_compression": {"monetary": "Neutral", "liquidity": "Expansive"}
        }

    def detect(self, feature_states):
        """
        Detects a compound regime stack based on feature states.
        """
        stack = CompoundRegimeStack()
        
        # 1. Monetary & Liquidity (Driven by Yields/Z-Scores)
        z_score = feature_states.get("Z_Score")
        if z_score and z_score.current_value > 2.0:
            stack.set_regime("monetary", "Hawkish Transition", 0.81, "Tightening", 
                             "Transition risk associated with policy framework evolution.")
            stack.set_regime("liquidity", "Restrictive", 0.78, "Contracting", 
                             "Elevated refinancing stress and reduced duration appetite.")
        else:
            stack.set_regime("monetary", "Neutral", 0.6, "Stable", "Standard policy environment.")
            stack.set_regime("liquidity", "Adequate", 0.7, "Stable", "No immediate stress detected.")

        # 2. Information Regime (Driven by Entropy/Lambda)
        entropy = feature_states.get("Entropy")
        if entropy and entropy.current_value > 1.5:
            stack.set_regime("information", "Synthetic Media Transition", 0.74, "Accelerating",
                             "AI-generated narrative environments increasing reflexivity.")
        else:
            stack.set_regime("information", "Internet/Social Media", 0.8, "Stable",
                             "Standard digital information flow.")

        # 3. Technological Regime (AI focus)
        # Assuming lambda or a new feature tracks AI acceleration
        stack.set_regime("technological", "AI Acceleration", 0.92, "Expansionary",
                         "Productivity expectations reshaping long-duration assumptions.")

        # 4. Social Regime
        stack.set_regime("social", "Fragmentation", 0.67, "Divergent",
                         "Declining institutional synchronization.")

        # 5. Energy Regime
        oil = feature_states.get("Oil")
        if oil and oil.current_value > 100:
            stack.set_regime("energy", "Commodity Shock", 0.85, "Expansionary", "High oil prices driving energy sensitivity.")
        else:
            stack.set_regime("energy", "Electrification Transition", 0.63, "Expansionary",
                             "Grid stress and AI datacenter demand increasing energy sensitivity.")

        # 6. Geopolitical
        stack.set_regime("geopolitical", "Multipolar Realignment", 0.71, "Unstable",
                         "Supply chain fragmentation and strategic competition.")

        # Add predefined interference patterns
        self._detect_interference(stack)
        
        return stack

    def _detect_interference(self, stack):
        monetary = stack.stack["monetary"]
        info = stack.stack["information"]
        tech = stack.stack["technological"]
        social = stack.stack["social"]

        if monetary.trend == "Expansive" and info.state == "Social Media Regime":
            stack.add_interference("Low Rate Regime", "Social Media Regime", 
                                   "Speculative reflexivity amplification and meme asset acceleration.")
        
        if tech.state == "AI Acceleration" and social.state == "Fragmentation":
            stack.add_interference("AI Productivity Regime", "Demographic Aging",
                                   "Productivity expansion partially offset by structural labor contraction.")

        if stack.stack["liquidity"].trend == "Contracting" and info.trend == "Accelerating":
            stack.add_interference("Liquidity Tightening", "Narrative Volatility",
                                   "Reduced stability of historical pricing assumptions.")
