import subprocess

def convfile_tab2space(in_fname):
    out_fname='py_tab2space_'+in_fname
    with open(in_fname) as fin, open(out_fname,'w') as fout:
        for line in fin:
            fout.write(line.replace('¥t',','))
    return out_fname

def convfile_tab2space_unix(in_fname):
    out_fname='unix_tab2space_'+in_fname
    res = subprocess.call('cp '+in_fname+' '+out_fname)
    res = subprocess.call('expand -t 1 '+out_fname)
    return out_fname

#os.system('wc -l hightemp.txt')
