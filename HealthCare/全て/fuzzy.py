import matplotlib.pyplot as plt
from knowledge import *

#=====================================================================
# SHAPE FOR FUZZIFICATION CLASS
#=====================================================================
def trapesiumL(x,a,b,c):
 if (x<=b):
  return 1
 elif (b<x and x<=c):
  return (c-x)/(c-b)
 else:
  return 0
def trapesiumR(x,a,b,c):
 if (a<=x and x<b):
  return (x-a)/(b-a)
 elif (b<=b):
  return 1
 else:
    return 0
def trapesium(x,a,b,c,d):
 if (a<=x and x<b):
  return (x-a)/(b-a)
 elif (c<x and x<=d):
  return (d-x)/(d-c)
 elif (b<=x and x<=c):
  return 1
 else:
  return 0
def triangle(x,a,b,c):
 if (x==b):
  return 1
 elif (a<=x and x<b):
  return (x-a)/(b-a)
 elif (b<x and x<=c):
  return (c-x)/(c-b)
 else:
  return 0

#=====================================================================
# Finding HIGHER DEGREE [OR]
#=====================================================================
def maxd(ar,ft):
 i=0
 a=ar[0][0]
 b=ar[0][1]
 max=len(ar)
 while(i<max):
  if(a==ar[i][0] and b<ar[i][1]):
   a=ar[i][0]
   b=ar[i][1]
  i+=1
 ft.extend([[a,b]])
 i=0

def delete(ar):
 i=0
 c=0
 a=ar[0][0]
 b=ar[0][1]
 max=len(ar)
 while(i<max):
  if(a==ar[c][0]):
   ar.pop(c)
  elif(a!=ar[c][0]):
   c+=1
  i+=1

def counterMAX(ar,ft):
 while(len(ar)>1):
  maxd(ar,ft) # input  b
  delete(ar) # delete a
 ft.extend(ar)
 return(ft)

#=====================================================================
# Fuzzy shape type 0
#=====================================================================
# this shape fokus maximal with 0,1,2,3,4 que input
# shape is |-\ /\ /-|
# M shaped fuzzy 1 in 3 out
def type_0(read,th):
 if(read <= th[2]): lo = trapesiumL(read,th[0],th[1],th[2])
 else: lo = 0
 if(read >= th[1] and read <= th[3]): md = triangle(read,th[1],th[2],th[3])
 else: md = 0
 if(read >= th[2]): hi = trapesiumR(read,th[2],th[3],th[4])
 else: hi = 0
 return [lo,md,hi]

def result(fo,cntr):
 i=0
 temp=fo[0][1]
 out=["blank",0]
 while(i<len(fo)):
  if(temp<=fo[i][1]):
   out=[fo[i][0],cntr]
  i+=1
 return out
