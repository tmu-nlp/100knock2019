# python -m unittest discover

import subprocess
from shutil import copyfile

def convfile_tab2space(in_fname):
    out_fname='py_tab2space_'+in_fname
    with open(in_fname) as fin, open(out_fname,'w') as fout:
        for line in fin:
            fout.write(line.replace('\t',' '))
    return out_fname

def convfile_tab2space_unix(in_fname):
    out_fname='unix_tab2space_'+in_fname
    print('convert '+in_fname+' to '+out_fname)
    copyfile(in_fname, out_fname)
    try:
        with open(out_fname,'w') as f:
            subprocess.run(["expand","-t","1",in_fname],stdout=f)
    except:
        print('Error.')
    return out_fname

#os.system('wc -l hightemp.txt')
