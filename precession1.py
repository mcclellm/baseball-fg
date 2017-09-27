# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:26:43 2017

@author: mjm
"""

import math
import numpy as np
import matplotlib.pyplot as plt

r = 0.036888137 #meters
m = 0.145291188 #kg

#alpha is theta, m2pct is m2 as % of m, omega is total intial spin, diag is diagnostic flag
def getomegax(alphadeg,m2pct,omega,diag):
    m2 = m*m2pct #mass of point mass at surface
    m1 = m-m2 #mass of isotropic bulk
    if diag: print m, m1, m2
    Ix = (2./5)*m1*r*r #moment of inertia in x
    Iyz = Ix + m2*r*r #moment of inertia in y and z
    B = Iyz/Ix #spin-to-wobble ratio
    C = np.cos(math.radians(alphadeg)) #C stands for cos(theta)
    if diag: print Ix, Iyz, B, C
    omegax = omega*((C**(-2)-1)/B**2+1)**(-1/2) #spin in x-direction, rad/s
    if diag: print omega, omegax
    omegayz = math.sqrt((omega**2-omegax**2)/2) #spin in combined y-z, rad/s
    return [omegax,omegayz]

#Apct is percentage of omega_tot in A = sqrt(wy^2 + wz^2), magnitude of non-x spin    
def gettheta(Apct,m2pct,omega,diag):
    m2 = m*m2pct
    m1 = m-m2
    if diag: print m, m1, m2
    Ix = (2./5)*m1*r*r
    Iyz = Ix + m2*r*r
    B = Iyz/Ix
    if diag: print Ix, Iyz, B
    omegax = math.sqrt(omega**2-(Apct*omega)**2)
    theta = math.acos((1+B**2*(A**2/omegax**2))**(-1/2)) #calculated angle theta (also called alpha)
    return [omegax,theta]

masses = np.arange(0,0.1,0.001) #range of masses to explore
aa = np.arange(0,0.2,0.01) #range of A to explore as percentage of omega
wxs = np.ones((len(masses),len(aa))) #placeholder for omega_x values
thetas = np.ones((len(masses),len(aa))) #placeholder for theta values

wtot = 240. #rad/s, total omega

for M in range(len(masses)):
    for A in range(len(aa)):
        [wx,th] = getomegax(aa[A],masses[M],wtot,False)
        print wx, th
        wxs[M,A] = wx
        thetas[M,A] = th

#contour plot for omega_x, against A and m2        
plt.figure()
CS = plt.contour(aa, masses, wxs)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('omega_x with omega_tot = 240 rad/s')
plt.xlabel('A or omega_yz_hat (as % of omega_tot)')
plt.ylabel('m2 (as % of m_tot)')

#contour plot for theta, against A and m2
plt.figure()
CS = plt.contour(aa, masses, np.degrees(thetas))
plt.clabel(CS, inline=1, fontsize=10)
plt.title('theta with omega_tot = 240 rad/s')
plt.xlabel('A or omega_yz_hat (as % of omega_tot)')
plt.ylabel('m2 (as % of m_tot)')  
#FIGURE 4  


    
masses = np.arange(0,0.1,0.001) #range of masses to explore
angles = np.arange(0,6.,0.1) #range of theta to explore
wxs = np.ones((len(masses),len(angles))) #placeholder for omega_x values
wyzs = np.ones((len(masses),len(angles))) #placeholder for A (or omega_yz_hat) values

wtot = 240. #rad/s

for M in range(len(masses)):
    for A in range(len(angles)):
        [wx,wyz] = getomegax(angles[A],masses[M],wtot,False)
        wxs[M,A] = wx
        wyzs[M,A] = wyz

#contour plot for omega_x, against theta and m2         
plt.figure()
CS = plt.contour(angles, masses, wxs)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('omega_x with omega_tot = 240 rad/s')
plt.xlabel('theta')
plt.ylabel('m2 (as % of m_tot)')
#FIGURE 5a

#contour plot for A (also called omega_yz_hat), against theta and m2    
plt.figure()
CS = plt.contour(angles, masses, wyzs)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('A (omega_yz_hat) with omega_tot = 240 rad/s')
plt.xlabel('theta')
plt.ylabel('m2 (as % of m_tot)')
#FIGURE 5b      