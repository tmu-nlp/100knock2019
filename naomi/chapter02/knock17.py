
import subprocess
import locale

def uniq_column(n: int, in_fname: str, out_fname: str):
    d = dict()
    with open(in_fname) as fin,open(out_fname,'w') as fout:
        content=fin.readlines()
        for line in content:
            words=line.split('\t')
            if words[0] in d:
                d[words[0]] += 1
            else:
                d[words[0]] = 1
        # locale.setlocale(locale.LC_ALL, "C")
        # d.keys().sort(cmp=locale.stroll)
        sorted_items=sorted(d.keys())
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