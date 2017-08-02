from vis0 import *
print()
def read_ipk(ipk):
  if(ipk <= 2.75):
    lo = trapesiumL(ipk,0,2.00,2.75)
  else:
    lo = 0
  if(ipk >= 2.00 and ipk <= 3.25):
    md = triangle(ipk,2.00,2.75,3.25)
  else:
    lo = 0
  if(ipk >= 2.75):
    hi = trapesiumR(ipk,2.75,3.25,4.00)
  else:
    lo = 0
  return [lo,md,hi]
	
def read_gaji(gaji):
  if(gaji <= 3):
    log = trapesiumL(gaji,0,1,3)
  else:
    log = 0
  if(gaji >= 1 and gaji <= 6):
    mdg = trapesium(gaji,1,3,4,6)
  else:
    mdg = 0
  if(gaji >= 4 and gaji <= 12):
    hig = trapesium(gaji,4,6,7,12)
  else:
    hig = 0
  if(gaji >= 7):
    vhg = trapesiumR(gaji,7,12,15)
  else:
    vhg = 0
  return [log, mdg, hig, vhg]

ipk = 3
gaji= 10

print("",x1,y1,x2,y2,x3,y3,"\n\n",x4,y4,x5,y5,x6,y6,x7,y7,"\n\n",x8,y8,x9,y9,"\n\n")

print(read_ipk(ipk))
print(read_gaji(gaji))


