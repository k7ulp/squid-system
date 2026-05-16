class MarketNode:
    """
    Represents a market variable in an evolving influence topology.
    """
    def __init__(self, name):
        self.name = name
        self.connections = {}  # {target_node_name: influence_weight}
        self.current_relevance = 0.5
        self.regime_dependence = {} # {regime_name: relevance_multiplier}

    def add_connection(self, target_name, weight):
        self.connections[target_name] = weight

    def __repr__(self):
        return f"MarketNode({self.name}, relevance={self.current_relevance:.2f})"

class MarketGraph:
    """
    Manages the evolving influence topology of market variables.
    """
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = MarketNode(name)
        return self.nodes[name]

    def update_topology(self, regime_name):
        """
        Adjusts weights based on the active regime.
        """
        for name, node in self.nodes.items():
            # Example logic: in 'commodity_shock', Oil's relevance increases
            if regime_name == "commodity_shock" and name == "Oil":
                node.current_relevance = 0.9
            else:
                node.current_relevance *= 0.95 # Gradual decay of relevance
