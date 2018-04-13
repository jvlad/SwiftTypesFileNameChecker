import sys
from os import walk
f = []
mypath = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
endf = []
for i in f:
    if ".swift" in i:
        endf.append(i)
print(endf)        


