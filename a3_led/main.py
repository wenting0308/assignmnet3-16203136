
import os
import sys
import argparse
from pprint import pprint

def check_is_instr(string):
    """return True if words is in the list"""
    return string in ["turn", "on", "off", "switch"]

def check_combin_instr(instr):
    """return True if instruction afer combination is valid"""
    return instr in ["turnon", "turnoff", "switch"]

def check_region(size, r):
    """return adjust region with valid x, y coordinate"""
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

def run_led(led, instr, r):
    """return 2D list after run the command"""
    xFrom, xTo = r[0], r[2]
    yFrom, yTo = r[1], r[3]
    
    #turn on
    if instr == "turnon":
        for x in range(xFrom, xTo+1):
            for y in range(yFrom, yTo+1):
                led[x][y] = True
    
    #turn off
    elif instr == "turnoff":
        for x in range(xFrom, xTo+1):
            for y in range(yFrom, yTo+1):
                led[x][y] = False
    
    #switch
    else:
        for x in range(xFrom, xTo+1):
            for y in range(yFrom, yTo+1):
                if led[x][y] == True:
                    led[x][y] = False
                else:
                    led[x][y] = True
    return led
    

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
            for s in command:
                #first check if is instruction 
                if check_is_instr(s):
                    instr += s
                #ignore "through"
                elif s.isdigit():
                    region[i] = int(s)
                    i+=1
            
            #check if instruction after combination is valid
            if not check_combin_instr(instr):
                continue
            print("before:",instr, region)
            region = check_region(ledSize, region)
            print("return:", region)
            print()
            
            #run command
            ledLight = run_led(ledLight, instr, region)
            pprint(ledLight)
                    
                    
                    
            
            count += 1
        print(count)
    fn.close()
        
