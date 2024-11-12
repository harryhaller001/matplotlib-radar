from typing import List, Literal, Optional

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes


def radar_chart(  # noqa: D417
    label: List[str],
    axes_shape: Literal["circle", "polygon"] = "circle",
    cmap=None,
    ax: Optional[Axes] = None,
    show_figure: bool = True,
) -> Axes:
    """Generate radar chart with matplotlib.

    Args:
        labels: List of labels to annotate plot.
    """
    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

    ax.plot(theta, r)

    ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("A line plot on a polar axis", va="bottom")

    if show_figure is True:
        plt.show()
    else:
        return ax
