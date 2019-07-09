import re
import xml.dom.minidom
from . import xmlpp
import cudatext as app

def format_pp(text):

    WIDTH = 100 #reformat at max width
    indent = app.ed.get_prop(app.PROP_TAB_SIZE)
    eol = '\n'
    text = xmlpp.get_pprint(text, indent=indent, width=WIDTH)
    lines = text.splitlines()
    text = eol.join(lines)+eol
    return text

def format_dom(source):

    try:
        parsedCheck = xml.dom.minidom.parseString(source)
    except xml.parsers.expat.ExpatError as e:
        app.msg_box('XML Tidy:\n'+str(e), app.MB_OK+app.MB_ICONERROR)
        return

    re_compile = re.compile("<.*?>")
    result = re_compile.findall(source)
    source = ''.join(result)

    indent_text = ' '*app.ed.get_prop(app.PROP_TAB_SIZE)
    parsed = parsedCheck
    lines = parsed.toprettyxml(indent=indent_text).split('\n')
    source = '\n'.join([line for line in lines if line.strip()])
    return source
