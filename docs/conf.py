#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Spinning Up documentation build configuration file.

import os
import sys

# Make sure spinup is accessible without going through setup.py
dirname = os.path.dirname
sys.path.insert(0, dirname(dirname(__file__)))

# Mock modules that are heavy or hard to install in doc builds
from unittest.mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

MOCK_MODULES = ['mpi4py',
                'torch',
                'torch.optim',
                'torch.nn',
                'torch.distributions',
                'torch.distributions.normal',
                'torch.distributions.categorical',
                'torch.nn.functional',
                'gymnasium',
                'gymnasium.spaces',
                'scipy',
                'scipy.signal',
                ]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

import spinup

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

project = 'Spinning Up'
copyright = '2018, OpenAI'
author = 'Joshua Achiam'

version = ''
release = ''

# -- i18n configuration --------------------------------------------------

locale_dirs = ['locales/']
gettext_compact = False

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']

html_logo = 'images/spinning-up-logo2.png'
html_theme_options = {
    'logo_only': True
}
html_favicon = 'openai_icon.ico'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'default'

todo_include_todos = False

# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'SpinningUpdoc'

# -- MathJax configuration -----------------------------------------------

mathjax3_config = {
    'tex': {
        'macros': {
            'E': r'{\mathrm E}',
            'underE': [r'\underset{\begin{subarray}{c}#1 \end{subarray}}{\E}\left[ #2 \right]', 2],
            'Epi': [r'\underset{\begin{subarray}{c}\tau \sim \pi \end{subarray}}{\E}\left[ #1 \right]', 1],
        }
    }
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'preamble': r'''
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{amsmath}
\usepackage{cancel}


\newcommand{\E}{{\mathrm E}}

\newcommand{\underE}[2]{\underset{\begin{subarray}{c}#1 \end{subarray}}{\E}\left[ #2 \right]}

\newcommand{\Epi}[1]{\underset{\begin{subarray}{c}\tau \sim \pi \end{subarray}}{\E}\left[ #1 \right]}
''',
}

latex_documents = [
    (master_doc, 'SpinningUp.tex', 'Spinning Up Documentation',
     'Joshua Achiam', 'manual'),
]

man_pages = [
    (master_doc, 'spinningup', 'Spinning Up Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'SpinningUp', 'Spinning Up Documentation',
     author, 'SpinningUp', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    app.add_css_file('css/modify.css')
