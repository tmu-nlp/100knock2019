
import subprocess
import locale

def uniq_column(n: int, in_fname: str, out_fname: str):
    d = dict()
    with open(in_fname) as fin,open(out_fname,'w') as fout:
        n_column = []
        content=fin.readlines()
        for line in content:
            words=line.split('\t')
            n_column.append(words[0])
        n_column = set(n_column)
        sorted_items=sorted(n_column)
        for item in sorted_items:
            fout.write(item+'\n')
    return


def uniq_column_unix(n: int, in_fname: str, out_fname: str):
    with open(out_fname,'w') as fout:
        ps_cut = subprocess.Popen(['cut','-f',str(n),'-d','\t',in_fname], stdout=subprocess.PIPE)
        ps_sort = subprocess.Popen(['sort'], stdout=subprocess.PIPE,stdin=ps_cut.stdout)
        ps_uniq = subprocess.Popen(['uniq'],stdout=fout,stdin=ps_sort.stdout)
        # 書いたけどよく意味分かってない。
        ps_cut.wait()
        ps_sort.wait()
        ps_uniq.wait()
    return