import numpy as np # for calculations 
import matplotlib.pyplot as plt # for plots
from helpers import * # misc functions

G = 6.6743e-11 # N m2 kg-2; Newton's Constant
k_B = 1.380649e-23 # J/K; Boltzmann's Constant
m_p = 1.67262192e-27 # kg; proton mass
c = 299792458 # m/s

M_sun = 1.9884e30 # kg
R_sun = 6.957e8 # m
L_sun = 3.86e26 # W
Teff_sun = 5780 # effective temperature, K

M_earth = 5.972e24 # kg
R_earth = 6371e3 # m 

year = 365.25 * 24 * 3600