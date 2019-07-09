import xmlpp
import unittest

class xmlpptest(unittest.TestCase):
    def testBasic(self):
        basic = """<xml><test><test>foo bar</test></test><test>foo</test></xml>"""
        result = """<xml>\n    <test>\n        <test>\n            foo bar\n        </test>\n    </test>\n    <test>\n        foo\n    </test>\n</xml>\n"""
        self.assertEquals(xmlpp.get_pprint(basic), result)
    
    def testSpecialTokens(self):
        specialtokens = """<xml:test foo="b:ar">foo::bar:/adf32</xml:test>"""
        result = """<xml:test foo="b:ar">\n    foo::bar:/adf32\n</xml:test>\n"""
        self.assertEquals(xmlpp.get_pprint(specialtokens), result)
        

    def testEncodingWithCDATA(self):
        encodingWithCDATA = """<?xml version="1.0" encoding="UTF-8" ?><testcase><system-out><![CDATA[<fdaa>fda>]]></system-out><system-err><![CDATA[]]></system-err></testcase>"""
        result = """<?xml version="1.0" encoding="UTF-8" ?>\n<testcase>\n    <system-out>\n        <![CDATA[<fdaa>fda>]]>\n    </system-out>\n    <system-err>\n        <![CDATA[]]>\n    </system-err>\n</testcase>\n"""
        self.assertEquals(xmlpp.get_pprint(encodingWithCDATA), result)

if __name__ == "__main__":
    unittest.main()
