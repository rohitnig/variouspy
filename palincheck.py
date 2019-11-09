# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:47:44 2019

@author: rpnigam
"""

import numpy as np
string=input()

d={c : string.count(c) for c in list(string)}
ar1 = np.array(list(d.values()))
print ('Yes') if sum(ar1%2 == 1)<=1 else print ('No')
