from distutils.sysconfig import customize_compiler
from math import sqrt 
import numpy as np
import matplotlib.pyplot as plt


def brute_force(customers,fuel_stations):

    #grid
    

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

        

    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 101, 20)
    minor_ticks = np.arange(0, 101, 5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)



    # Or if you want different settings for the grids:
    ax.grid(which='minor',color='black', alpha=0.2)
    ax.grid(which='major',color='black', alpha=0.5)

    cust=customers
    stat=fuel_stations

    
    #o-customer,x-station
    rng = np.random.RandomState(0)
    flag=True
    for i in cust:
        marker='o'
        if flag==True:
            plt.plot(i[0],i[1], marker,label="customer-'{0}'".format(marker),color='blue')
            flag=False
        else:
            plt.plot(i[0],i[1], marker,color='blue')   
        plt.legend(numpoints=1)
    flag=True
    for i in stat:
        marker='x'
        if flag==True:
            plt.plot(i[0],i[1], marker,label="station-'{0}'".format(marker),color='red')
            flag=False
        else:
            plt.plot(i[0],i[1], marker,color='red')   
        plt.legend(numpoints=1)

#brute force algorithm


    for customer in customers:
        d=[]
        for station in fuel_stations:
            dist= sqrt((customer[0]-station[0])**2 + (customer[1]-station[1])**2)
            d.append(dist)
        m=min(d)
        m_index=d.index(m)
        print("k",customer,fuel_stations[m_index])
        point1 = customer
        point2 = fuel_stations[m_index]
        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values, linestyle="--")
        plt.text(point1[0]-0.015, point1[1]+0.25,"c")
        plt.text(point2[0]-0.050, point2[1]-0.25, fuel_stations[m_index][2])

    fig.savefig('.\static\pbruteplot.png')
