import sys
import re

def replace_etiquettes(file_name, dict_etiquettes):
    f = open(file_name, "r")
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        #for i in range(len(lines)):



"""
   
    ([^\/]+$)
"""