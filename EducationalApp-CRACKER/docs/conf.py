# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EducationalApp-CRACKER'
copyright = '2024, Super Jeż, Super Krowa, Super Pies'
author = 'Super Jeż, Super Krowa, Super Pies'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output

html_theme = 'alabaster'
html_static_path = ['_static']

# Include the paths to your project modules
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- License Information
license_text = '''
EducationalApp-CRACKER jest dostępny na licencji MIT. Zobacz plik `LICENSE` w katalogu głównym projektu, aby uzyskać więcej informacji.

MIT License

Copyright (c) 2024 Super Jeż, Super Krowa, Super Pies

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
