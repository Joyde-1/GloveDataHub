# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# Aggiungi il percorso del progetto alla variabile sys.path
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../../API'))
sys.path.insert(0, os.path.abspath('../../GUI'))

project = 'GloveDataHub'
copyright = '2024, Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio'
author = 'Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

language = 'Python'

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

napoleon_google_docstring = False
napoleon_numpy_docstring = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# Logo configuration
html_logo = "_static/GDH.ico"

# Specific options for alabasyer theme
html_theme_options = {
    'logo': '',
    'logo_name': True,
    'description': 'GloveDataHub documentation',
}