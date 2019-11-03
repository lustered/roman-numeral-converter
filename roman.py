#!/usr/bin/env python3   
import os
import sys

# takes an argument  ex: MDCIXI
# otherwise uses a default roman numeral
# can also take an int and convert it to a roman numeral 
default_string = 'MDCXIII'
arg = str(sys.argv[1]) if len(sys.argv) == 2 else default_string 

def converter(arg):
    print('Using string %s:' % (default_string if arg == default_string else arg))
    dic = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    
    if arg.isdigit():
        dic = {v: k for k, v in dic.items()}
        print(dic[int(arg)])
    else:
        values = [value for value in arg]
        values = [dic[x] for x in values]

        for n in range(len(values)-1):
            if values[n] < values[ n+1]:
                values[n] *= -1

    print('Value of %s: \t %s' % (arg, str(sum(values))))

if __name__ == '__main__':
    converter(arg)


