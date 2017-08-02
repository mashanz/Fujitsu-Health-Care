#=====================================================================
# FUZZY LIBRARY
#=====================================================================
# SHAPE FINDER
def shape_finder(ling,range):
  loop=1
  i=0
  l_ling = len(ling)
  l_range= len(range)
  print(l_ling,l_range)

  while(loop):
    if (i< l_range):
      print(len(range[i]))
      i+=1
    else:
      loop=0

# I/O FUZZY FUNCTION
def in_fuzzy_ipk(ipk,ipk_th):
  ipk_th[0]
#def in_fuzzy_gaji(gaji,gaji_th):
  
#def out_fuzzy_kelayakan(kelayakan,kelayakan_th):
  
#=====================================================================
# FUZZY TEMPORARY FILE
#=====================================================================
# I/O
# I array[ipk,gaji]
# O Kelayakan
a = [3.00, 10]
b = [2.99, 1]

# Fuzzification
# get fuzzy value for input
# linguistic value and degree value
ipk          = ["buruk", "cukup", "bagus"]
ipk_th       = [[0,2.75],[2.00,2.75,3.25],[2.75,3.25,4.00]]
gaji         = ["kecil", "sedang", "besar", "sangat besar"]
gaji_th      = [[0,1,3],[1,3,4,6],[4,6,7,12],[7,12]]
kelayakan    = ["layak", "tidak layak"]
kelayakan_th = [[0,50,80], [50,80,100]]
#print(ipk_th[0][1])	


# Inferensi


# defuzzification

# main routine
if "__main__"==__name__:
  shape_finder(ipk,ipk_th)

