from fuzzy import *
# ######################################################################
# BEASISWA
# ######################################################################
def fx_a(read,th):
 if(read <= th[1]): lo = trapesiumL(read,th[0],th[1],th[2])
 else: lo = 0
 if(read >= th[1] and read <= th[3]): md = triangle(read,th[1],th[2],th[3])
 else: md = 0
 if(read >= th[2]): hi = trapesiumR(read,th[2],th[3],th[4])
 else: hi = 0
 return [lo,md,hi]

def fx_b(read,th):
 if(read <= 3): log = trapesiumL(read,th[0],th[1],th[2])
 else: log = 0
 if(read >= 1 and read <= 6): mdg = trapesium(read,th[1],th[2],th[3],th[4])
 else: mdg = 0
 if(read >= 4 and read <= 12): hig = trapesium(read,th[3],th[4],th[5],th[6])
 else: hig = 0
 if(read >= 7): vhg = trapesiumR(read,th[5],th[6],th[7])
 else: vhg = 0
 return [log, mdg, hig, vhg]

def fx_knowladge_most(most,output):
 i=0
 th=most[0][0]
 td=most[0][1]
 #find most 1st
 #print("starting VALUE: ",th,td)
 while(i<len(most)):
  if(th==most[i][0]):
   if (td<most[i][1]):
    td=most[i][1]
    #print("update VALUE: ",th,td)
  i+=1
 i=0
 output.extend([[th,td]])
 #find diferent
 while(i<len(most)):
  if(th!=most[i][0]):
   th=most[i][0]
   td=most[i][1]
   break
  i+=1
 i=0
 #find most for this
 while(i<len(most)):
  if(th==most[i][0]):
   if (td<most[i][1]):
    td=most[i][1]
    #print("update VALUE: ",th,td)
  i+=1
 i=0
 output.extend([[th,td]])
 print(output)
 
def fx_knowladge_check(coordinat,fuzzy_value_a,fuzzy_value_b,output):
 # compare if thare a value more than 0 << bugs may accure
 if (fuzzy_value_a[coordinat[0]]>0 and fuzzy_value_b[coordinat[1]]>0):
  # get lowest value cause use AND comparator
  if (fuzzy_value_a[coordinat[0]] <= fuzzy_value_b[coordinat[1]]): 
   out = fuzzy_value_a[coordinat[0]]
  else: 
   out = fuzzy_value_b[coordinat[1]]
  #print result
  #print(coordinat[0],coordinat[1],knowladge_34[coordinat[0]][coordinat[1]],output)
  output.extend([[knowladge_34[coordinat[0]][coordinat[1]],out]])
  #print(output)

def fx_out_ab(a,b,z):
 x = 0
 y = 0
 while(x<len(a)):
  while(y<len(b)):
   #z.extend([[x,y]]) # fuzzy function relation check
   fx_knowladge_check([x,y],a,b,z)
   y+=1
  if(y>=len(b)):
   y=0
  x+=1
#f_out is output
def fx_centroid(resolution,f_out,output):
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
 #print( ((s1*output[0][1])+(s2*output[1][1]))/((c1*output[0][1])+(c2*output[1][1])) )
 return ((s1*output[0][1])+(s2*output[1][1]))/((c1*output[0][1])+(c2*output[1][1]))

def fx_function(resolution,a,b,in_a,in_b,out):
 print("\n Coordinats")
 # input IPK
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
 plt.figure("fx_a")
 plt.plot(x1, y1, x2, y2, x3, y3)
 plt.axvline(a, color='black')
 plt.axis([in_a[0],in_a[4], 0, 1.1])
 plt.ylabel('IPK')
 
 # input GAJI
 x4=[]
 y4=[]
 x5=[]
 y5=[]
 x6=[]
 y6=[]
 x7=[]
 y7=[]
 while(1):
  x4.extend([in_b[i]])
  x5.extend([in_b[i+1]])
  x6.extend([in_b[i+3]])
  y4.extend([trapesiumL(x4[i],in_b[0],in_b[1],in_b[2])])
  y5.extend([trapesium(x5[i],in_b[1],in_b[2],in_b[3],in_b[4])])
  y6.extend([trapesium(x6[i],in_b[3],in_b[4],in_b[5],in_b[6])])
  if(i<3):
   x7.extend([in_b[i+5]])
   y7.extend([trapesiumR(x7[i],in_b[5],in_b[6],in_b[7])])
  i+=1
  if(i==4):
   i=0
   break
 #print(x4, y4, x5, y5, x6, y6, x7, y7)
 plt.figure("fx_b")
 plt.plot(x4, y4, x5, y5, x6, y6, x7, y7)
 plt.axvline(b, color='black')
 plt.axis([in_b[0],in_b[7], 0, 1.1])
 plt.ylabel('GAJI')
 
 # processing fuzzy
 z0=[]
 z1=[]
 print("FUZZY VALUE FROM INPUT 1")
 print(fx_a(a,in_a)) # read and calculate fuzzy value
 print("\n FUZZY VALUE FROM INPUT 2")
 print(fx_b(b,in_b)) # read and calculate fuzzy value
 print("\n ALL FUZZY OUTPUT")
 print(fx_out_ab(fx_a(a,in_a),fx_b(b,in_b),z0))
 print(z0)
 print("\n GET THE MOST VALUE")
 fx_knowladge_most(z0,z1)
 print("\n centroid")
 print(fx_centroid(resolution,out,z1))
 
 # output BEASISWA
 x8=[]
 y8=[]
 x9=[]
 y9=[]
 while(1):
  x8.extend([out[i]])
  x9.extend([out[i+1]])
  y8.extend([trapesiumL(x8[i],out[0],out[1],out[2])])
  y9.extend([trapesiumR(x9[i],out[1],out[2],out[3])])
  i+=1
  if(i==3):	
   i=0
   break
 #print(x8, y8, x9, y9)
 plt.figure("fx_out")
 plt.plot(x8, y8, x9, y9)
 plt.axvline(fx_centroid(resolution,out,z1), color='black')
 plt.axis([out[0],out[3], 0, 1.1])
 plt.ylabel('BEASISWA')
 
 #show diagram
 #plt.show()
 