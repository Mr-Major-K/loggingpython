# Allgemeine Konfiguration
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Projektinformationen
project = 'Mein Projekt'
copyright = '2024, Mein Name'
author = 'Mein Name'

# Version
version = '0.1'
release = '0.1.0'

# Sprache
language = 'de'

# Theme
html_theme = 'python_docs_theme'

# HTML-Theme-Optionen
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Weitere Optionen können hier hinzugefügt werden
}

# Pfad für statische Dateien
html_static_path = ['_static']

# Exclude-Muster
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Erweiterungen
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    # Weitere Erweiterungen können hier hinzugefügt werden
]

# Autodoc-Optionen
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# Weitere Konfigurationen können hier hinzugefügt werden
