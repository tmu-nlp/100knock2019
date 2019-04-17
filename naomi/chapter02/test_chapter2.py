import unittest
import os
import filecmp
from knock010 import file_len, file_len_unix

class TestKnockChp2(unittest.TestCase):
    def test_knock010(self):
        print("test knock010")
        file="hightemp.txt"
        py_result =  file_len(file)
        unix_result = file_len_unix(file)
        self.assertEqual(py_result,unix_result)

    def test_knock011(self):
        print("test knock011")
        file1='hightemp.txt'
        file2='hightemp.txt'
        self.assertTrue(filecmp.cmp(file1,file2,shallow=True))

if __name__=='__main__':
    unittest.main()
