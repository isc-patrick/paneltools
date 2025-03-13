# panel-tools
Components, Templates, tools for use with Panel

Right now this just contains a customized version of the GoldenLayout Template which adds functionality to:

 - Saving state to local browser cache
 - Frost-like css
 - ISC logo
 - Lock components from dragging, resize only


## Examples
All examples require installation of the paneltools library
examples/basic_example.py
    1. python -m panel serve examples/basic_use.py --static-dirs assets=paneltools/static/



### Notes
- Removing the tabs headers currently does not work if there is more than one tab in a stack as the HasHeaders property is set globally. I think this can be modified by setting individual stacks and not setting for shared headers Details here: https://github.com/golden-layout/golden-layout/pull/245



### TODO
 - Add app name to savedState variable

Whether this is because people are busy, don’t think this is useful and will take too much of their time, or because of a preference toward holding their cards close, I am not sure and it is likely a bit of all of those and other things I don’t know. But I do know that this is only something that I can facilitate with the help of those who know the products and more importantly know the prospects and use cases they are pitching

