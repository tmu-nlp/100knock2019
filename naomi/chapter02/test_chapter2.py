# python -m unittest discover
import unittest
import os
from os.path import join, getsize
import filecmp
import subprocess
from knock10 import count_file_lines_py, count_file_lines_unix
from knock11 import convfile_tab2space, convfile_tab2space_unix
from knock12 import extcolumn, extcolumn_unix
from knock13 import mergefiles, mergefiles_unix
from knock14 import headfile, headfile_unix
from knock15 import tailfile, tailfile_unix
from knock16 import splitfile, splitfile_unix
from knock17 import uniq_column, uniq_column_unix
from knock18 import sort_column, sort_column_unix
from knock19 import countfreq, countfreq_unix

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

    def test_knock012(self):
        print("test knock012")
        in_file='hightemp.txt'
        extcolumn(0,in_file,'col1.txt')
        extcolumn_unix(0,in_file,'col1_unix.txt')
        extcolumn(1,in_file,'col2.txt')
        extcolumn_unix(1,in_file,'col2_unix.txt')
        self.assertTrue(filecmp.cmp('col1.txt','col1_unix.txt',shallow=False))
        self.assertTrue(filecmp.cmp('col2.txt','col2_unix.txt',shallow=False))

    def test_knock013(self):
        print("test knock013")
        mergefiles('col1.txt','col2.txt','merged.txt')
        mergefiles_unix('col1.txt','col2.txt','merged_unix.txt')
        self.assertTrue(filecmp.cmp('merged.txt','merged_unix.txt',shallow=False))
    
    def test_knock014(self):
        print("test knock014")
        headfile(5,'hightemp.txt','head.txt')
        headfile_unix(5,'hightemp.txt','head_unix.txt')
        self.assertTrue(filecmp.cmp('head.txt','head_unix.txt',shallow=False))

    def test_knock015(self):
        print("test knock015")
        tailfile(5,'hightemp.txt','tail.txt')
        tailfile_unix(5,'hightemp.txt','tail_unix.txt')
        self.assertTrue(filecmp.cmp('tail.txt','tail_unix.txt',shallow=False))
        
    def test_knock016(self):
        nsplit = 5
        pythondir = 'dir_splitfiles'
        unixdir = 'dir_splitfiles_unix'
        print("test knock016")
        splitfile(nsplit,'hightemp.txt',pythondir)
        splitfile_unix(nsplit,'hightemp.txt',unixdir)

        flistpy = os.listdir(pythondir)
        flistunix = os.listdir(unixdir)

        self.assertEqual(len(flistpy),len(flistunix))
        for i in range(nsplit):
            print('iterator={0}'.format(i))
            self.assertTrue(filecmp.cmp(pythondir+'/'+flistpy[i],unixdir+'/'+flistunix[i]))

    def test_knock017(self):
        uniq_column(1,'hightemp.txt','uniq.txt')
        uniq_column_unix(1,'hightemp.txt','uniq_unix.txt')
        with open('uniq.txt') as pyf, open('uniq_unix.txt') as unixf:
            items_py = []
            items_unix = []
            lines_py = pyf.readlines()
            lines_unix = unixf.readlines()
            for item in lines_py:
                items_py.append(item)
            for item in lines_unix:
                items_unix.append(item)
        # self.assertTrue(filecmp.cmp('uniq.txt','uniq_unix.txt',shallow=False))
        self.assertCountEqual(items_py,items_unix)

    def test_knock018(self):
        print("test knock018")
        sort_column(3,'hightemp.txt','sort.txt')
        sort_column_unix(3,'hightemp.txt','sort_unix.txt')
        self.assertTrue(filecmp.cmp('sort.txt','sort_unix.txt',shallow=False))

    def test_knock019(self):
        countfreq(1,'hightemp.txt','count.txt')
        countfreq_unix(1,'hightemp.txt','count_unix.txt')
        self.assertTrue(filecmp.cmp('count.txt','count_unix.txt',shallow=False))

if __name__=='__main__':
    unittest.main()