
import os
import sys
import argparse
from pprint import pprint

def check_instruction(instr):
    return instr in ["turn", "on", "off", "switch", "turnon","turnoff","switch"]

def check_region(size, r):
    #check if out of size
    for i in range(4):
        if r[i] < 0:
            r[i] = 0
        elif r[i] > size-1:
            r[i] = size - 1
    #check if start point is less than end point
    if r[0]>r[2] or r[1]>r[3]:
        #swap
        r[0], r[2] = r[2], r[0]
        r[1], r[3] = r[3], r[1]
        
    return r

    

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
        #create 2D list and initialize value to False (turn off)
        ledLight = [ [False for i in range(ledSize)] for i in range(ledSize) ]
        pprint(ledLight)
         
        count = 0
        while line !='':
            
            line = fn.readline()
            #split command and store as list
            line = line.replace(","," ")
            command=line.split()
            
            #decompose command to instruction and region
            #initialize
            instr = ""
            region = [0,0,0,0]
            i = 0
            for x in command:
                #first check if is valid instruction 
                if check_instruction(x):
                    instr += x
                #ignore "through"
                elif x.isdigit():
                    region[i] = int(x)
                    i+=1
            
            #check if instruction after combination is valid
            if not check_instruction(instr):
                continue
            print("before:",region)
            region = check_region(ledSize, region)
            print("return:", region)
            print()
            
                    
                    
                    
                    
                    
            
            count += 1
        print(count)
    fn.close()
        
