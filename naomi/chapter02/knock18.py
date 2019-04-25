
import subprocess
import operator
from operator import itemgetter

def sort_column(col: int, in_fname: str, out_fname: str):
    with open(in_fname) as fin,open(out_fname,'w') as fout:
        lines=fin.readlines()
        locs=[]
        
        for line in lines:
            locs.append(cityclass(line.split()[0],line.split()[1],line.split()[2],line.split()[3]))

        # sortedlines=sorted(linelist,key=itemgetter(col-1))
        sortedlocs=sorted(locs, key=lamda cityclass: cityclass.temp)
                
        # for line in sortedlines:
        #         fout.write('\t'.join(line)+'\n')
    return


def sort_column_unix(col: int, in_fname: str, out_fname: str):
    with open(out_fname,'w') as fout:
        ps_cut = subprocess.Popen(['sort','--key',str(col-1),in_fname], stdout=fout)
    return


class cityclass:
    def __init__(self, pref, city, temp, date):
        self.pref = pref
        self.city = city
        self.temp = temp
        self.date = date
    def __repr__(self):
        return repr((self.pref, self.city, self.temp, self.date))