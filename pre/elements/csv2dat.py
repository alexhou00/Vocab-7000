# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:47:52 2021

@author: alexhou00
"""

import csv

import eng_to_ipa as p
  
  
dictionary = [[] for x in range(6)]
for i in range(6):
    f = open('senior_7000_'+str(i+1)+'.csv', newline='', encoding='utf-8')
    reader = csv.reader(f)
    dictionary[i] = list(reader)
    f.close()
    
with open('senior_7000_0.dat', 'w',  encoding='utf-8') as f1:
    for cnt, i in enumerate(dictionary):
        f1.write("\n==== Level "+str(cnt+1)+" ====\n")
        for line in i:
            linedata = line[0].split("@")
            phonics = '['+p.convert(linedata[0])+']'
            linedata.insert(1, phonics)
            f1.write('@'.join(linedata)+'\n')
            
