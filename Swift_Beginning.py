import sys
from os import walk
'''file = sys.argv[1]
f = open(file, 'r+')
print(f.read())'''


f = []
mypath = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
endf = []
for i in f:
    if ".py" in i:
        endf.append(i)
print(endf)        


