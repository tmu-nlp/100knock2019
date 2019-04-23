import unittest
import os
import filecmp
from knock010 import count_file_lines_py, count_file_lines_unix
from knock011 import convfile_tab2space, convfile_tab2space_unix

class TestKnockChp2(unittest.TestCase):
    def test_knock010(self):
        print("test knock010")
        in_file="hightemp.txt"
        lines_py =  count_file_lines_py(in_file)
        lines_unix = count_file_lines_unix(in_file)
        self.assertEqual(lines_py,lines_unix)

    def test_knock011(self):
        print("test knock011")
        in_file='hightemp.txt'
        conv_fname_py=convfile_tab2space(in_file)
        conv_fname_unix=convfile_tab2space_unix(in_file)
        print("compare "+conv_fname_py+" and "+conv_fname_unix)
        self.assertTrue(filecmp.cmp(conv_fname_py,conv_fname_unix,shallow=False))
        # self.assertTrue(filecmp.cmp(conv_fname_py,'py_tab2space_hightemp1.txt',shallow=False))

if __name__=='__main__':
    unittest.main()
