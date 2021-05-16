# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'recobase'
copyright = '2021, Sparsh A.'
author = 'Sparsh A.'

extensions = ['sphinx.ext.autodoc',
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.githubpages',
              'IPython.sphinxext.ipython_console_highlighting',
              'rst2pdf.pdfbuilder'
]

source_suffix = ['.rst', '.ipynb']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
master_doc = 'index'