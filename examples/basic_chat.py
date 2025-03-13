import panel as pn
from paneltools import utils, components
from paneltools.main import ComponentRegistry, Subscriptions
from paneltools.golden import IRISGoldenTemplate
from panel.chat import ChatInterface

pn.extension("perspective")

def message_bus(contents, user, instance):
    print(f"Contents - {contents}")
    print(f"User - {user}")
    print(instance.metadata)
    print(f"Instance - ID:{id(instance)} - {instance}")

    #comp = registry.get(metadata.get("name"))
    return f"Thanks: " #{comp.name}"

template = IRISGoldenTemplate(
        title="IRIS Chat",
        sidebar = [],
        header=[],
        header_background = '#FFFFFF',
        logo='/assets/intersystems-logo.svg')

registry = ComponentRegistry()
listeners = Subscriptions()

chat_wrapper = components.Chat(callback=message_bus, name="chat", metadata={"random1": 12})
chat = chat_wrapper.chat
registry.add_component("chat", chat_wrapper)

print(f"registered components {[c for c in registry.components]}")
template.main.append(pn.Card(chat, title="Chat", name="Chat", hide_header=True))

pn.extension(raw_css=[utils.frost_css])


template.servable()