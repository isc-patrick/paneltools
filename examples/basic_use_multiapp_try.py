import panel as pn
from paneltools import utils
from paneltools.golden import IRISGoldenTemplate
from paneltools.main import MainTemplate

from panel import HSpacer, Spacer

import importlib

import importlib.util


template = MainTemplate(
        title="Basic Usage",
        header_background = '#FFFFFF',
        logo='/assets/intersystems-logo.svg',
        sidebar_width=10)

#app1 = importlib.import_module("./basic_use_app.py", "paneltools")

spec = importlib.util.spec_from_file_location("basic_use_app", "basic_use_app.py")
my_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_module)


template.add_app(my_module)

pn.extension(raw_css=[utils.frost_css])

template.servable()