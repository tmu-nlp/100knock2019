# python -m unittest discover
import unittest
import filecmp
import re
from knock20 import jsons2dict
from knock21 import extcategories
from knock22 import extcatnames

class TestKnockChp3(unittest.TestCase):
    def test20_jsons2dict(self):
        print('test_jsons2dict')
        in_file='test1.json'

        refdict = { "text": "#転送 [[アイルランド共和国]]",\
                    "title": "アイルランド"}

        with open(in_file) as fin:
            mydict = jsons2dict(fin,'アイルランド')
        
        self.assertEqual(mydict,refdict)
    
    def test21_extcategories(self):
        print('test21_extcategories')
        in_file ='test1.json'

        with open(in_file) as fin:
            mydict = jsons2dict(fin,'南オセチア')
            refcategories=[]
            refcategories.append('[[Category:南オセチア|*]]')
            refcategories.append('[[Category:グルジアの地理]]')
            refcategories.append('[[Category:カフカス]]')
            refcategories.append('[[Category:オセット]]')

            mycategories = extcategories(mydict['text'])


            self.assertEqual(refcategories,mycategories)
        
    def test22_extcatnames(self):
        print('test22_extcatnames')
        in_file ='test1.json'

        with open(in_file) as fin:
            mydict = jsons2dict(fin,'南オセチア')
            refcatnames=[]
            refcatnames.append('南オセチア|*')
            refcatnames.append('グルジアの地理')
            refcatnames.append('カフカス')
            refcatnames.append('オセット')

            mycatnames = extcatnames(mydict['text'])
            self.assertEqual(refcatnames,mycatnames)
        


if __name__=='__main__':
    unittest.main()