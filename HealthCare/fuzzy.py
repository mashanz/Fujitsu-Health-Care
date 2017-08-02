"""
PROJECT     : FUJITSU GLOBAL INTERNSHIP
OFFICE      : KAWASAKI OFFICE
DEPARTEMENT : INOVATION IOT BUSINESS UNIT
AUTHOR      : Hanjara Cahya Adhyatma
E-MAIL      : adhyatma.han@gmail.com
YEAR        : 2017
COMMENT     :

This is library for fuzzy fication transorm, this file include 3 
differents fuzzy members function: sigmoid, triangle, trapesium.
Chose one of them.
"""

#######################################################################
##SHAPE FOR FUZZIFICATION CLASS
#######################################################################

#Trapesium Function
def trapesiumL(x,a,b,c):
  if (x<=b):
    return 1
  elif (b<x and x<=c):
    return (c-x)/(c-b)
  else:
    return 0

def trapesiumR(x,a,b,c):
  if (a<=x and x<b):
    return (d-x)/(d-c)
  elif (b<=b):
    return 1
  else:
    return 0
#center of trapessium
def trapesium(x,a,b,c,d):
  if (x>=b and x>=c):
    return 1
  elif (a<=x and x<b):
    return (x-a)/(b-a)
  elif (c<x and x<=d):
    return (d-x)/(d-c)
  else:
    return 0

#Triangle Function
#sharp tough
def triangle(x,a,b,c):
  if (x==b):
    return 1
  elif (a<=x and x<b):
    return (x-a)/(b-a)
  elif (b<x and x<=c):
    return -(x-c)/(c-b)
  else:
    return 0

#Sigmoid Function
#Curve analytic
def sigmoid(x,a,c):
  return 1/(1+exp(-a(x-c)))

#test print
def test():
  loop = 1
  i    = 1
  n    = 5.1
  while(loop):
    if i<=n:
      print("i = ", i)
      print(triangle(i,1,3,5))
      i+=0.1
    else:
      loop = 0

#######################################################################
## TRIPPING FUZZY
#######################################################################









