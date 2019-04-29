# python -m unittest discover
import unittest
import filecmp
from knock20 import jsons2dict

class TestKnockChp3(unittest.TestCase):
    def test_jsons2dict(self):
        print('test_jsons2dict')
        in_file='test.json'

        refdict = { "text": "#転送 [[アイルランド共和国]]",\
                    "title": "アイルランド"}

        with open(in_file) as fin:
            mydict = jsons2dict(fin,'アイルランド')
        
        self.assertEqual(mydict,refdict)

if __name__=='__main__':
    unittest.main()