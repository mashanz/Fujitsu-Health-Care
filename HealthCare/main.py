"""
PROJECT     : FUJITSU GLOBAL INTERNSHIP
OFFICE      : KAWASAKI OFFICE
DEPARTEMENT : INOVATION IOT BUSINESS UNIT
AUTHOR      : Hanjara Cahya Adhyatma
E-MAIL      : adhyatma.han@gmail.com
YEAR        : 2017
COMMENT     :

"""
#=====================================================================
# IMPORT FILE
#=====================================================================
import os
from const import *
#=====================================================================
# ADDITIONAL FUNCTION
#=====================================================================
def welcome():
 print()
 print("Menu:")
 print("1. collecting sensor data from excel file")
 print("2. view summary data")
 print("3. run simulation with collected data")
 print("4. exit")
 x=input("Select: ")
 print()
 if (int(x)==1):
  load=1
  import expertknowladge.read_xl
  print(load)
  kb=input("press any key to continue...")
 #if (int(x)==2 and load==1):
 if (int(x)==2):
  print()
  print("Name \t",name)
  print("Gender \t",gender)
  print(age, "\t years old")
  print(weigh, "\t kg")
  print(heigh, "\t cm")
  print(round(pulse/avcnt, 2), "\t bpm")
  print(stair,"\t times detected using stairs")
  print(elevator,"\t times detected using elevator")
  print(walking, "\t times detected walking")
  print(stp,"\t total steps")
  print(stay, "\t times detected stay")
  print(round(clr, 2),"\t kcal burned total?")
  kb=input("press any key to continue...")
 if (int(x)==4):
  loop=0
 global loop,load
#=====================================================================
# MAIN ROUTINE
#=====================================================================
if "__main__"==__name__:
 load=0
 loop=1
 while(loop):
  os.system("cls")
  welcome()
 kb=input("press any key to exit...")


  
  

