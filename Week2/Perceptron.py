# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:39:43 2020

@author: Jeremy
"""
import numpy as np

x = np.array([[1,0],[-1,1.5],[-1,-1]])
y = np.array([1,-1,1])

def Perceptron(x,y,T):
    theta = np.array([0,0])
    theta_0 = 0
    for t in range(1,T):
        for i in range(0,len(y)-1):
            if y[i]*(np.dot(theta,x[i])+theta_0) <= 0:
                theta = theta + y[i]*x[i]
                theta_0 = theta_0 + y[i]
                
    return theta, theta_0

def PerceptronOrigin(x,y,T):
    counter = 0
    theta = np.array([0,0])
    for t in range(1,T):
        tmp = theta
        for i in range(0,len(y)):
            if y[i]*(np.dot(theta,x[i])) <= 0:
                theta = theta + y[i]*x[i]
                print(theta)
        if tmp is not theta:
            counter=counter+1
    return theta, counter

print(PerceptronOrigin(x,y,5))