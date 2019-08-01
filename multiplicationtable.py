# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 06:06:30 2019

@author: Oluleye
"""

for i in range(1,13):
    for j in range(1,13):
        output='{0}*{1}={2},'
        print(output.format(i,j,i*j))