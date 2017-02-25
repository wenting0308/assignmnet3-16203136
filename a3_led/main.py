
import os
import sys
import argparse


# --input as optional argument for user to input a filename to process
parser = argparse.ArgumentParser("Process input file")
# at least one argument is required
parser.add_argument('--input', help='a filename for caluclation', nargs='+')
args = parser.parse_args()
input = args.input

# read file of argument input and check if file exists
infile = '../input_file/' + str(input[0])

try:
    fn = open(infile,'r')

except IOError as e:
    print("Error: ", e)

#if file exist
else:
    #check if content of the file is well structured
    #first line should be the size of LEDs
    line = fn.readline()
    try:
        ledSize = int(line)
        if ledSize <= 0:
            raise ValueError()
        
    except ValueError:
        print("Error: No proper size of LEDs!")
    
    #if size > 0
    else:
        count = 0
        while line !='':
            
            line = fn.readline()
            #split command and store as list
            line = line.replace(","," ")
            command=line.split()
            print(command)
            count += 1
        print(count)
    fn.close()
        
