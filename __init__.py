import re
import json
import xml.dom.minidom
from . import xmlpp
import cudatext as app
from cuda_fmt import get_config_filename

def options():

    fn = get_config_filename('XML Pretty Print')
    s = open(fn, 'r').read()
    d = json.loads(s)

    tabsize = d.get('tab_size', 2)
    width = d.get('max_width', 100)

    return tabsize, width


def format_pp(text):

    tabsize, width = options()
    text = xmlpp.get_pprint(text, indent=tabsize, width=width)
    lines = text.splitlines()
    text = '\n'.join(lines)+'\n'
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

    tabsize, width = options()

    parsed = parsedCheck
    lines = parsed.toprettyxml(indent=' '*tabsize).split('\n')
    source = '\n'.join([line for line in lines if line.strip()])
    return source
