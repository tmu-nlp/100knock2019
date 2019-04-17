import os
import subprocess
import re

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def file_len_unix(fname):
    resultstring =''.join(os.popen('wc -l < hightemp.txt').readlines())
    return (int(resultstring))
