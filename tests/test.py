
import sys
from nose.tools import *
from a3_led.main import *
from dis import Instruction

def test_parse_input():
    """test input filename from the argument"""
    #eq_(parse_input(), "input_assign3_test.txt", 'Capture filename is not equal to input filename!')
    pass

def test_check_is_instr():
    ok_(check_is_instr("on"), 'Fail checking valid instruction: turn, on, off, switch')
    
def test_check_combin_instr():
    ok_(check_combin_instr("switch"), 'Fail checking valid instruction: turnon, turnoff, switch')
    
def test_check_region():
    correctRegion = [0,0,2,2]
    eq_(check_region(3, [0,0,3,3]), correctRegion, 'Region is not properly corrected.')
    
def test_run_led():
    
    ledBefore = [[False, False, False],
                 [False, False, False],
                 [False, False, False]]
    
    ledAfter = [[True, True, False],
                 [False, False, False],
                 [False, False, False]]
    
    instruction = "turnon"
    runRegion = [0, 0, 0, 1]
    
    eq_(run_led(ledBefore, instruction, runRegion), ledAfter, 'Command is not properly executed on LED light.')
    
def test_main():
    pass
    #lightOn, commandRun = main()
    
    #eq_(lightOn, 3, 'The number on total light on is not correct.')
    #eq_(commandRun, 0, 'The number of command line read is not correct.')




    