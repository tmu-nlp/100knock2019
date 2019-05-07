from collections import defaultdict
import subprocess

def countfreq(col: int, in_fname: str, out_fname: str):

    with open(in_fname) as fin,open(out_fname,'w') as fout:
        lines=fin.readlines()
        tokendict = defaultdict(lambda:0)

        for line in lines:
            words = line.split()
            if words[col-1] in tokendict:
                tokendict[words[col-1]]+=1
            else:
                tokendict[words[col-1]]=1        
        for k,v in sorted(tokendict.items(), key=lambda x: x[1],reverse = True):
            fout.write('{0}\t{1}\n'.format(k,v))
            
    return


def countfreq_unix(col: int, in_fname: str, out_fname: str):

    with open(out_fname,'w') as fout:

        ps_cut = subprocess.Popen(['cut','-f',str(col),'-d','\t',in_fname], stdout=subprocess.PIPE)
        ps_sort = subprocess.Popen(['sort'], stdout=subprocess.PIPE,stdin=ps_cut.stdout)
        subprocess.run(['uniq','-c'],stdout=fout,stdin=ps_sort.stdout)
        ps_cut.terminate()
        ps_sort.terminate()


    return

if __name__=='__main__':
    main()

def main():

    return