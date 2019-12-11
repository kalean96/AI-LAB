import random
import math
import numpy as np

maketrans = 'abcdefghijklmnopqrstuvwxy'
rottransN  = '??qgiumeaylnof?xjkrcvstzwb'
def getRot():
    rottransN  = '??qgiumeaylnof?xjkrcvstzwb'
    return rottransN


def decript(word, rottrans):
    enpass = ''
    j = 0
    for i in word:
        id = rottrans.find(i)
        if id >= 0:
            enpass += maketrans[id]
        else:
            enpass += i
    return enpass

new = []

def find():
    flag = True
    for b in maketrans:
        for x in rottransN:
            if x == b:
                flag = False
                break
            else:
                flag = True
        if flag:
            new.append( b )
    return new



    
array = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def verify(rottrans):
    tab = find()
    num = math.factorial(len(tab))
    for x in range(0, num):
        for j in range(0, len(tab)):
            i = rottrans.find("?")
           # print( array[x][j], tab[array[x][j] - 1] )
            rottrans = rottrans[:i] + tab[array[x][j] - 1] + rottrans[(i+1):]
        #print(rottrans)
        print(decript('hdohp', rottrans))
        rottrans = getRot()

verify(getRot())
