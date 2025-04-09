# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 08:21:28 2025

@author: Matt
"""

from numpy import sqrt
from pint import UnitRegistry

units = UnitRegistry()
metre = units.metre
second = units.second
a = 9.8 * metre / second**2



u = 0                     # initial velocity
# a = 9.8                   # acceleration due to gravity
t = 3.4                   # time in seconds

v = u + a*t               # final velocity = iniial velocity + velocity due to acceleration over time t
x = u*t + a*t**2 / 2      # distance travelled given time, acceleration and initial velocity


h = 381                   # height of building



def DistGivenTime(t, u=0):
    
    return u*t + a*t**2 / 2 



def TimeGivenDist(x, u=0):
    
    return -1 * (-u + sqrt(u**2 + 2*a*x)) / a



def VelocityOnImpact(t, u=0):
    
    return u + a*t