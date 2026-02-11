from matplotlib.projections import PolarAxes
import matplotlib.pyplot as plt
from matplotlib_radar import radar_chart
import numpy as np
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

np.random.seed(100)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(polar=True)
assert isinstance(ax, PolarAxes)
ax = radar_chart(
    label=["A", "B", "C", "D", "E"],
    data={"Sample 1": np.random.rand(5), "Sample 2": np.random.rand(5), "Sample 3": np.random.rand(5)},
    ax=ax,
    vmax=1,
    ticks=3,
    return_axis=True,
    cmap="Set2",
)

fig.savefig(fname=os.path.join(BASEDIR, "source", "_static", "example-radar-chart.jpg"), dpi=150)
