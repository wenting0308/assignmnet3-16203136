

import os
import sys

infile = 'input_assign3.txt'
if not os.path.isfile(infile):
    print('File', infile, 'does not exist.')
    sys.exit()
else:
    count=0
    fn = open(infile,'r')
    for line in fn:
        string=line
        print(string)
        count += 1
        if count == 20:
            break
fn.close()
    
