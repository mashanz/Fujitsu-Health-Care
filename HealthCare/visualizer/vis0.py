import matplotlib.pyplot as plt
i=0
# ######################################################################
# SHAPE FOR FUZZIFICATION CLASS
# ######################################################################
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
# ######################################################################
# IPK FUZZIFICATION
# ######################################################################
ipk_th = [[0,2.00,2.75],[2.00,2.75,3.25],[2.75,3.25,4.00]]
x1=list(range(len(ipk_th[0])))
y1=list(range(len(ipk_th[0])))
while(1):
  x1[i]=ipk_th[0][i]
  y1[i]=trapesiumL(x1[i],0,2.00,2.75)
  i+=1
  if(i==len(ipk_th[0])):
    break
#print(x1,y1)
i=0
x2=list(range(len(ipk_th[1])))
y2=list(range(len(ipk_th[1])))
while(1):
  x2[i]=ipk_th[1][i]
  y2[i]=triangle(x2[i],2.00,2.75,3.25)
  i+=1
  if(i==len(ipk_th[1])):
    break
#print(x2,y2)
i=0
x3=list(range(len(ipk_th[2])))
y3=list(range(len(ipk_th[2])))
while(1):
  x3[i]=ipk_th[2][i]
  y3[i]=trapesiumR(x3[i],2.75,3.25,4.00)
  i+=1
  if(i==len(ipk_th[2])):
    break
#print(x3,y3)
plt.figure(1)
plt.plot(x1, y1, x2, y2, x3, y3)
plt.axis([0, 4, 0, 1.1])
plt.ylabel('Heigh')
# ######################################################################
# GAJI FIZZIFICATION
# ######################################################################
print()
gaji_th = [[0,1,3],[1,3,4,6],[4,6,7,12],[7,12,15]]
i=0
x4=list(range(len(gaji_th[0])))
y4=list(range(len(gaji_th[0])))
while(1):
  x4[i]=gaji_th[0][i]
  y4[i]=trapesiumL(x4[i],0,1,3)
  i+=1
  if(i==len(gaji_th[0])):
    break
#print(x1,y1)
i=0
x5=list(range(len(gaji_th[1])))
y5=list(range(len(gaji_th[1])))
while(1):
  x5[i]=gaji_th[1][i]
  y5[i]=trapesium(x5[i],1,3,4,6)
  i+=1
  if(i==len(gaji_th[1])):
    break
#print(x2,y2)
i=0
x6=list(range(len(gaji_th[2])))
y6=list(range(len(gaji_th[2])))
while(1):
  x6[i]=gaji_th[2][i]
  y6[i]=trapesium(x6[i],4,6,7,12)
  i+=1
  if(i==len(gaji_th[2])):
    break
#print(x3,y3)
i=0
x7=list(range(len(gaji_th[3])))
y7=list(range(len(gaji_th[3])))
while(1):
  x7[i]=gaji_th[3][i]
  y7[i]=trapesiumR(x7[i],7,12,15)
  i+=1
  if(i==len(gaji_th[3])):
    break
#print(x7,y7)
plt.figure(2)
plt.plot(x4, y4, x5, y5, x6, y6, x7, y7)
plt.axis([0, 15, 0, 1.1])
plt.ylabel('AGE')
# ######################################################################
# BEA FIZZIFICATION
# ######################################################################
print()
kelayakan_th = [[0,50,80], [50,80,100]]
i=0
x8=list(range(len(kelayakan_th[0])))
y8=list(range(len(kelayakan_th[0])))
while(1):
  x8[i]=kelayakan_th[0][i]
  y8[i]=trapesiumL(x8[i],0,50,80)
  i+=1
  if(i==len(kelayakan_th[0])):
    break
#print(x5,y5)
i=0
x9=list(range(len(kelayakan_th[1])))
y9=list(range(len(kelayakan_th[1])))
while(1):
  x9[i]=kelayakan_th[1][i]
  y9[i]=trapesiumR(x9[i],50,80,100)
  i+=1
  if(i==len(kelayakan_th[1])):
    break
#print(x6,y6)
plt.figure(3)
plt.plot(x8, y8, x9, y9)
plt.axis([0, 100, 0, 1.1])
plt.ylabel('WEIGH')
plt.show()
