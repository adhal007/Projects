import os
import sys

# Add the 'src' directory to sys.path
sys.path.insert(0, os.path.abspath('../src'))

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'OmixHub'
copyright = '2024, Aditya Dhall'
author = 'Aditya Dhall'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
  # Example custom extension from src
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for Napoleon extension ------------------------------------------

# Use Google style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- Options for autodoc extension -------------------------------------------

# Add module names to the documentation
add_module_names = True

# Sort members by type
autodoc_member_order = 'bysource'

# -- Options for todo extension ----------------------------------------------

# Include TODOs in the output
todo_include_todos = True