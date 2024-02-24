# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# NOTE:
# pip install sphinx_rtd_theme
# is needed in order to build the documentation

import sys
from pathlib import Path
from sequence.__version__ import __version__
from datetime import datetime

sys.path.append(str(Path.cwd().parent.parent))
print(sys.path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sequentium"
author = "Vasco Schiavo"
copyright = f"2023 - {datetime.now().year}, Vasco Schiavo"
version = f"{__version__}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",  # parameters look better than with numpydoc only
    "numpydoc",
]

templates_path = ["templates"]
exclude_patterns = []

language = "en"
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["static"]
html_theme_options = {
    "github_url": "https://github.com/unit8co/darts",
}
