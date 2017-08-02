ar=[["a",0],["b",0],["a",1],["b",1],["c",0],["a",1],["b",1],["a",0],["b",1],["d",0]]
ax=[["a",0],["b",0],["a",1],["b",1],["c",0],["e",1],["b",1],["a",0],["b",1],["d",0],["a",0],["e",0],["a",1],["d",1],["c",0],["a",4],["b",1],["f",0],["b",1],["d",4]]
ax1=[["a",0],["e",0],["c",1],["b",1],["e",0],["a",1],["b",1],["a",0]]
ft=[]

def counterMAX(ar,ft):
 while(len(ar)!=1):
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
  c=0
  a=ar[0][0]
  b=ar[0][1]
  while(i<max):
   if(a==ar[c][0]):
    ar.pop(c)
   elif(a!=ar[c][0]):
    c+=1
   i+=1

print(ar)
counterMAX(ax1,ft)
print("now    ",ar)
print("filter ",ft)