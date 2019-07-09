import cudatext as app
from . import xmlpp

WIDTH = 100 #reformat at max width

def format(text):
    indent = app.ed.get_prop(app.PROP_TAB_SIZE)
    eol = '\n'
    text = xmlpp.get_pprint(text, indent=indent, width=WIDTH)
    lines = text.splitlines()
    text = eol.join(lines)+eol
    return text
