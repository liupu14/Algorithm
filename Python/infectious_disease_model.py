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

def SIS_model(Num,infections=1,r=10,beta=0.01,gamma=0.02,days=200):
    """
    Num = Total population an area
    infections = initial number of people by infected
    r = number of people touched by every infection 
    beta = the probility by infected
    days = the days 
    gamma = the problity a infection to suscend 
    """
    Suscends = Num - infections 
    Suscends_list = []
    infections_list = []
    Suscends_list.append(Suscends)
    infections_list.append(infections)

    for ii in range(days):
        sus_next = Suscends_list[-1] - r * beta * Suscends_list[-1] / Num * infections_list[-1] + gamma * infections_list[-1]
        inf_next = infections_list[-1] + r * beta * Suscends_list[-1] / Num * infections_list[-1] - gamma * infections_list[-1]
        Suscends_list.append(sus_next)
        infections_list.append(inf_next)

    plt.plot(Suscends_list,label="Suscends")
    plt.plot(infections_list,label="infection")
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("SIS Model") 

def SIR_model(Num,infections=1,R=0,r=10,beta=0.01,gamma=0.02,days=200):
    """
    Num = Total population an area
    infections = initial number of people by infected
    R = recovery
    r = number of people touched by every infection 
    beta = the probility by infected
    gamma = the probility infections to recovery
    days = the days 
    """
    Suscends = Num - infections 
    Suscends_list = []
    infections_list = []
    Recovery_list = []
    Suscends_list.append(Suscends)
    infections_list.append(infections)
    Recovery_list.append(R) 

    for ii in range(days):
        sus_next = Suscends_list[-1] - r * beta * Suscends_list[-1] / Num * infections_list[-1]
        inf_next = infections_list[-1] + r * beta * Suscends_list[-1] / Num * infections_list[-1] - gamma * infections_list[-1]
        rec_next = Recovery_list[-1] + gamma * infections_list[-1]
        Suscends_list.append(sus_next)
        infections_list.append(inf_next)
        Recovery_list.append(rec_next)  

    plt.plot(Suscends_list,label="Suscends")
    plt.plot(infections_list,label="infection")
    plt.plot(Recovery_list,label="Recovery")
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("SIR Model") 

def SEIR_model(Num,exposion=0,infections=1,R=0,r=10,alpha=0.1,beta=0.01,gamma=0.02,days=200):
    """
    Num = Total population an area
    exposion = initial exposion poupulation
    infections = initial number of people by infected
    R = recovery
    alpha = the probility a exposion to infections 
    r = number of people touched by every infection 
    beta = the probility by infected
    gamma = the probility infections to recovery
    days = the days 
    """
    Suscends = Num - infections 
    Suscends_list = []
    exposion_list = []
    infections_list = []
    Recovery_list = []
    Suscends_list.append(Suscends)
    exposion_list.append(exposion)
    infections_list.append(infections)
    Recovery_list.append(R) 

    for ii in range(days):
        sus_next = Suscends_list[-1] - r * beta * Suscends_list[-1] / Num * infections_list[-1]
        exp_next = exposion_list[-1] + r * beta * Suscends_list[-1] / Num * infections_list[-1] - alpha * exposion_list[-1]
        inf_next = infections_list[-1] + alpha * exposion_list[-1] - gamma * infections_list[-1]
        rec_next = Recovery_list[-1] + gamma * infections_list[-1]
        Suscends_list.append(sus_next)
        exposion_list.append(exp_next)
        infections_list.append(inf_next)
        Recovery_list.append(rec_next)  

    plt.plot(Suscends_list,label="Suscends")
    plt.plot(exposion_list,label="exposions")
    plt.plot(infections_list,label="infection")
    plt.plot(Recovery_list,label="Recovery")
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("SEIR Model") 
