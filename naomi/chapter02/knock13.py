
import subprocess
from itertools import zip_longest

def mergefiles(in_fname1, in_fname2, out_fname):
    with open(in_fname1) as fin1, open(in_fname2) as fin2, open(out_fname,'w') as fout:
            content1 = fin1.readlines()
            content2 = fin2.readlines()
            for l1, l2 in zip_longest(content1,content2):
                fout.write(l1.replace('\n','')+'\t'+l2)
    return


def mergefiles_unix(in_fname1, in_fname2, out_fname):
    with open(out_fname,'w') as fout:
        subprocess.run(["paste",in_fname1,in_fname2],stdout=fout)
    return