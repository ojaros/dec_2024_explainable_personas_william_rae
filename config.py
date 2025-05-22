from dataclasses import dataclass

@dataclass
class AnalysisConfig:
    """Configuration options for clustering analysis."""
    min_clusters: int = 2
    max_clusters: int = 10
    min_subclusters: int = 2
    max_subclusters: int = 25
    encoded: bool = True
    num_epochs: int = 50
    min_cluster_size: int = 25
