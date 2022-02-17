# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:55:02 2021

@author: alexhou00
"""

with open("extracted_7000_edited.txt", "r", encoding="utf-8") as f1:
    f = open("extracted_7000_edited.dat", "w", encoding="utf-8")
    for line in f1:
        f.write(line)
    f.close()
