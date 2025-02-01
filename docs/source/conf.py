"""Configure the Sphinx documentation builder."""

# Path setup
import os
import sys
from pathlib import Path
from typing import List
from datetime import datetime

DOCS_DIR = Path(__file__).parent
sys.path.insert(0, os.path.abspath("../../matplotlib_radar"))

# Project information
project = "matplotlib-radar"
author = "harryhaller001"
copyright = f"{datetime.now():%Y}, {author}."

# Configuration

templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"
default_role = "literal"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    # Required for syntax highlighing (https://github.com/spatialaudio/nbsphinx/issues/24)
    "IPython.sphinxext.ipython_console_highlighting",
    "myst_parser",
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Mapping for intersphinx extension
intersphinx_mapping = dict(
    python=("https://docs.python.org/3", None),
    numpy=("https://numpy.org/doc/stable/", None),
    matplotlib=("https://matplotlib.org/stable", None),
    # pandas=("https://pandas.pydata.org/pandas-docs/stable/", None),
    # anndata=("https://anndata.readthedocs.io/en/latest/", None),
    # scipy=("https://docs.scipy.org/doc/scipy", None),
    # sklearn=("https://scikit-learn.org/stable", None),
    # flowio=("https://flowio.readthedocs.io/en/latest/", None),
)

# don't run the notebooks
nbsphinx_execute = "never"
pygments_style = "sphinx"

exclude_trees = ["_build", "dist"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


autoapi_type = "python"
autoapi_add_toctree_entry = False
autoapi_ignore: List[str] = ["_*.py"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_dirs = ["../../matplotlib_radar"]
autoapi_member_order = "alphabetical"
autodoc_typehints = "description"

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_rtype = True
napoleon_use_param = True


# Options for HTML output
html_theme = "sphinx_book_theme"
html_title = "matplotlib-radar"
html_static_path = ["_static"]
html_logo = "_static/image/radar-chart.png"
html_css_files = [
    "css/custom.css",
]
html_theme_options = dict(
    repository_url="https://github.com/harryhaller001/matplotlib-radar",
    repository_branch="main",
    use_download_button=True,
    use_fullscreen_button=False,
    use_repository_button=True,
    # collapse_navbar=False,
)
html_context = dict(
    display_github=True,
    github_user="harryhaller001",
    github_repo="matplotlib-radar",
    github_version="main",
    conf_py_path="/docs/",
    github_button=True,
    show_powered_by=False,
)
html_show_sphinx = False
html_favicon = "./_static/radar-chart.ico"


plot_include_source = True
plot_formats = [("svg", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False
plot_working_directory = DOCS_DIR.parent
