import numpy as np

class FeatureState:
    """
    Stateful feature object that carries memory, confidence, 
    and relevance evolution.
    """
    def __init__(self, name, window=50):
        self.name = name
        self.window = window
        self.current_value = None
        self.regime_mean = None
        self.importance_weight = 1.0
        self.stability = 1.0
        self.history = []
        self.relevance_history = []

    def update(self, value, importance=None):
        self.current_value = value
        self.history.append(value)
        if len(self.history) > self.window:
            self.history.pop(0)
        
        # Calculate stability (inverse of coefficient of variation)
        if len(self.history) > 5:
            std = np.std(self.history)
            mean = np.mean(self.history)
            self.stability = 1.0 / (std / (abs(mean) + 1e-6) + 1.0)
            self.regime_mean = mean

        if importance is not None:
            self.importance_weight = importance
            self.relevance_history.append(importance)
            if len(self.relevance_history) > self.window:
                self.relevance_history.pop(0)

    def __repr__(self):
        return f"FeatureState({self.name}, val={self.current_value}, stability={self.stability:.2f})"

class EventMemory:
    """
    Episodic memory for storing significant market events and responses.
    """
    def __init__(self, event_type, pre_state, post_state=None, market_response=None, relevance_score=1.0):
        self.event_type = event_type
        self.pre_state = pre_state  # Dict of FeatureState snapshots
        self.post_state = post_state
        self.market_response = market_response
        self.relevance_score = relevance_score
        self.timestamp = None

    def record_response(self, post_state, market_response):
        self.post_state = post_state
        self.market_response = market_response

class BeliefState:
    """
    Maintains internal belief about market structure, 
    separating observation from interpretation.
    """
    def __init__(self):
        self.confidence = 0.5
        self.stability = "fragile"
        self.relevance_map = {}  # {feature_name: relevance_score}
        self.active_regime = "unknown"
        self.uncertainty = 1.0

    def update_belief(self, relevance_map, confidence, regime):
        self.relevance_map = relevance_map
        self.confidence = confidence
        self.active_regime = regime
        self.uncertainty = 1.0 - confidence
        
        if self.confidence > 0.8:
            self.stability = "robust"
        elif self.confidence > 0.4:
            self.stability = "stable"
        else:
            self.stability = "fragile"

    def __repr__(self):
        return f"BeliefState(regime={self.active_regime}, conf={self.confidence:.2f}, stability={self.stability})"
