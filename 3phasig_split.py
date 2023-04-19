# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:38:01 2021

@author: w010586
"""

import numpy as np
import matplotlib.pyplot as plt

T = 25 #Zeit [ms] über den Plot
t=np.linspace(0,T,100)

a=230
c=a*0.3
b=0
f=50
k=3
angle_deg1= 0
angle_deg2=120
angle_deg3=240
legend1='L1'
legend1_3='Harmonische'
legend2='L2'
legend2_3=legend1_3
legend3='L3'
legend3_3=legend1_3
legendn="N"
legendn_3=legend1_3

L1=a*np.sin(2*np.pi*f*t/1000+angle_deg1*(np.pi/180))
L1_3=c*np.sin(2*np.pi*f*k*t/1000+angle_deg1*(np.pi/180)*k)
L2=a*np.sin(2*np.pi*f*t/1000+angle_deg2*(np.pi/180))
L2_3=c*np.sin(2*np.pi*f*k*t/1000+angle_deg2*(np.pi/180)*k)
L3=a*np.sin(2*np.pi*f*t/1000+angle_deg3*(np.pi/180))
L3_3=c*np.sin(2*np.pi*f*k*t/1000+angle_deg3*(np.pi/180)*k)

N0=b*np.sin(2*np.pi*f*k*t/1000)
Neutral=L1_3+L2_3+L3_3

'''
plt.plot(t,L1,'o-',markevery=100,linewidth=2, label=legend1)
plt.plot(t,L2,'s-',markevery=105,linewidth=2, label=legend2)
plt.plot(t,L3,'x-',markevery=110,linewidth=2, label=legend3)
plt.plot(t,Neutral,linewidth=2, label="Neutralleiter")
plt.show()
'''
fig, ax = plt.subplots(4,dpi=600,figsize=(8,8),constrained_layout=True)   
fig.suptitle('')
line_labels = []
ax[0].plot(t,L1,linewidth=2,color='red')
#ax[0].plot(t,L1_3,linewidth=2,color='orange')
ax[0].grid()
ax[1].plot(t,L2,linewidth=2, color='green') 
#ax[1].plot(t,L2_3,linewidth=2, color='orange') 
ax[1].grid()
ax[2].plot(t,L3,linewidth=2, color='purple') 
#ax[2].plot(t,L3_3,linewidth=2, color='orange') 
ax[2].grid()
ax[3].plot(t,N0,linewidth=2,color='blue')
#ax[3].plot(t,Neutral,linewidth=2,color='orange')
ax[3].grid()

# Create the legend
fig.legend([legend1,"", legend2,"", legend3,"", legendn],     # The line objects
           labels=line_labels,   # The labels for each line
           loc="center right",   # Position of legend
           borderaxespad=0.1,    # Small spacing around legend box
           title="")  # Title for the legend

# Adjust the scaling factor to fit your legend text completely outside the plot
# (smaller value results in more space being made for the legend)
plt.subplots_adjust(right=1)
        
plt.show()
     
        
        