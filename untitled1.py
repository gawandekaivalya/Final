# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:48:22 2016

@author: Kaivalya
"""

#==============================================================================================================================#

import matplotlib.pyplot
import numpy

#==============================================================================================================================#

'''Creating a random array of desired dimensions containing only 0,1,2,3 as its elements'''
M=numpy.random.randint(0,10,(1000,1000))

'''A 30x30 matrix as an example'''
M1= [[3,0,1,0,1,2,3,0,2,1,2,3,0,1,2,3,2,3,1,0,2,3,1,3,0,3,2,1,2,3],
     [1,2,2,2,3,1,2,3,3,2,2,3,1,2,3,2,1,2,0,2,3,0,2,2,3,1,2,0,2,1],
     [2,2,0,3,1,2,1,0,3,1,1,2,3,1,0,2,3,1,2,1,2,0,2,3,1,0,1,2,2,0],
     [3,3,2,3,2,1,3,2,3,0,1,2,3,2,3,0,0,1,2,3,2,1,2,3,0,3,2,3,0,1],
     [0,3,3,1,1,3,2,3,2,0,1,2,3,0,1,2,3,1,0,3,1,2,3,1,0,3,2,1,0,1],
     [2,1,1,3,2,2,3,3,1,1,1,2,3,2,1,2,0,3,2,1,0,3,2,1,0,3,2,3,2,2],
     [2,3,2,0,3,1,0,1,2,0,1,2,1,2,3,1,2,3,1,1,2,0,0,3,1,2,3,1,2,3],
     [3,2,3,2,1,0,3,2,3,2,3,2,2,1,2,0,3,2,1,0,3,1,2,0,3,2,1,0,1,2],
     [0,3,2,3,2,0,2,3,0,0,1,1,3,0,3,2,0,3,2,2,3,1,1,2,3,1,2,1,2,0],
     [1,2,0,1,0,1,2,2,0,3,2,2,3,1,2,3,2,2,2,3,2,0,2,2,2,2,3,2,2,1],
     [0,3,2,2,1,0,2,3,2,2,1,3,2,2,1,2,1,1,1,1,1,2,1,1,2,1,0,3,1,2],
     [1,1,1,3,2,3,2,2,3,3,0,1,1,0,3,1,2,2,0,3,0,1,2,3,3,0,1,1,0,0],
     [2,0,2,2,3,2,2,1,1,0,2,3,1,2,0,3,3,0,3,2,2,2,3,0,3,0,2,3,2,3],
     [3,2,0,1,0,1,2,2,2,1,2,1,2,3,2,1,0,3,0,3,3,0,3,1,2,1,0,0,3,2],
     [2,2,3,2,1,1,2,0,1,2,1,3,2,1,3,2,3,2,0,3,2,3,0,0,1,1,2,1,1,1],
     [1,2,2,0,2,0,2,1,1,3,0,2,1,2,2,0,3,1,0,2,1,1,3,1,1,1,3,2,3,2],
     [3,1,2,1,1,2,3,2,2,2,3,1,3,3,1,3,1,2,1,1,2,2,2,0,2,2,2,2,1,1],
     [2,0,1,2,2,3,2,3,2,1,1,1,1,1,2,2,2,2,1,0,2,3,2,0,3,3,1,1,2,2],
     [1,3,2,0,1,2,1,2,1,3,2,2,0,2,0,1,1,1,2,1,0,1,0,2,0,0,0,0,0,3],
     [0,3,1,1,0,1,0,2,0,2,2,1,3,3,1,2,2,2,3,2,3,2,2,0,2,2,2,2,1,2],
     [1,2,2,2,2,3,2,1,1,0,3,2,1,1,2,3,2,0,0,1,3,2,3,3,1,1,3,1,2,0], 
     [2,1,2,3,3,2,1,3,2,2,2,1,2,2,3,2,3,2,2,3,2,1,0,2,2,2,1,3,0,2], 
     [3,2,1,1,1,1,3,0,3,1,1,1,3,0,1,1,1,3,1,2,0,0,2,2,0,0,3,2,3,3],
     [2,1,3,0,2,0,1,1,0,2,0,2,0,1,1,0,0,3,2,0,3,2,3,2,2,3,0,1,2,1],
     [1,2,0,1,1,2,2,0,1,2,2,3,2,2,2,2,0,1,0,2,2,1,2,0,3,2,2,3,3,3],
     [2,0,1,2,3,3,0,2,2,2,1,2,1,3,0,3,3,3,1,1,1,2,2,2,1,1,1,1,1,1],
     [0,1,0,2,0,1,3,3,3,2,2,0,3,3,2,2,2,2,2,0,0,3,0,1,3,3,2,2,0,2],
     [2,2,1,0,2,2,2,1,1,1,3,2,2,3,3,1,1,3,1,2,2,1,2,2,1,3,3,0,3,2],
     [3,2,3,3,1,3,1,1,2,1,2,1,1,2,2,2,2,2,3,3,2,2,0,0,2,2,0,1,2,3],
     [2,1,1,3,2,0,3,0,3,2,3,2,2,2,2,1,3,1,3,1,3,2,3,2,3,3,1,0,1,2]]


#============================================================================================================#     
'''Making an array of neighbours of an element having coordinates (x,y)'''

'''Counting numbers of neighbours of a particular type'''
k1=1
def counting(M):
    
   Rows,Columns = len(M), len(M[0])
   n0 = [[0,]*(Columns)  for i in range(Rows)]
   n1 = [[0,]*(Columns)  for i in range(Rows)]
   n2 = [[0,]*(Columns)  for i in range(Rows)]
   n3 = [[0,]*(Columns)  for i in range(Rows)]
   n4 = [[0,]*(Columns)  for i in range(Rows)]
   n5 = [[0,]*(Columns)  for i in range(Rows)]
   n6 = [[0,]*(Columns)  for i in range(Rows)]
   n7 = [[0,]*(Columns)  for i in range(Rows)]
   n8 = [[0,]*(Columns)  for i in range(Rows)]
   n9 = [[0,]*(Columns)  for i in range(Rows)]
   n10 = [[0,]*(Columns)  for i in range(Rows)]
   for x in range(1,Columns-1):
       for y in range(1,Rows-1):
           Neigh=[M[x-1][y-1],M[x][y-1],M[x+1][y-1],M[x-1][y],M[x+1][y],M[x-1][y+1],M[x][y+1],M[x+1][y+1]]
           n0[x][y]=Neigh.count(0)
           n1[x][y]=Neigh.count(1)
           n2[x][y]=Neigh.count(2)
           n3[x][y]=Neigh.count(3)
           n4[x][y]=Neigh.count(4)
           n5[x][y]=Neigh.count(5)
           n6[x][y]=Neigh.count(6)
           n7[x][y]=Neigh.count(7)
           n8[x][y]=Neigh.count(8)
           n9[x][y]=Neigh.count(9)
           n10[x][y]=Neigh.count(10)
           n=[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]     
        
   return n
   
#=========================================================================================================#'''    

'''Bringing in the rules of 'GOL' into the action'''
def conditions(M):
    Rows,Columns = len(M), len(M[0])
    n = counting(M)
    n0=n[0]
    n1=n[1]
    n2=n[2]
    n3=n[3]
    n4=n[4]
    n5=n[5]
    n6=n[6]
    n7=n[7]
    n8=n[8]
    n9=n[9]
    n10=n[10]
    Add=1*n1+2*n2+3*n3+4*n4+5*n5+6*n6+7*n7+8*n8+9*n9+10*n10
    for x in range(0,Rows):
        for y in range(0,Columns):
            if Add[x][y]<40 and M[x][y]>0 :
                M[x][y]=M[x][y]-1
            elif Add[x][y]>60 and Add[x][y]<80 :
                M[x][y]=M[x][y]+1
            elif Add[x][y]==80 :
                M[x][y]=M[x][y]
    return M

#==============================================================================================================#
'''Creating blank window'''

fig = matplotlib.pyplot.figure()
graph=fig.add_subplot()
fig.show()

#===============================================================================================================#

'''Iniating a never ending loop'''

NoEnd=1
while NoEnd>0:
    conditions(M)
    graph.clear()
    graph.imshow(M,interpolation='none', cmap=matplotlib.pyplot.cm.pink_r)
    matplotlib.pyplot.pause(0.2)

#=============================================================================================================#
