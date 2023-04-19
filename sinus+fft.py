# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:51:01 2021

@author: w010586
"""
import numpy as np
import matplotlib.pyplot as plt

#import scipy.fftpack
from scipy.fftpack import fft
#T = 20 #Zeit [ms] über den Plot

#t=np.linspace(0,T,1000)
N = 5000 # Number of samplepoints
T = 1.0 / 100.0 # sample spacing
t = np.linspace(0.0, N*T, N)

#Definition Sinusfunktion übergabe Amplitude [x], Frequenz[Hz], Phasenwinkel [Grad], Schwingungsgrad [1,2,3,4...]
def sin(a,f,angle_deg,k):
    phi=angle_deg*(np.pi/180)
    x=a*np.sin(2*np.pi*f*k*t/1000+phi*k)
    return x

#Defintion Graph für einen Sinus
def graph(x,legend):
    plt.plot(t,x,linewidth=2, label=legend)
    plot()
    return
#Definition Graph 3phasig + Nulleiter
def graph_3(L1,L2,L3,legend1,legend2,legend3):
    O=L1+L2+L3     

    plt.subplot(4,1,1)
    
    plt.plot(t,L1,linewidth=2,color='red', label='L1')  
    plt.subplot(4,1,2)

    plt.plot(t,L2,linewidth=2, color='green',label='L2')   
    plt.subplot(4,1,3)
    
    plt.plot(t,L3,linewidth=2, color='purple',label='L3') 
    plt.subplot(4,1,4)
   
    plt.plot(t,O,linewidth=2,color='blue', label="Neutralleiter")
    plot()
    return
#Definition Diagramm
def plot():
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
    plt.xlim(0, T*N)
    plt.ylabel(r'$\hat x$ [Amplitude]', fontsize='x-large')
    axes1 = plt.gca()
    #axes2 = axes1.twiny()
    #äaxes2.set_xticks([0, np.pi, 2*np.pi, 3*np.pi,4*np.pi, 5*np.pi, 6*np.pi])
    #plt.xticks(np.pi*np.arange(0, 7), ('0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$'),size='x-large', color='b')
    axes1.set_xlabel("t [Zeit in ms]", fontsize='x-large')
    #axes2.set_xlabel(r'$\pi$', fontsize='x-large')
    plt.show()
    return

'''
"Sinus Funkion"
plt.title('Sinus Funkion',fontsize='x-large')
graph(sin(1, 50, 0, 1),"Sinus 50 Hz")
'''
"Sinus 3.Phasig"
plt.title('Sinus 3.Phasig',fontsize='x-large')
L1 = sin(1,50,0,1)
L2 = sin(1,50,120,1)
L3 = sin(1,50,240,1)
graph_3(L1, L2, L3,"L1","L2","L3")
'''
"Sinus 3.Phasig 3 Harmonische"
plt.title('Sinus 3.Phasig 3 Harmonische',fontsize='x-large')
L1 = sin(1,50,0,3)
L2 = sin(1,50,120,3)
L3 = sin(1,50,240,3)
graph_3(L1, L2, L3,"L1","L2","L3")
'''
"Sinus 3.Phasig 3 harmonische Amplitudenanpassung"
plt.title('Sinus 3.Phasig 3 Harmonische',fontsize='x-large')
L1 = sin(0.3,50,0,3)
L2 = sin(0.3,50,120,3)
L3 = sin(0.3,50,240,3)
graph_3(L1, L2, L3,"L1","L2","L3")
'''

x1 = sin(1,50,0,1)
x2 = sin(0.3,50,0,2)
x3 = sin(0.1,50,0,3)
x4 = sin(0.05,50,0,4)
xc = x1+x3+x2+x4

plt.title('Das Stromnetz in der Applikation (einzeln)',fontsize='x-large')
plt.plot(t,x1,color="red",linewidth=2,label="Grundschwingung")
plt.plot(t,x2,color="blue",linewidth=2,label="1. Oberschwingung")
plt.plot(t,x3,color="green",linewidth=2,label="2. Oberschwingung")
plt.plot(t,x4,color="yellow",linewidth=2,label="3. Oberschwingung")
plot()
plt.title('Das Stromnetz in der Applikation (addiert)',fontsize='x-large')
plt.plot(t,xc,color="red",linewidth=2,label="Gesamtschwingung")
plot()






yf = scipy.fftpack.fft(xc)

yf = np.fft.fftshift(yf)

xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)

fig, ax = plt.subplots()

ax.plot(xf, 1.0/N *np.abs(yf) )

plt.xlim(0,4)
plt.title('FFT power spectrum')

plt.grid()

k=1
phi=0
fx1=10*np.sin(2*np.pi*50*k*t/1000+phi*k)
fx2=5*np.sin(2*np.pi*42*k*t/1000+phi*k)
fx3=2*np.sin(2*np.pi*1*k*t/1000+phi*k)
fx4=1*np.sin(2*np.pi*420*k*t/1000+phi*k)
fg =10*np.sin(2*np.pi*50*k*t/1000+phi*k)+5*np.sin(2*np.pi*42*k*t/1000+phi*k)+2*np.sin(2*np.pi*1*k*t/1000+phi*k)+1*np.sin(2*np.pi*420*k*t/1000+phi*k)

graph(fg, 'Testfunktion')

yf = fft(fg)
xf = np.linspace(0.0, 10.0/(2.0*T), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
'''