# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GloveDataHub'
copyright = '2024, Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio'
author = 'Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Aggiungi questa linea
]

templates_path = ['_templates']
exclude_patterns = []

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./API'))
sys.path.insert(0, os.path.abspath('./GUI'))

gdh_logo = "_static/GDH.png"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
