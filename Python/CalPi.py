## _*_ coding:utf-8 _*_
#************************************************#
# File Name: CalPi.py
# Author: liupu
# mail: lpgauss@163.com
# Created Time: 一  3/23 21:11:24 2020
#************************************************#

import numpy as np 
import math 

def calpi_basedon_square(r):
    """
    r represent radium
    """
    width = r * 2
    area = width ** 2
    PI = area / r ** 2
    return PI 
def calpi_basedon_sixboards(r):
    area = 1 * np.power(3,1/2) + np.power(3,1/2) * 1/2
    PI = area / r ** 2
    return PI 

