#!/usr/bin/env python3   
import os
import sys

# takes an argument  ex: MDCIXI
# otherwise uses a default roman numeral
# can also take an int and convert it to a roman numeral 
default_string = 'MDCXIII'
arg = str(sys.argv[1]) if len(sys.argv) == 2 else default_string 

def get_values(arg, dic):
    values = [value for value in arg]
    values = [dic[x] for x in values]

    for n in range(len(values)-1):
        if values[n] < values[ n+1]:
            values[n] *= -1

    return values


def converter(arg):
    print('Using string %s:' % (default_string if arg == default_string else arg))
    dic = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    
    if arg.isdigit():
        inv_map = {value: key for key, value in dic.items()}
        print(inv_map[int(arg)])
    else:
        values = get_values(arg, dic)
        print(values)
        print('Value of %s: \t %s' % (arg, str(sum(values))))

if __name__ == '__main__':
    converter(arg)


