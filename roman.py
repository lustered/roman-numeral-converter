#!/usr/local/bin/python3
import sys

# takes an argument  ex: MDCIXI
# otherwise uses a default roman numeral
default_string = 'MDCXIII'
if len(sys.argv) == 2 :
    roman = str(sys.argv[1])
else:
    roman = default_string
    print('Using default string: ' + default_string)

#key:value   numeral:value
dic = {'M': 1000,'D': 500,'C':100,'L':50,'X':10,'V':5,'I':1}
values = [value for value in roman]
values = [dic[x] for x in values]

for n in range(len(values)-1):
    if values[n] < values[ n+1]:
        values[n] *= -1


print('Value of: ' + roman +"\t"+ str(sum(values)))


