#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:59:49 2022

@author: sjcet
"""

import numpy as np
array_2d=np.random.randint(1,50,16).reshape(4,4)
print("the array is:")
print(array_2d)
print("elements of 1st and 2nd column in 2nd and 3rd row:")
print(array_2d[0:4,0:2])
print("2nd and 3rd elements of 1st row:")
print(array_2d[0,1:3])
