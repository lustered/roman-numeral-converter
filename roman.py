#!/usr/bin/env python3   
from rome import Roman as rm
import os
import sys

# takes an argument  ex: MDCIXI
# otherwise uses a default roman numeral
# can also take an int and convert it to a roman numeral 

default_string = 'MDCXIII'
arg = str(sys.argv[1]).upper() if len(sys.argv) == 2 else default_string 

def get_values(arg):
    values = [value for value in arg]
    if not arg.isdigit():
        dic = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        values = [dic[x] for x in values]

        for n in range(len(values)-1):
            if values[n] < values[n+1]:
                values[n] *= -1
    else:
        values = rm(int(arg))
    return values


def converter(arg):
    print('Using string %s:' % (default_string if arg == default_string else arg))
    
    values = get_values(arg)
    print('Value of %s: \t %s' % (arg, str(sum(values) if not arg.isdigit() else values)))


if __name__ == '__main__':
    try:
        converter(arg)
    except KeyError:
        print('Please enter a valid string or digit to convert')


