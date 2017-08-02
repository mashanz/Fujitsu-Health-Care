import os
import openpyxl
from cfg import *
from param import *
from knowledge import *
from reader import *
#from fuzzy import *
from fx import *
from f0 import *
from f1 import *
from f2 import *
from f3 import *
from f4 import *
from f5 import *

if "__main__"==__name__:
 os.system("cls")
 print("[INPUT]: ALL MANUAL AND COLLECTED DATA ==========================")
 print("Name     :",name)
 print("GENDER   :",gender)
 print("AGE      :",age, " years old")
 print("WEIGH    :",weigh," kg")
 print("WEIGH    :",heigh, " cm")
 print("PULSE    :",pulse, " bpm")
 print("STAIRS   :",stairs," times detected using stairs")
 print("ELEVATORS:",elevators," times detected using elevator")
 print("WALK     :",time_wlk, " times detected walking")
 print("STEPS    :",stp," total steps")
 print("STAY     :",time_sty, " times detected stay")
 print("CALORIES :",calories," kcal burned total?")
 #fx_function(resolution,a,b,in_a,in_b,out)
 print("\n[F0]: Overweigh Detection =======================================")
 f0_function(resolution,age,heigh,weigh,in_age,in_heigh,in_weigh,out_wo, f0_out)   # 3 inputs
 print("\n[F1]: Pulserate Condition =======================================")
 f1_function(resolution,age,pulse,in_age,in_pulse,out_pr,f1_out)                  # 2 inputs
 print("\n[F2]: Stairs to do ==============================================")
 f2_function(resolution,stairs,elevators,in_stairs,in_elevators,out_use, f2_out)   # 2 inputs
 print("\n[F3]: Exercise to do ============================================")
 f3_function(resolution,f0_out,f1_out,f2_out,out_exe,out_exe,out_exe,out_exe, f3_out)        # 4 inputs need events as input
 #print("\n[F4]===========================================================")
 #f4_function(resolution,age,pulse,in_age,in_pulse,out_pr)                  # 4 inputs
 #print("\n[F5]===========================================================")
 #f5_function(resolution,calories,f1_out,in_calories,out_wo,out_cal)        # 2 inputs
 #nm=input()
 #os.system("cls")
 print("\nSUGGESTION ======================================================")
 #print(xs)
 #plt.show()
 