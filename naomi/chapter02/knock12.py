# python -m unittest discover

import subprocess

def extcolumn(nst_colmn: int, in_fname: str, out_fname: str):
    with open(in_fname) as fin, open(out_fname,'w') as fout:
            for line, l in enumerate(fin):
                words=l.split('\t')
                
                fout.write(words[nst_colmn]+'\n')
    return


def extcolumn_unix(nst_colmn: int,in_fname: str,out_fname: str):
    nst_colmn=str(nst_colmn+1)
    with open(out_fname,'w') as fout:
        subprocess.run(["cut","-f",nst_colmn,"-d",'\t',in_fname],stdout=fout)
        
    return