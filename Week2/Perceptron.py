# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:39:43 2020

@author: Jeremy
"""
import numpy as np

x = np.array([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
y = np.array([1,1,-1,-1,-1])

def Perceptron(x,y,T):
    counter = []
    theta = np.array([-3,3])
    theta_0 = -3
    for t in range(1,T):
        for i in range(0,len(y)):
            if y[i]*(np.dot(theta,x[i])+theta_0) <= 0:
                theta = theta + y[i]*x[i]
                theta_0 = theta_0 + y[i]
                counter.append(theta)
    return theta, theta_0, len(counter)
                
    #return theta, theta_0, counter

def PerceptronOrigin(x,y,T):
    counter = []
    theta = np.array([0,0])
    for t in range(1,T):
        for i in range(0,len(y)):
            if y[i]*(np.dot(theta,x[i])) <= 0:
                theta = theta + y[i]*x[i]
                counter.append(theta)
    return counter, len(counter)

print(Perceptron(x,y,10))