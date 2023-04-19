# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:51:01 2021

@author: w010586
"""
import numpy as np
import matplotlib.pyplot as plt


T = 20 #Zeit [ms] über den Plot

t=np.linspace(0,T,1000)

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
    N=L1+L2+L3
    plt.plot(t,L1,'o-',markevery=100,linewidth=2, label=legend1)
    plt.plot(t,L2,'s-',markevery=105,linewidth=2, label=legend2)
    plt.plot(t,L3,'x-',markevery=110,linewidth=2, label=legend3)
    plt.plot(t,N,linewidth=2, label="Neutralleiter")
    plot()
    return
#Definition Diagramm
def plot():
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
    plt.xlim(0, T)
    plt.ylabel(r'$\hat x$ [amplitude]', fontsize='x-large')
    axes1 = plt.gca()
    #axes2 = axes1.twiny()
    #äaxes2.set_xticks([0, np.pi, 2*np.pi, 3*np.pi,4*np.pi, 5*np.pi, 6*np.pi])
    #plt.xticks(np.pi*np.arange(0, 7), ('0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$'),size='x-large', color='b')
    axes1.set_xlabel("t [time in ms]", fontsize='x-large')
    #axes2.set_xlabel(r'$\pi$', fontsize='x-large')
    plt.show()
    return

'''
"Sinus Funkion"
plt.title('Sinus Funkion',fontsize='x-large')
graph(sin(1, 50, 0, 1),"Sinus 50 Hz")

"Sinus 3.Phasig"
plt.title('Sinus 3.Phasig',fontsize='x-large')
L1 = sin(1,50,0,1)
L2 = sin(1,50,120,1)
L3 = sin(1,50,240,1)
graph_3(L1, L2, L3,"L1","L2","L3")

"Sinus 3.Phasig 3 Harmonische"
plt.title('Sinus 3.Phasig 3 Harmonische',fontsize='x-large')
L1 = sin(1,50,0,3)
L2 = sin(1,50,120,3)
L3 = sin(1,50,240,3)
graph_3(L1, L2, L3,"L1","L2","L3")

"Sinus 3.Phasig 3 harmonische Amplitudenanpassung"
plt.title('Sinus 3.Phasig 3 Harmonische',fontsize='x-large')
L1 = sin(0.3,50,0,3)
L2 = sin(0.3,50,120,3)
L3 = sin(0.3,50,240,3)
graph_3(L1, L2, L3,"L1","L2","L3")


xg = sin(1,50,0,1)
x2 = sin(0.8,50,0,2)
x3 = sin(0.68,50,0,3)
x4 = sin(0.5,50,0,4)
x5 =sin(0.4,50,0,5)
x6 =sin(0.25,50,0,6)
x7 =sin(0.1,50,0,7)
x8 =sin(0.1,50,0,7)
xc = xg+x3+x2+x4

plt.title('Das Stromnetz in der Applikation (einzeln)',fontsize='x-large')
plt.plot(t,xg,color="red",linewidth=2,label="Grundschwingung")
plt.plot(t,x2,color="blue",linewidth=2,label="1. Oberschwingung")
plt.plot(t,x3,color="green",linewidth=2,label="2. Oberschwingung")
plt.plot(t,x4,color="yellow",linewidth=2,label="3. Oberschwingung")
plot()
#plt.title('Das Stromnetz in der Applikation (addiert)',fontsize='x-large')
#plt.plot(t,xc,color="red",linewidth=2,label="Gesamtschwingung")
#plot()

plt.title('Co-system (+) [3k-2]',fontsize='x-large')
plt.plot(t,xg,linewidth=3,label="1. harmonic")
plt.plot(t,x2,linewidth=0.5,label="2. harmonic")
plt.plot(t,x3,linewidth=0.5,label="3. harmonic")
plt.plot(t,x4,linewidth=3,label="4. harmonic")
plt.plot(t,x5,linewidth=0.5,label="5. harmonic")
plt.plot(t,x6,linewidth=0.5,label="6. harmonic")
plot()
plt.title('Counter system (-) [3k-1]',fontsize='x-large')
plt.plot(t,xg,linewidth=0.5,label="1. harmonic")
plt.plot(t,x2,linewidth=3,label="2. harmonic")
plt.plot(t,x3,linewidth=0.5,label="3. harmonic")
plt.plot(t,x4,linewidth=0.5,label="4. harmonic")
plt.plot(t,x5,linewidth=3,label="5. harmonic")
plt.plot(t,x6,linewidth=0.5,label="6. harmonic")
plot()
plt.title('Neutral system [3k]',fontsize='x-large')
plt.plot(t,xg,linewidth=0.5,label="1. harmonic")
plt.plot(t,x2,linewidth=0.5,label="2. harmonic")
plt.plot(t,x3,linewidth=3,label="3. harmonic")
plt.plot(t,x4,linewidth=0.5,label="4. harmonic")
plt.plot(t,x5,linewidth=0.5,label="5. harmonic")
plt.plot(t,x6,linewidth=3,label="6. harmonic")
plot()


s1=sin(1,50,0,1)
s2=sin(0.3,50,0,2)
s3=sin(0.1,50,0,3)
s4=sin(0.05,50,0,4)
plt.title('Power grid in the application (seperated)',fontsize='x-large')
plt.plot(t,s1,color="red",linewidth=2,label="1. harmonic")
plt.plot(t,s2,color="blue",linewidth=2,label="2. harmonic")
plt.plot(t,s3,color="green",linewidth=2,label="3. harmonic")
plt.plot(t,s4,color="yellow",linewidth=2,label="4. harmonic")
plot()
sg=s1+s2+s3+s4
plt.title('Power grid in apllication (combined)',fontsize='x-large')
plt.plot(t,sg,color="red",linewidth=2,label="combined")
plot()
'''

s1=sin(0.2,25,0,5)
s2=sin(0.2,25,180,5)
plt.plot(t,s1,color="red",linewidth=2,label="")
plt.plot(t,s2,color="blue",linewidth=2,label="")
plt.show()