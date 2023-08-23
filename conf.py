#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OXID eSales GraphQL Documentation build configuration file, created by
# sphinx-quickstart on Wed May 20 17:11:52 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime
import sphinx_rtd_theme

# adding PhpLexer
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
from pygments_graphql import GraphqlLexer

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'OXID eSales GraphQL Documentation'
copyright = '{}, OXID eSales AG'.format(datetime.date.today().year)
author = 'OXID eSales AG'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '3.2.0'
# The full version, including alpha/beta/rc tags.
release = '3.2.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# exclude_patterns = ['SPECIFICATION.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_context = {
    'current_version': '3.2',
    'versions': [
            ('5.0', 'https://docs.oxid-esales.com/interfaces/graphql/en/5.0/'),
            ('5.1', 'https://docs.oxid-esales.com/interfaces/graphql/en/5.1/'),
            ('5.2', 'https://docs.oxid-esales.com/interfaces/graphql/en/5.2/'),
            ('6.0', 'https://docs.oxid-esales.com/interfaces/graphql/en/6.0/'),
            ('7.0', 'https://docs.oxid-esales.com/interfaces/graphql/en/7.0/'),
            ('8.0', 'https://docs.oxid-esales.com/interfaces/graphql/en/8.0/'),
            ('latest', 'https://docs.oxid-esales.com/interfaces/graphql/en/latest/')
        ],
    'theme_logo_only': True,
    'show_sphinx': False,
    'display_github': True,
    'github_user': 'OXID-eSales',
    'github_repo': 'graphql-base-module',
    'github_version': 'master',
    'conf_py_path': '/docs/',
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'analytics_id': 'UA-57247309-8',
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'OXID eSales GraphQL Documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    '_static'
]

html_css_files = [
    'oxid.css'
]

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['graphql'] = GraphqlLexer(startinline=True)

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'OXIDe-SalesGraphQLDocumentationdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'OXIDe-SalesGraphQLDocumentation.tex', 'OXID eSales GraphQL Documentation Documentation',
     'OXID eSales', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'oxide-salesgraphqldocumentation', 'OXID eSales GraphQL Documentation Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OXIDe-SalesGraphQLDocumentation', 'OXID eSales GraphQL Documentation Documentation',
     author, 'OXIDe-SalesGraphQLDocumentation', 'One line description of project.',
     'Miscellaneous'),
]

# Use PHP syntax highlighting in code examples by default
highlight_language='php'
