
import subprocess
import operator
from operator import itemgetter

def sort_column(col: int, in_fname: str, out_fname: str):
    with open(in_fname) as fin,open(out_fname,'w') as fout:
        lines=fin.readlines()
        cities=[]

        for line in lines:
            cities.append(line.split())

        sortedcities=sorted(cities, key=lambda x:x[2], reverse=True)

        for line in sortedcities:
            print(line)
            fout.write('\t'.join(line)+'\n')
    return


def sort_column_unix(col: int, in_fname: str, out_fname: str):

    with open(out_fname,'w') as fout:
# https://unix.stackexchange.com/questions/104525/sort-based-on-the-third-column
        # subprocess.Popen(['sort','-k',str(col-1),','+str(col-1),in_fname], stdout=fout)
        subprocess.run(['sort','-r','-k3',in_fname], stdout=fout)

    return

if __name__=='__main__':
    main()

def main():

    return