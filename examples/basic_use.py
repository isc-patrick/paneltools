import panel as pn
from paneltools import utils
from paneltools.golden import IRISGoldenTemplate

pn.extension()

template = IRISGoldenTemplate(
        title="Basic Usage",
        # sidebar = [],
        # header=[],
        header_background = '#FFFFFF')

main_content = pn.pane.HTML('<BR><B>I am the first content pane</B>', )
main_content2 = pn.pane.HTML('<BR><B>Second content pane, here</B>')
main_content3 = pn.pane.HTML('<BR><B>Number three in the house</B>')

# app_components = [main_content, main_content2, main_content3]
# icon = "square"
template.main.append(pn.Card(main_content, title="One", name="One", hide_header=True))
template.main.append(pn.Card(main_content2, title="Two", name="Two", hide_header=True))
template.main.append(pn.Card(main_content3,  title="Three ", name="Three", hide_header=True))

pn.extension(raw_css=[utils.frost_css])

template.servable()