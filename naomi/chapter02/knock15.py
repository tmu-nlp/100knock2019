
import subprocess

def tailfile(n: int, in_fname: str, out_fname: str):
    with open(in_fname) as fin,open(out_fname,'w') as fout:
        rv_content=reversed(fin.readlines())
        lines=[]
        for counter, line in enumerate(rv_content):
            if counter>=n:
                break
            lines.insert(0,line)
        print(''.join(lines))
        fout.write(''.join(lines))
    return


def tailfile_unix(n: int, in_fname: str, out_fname: str):
    with open(out_fname,'w') as fout:
        subprocess.run(["tail","-n",str(n),in_fname],stdout=fout)
    return