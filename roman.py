#!/usr/local/bin/python3

# takes a string ex: 'MDCIIIX'

roman = 'MDCIIIX'
dic = {'M': 1000,'D': 500,'C':100,'L':50,'X':10,'V':5,'I':1}
values = [value for value in roman]
values = [dic[x] for x in values]
#print(values)

for n in range(len(values)-1):
    if n < n+1:
        n *= -1

print(sum(values))

