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
import sphinx_rtd_theme
import time  ###

project = 'SunFounder Beginners Lab Kit'
copyright = f'{time.localtime().tm_year}, SunFounder'  ###
author = 'www.sunfounder.com'

# -- sphinx_rtd_theme Theme options -----------------------------------------------------
html_theme_options = {
    'flyout_display': 'attached',
    'version_selector': False,
    'language_selector': False,
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# SunFounder logo

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js', 
    './lang.js', # new
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]

#### RTD+

# html_js_files = [
#     'https://ezblock.cc/readDocFile/custom.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',

# ]
# html_css_files = [
#     'https://ezblock.cc/readDocFile/custom.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
# ]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.



# open link in a new window

rst_epilog = """

.. |link_beginner_lab_kit| raw:: html

    <a href="https://www.sunfounder.com/products/sunfounder-beginners-lab-starter-kit" target="_blank">Beginner's Lab Kit</a>


.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>


.. |link_wiki_avometer| raw:: html

    <a href="https://en.wikipedia.org/wiki/Avometer" target="_blank">Wikipedia - Avometer</a>


.. |link_docs_ide| raw:: html

    <a href="https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2/" target="_blank">Getting Started with Arduino IDE 2</a>


.. |link_arduino_forum| raw:: html

    <a href="https://forum.arduino.cc/" target="_blank">Arduino Forum</a>

.. |link_arduino_project_hub| raw:: html

    <a href="https://projecthub.arduino.cc/" target="_blank">Arduino Project Hub</a>

.. |link_arduino_docs| raw:: html

    <a href="https://docs.arduino.cc/" target="_blank">Official Arduino Documentation</a>

.. |link_download_arduino| raw:: html

    <a href="https://www.arduino.cc/en/software#future-version-of-the-arduino-ide" target="_blank">Arduino Software Page</a>

.. |link_ascii| raw:: html

    <a href="https://www.asciitable.com/" target="_blank">ASCII table of characters</a>

.. |link_arduino_reference| raw:: html

    <a href="https://www.arduino.cc/reference/en/" target="_blank">Language Reference</a>


"""


# language links

rst_epilog += """

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/beginners-lab-kit/de/latest/" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/beginners-lab-kit/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/beginners-lab-kit/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_fr_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/beginners-lab-kit/fr/latest/" target="_blank">Didacticiels en ligne en français</a>

.. |link_es_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/beginners-lab-kit/es/latest/" target="_blank">Tutoriales en línea en español</a>

.. |link_it_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/beginners-lab-kit/it/latest/" target="_blank">Tutorial online in italiano</a>
    
"""

# component pic
rst_epilog += """

.. |list_green_led| image:: /img/list_cpn/list_green_led.png 
.. |list_red_led| image:: /img/list_cpn/list_red_led.png 
.. |list_blue_led| image:: /img/list_cpn/list_blue_led.png 
.. |list_yellow_led| image:: /img/list_cpn/list_yellow_led.png 
.. |list_white_led| image:: /img/list_cpn/list_white_led.png 
.. |list_rgb_led| image:: /img/list_cpn/list_rgb_led.png 
.. |list_10ohm| image:: /img/list_cpn/list_10ohm.png 
.. |list_100ohm| image:: /img/list_cpn/list_100ohm.png 
.. |list_220ohm| image:: /img/list_cpn/list_220ohm.png 
.. |list_330ohm| image:: /img/list_cpn/list_330ohm.png 
.. |list_1kohm| image:: /img/list_cpn/list_1kohm.png 
.. |list_2kohm| image:: /img/list_cpn/list_2kohm.png 
.. |list_5_1ohm| image:: /img/list_cpn/list_5_1ohm.png 
.. |list_10kohm| image:: /img/list_cpn/list_10kohm.png 
.. |list_100kohm| image:: /img/list_cpn/list_100kohm.png 
.. |list_1mohm| image:: /img/list_cpn/list_1mohm.png 
.. |list_active_buzzer| image:: /img/list_cpn/list_active_buzzer.png 
.. |list_passive_buzzer| image:: /img/list_cpn/list_passive_buzzer.png 
.. |list_button| image:: /img/list_cpn/list_button.png 
.. |list_thermistor| image:: /img/list_cpn/list_thermistor.png 
.. |list_photoresistor| image:: /img/list_cpn/list_photoresistor.png 
.. |list_potentiometer| image:: /img/list_cpn/list_potentiometer.png 
.. |list_7segment| image:: /img/list_cpn/list_7segment.png 
.. |list_74hc595| image:: /img/list_cpn/list_74hc595.png 
.. |list_ultrasonic| image:: /img/list_cpn/list_ultrasonic.png 
.. |list_meter| image:: /img/list_cpn/list_meter.png 
.. |list_wire| image:: /img/list_cpn/list_wire.png
.. |list_breadboard| image:: /img/list_cpn/list_breadboard.png 
.. |list_usb_cable| image:: /img/list_cpn/list_usb_cable.png 
.. |list_uno_r3| image:: /img/list_cpn/list_uno_r3.png 

"""
