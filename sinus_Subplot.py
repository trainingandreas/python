# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:51:01 2021

@author: w010586
"""
import numpy as np
import matplotlib.pyplot as plt


T = 20 #Zeit [ms] über den Plot
t=np.linspace(0,T,1000)

Subp=True

#Definition Sinusfunktion übergabe Amplitude [x], Frequenz[Hz], Phasenwinkel [Grad], Schwingungsgrad [1,2,3,4...]
def sin(a,f,angle_deg,k):
    phi=angle_deg*(np.pi/180)
    x=a*np.sin(2*np.pi*f*k*t/1000+phi*k)
    return x

#Defintion Graph für einen Sinus
def graph(x,legend):
    plt.plot(t,x,linewidth=2, label=legend)
    grid()
    plt.show()
    return
#Definition Graph 3phasig + Nulleiter
def graph_3(L1,L2,L3,legend1,legend2,legend3):
    
    if Subp == False:
        N=L1+L2+L3
        plt.plot(t,L1,'o-',markevery=100,linewidth=2, label=legend1)
        plt.plot(t,L2,'s-',markevery=105,linewidth=2, label=legend2)
        plt.plot(t,L3,'x-',markevery=110,linewidth=2, label=legend3)
        plt.plot(t,N,linewidth=2, label="Neutralleiter")
        grid()
        plt.show()
    elif Subp == True:
        N=L1+L2+L3
        fig, ax = plt.subplots(4,constrained_layout=True)       
        ax[0].plot(t,L1,linewidth=2,color='red')
        ax[0].grid()
        ax[0].label=legend1
        ax[1].plot(t,L2,linewidth=2, color='green',label='L2')   
        ax[1].grid()
        ax[2].plot(t,L3,linewidth=2, color='purple',label='L3') 
        ax[2].grid()
        ax[3].plot(t,N,linewidth=2,color='blue', label="Neutralleiter")
        ax[3].grid()
        plt.show()
    else:
        print ("Error")
    return
#Definition Diagramm
def grid():
    if Subp == False:
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
        plt.xlim(0, T)
        plt.ylabel(r'$\hat x$ [Amplitude]', fontsize='x-large')
        axes1 = plt.gca()
        #axes2 = axes1.twiny()
        #äaxes2.set_xticks([0, np.pi, 2*np.pi, 3*np.pi,4*np.pi, 5*np.pi, 6*np.pi])
        #plt.xticks(np.pi*np.arange(0, 7), ('0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$'),size='x-large', color='b')
        axes1.set_xlabel("t [Zeit in ms]", fontsize='x-large')
        #axes2.set_xlabel(r'$\pi$', fontsize='x-large')
    elif Subp == True:
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
        plt.xlim(0, T)
    else:
        print ("Error")
    return


"Sinus Funkion"
#plt.title( 'Induktive Load',fontsize='x-large')
u=sin(230, 50, 0, 1)

i=sin(1/4*230, 50, 90, 1)
#plt.plot(t,u,linewidth=2, label="Spannung")
#plt.plot(t,i,linewidth=2,color="orange", label="Current")
#grid()
#plt.show()
'''
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
'''
