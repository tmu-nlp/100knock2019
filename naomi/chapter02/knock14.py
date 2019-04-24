
import subprocess

def shownlines(n: int, in_fname: str, out_fname: str):
    with open(in_fname) as fin,open(out_fname,'w') as fout:
        content=fin.readlines()
        for counter, l in enumerate(content):
            if counter>=n:
                break
            fout.write(l)
            print(l)
    return


def shownlines_unix(n: int, in_fname: str, out_fname: str):
    with open(out_fname,'w') as fout:
        subprocess.run(["head","-n",str(n),in_fname],stdout=fout)
    return