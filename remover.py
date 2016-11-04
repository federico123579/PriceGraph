import os
from glob import glob
filelist = glob('**/*.pyc')
for f in filelist:
    os.remove(f)
