import os
import subprocess
import re

def count_file_lines_py(fname):
    with open(fname) as f:
        for line, l in enumerate(f):
            pass
    return line + 1

def count_file_lines_unix(fname):
    lines_string =''.join(os.popen('wc -l < '+fname).readlines())
    return (int(lines_string))
