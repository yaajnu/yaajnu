# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:45:56 2017

@author: Yaajnu Subramanian
"""
a=[-1.0, 0.5, -0.5, 1.0]
a.insert(0,0.0) #adding 0.0 to the list at index 0
a.append(-2.0)  #adding 2.0 to the list
print(a)        #Displaying the new list
a.reverse()     #Reversing the list
print(a)        #Reversed list
d=[]
b=0
x=len(a)
while b<x:
    c=a[b]
    if c<1:
        d.append(c)
    b+=1
b=0
x=len(d)
while b< x:
    a.remove(d[b])       # Removing the individual elements that are lesser than 1 
    b+=1
print(a)
print("Hey")
                  


        
    
            
