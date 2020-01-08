#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:29:47 2019

@author: liupu
"""

import numpy as np
S0 = 100
K = 110
r = 0.05
sigma = 0.2
T = 1
St = S0 * np.exp(r - 0.5 * sigma**2 + sigma *np.sqrt(T)*np.random.randn(1000))
Hi = np.maximum(St-K,0)
c0 = np.exp(-r*T)*sum(St)/1000
print(c0)
