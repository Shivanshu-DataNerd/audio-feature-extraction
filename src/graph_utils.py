"""
Utility functions for saving graphs produced during experiments.
All figures are saved to the top-level 'graphs/' directory.
"""

import os
import matplotlib.pyplot as plt

def get_graph_dir() -> str:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    graph_dir = os.path.join(project_root, "graphs")
    os.makedirs(graph_dir, exist_ok=True)
    return graph_dir

def save_graph(filename: str, fig=None, dpi: int = 200):
    """
    Save the current matplotlib figure to graphs/ directory.

    Parameters
    ----------
    filename : str
        Name of the image file (e.g. '01_waveform.png')
    fig : matplotlib.figure.Figure or None
        Figure to save (defaults to current figure)
    dpi : int
        Resolution
    """
    graph_dir = get_graph_dir()
    path = os.path.join(graph_dir, filename)

    if fig is None:
        fig = plt.gcf()

    fig.savefig(path, bbox_inches="tight", dpi=dpi)
    return path
