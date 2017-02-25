
import os
import sys
import argparse


# --input as optional argument for user to input a filename to process
parser = argparse.ArgumentParser("Process input file")
# at least one argument is required
parser.add_argument('--input', help='a filename for caluclation', nargs='+')
args = parser.parse_args()

filename = args.input
print(type(filename))

# read file of argument input
infile = '../input_file/' + str(filename[0])
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
fn.close()
    
