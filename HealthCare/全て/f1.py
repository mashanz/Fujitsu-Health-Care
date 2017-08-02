from fuzzy import *

#=====================================================================
# COMPARATOR EACH INPUT TO DECIDE OUTPUT COORDINATE
#=====================================================================
def f1_knowladge_check(coordinat,fuzzy_value_a,fuzzy_value_b,output):
 # compare if thare a value more than 0 << bugs may accure
 if (fuzzy_value_a[coordinat[0]]>0 and fuzzy_value_b[coordinat[1]]>0):
  # get lowest value cause use AND comparator
  if (fuzzy_value_a[coordinat[0]] <= fuzzy_value_b[coordinat[1]]): 
   out = fuzzy_value_a[coordinat[0]]
  else: 
   out = fuzzy_value_b[coordinat[1]]
  #print result
  #print(coordinat[0],coordinat[1],knowladge_34[coordinat[0]][coordinat[1]],output)
  output.extend([[knowladge_F1[coordinat[0]][coordinat[1]],out]])
  #print(output)

#=====================================================================
# RELATION OUTPUT ROUGH
#=====================================================================
def f1_out_ab(a,b,z):
 x = 0
 y = 0
 while(x<len(a)):
  while(y<len(b)):
   #z.extend([[x,y]]) # fuzzy function relation check
   f1_knowladge_check([x,y],a,b,z)
   y+=1
  if(y>=len(b)):
   y=0
  x+=1
#=====================================================================
# Find CENTROID OF M SHAPE
#=====================================================================
# I think i'll make it callable on fuzzy.py
# every shape centroid finder  
def f1_centroid(resolution,f_out,output):
 #print(f_out,output)
 i=resolution
 s1=0
 s2=0
 c1=0
 c2=0
 while(i<=f_out[3]):
  if(i<=f_out[1]):
   s1+=i
   c1+=1
  elif(i>f_out[1] and i<f_out[2]	):
   if(trapesiumL(i,f_out[0],f_out[1],f_out[2])>=trapesiumR(i,f_out[1],f_out[2],f_out[3])):
    s1+=i
    c1+=1
   else:
    s2+=i
    c2+=1
  elif(i>=f_out[2]):
   s2+=i
   c2+=1
  #print(i,s1,c1,s2,c2)
  i+=resolution
 if (len(output)==1):
  output.extend([["",0]])
 #print( ((s1*output[0][1])+(s2*output[1][1]))/((c1*output[0][1])+(c2*output[1][1])) )
 return ((s1*output[0][1])+(s2*output[1][1]))/((c1*output[0][1])+(c2*output[1][1]))

#=====================================================================
# f1 working as OVERWEIGH DETECTION
#=====================================================================
def f1_function(resolution,a,b,in_a,in_b,out,f1):
#=====================================================================
# INPUT AGE FUZZY
#=====================================================================
 i=0
 x1=[]
 y1=[]
 x2=[]
 y2=[]
 x3=[]
 y3=[]
 while(1):
  x1.extend([in_a[i]])
  x2.extend([in_a[i+1]])
  x3.extend([in_a[i+2]])
  y1.extend([trapesiumL(x1[i],in_a[0],in_a[1],in_a[2])])
  y2.extend([triangle(x2[i],in_a[1],in_a[2],in_a[3])])
  y3.extend([trapesiumR(x3[i],in_a[2],in_a[3],in_a[4])])
  i+=1
  if(i==3):	
   i=0
   break
 #print(x1, y1, x2, y2, x3, y3)
 plt.figure("f1_a")
 plt.plot(x1, y1, x2, y2, x3, y3)
 plt.axvline(a, color='black')
 plt.axis([in_a[0],in_a[4], 0, 1.1])
 plt.ylabel('AGE')
 
#=====================================================================
# INPUT PULSE_RATE FUZZY
#=====================================================================
 x4=[]
 y4=[]
 x5=[]
 y5=[]
 x6=[]
 y6=[]
 while(1):
  x4.extend([in_b[i]])
  x5.extend([in_b[i+1]])
  x6.extend([in_b[i+2]])
  y4.extend([trapesiumL(x4[i],in_b[0],in_b[1],in_b[2])])
  y5.extend([triangle(x5[i],in_b[1],in_b[2],in_b[3])])
  y6.extend([trapesiumR(x6[i],in_b[2],in_b[3],in_b[4])])
  i+=1
  if(i==3):	
   i=0
   break
 #print(x1, y1, x2, y2, x3, y3)
 plt.figure("f1_b")
 plt.plot(x4, y4, x5, y5, x6, y6)
 plt.axvline(b, color='black')
 plt.axis([in_b[0],in_b[4], 0, 1.1])
 plt.ylabel('PULSE_RATE')

#=====================================================================
# PROCESSING INPUT DATA
#=====================================================================
 z0=[]
 z1=[]
 print("AGE      :",type_0(a,in_a)) # read and calculate fuzzy value
 print("PULSE    :",type_0(b,in_b)) # read and calculate fuzzy value
 f1_out_ab(type_0(a,in_a),type_0(b,in_b),z0)
 #print("ALL      :",z0)
 print("MOST     :",counterMAX(z0,z1))
 #print("CENTROID :",f1_centroid(resolution,out,z1))
 f1_out = f1_centroid(resolution,out,z1)
 f1=result(counterMAX(z0,z1),f1_centroid(resolution,out,z1))
 print("\n",f1)
#=====================================================================
# OUTPUT DETECTION FUZZY
#=====================================================================
 x10=[]
 y10=[]
 x11=[]
 y11=[]
 x12=[]
 y12=[]
 while(1):
  x10.extend([out[i]])
  x11.extend([out[i+1]])
  x12.extend([out[i+2]])
  y10.extend([trapesiumL(x10[i],out[0],out[1],out[2])])
  y11.extend([triangle(x11[i],out[1],out[2],out[3])])
  y12.extend([trapesiumR(x12[i],out[2],out[3],out[4])])
  i+=1
  if(i==3):	
   i=0
   break
 #print(x1, y1, x2, y2, x3, y3)
 plt.figure("f1_out")
 plt.plot(x10, y10, x11, y11, x12, y12)
 plt.axvline(f1_centroid(resolution,out,z1), color='black')
 plt.axis([out[0],out[4], 0, 1.1])
 plt.ylabel('PULSE')
 
 #show diagram
 #plt.show()

