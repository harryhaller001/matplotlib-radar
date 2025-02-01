from numbers import Number as Number

from _typeshed import Incomplete
from cycler import cycler as cycler
from matplotlib import cbook as cbook
from matplotlib import cm as cm
from matplotlib import get_backend as get_backend
from matplotlib import interactive as interactive
from matplotlib import mlab as mlab
from matplotlib import rcParams as rcParams
from matplotlib import rcParamsDefault as rcParamsDefault
from matplotlib import rcParamsOrig as rcParamsOrig
from matplotlib import rcsetup as rcsetup
from matplotlib import style as style
from matplotlib.artist import Artist as Artist
from matplotlib.axes import Axes as Axes
from matplotlib.axes import Subplot as Subplot
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import MouseButton as MouseButton
from matplotlib.cm import register_cmap as register_cmap
from matplotlib.colors import Normalize as Normalize
from matplotlib.figure import Figure as Figure
from matplotlib.figure import FigureBase as FigureBase
from matplotlib.figure import figaspect as figaspect
from matplotlib.gridspec import GridSpec as GridSpec
from matplotlib.gridspec import SubplotSpec as SubplotSpec
from matplotlib.lines import Line2D as Line2D
from matplotlib.patches import Arrow as Arrow
from matplotlib.patches import Circle as Circle
from matplotlib.patches import Polygon as Polygon
from matplotlib.patches import Rectangle as Rectangle
from matplotlib.projections import PolarAxes as PolarAxes
from matplotlib.scale import get_scale_names as get_scale_names
from matplotlib.text import Annotation as Annotation
from matplotlib.text import Text as Text
from matplotlib.ticker import AutoLocator as AutoLocator
from matplotlib.ticker import FixedFormatter as FixedFormatter
from matplotlib.ticker import FixedLocator as FixedLocator
from matplotlib.ticker import FormatStrFormatter as FormatStrFormatter
from matplotlib.ticker import Formatter as Formatter
from matplotlib.ticker import FuncFormatter as FuncFormatter
from matplotlib.ticker import IndexLocator as IndexLocator
from matplotlib.ticker import LinearLocator as LinearLocator
from matplotlib.ticker import Locator as Locator
from matplotlib.ticker import LogFormatter as LogFormatter
from matplotlib.ticker import LogFormatterExponent as LogFormatterExponent
from matplotlib.ticker import LogFormatterMathtext as LogFormatterMathtext
from matplotlib.ticker import LogLocator as LogLocator
from matplotlib.ticker import MaxNLocator as MaxNLocator
from matplotlib.ticker import MultipleLocator as MultipleLocator
from matplotlib.ticker import NullFormatter as NullFormatter
from matplotlib.ticker import NullLocator as NullLocator
from matplotlib.ticker import ScalarFormatter as ScalarFormatter
from matplotlib.ticker import TickHelper as TickHelper
from matplotlib.widgets import Button as Button
from matplotlib.widgets import Slider as Slider
from matplotlib.widgets import Widget as Widget

def install_repl_displayhook() -> None: ...
def uninstall_repl_displayhook() -> None: ...

draw_all: Incomplete

def set_loglevel(*args, **kwargs): ...
def findobj(o: Incomplete | None = None, match: Incomplete | None = None, include_self: bool = True): ...
def switch_backend(newbackend): ...
def new_figure_manager(*args, **kwargs): ...
def draw_if_interactive(*args, **kwargs): ...
def show(*args, **kwargs): ...
def isinteractive(): ...
def ioff(): ...
def ion(): ...
def pause(interval) -> None: ...
def rc(group, **kwargs) -> None: ...
def rc_context(rc: Incomplete | None = None, fname: Incomplete | None = None): ...
def rcdefaults() -> None: ...
def getp(obj, *args, **kwargs): ...
def get(obj, *args, **kwargs): ...
def setp(obj, *args, **kwargs): ...
def xkcd(scale: int = 1, length: int = 100, randomness: int = 2): ...
def figure(
    num: Incomplete | None = None,
    figsize: Incomplete | None = None,
    dpi: Incomplete | None = None,
    facecolor: Incomplete | None = None,
    edgecolor: Incomplete | None = None,
    frameon: bool = True,
    FigureClass=...,
    clear: bool = False,
    **kwargs,
): ...
def gcf(): ...
def fignum_exists(num): ...
def get_fignums(): ...
def get_figlabels(): ...
def get_current_fig_manager(): ...
def connect(s, func): ...
def disconnect(cid): ...
def close(fig: Incomplete | None = None) -> None: ...
def clf() -> None: ...
def draw() -> None: ...
def savefig(*args, **kwargs): ...
def figlegend(*args, **kwargs): ...
def axes(arg: Incomplete | None = None, **kwargs): ...
def delaxes(ax: Incomplete | None = None) -> None: ...
def sca(ax) -> None: ...
def cla(): ...
def subplot(*args, **kwargs): ...
def subplots(
    nrows: int = 1,
    ncols: int = 1,
    *,
    sharex: bool = False,
    sharey: bool = False,
    squeeze: bool = True,
    width_ratios: Incomplete | None = None,
    height_ratios: Incomplete | None = None,
    subplot_kw: Incomplete | None = None,
    gridspec_kw: Incomplete | None = None,
    **fig_kw,
): ...
def subplot_mosaic(
    mosaic,
    *,
    sharex: bool = False,
    sharey: bool = False,
    width_ratios: Incomplete | None = None,
    height_ratios: Incomplete | None = None,
    empty_sentinel: str = ".",
    subplot_kw: Incomplete | None = None,
    gridspec_kw: Incomplete | None = None,
    per_subplot_kw: Incomplete | None = None,
    **fig_kw,
): ...
def subplot2grid(shape, loc, rowspan: int = 1, colspan: int = 1, fig: Incomplete | None = None, **kwargs): ...
def twinx(ax: Incomplete | None = None): ...
def twiny(ax: Incomplete | None = None): ...
def subplot_tool(targetfig: Incomplete | None = None): ...
def box(on: Incomplete | None = None) -> None: ...
def xlim(*args, **kwargs): ...
def ylim(*args, **kwargs): ...
def xticks(ticks: Incomplete | None = None, labels: Incomplete | None = None, *, minor: bool = False, **kwargs): ...
def yticks(ticks: Incomplete | None = None, labels: Incomplete | None = None, *, minor: bool = False, **kwargs): ...
def rgrids(
    radii: Incomplete | None = None,
    labels: Incomplete | None = None,
    angle: Incomplete | None = None,
    fmt: Incomplete | None = None,
    **kwargs,
): ...
def thetagrids(
    angles: Incomplete | None = None, labels: Incomplete | None = None, fmt: Incomplete | None = None, **kwargs
): ...
def get_plot_commands(): ...
def colorbar(
    mappable: Incomplete | None = None, cax: Incomplete | None = None, ax: Incomplete | None = None, **kwargs
): ...
def clim(vmin: Incomplete | None = None, vmax: Incomplete | None = None) -> None: ...
def get_cmap(name: Incomplete | None = None, lut: Incomplete | None = None): ...
def set_cmap(cmap) -> None: ...
def imread(fname, format: Incomplete | None = None): ...
def imsave(fname, arr, **kwargs): ...
def matshow(A, fignum: Incomplete | None = None, **kwargs): ...
def polar(*args, **kwargs): ...
def figimage(
    X,
    xo: int = 0,
    yo: int = 0,
    alpha: Incomplete | None = None,
    norm: Incomplete | None = None,
    cmap: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    origin: Incomplete | None = None,
    resize: bool = False,
    **kwargs,
): ...
def figtext(x, y, s, fontdict: Incomplete | None = None, **kwargs): ...
def gca(): ...
def gci(): ...
def ginput(n: int = 1, timeout: int = 30, show_clicks: bool = True, mouse_add=..., mouse_pop=..., mouse_stop=...): ...
def subplots_adjust(
    left: Incomplete | None = None,
    bottom: Incomplete | None = None,
    right: Incomplete | None = None,
    top: Incomplete | None = None,
    wspace: Incomplete | None = None,
    hspace: Incomplete | None = None,
): ...
def suptitle(t, **kwargs): ...
def tight_layout(
    *,
    pad: float = 1.08,
    h_pad: Incomplete | None = None,
    w_pad: Incomplete | None = None,
    rect: Incomplete | None = None,
): ...
def waitforbuttonpress(timeout: int = -1): ...
def acorr(x, *, data: Incomplete | None = None, **kwargs): ...
def angle_spectrum(
    x,
    Fs: Incomplete | None = None,
    Fc: Incomplete | None = None,
    window: Incomplete | None = None,
    pad_to: Incomplete | None = None,
    sides: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def annotate(
    text,
    xy,
    xytext: Incomplete | None = None,
    xycoords: str = "data",
    textcoords: Incomplete | None = None,
    arrowprops: Incomplete | None = None,
    annotation_clip: Incomplete | None = None,
    **kwargs,
): ...
def arrow(x, y, dx, dy, **kwargs): ...
def autoscale(enable: bool = True, axis: str = "both", tight: Incomplete | None = None): ...
def axhline(y: int = 0, xmin: int = 0, xmax: int = 1, **kwargs): ...
def axhspan(ymin, ymax, xmin: int = 0, xmax: int = 1, **kwargs): ...
def axis(arg: Incomplete | None = None, /, *, emit: bool = True, **kwargs): ...
def axline(xy1, xy2: Incomplete | None = None, *, slope: Incomplete | None = None, **kwargs): ...
def axvline(x: int = 0, ymin: int = 0, ymax: int = 1, **kwargs): ...
def axvspan(xmin, xmax, ymin: int = 0, ymax: int = 1, **kwargs): ...
def bar(
    x,
    height,
    width: float = 0.8,
    bottom: Incomplete | None = None,
    *,
    align: str = "center",
    data: Incomplete | None = None,
    **kwargs,
): ...
def barbs(*args, data: Incomplete | None = None, **kwargs): ...
def barh(
    y,
    width,
    height: float = 0.8,
    left: Incomplete | None = None,
    *,
    align: str = "center",
    data: Incomplete | None = None,
    **kwargs,
): ...
def bar_label(
    container,
    labels: Incomplete | None = None,
    *,
    fmt: str = "%g",
    label_type: str = "edge",
    padding: int = 0,
    **kwargs,
): ...
def boxplot(
    x,
    notch: Incomplete | None = None,
    sym: Incomplete | None = None,
    vert: Incomplete | None = None,
    whis: Incomplete | None = None,
    positions: Incomplete | None = None,
    widths: Incomplete | None = None,
    patch_artist: Incomplete | None = None,
    bootstrap: Incomplete | None = None,
    usermedians: Incomplete | None = None,
    conf_intervals: Incomplete | None = None,
    meanline: Incomplete | None = None,
    showmeans: Incomplete | None = None,
    showcaps: Incomplete | None = None,
    showbox: Incomplete | None = None,
    showfliers: Incomplete | None = None,
    boxprops: Incomplete | None = None,
    labels: Incomplete | None = None,
    flierprops: Incomplete | None = None,
    medianprops: Incomplete | None = None,
    meanprops: Incomplete | None = None,
    capprops: Incomplete | None = None,
    whiskerprops: Incomplete | None = None,
    manage_ticks: bool = True,
    autorange: bool = False,
    zorder: Incomplete | None = None,
    capwidths: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
): ...
def broken_barh(xranges, yrange, *, data: Incomplete | None = None, **kwargs): ...
def clabel(CS, levels: Incomplete | None = None, **kwargs): ...
def cohere(
    x,
    y,
    NFFT: int = 256,
    Fs: int = 2,
    Fc: int = 0,
    detrend=...,
    window=...,
    noverlap: int = 0,
    pad_to: Incomplete | None = None,
    sides: str = "default",
    scale_by_freq: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def contour(*args, data: Incomplete | None = None, **kwargs): ...
def contourf(*args, data: Incomplete | None = None, **kwargs): ...
def csd(
    x,
    y,
    NFFT: Incomplete | None = None,
    Fs: Incomplete | None = None,
    Fc: Incomplete | None = None,
    detrend: Incomplete | None = None,
    window: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    pad_to: Incomplete | None = None,
    sides: Incomplete | None = None,
    scale_by_freq: Incomplete | None = None,
    return_line: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def errorbar(
    x,
    y,
    yerr: Incomplete | None = None,
    xerr: Incomplete | None = None,
    fmt: str = "",
    ecolor: Incomplete | None = None,
    elinewidth: Incomplete | None = None,
    capsize: Incomplete | None = None,
    barsabove: bool = False,
    lolims: bool = False,
    uplims: bool = False,
    xlolims: bool = False,
    xuplims: bool = False,
    errorevery: int = 1,
    capthick: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def eventplot(
    positions,
    orientation: str = "horizontal",
    lineoffsets: int = 1,
    linelengths: int = 1,
    linewidths: Incomplete | None = None,
    colors: Incomplete | None = None,
    alpha: Incomplete | None = None,
    linestyles: str = "solid",
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def fill(*args, data: Incomplete | None = None, **kwargs): ...
def fill_between(
    x,
    y1,
    y2: int = 0,
    where: Incomplete | None = None,
    interpolate: bool = False,
    step: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def fill_betweenx(
    y,
    x1,
    x2: int = 0,
    where: Incomplete | None = None,
    step: Incomplete | None = None,
    interpolate: bool = False,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def grid(visible: Incomplete | None = None, which: str = "major", axis: str = "both", **kwargs): ...
def hexbin(
    x,
    y,
    C: Incomplete | None = None,
    gridsize: int = 100,
    bins: Incomplete | None = None,
    xscale: str = "linear",
    yscale: str = "linear",
    extent: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    alpha: Incomplete | None = None,
    linewidths: Incomplete | None = None,
    edgecolors: str = "face",
    reduce_C_function=...,
    mincnt: Incomplete | None = None,
    marginals: bool = False,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def hist(
    x,
    bins: Incomplete | None = None,
    range: Incomplete | None = None,
    density: bool = False,
    weights: Incomplete | None = None,
    cumulative: bool = False,
    bottom: Incomplete | None = None,
    histtype: str = "bar",
    align: str = "mid",
    orientation: str = "vertical",
    rwidth: Incomplete | None = None,
    log: bool = False,
    color: Incomplete | None = None,
    label: Incomplete | None = None,
    stacked: bool = False,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def stairs(
    values,
    edges: Incomplete | None = None,
    *,
    orientation: str = "vertical",
    baseline: int = 0,
    fill: bool = False,
    data: Incomplete | None = None,
    **kwargs,
): ...
def hist2d(
    x,
    y,
    bins: int = 10,
    range: Incomplete | None = None,
    density: bool = False,
    weights: Incomplete | None = None,
    cmin: Incomplete | None = None,
    cmax: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def hlines(
    y,
    xmin,
    xmax,
    colors: Incomplete | None = None,
    linestyles: str = "solid",
    label: str = "",
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def imshow(
    X,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    *,
    aspect: Incomplete | None = None,
    interpolation: Incomplete | None = None,
    alpha: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    origin: Incomplete | None = None,
    extent: Incomplete | None = None,
    interpolation_stage: Incomplete | None = None,
    filternorm: bool = True,
    filterrad: float = 4.0,
    resample: Incomplete | None = None,
    url: Incomplete | None = None,
    data: Incomplete | None = None,
    **kwargs,
): ...
def legend(*args, **kwargs): ...
def locator_params(axis: str = "both", tight: Incomplete | None = None, **kwargs): ...
def loglog(*args, **kwargs): ...
def magnitude_spectrum(
    x,
    Fs: Incomplete | None = None,
    Fc: Incomplete | None = None,
    window: Incomplete | None = None,
    pad_to: Incomplete | None = None,
    sides: Incomplete | None = None,
    scale: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def margins(*margins, x: Incomplete | None = None, y: Incomplete | None = None, tight: bool = True): ...
def minorticks_off(): ...
def minorticks_on(): ...
def pcolor(
    *args,
    shading: Incomplete | None = None,
    alpha: Incomplete | None = None,
    norm: Incomplete | None = None,
    cmap: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    data: Incomplete | None = None,
    **kwargs,
): ...
def pcolormesh(
    *args,
    alpha: Incomplete | None = None,
    norm: Incomplete | None = None,
    cmap: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    shading: Incomplete | None = None,
    antialiased: bool = False,
    data: Incomplete | None = None,
    **kwargs,
): ...
def phase_spectrum(
    x,
    Fs: Incomplete | None = None,
    Fc: Incomplete | None = None,
    window: Incomplete | None = None,
    pad_to: Incomplete | None = None,
    sides: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def pie(
    x,
    explode: Incomplete | None = None,
    labels: Incomplete | None = None,
    colors: Incomplete | None = None,
    autopct: Incomplete | None = None,
    pctdistance: float = 0.6,
    shadow: bool = False,
    labeldistance: float = 1.1,
    startangle: int = 0,
    radius: int = 1,
    counterclock: bool = True,
    wedgeprops: Incomplete | None = None,
    textprops: Incomplete | None = None,
    center=(0, 0),
    frame: bool = False,
    rotatelabels: bool = False,
    *,
    normalize: bool = True,
    hatch: Incomplete | None = None,
    data: Incomplete | None = None,
): ...
def plot(*args, scalex: bool = True, scaley: bool = True, data: Incomplete | None = None, **kwargs): ...
def plot_date(
    x,
    y,
    fmt: str = "o",
    tz: Incomplete | None = None,
    xdate: bool = True,
    ydate: bool = False,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def psd(
    x,
    NFFT: Incomplete | None = None,
    Fs: Incomplete | None = None,
    Fc: Incomplete | None = None,
    detrend: Incomplete | None = None,
    window: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    pad_to: Incomplete | None = None,
    sides: Incomplete | None = None,
    scale_by_freq: Incomplete | None = None,
    return_line: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def quiver(*args, data: Incomplete | None = None, **kwargs): ...
def quiverkey(Q, X, Y, U, label, **kwargs): ...
def scatter(
    x,
    y,
    s: Incomplete | None = None,
    c: Incomplete | None = None,
    marker: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    alpha: Incomplete | None = None,
    linewidths: Incomplete | None = None,
    *,
    edgecolors: Incomplete | None = None,
    plotnonfinite: bool = False,
    data: Incomplete | None = None,
    **kwargs,
): ...
def semilogx(*args, **kwargs): ...
def semilogy(*args, **kwargs): ...
def specgram(
    x,
    NFFT: Incomplete | None = None,
    Fs: Incomplete | None = None,
    Fc: Incomplete | None = None,
    detrend: Incomplete | None = None,
    window: Incomplete | None = None,
    noverlap: Incomplete | None = None,
    cmap: Incomplete | None = None,
    xextent: Incomplete | None = None,
    pad_to: Incomplete | None = None,
    sides: Incomplete | None = None,
    scale_by_freq: Incomplete | None = None,
    mode: Incomplete | None = None,
    scale: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def spy(
    Z,
    precision: int = 0,
    marker: Incomplete | None = None,
    markersize: Incomplete | None = None,
    aspect: str = "equal",
    origin: str = "upper",
    **kwargs,
): ...
def stackplot(
    x,
    *args,
    labels=(),
    colors: Incomplete | None = None,
    baseline: str = "zero",
    data: Incomplete | None = None,
    **kwargs,
): ...
def stem(
    *args,
    linefmt: Incomplete | None = None,
    markerfmt: Incomplete | None = None,
    basefmt: Incomplete | None = None,
    bottom: int = 0,
    label: Incomplete | None = None,
    use_line_collection=...,
    orientation: str = "vertical",
    data: Incomplete | None = None,
): ...
def step(x, y, *args, where: str = "pre", data: Incomplete | None = None, **kwargs): ...
def streamplot(
    x,
    y,
    u,
    v,
    density: int = 1,
    linewidth: Incomplete | None = None,
    color: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    arrowsize: int = 1,
    arrowstyle: str = "-|>",
    minlength: float = 0.1,
    transform: Incomplete | None = None,
    zorder: Incomplete | None = None,
    start_points: Incomplete | None = None,
    maxlength: float = 4.0,
    integration_direction: str = "both",
    broken_streamlines: bool = True,
    *,
    data: Incomplete | None = None,
): ...
def table(
    cellText: Incomplete | None = None,
    cellColours: Incomplete | None = None,
    cellLoc: str = "right",
    colWidths: Incomplete | None = None,
    rowLabels: Incomplete | None = None,
    rowColours: Incomplete | None = None,
    rowLoc: str = "left",
    colLabels: Incomplete | None = None,
    colColours: Incomplete | None = None,
    colLoc: str = "center",
    loc: str = "bottom",
    bbox: Incomplete | None = None,
    edges: str = "closed",
    **kwargs,
): ...
def text(x, y, s, fontdict: Incomplete | None = None, **kwargs): ...
def tick_params(axis: str = "both", **kwargs): ...
def ticklabel_format(
    *,
    axis: str = "both",
    style: str = "",  # noqa: F811
    scilimits: Incomplete | None = None,
    useOffset: Incomplete | None = None,
    useLocale: Incomplete | None = None,
    useMathText: Incomplete | None = None,
): ...
def tricontour(*args, **kwargs): ...
def tricontourf(*args, **kwargs): ...
def tripcolor(
    *args,
    alpha: float = 1.0,
    norm: Incomplete | None = None,
    cmap: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    shading: str = "flat",
    facecolors: Incomplete | None = None,
    **kwargs,
): ...
def triplot(*args, **kwargs): ...
def violinplot(
    dataset,
    positions: Incomplete | None = None,
    vert: bool = True,
    widths: float = 0.5,
    showmeans: bool = False,
    showextrema: bool = True,
    showmedians: bool = False,
    quantiles: Incomplete | None = None,
    points: int = 100,
    bw_method: Incomplete | None = None,
    *,
    data: Incomplete | None = None,
): ...
def vlines(
    x,
    ymin,
    ymax,
    colors: Incomplete | None = None,
    linestyles: str = "solid",
    label: str = "",
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def xcorr(
    x,
    y,
    normed: bool = True,
    detrend=...,
    usevlines: bool = True,
    maxlags: int = 10,
    *,
    data: Incomplete | None = None,
    **kwargs,
): ...
def sci(im): ...
def title(
    label,
    fontdict: Incomplete | None = None,
    loc: Incomplete | None = None,
    pad: Incomplete | None = None,
    *,
    y: Incomplete | None = None,
    **kwargs,
): ...
def xlabel(
    xlabel,
    fontdict: Incomplete | None = None,
    labelpad: Incomplete | None = None,
    *,
    loc: Incomplete | None = None,
    **kwargs,
): ...
def ylabel(
    ylabel,
    fontdict: Incomplete | None = None,
    labelpad: Incomplete | None = None,
    *,
    loc: Incomplete | None = None,
    **kwargs,
): ...
def xscale(value, **kwargs): ...
def yscale(value, **kwargs): ...
def autumn() -> None: ...
def bone() -> None: ...
def cool() -> None: ...
def copper() -> None: ...
def flag() -> None: ...
def gray() -> None: ...
def hot() -> None: ...
def hsv() -> None: ...
def jet() -> None: ...
def pink() -> None: ...
def prism() -> None: ...
def spring() -> None: ...
def summer() -> None: ...
def winter() -> None: ...
def magma() -> None: ...
def inferno() -> None: ...
def plasma() -> None: ...
def viridis() -> None: ...
def nipy_spectral() -> None: ...
