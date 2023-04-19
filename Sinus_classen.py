# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:19:56 2021

@author: w010586
"""

import numpy as np
import matplotlib.pyplot as plt

class Function():
    N = 5000 # Number of samplepoints
    T = 1.0 / 100.0 # sample spacing
    t = np.linspace(0.0, N*T, N)
    v = 0
    
    
    def sin(self,a,f,angle_deg,k):
        phi=angle_deg*(np.pi/180)
        self.v=a*np.sin(2*np.pi*f*k*self.t/1000+phi*k)
        return 
    
    
class Plot():
    
    language = "DE"   
  
    
    def plot(self,X,Y):
        plt.plot(X,Y,linewidth = 1)
        
      
    def grid(self,T):                                                                     #Definition Diagramm
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
        plt.xlim(0, T)
        
        
        if(self.language == "DE"):
            plt.ylabel(r'$\hat x$ [Amplitude]', fontsize='x-large')
            axes1 = plt.gca()
            axes1.set_xlabel("t [Zeit in ms]", fontsize='x-large')
        else: 
            plt.ylabel(r'$\hat x$ [amplitude]', fontsize='x-large')
            axes1 = plt.gca()
            axes1.set_xlabel("t [time in ms]", fontsize='x-large')
        #axes2 = axes1.twiny()
        #axes2.set_xticks([0, np.pi, 2*np.pi, 3*np.pi,4*np.pi, 5*np.pi, 6*np.pi])
        #plt.xticks(np.pi*np.arange(0, 7), ('0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$'),size='x-large', color='b')
        #axes2.set_xlabel(r'$\pi$', fontsize='x-large')
        
        return
    
     
    
  
    
  
fx_1=Function()
fx_2=Function()
graph=Plot()

fx_1.sin(230, 50, 0, 1)    
fx_2.sin(100, 440, 0, 1)



graph.plot(fx_1.t,fx_1.v)
graph.plot(fx_2.t,fx_2.v)
graph.grid(fx_1.t)


#graph.grid(fx_1.t)
#graph.grid(fx_1.T)
#graph.plot(fx_1.t,fx_1.v)
#graph.show()
plt.plot(fx_1.t,fx_1.v,linewidth=2)
plt.plot(fx_2.t,fx_2.v,linewidth=2)


