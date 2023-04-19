# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:19:46 2021

@author: w010586
"""

# Make plots appear inline, set custom plotting style
#%matplotlib inline
import matplotlib.pyplot as plt
#plt.style.use('style/elegant.mplstyle')
import numpy as np


f = 50  # Frequency, in cycles per second, or Hertz
f_s = 100  # Sampling rate, or number of measurements per second


def sin(a,f,angle_deg,k):
    phi=angle_deg*(np.pi/180)
    x=a*np.sin(2*np.pi*f*k*t/1000+phi*k)
    return x

def graph(x,legend):
    plt.plot(t,x,linewidth=2, label=legend)
    plot()
    return

#Definition Diagramm
def plot():
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
    plt.xlim(0, t)
    plt.ylabel(r'$\hat x$ [Amplitude]', fontsize='x-large')
    axes1 = plt.gca()
    #axes2 = axes1.twiny()
    #äaxes2.set_xticks([0, np.pi, 2*np.pi, 3*np.pi,4*np.pi, 5*np.pi, 6*np.pi])
    #plt.xticks(np.pi*np.arange(0, 7), ('0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$'),size='x-large', color='b')
    axes1.set_xlabel("t [Zeit in ms]", fontsize='x-large')
    #axes2.set_xlabel(r'$\pi$', fontsize='x-large')
    plt.show()
    return

t = np.linspace(0, 200, 2 * f_s, endpoint=False)
x = np.sin(f*2*np.pi*t)




x1 = sin(1,50,0,1)
x2 = sin(0.3,50,0,2)
x3 = sin(0.1,50,0,3)
x4 = sin(0.05,50,0,4)

xc = x1+x3+x2+x4

'''
plt.title('Das Stromnetz in der Applikation (einzeln)',fontsize='x-large')
plt.plot(t,x1,color="red",linewidth=2,label="Grundschwingung")
plt.plot(t,x2,color="blue",linewidth=2,label="1. Oberschwingung")
plt.plot(t,x3,color="green",linewidth=2,label="2. Oberschwingung")
plt.plot(t,x4,color="yellow",linewidth=2,label="3. Oberschwingung")
plot()
plt.title('Das Stromnetz in der Applikation (addiert)',fontsize='x-large')
plt.plot(t,xc,color="red",linewidth=2,label="Gesamtschwingung")
plot()

'''


fig, ax = plt.subplots()
#ax.plot(t, xc)
#ax.set_xlabel('t [Zeit in ms]')
#ax.set_ylabel(r'$\hat x$ [Amplitude]')
#ax.grid(b=True, color='black', linestyle='-',alpha=0.1)
#ax.xlim(0, t)
# Make plots appear inline, set custom plotting style


from scipy import fftpack

X = fftpack.fft(xc)
freqs = fftpack.fftfreq(len(x3)) *1000

fig, ax = plt.subplots()

ax.stem(freqs, np.abs(X))
ax.grid(b=True, color='black', linestyle='-',alpha=0.1)
ax.set_xlabel('Hz [frequency in Hertz]')
ax.set_ylabel( 'X [Spectrum in %]')
ax.set_xlim(0, 300)
ax.set_ylim(-5, 105)