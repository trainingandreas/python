# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:11:14 2021

@author: w010586 - Kevin Schäfer
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~Settings~~~~~~~~~~~~~~~~~~~~~~~~~
#Sound select: Stimmgabel, Horn, Klarinette
Sound='Horn'   
#Language select: DE EN
Language = 'DE'
#Duration select
duration = 10.0   # in seconds, may be float
#Volume select
volume = 1     # range [0.0, 1.0]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~define classes
class Function():
    N = 441000 # Number of samplepoints # Printing Time X-Achses
    T = 1.0 / 100.0 # sample spacing
    t = np.linspace(0.0, N*T, N)
    v = 0
    N_plot=1000
    t_plot = np.linspace(0.0, T*N_plot,N_plot)
    
    def sin(self,a,f,angle_deg,k):
        phi=angle_deg*(np.pi/180)
        self.v=a*np.sin(2*np.pi*f*k*self.t/1000+phi*k)
        return 
    
class Plot():
    language = "XX"  
    
    def plot(self,X,Y):
        plt.plot(X,Y,linewidth = 2)
        plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
        
        if(self.language == "DE"):
            plt.ylabel(r'$\hat x$ [Amplitude]', fontsize='x-large')
            axes1 = plt.gca()
            axes1.set_xlabel("t [Zeit in ms]", fontsize='x-large')
        else: 
            plt.ylabel(r'$\hat x$ [amplitude]', fontsize='x-large')
            axes1 = plt.gca()
            axes1.set_xlabel("t [time in ms]", fontsize='x-large')
            return
p = pyaudio.PyAudio()
#~~~~~~~~~~~~~~~~~~~~~~~~~~generate funktions
graph1=Plot()
graph2=Plot()
graph3=Plot()


    
fx_1_1=Function()


fx_2_1=Function()
fx_2_2=Function()
fx_2_3=Function()
fx_2_4=Function()
fx_2_5=Function()

fx_3_1=Function()
fx_3_2=Function()
fx_3_3=Function()
fx_3_4=Function()
fx_3_5=Function()
fx_3_6=Function()
fx_3_7=Function()


#~~~~~~~~~~~~~~~~~~~~~~~~~~define Sine

fx_1_1.sin(100, 440, 0, 1)  
  
fx_2_1.sin(50, 440, 0, 1)
fx_2_2.sin(60, 440, 0, 2)
fx_2_3.sin(100, 440, 0, 3)
fx_2_4.sin(50, 440, 0, 4)
fx_2_5.sin(20, 440, 0, 5)

fx_3_1.sin(70, 440, 0, 1)
fx_3_2.sin(30, 440, 0, 2)
fx_3_3.sin(85, 440, 0, 3)
fx_3_4.sin(40, 440, 0, 4)
fx_3_5.sin(65, 440, 0, 5)
fx_3_6.sin(40, 440, 0, 6)
fx_3_7.sin(55, 440, 0, 7)


#~~~~~~~~~~~~~~~~~~~~~~~~~~define instrument

Stimmgabel=fx_1_1.v
Horn=fx_2_1.v+fx_2_2.v+fx_2_3.v+fx_2_4.v+fx_2_5.v
Klarinette=fx_3_1.v+fx_3_2.v+fx_3_3.v+fx_3_4.v+fx_3_5.v+fx_3_6.v+fx_3_7.v




volume = 0.2     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
f = 440.0        # sine frequency, Hz, may be float

#~~~~~~~~~~~~~~~~~~~~~~~~~~select instrument

if Sound =='Klarinette':
    samples = (Klarinette/100).astype(np.float32)
    graph3.language = Language
    graph3.plot(fx_1_1.t_plot,Klarinette[0:fx_1_1.N_plot])  
    plt.show()
    
elif Sound == 'Horn':
    samples = (Horn/100).astype(np.float32)
    graph2.language = Language
    graph2.plot(fx_1_1.t_plot,Horn[0:fx_1_1.N_plot])
    plt.show()
    
else:
    samples = (Stimmgabel/100).astype(np.float32)
    graph1.language = Language
    graph1.plot(fx_1_1.t_plot,Stimmgabel[0:fx_1_1.N_plot])
    plt.show()
    
        


#~~~~~~~~~~~~~~~~~~~~~~~~~~output sound

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()