
import subprocess
import math
# from string import ascii_lowercase

def splitfile(n: int, in_fname: str, dir_name: str):
    # create directory if not existing
    subprocess.run(['mkdir','-p',dir_name])
    
    with open(in_fname) as fin:
        lines=fin.readlines()
        n_lines=len(lines)
        chnk_lines=math.ceil(n_lines/n)
        for i_file in range(n):
            print(lines)
            f = open('div_'+str(i_file),'w+')
            f.writelines(lines[chnk_lines*i_file:chnk_lines*(i_file+1)])

    return

def splitfile_unix(n: int, in_fname: str, dir_name: str):
    # create directory if not exiosting
    subprocess.run(['mkdir','-p',dir_name])
    with open(in_fname) as fin:
        lines=fin.readlines()
        n_lines=len(lines)
    chnk_lines=math.ceil(n_lines/n)
    subprocess.run(['split','-l',str(chnk_lines),'-d',in_fname,dir_name+'/div_'])
    return