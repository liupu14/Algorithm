## _*_ coding:utf-8 _*_
#************************************************#
# File Name: infectious_disease_model.py
# Author: liupu
# mail: lpgauss@163.com
# Created Time: 三  2/12 22:03:23 2020
#************************************************#

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def SI_model(Num,infections=1,r=10,beta=0.01,days=200):
    """
    Num = Total population an area
    infections = initial number of people by infected
    r = number of people touched by every infection 
    beta = the probility by infected
    days = the days 
    """
    Suscends = Num - infections 
    Suscends_list = []
    infections_list = []
    Suscends_list.append(Suscends)
    infections_list.append(infections)

    for ii in range(days):
        sus_next = Suscends_list[-1] - r * beta * Suscends_list[-1] / Num * infections_list[-1]
        inf_next = infections_list[-1] + r * beta * Suscends_list[-1] / Num * infections_list[-1]
        Suscends_list.append(sus_next)
        infections_list.append(inf_next)

    plt.plot(Suscends_list,label="Suscends")
    plt.plot(infections_list,label="infection")
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("SI Model") 


