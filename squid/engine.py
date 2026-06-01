import pandas as pd
import numpy as np
from squid.memory import FeatureState, BeliefState, EventMemory
from squid.regimes import RegimeDetector
from squid.topology import MarketGraph
from squid.alignment import AlignmentLayer, CoherenceFilter
from squid.features import calculate_shannon_entropy
from squid.thermodynamics import estimate_lambda, estimate_beta
from squid.analysis import DurationAnalyzer
from squid.reporting import RelevanceReport

class EpistemicEngine:
    """
    The central orchestrator for adaptive epistemology.
    Moves from "What will happen?" to "What matters right now?".
    """
    def __init__(self):
        self.feature_states = {}
        self.belief = BeliefState()
        self.detector = RegimeDetector()
        self.topology = MarketGraph()
        self.alignment_layer = AlignmentLayer()
        self.coherence_filter = CoherenceFilter(self.alignment_layer)
        self.memory = [] # List of EventMemory
        self.attention_threshold = 0.7
        self.duration_analyzer = DurationAnalyzer()

    def _get_feature_state(self, name):
        if name not in self.feature_states:
            self.feature_states[name] = FeatureState(name)
        return self.feature_states[name]

    def process_step(self, data_row):
        """
        Executes the 7-layer epistemological hierarchy for a single time step.
        """
        # 1. Perception & 2. State Physics
        self._update_states(data_row)

        # 3. Regime Detection
        current_regime = self.detector.detect(self.feature_states)
        
        # 4. Memory (Simplified: checking for spikes/events)
        self._process_memory(current_regime)

        # 5. Attention Allocation
        attention_map = self._allocate_attention(current_regime)

        # 5.5 Alignment Layer (New)
        # Identify key forces to evaluate based on regime members
        forces_to_evaluate = current_regime.union() # Set of elements active in regimes
        alignment_results = {}
        
        # Context for alignment evaluation
        feature_context = {name: s.current_value for name, s in self.feature_states.items()}
        
        # Regime-dependent weights (simplified placeholder)
        regime_weights = {
            "resilience": 1.2,
            "productivity": 1.5,
            "entropy_effect": -2.0
        }

        for force in forces_to_evaluate:
            alignment_results[force] = self.alignment_layer.evaluate_force(
                force, feature_context, regime_weights
            )

        # Apply Coherence Filter (Ultrafilter)
        admissible_forces = self.coherence_filter.select_admissible(
            forces_to_evaluate, feature_context, regime_weights
        )

        # 6. Interpretation (Generate Relevance Map / Belief Update)
        self.belief.update_belief(
            relevance_map=attention_map,
            confidence=self._calculate_confidence(),
            regime=current_regime,
            alignment_analysis=alignment_results,
            admissible_forces=admissible_forces
        )

        # 7. Execution (Handled by Agents/Trading logic using BeliefState)
        return self.belief

    def generate_interpretive_report(self, data_row, security_a="3M", security_b="6M"):
        """
        Generates a comprehensive RelevanceReport for the current state.
        """
        # Process the row to update internal state
        self.process_step(data_row)
        
        current_regime_stack = self.belief.active_regime
        entropy = data_row.get("Entropy", 1.0)
        
        # Duration Analysis
        yield_a = data_row.get(security_a, 0.0)
        yield_b = data_row.get(security_b, 0.0)
        
        duration_analysis = self.duration_analyzer.compare(
            security_a, security_b, yield_a, yield_b, 
            current_regime_stack, entropy, self.belief.confidence
        )
        
        report = RelevanceReport(
            regime_stack=current_regime_stack,
            confidence=self.belief.confidence,
            relevance_map=self.belief.relevance_map,
            entropy=entropy,
            duration_analysis=duration_analysis,
            alignment_analysis=self.belief.alignment_analysis
        )
        
        return report

    def _update_states(self, row):
        # Update raw and physics-based states
        for col in ["10Y", "Oil", "Z_Score", "Entropy", "lambda", "beta"]:
            if col in row:
                state = self._get_feature_state(col)
                state.update(row[col])
                self.topology.add_node(col)

    def _process_memory(self, regime_stack):
        # Logic to record or recall events
        regime_name = regime_stack.get_summary_name()
        if regime_name != "unknown":
            # Check if this is a new event
            if not self.memory or self.memory[-1].event_type != regime_name:
                event = EventMemory(
                    event_type=regime_name,
                    pre_state={name: s.current_value for name, s in self.feature_states.items()}
                )
                self.memory.append(event)

    def _allocate_attention(self, regime_stack):
        attention = {}
        # Simple heuristic: use the summary name for weight lookups for now
        # In a full compound implementation, this would aggregate weights from all regimes
        # dominant_state = regime_stack.get_summary_name()
        for name, state in self.feature_states.items():
            # Attention = Regime Weight * State Stability * Novelty (Simplified)
            regime_weight = 0.5 
            attention[name] = regime_weight * (1.0 / (state.stability + 1e-6))
        return attention

    def _calculate_confidence(self):
        # Confidence is higher when features are stable and regime is known
        avg_stability = np.mean([s.stability for s in self.feature_states.values()])
        regime_name = self.belief.active_regime.get_summary_name() if self.belief.active_regime else "unknown"
        regime_bonus = 0.2 if regime_name != "unknown" else 0.0
        return np.clip(avg_stability + regime_bonus, 0.0, 1.0)

    def generate_attention_surface(self):
        """
        Returns a human-readable relevance map.
        """
        return pd.Series(self.belief.relevance_map).sort_values(ascending=False)
