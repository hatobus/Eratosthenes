#coding:utf-8
#AOJ用（TLEになるので高速化する)

import math
import sys

def f(L):
    if isinstance(L, list):
        if L == []:
            return []
        else:
            return f(L[0]) + f(L[1:])
    else:
        return [L]

def E(d):

    p_list = [] 
    tmp = []
    num = int(math.sqrt(len(d)))+1
    for i in d:
        i=d[0]
        if i>num:
            break
        else:
            p_list.append(i)
            for j in d:
                if j%i == 0:
                    d.remove(j)
        
    p_list.append(d)
    return p_list

lists = []
for line in sys.stdin:
    x= list(range(2,(int(line)+1)))
    print(len(f(E(x))))
