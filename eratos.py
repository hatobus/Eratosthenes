#coding:utf-8
import time
import math
import numpy as np

def flatten(L):
    if isinstance(L, list):
        if L == []:
            return []
        else:
            return flatten(L[0]) + flatten(L[1:])
    else:
        return [L]

def Eratos(data):

    p_list = [] # そすー！
    tmp = []
    num = int(math.sqrt(len(data)))+1
    for i in data:
        i=data[0]
        if i>num:
            break
        else:
            p_list.append(i)
            for j in data:
                if j%i == 0:
                    data.remove(j)
        
    p_list.append(data)
    return p_list

x = int(input())

r_list = list(range(2,(x+1)))
ans = []
ans = Eratos(r_list)

print("prime numbers is ")
print(ans)
print(sorted(flatten(ans)))