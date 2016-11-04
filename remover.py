import os
from glob import glob
filelist = glob('**/*.pyc')
filelist.append('data_csv.csv')
for f in filelist:
    os.remove(f)
