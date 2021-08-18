#!/usr/bin/python3
import os
from pathlib import Path

class treetopath:
    def __init__(self):
        #self.f = open(file='file.txt', mode='r')
        self.ff = open(file='ffile.txt', mode='r')

    def replace2(self, s, char, index):
        return s[:index] + char + s[index +1:]

    """
    for line in range(1,len(lines)) :
        for ch in range(0,len(lines[line])) :
            while ord(lines[line][ch]) == 9:
                lines[line] = replace2(lines[line],lines[line-1] , ch)
                break
        print((lines[line]))
    """ 
    def mkdir(self, ff): 
        for line in ff:
            if ord(line.rstrip()[-1]) == 47:
                Path( line.rstrip()).mkdir(parents=True, exist_ok=True)
                print(line.rstrip() + ' path done')
            else:
                Path(line.rstrip()).touch()
                print(line.rstrip() + ' file done')
