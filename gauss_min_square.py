# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 01:14:24 2018

@author: oyata
"""
import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
n=300
for i in range(300):
    x.append(6*((i-1)/(n-1)-0.5))
    ipu = np.random.normal(0, 0.04, 1)
    y.append((np.sin(np.pi*x[i]))/(np.pi*x[i])+0.1*x[i]+ipu)

plt.plot(x,y)
plt.show()
h = 1
ra = 1
def create_K(x,h,num):
    tmp = []
    for i in range(len(x)):    
        tmp.append(np.exp((x[num]-x[i])**2/(-2*h**2)))
    return tmp

def K(x,h):
    tmp = []
    for i in range(len(x)):
        tmp.append(create_K(x,h,i))
    return tmp

k = np.array(K(x,h))
I = np.eye(n)
tp = np.dot(np.linalg.inv((np.dot(k,k)+ra*I)),k)
si = np.dot(tp,y)

xlist = x
ylist = []

def f(xtmp):
    tmp = 0
    for i in range(n):
        tmp = tmp + si[i]*np.exp(((xtmp-x[i])**2)/(-2*h**2))
    return tmp

for i in range(len(xlist)):
    ylist.append(f(xlist[i]))

plt.plot(xlist,ylist)
plt.plot(x,y)
#def min_square(x,y,h,ra):
