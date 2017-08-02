"""
PROJECT     : FUJITSU GLOBAL INTERNSHIP
OFFICE      : KAWASAKI OFFICE
DEPARTEMENT : INOVATION IOT BUSINESS UNIT
AUTHOR      : Hanjara Cahya Adhyatma
E-MAIL      : adhyatma.han@gmail.com
YEAR        : 2017
COMMENT     :

"""

#######################################################################
# IMPORTED LIBRARY
#######################################################################
import numpy as np

#######################################################################
# SELECTOR MODE
#######################################################################
# There is mode for running entire program:
# 0 (real_time), 1 (read_collected), 2 (view only)
MODE    = 0
# This is for debug mode, see 1 by 1 process to correct error
# 0 (OFF), 1 (ON)
DEBUG   = 0
# This is for activation print function while DEBUG is on
# 0 (OFF), 1 (ON)
COMMENT = 0

#######################################################################
# CLASIFICATION RANGE NAME
#######################################################################
ages        = np.array(["child","teen","adult","elder"])
ages_th	    = np.array([12,18,50,100])

weigh       = np.array(["underw", "normw", "overw"])
weigh_th    = np.array([20,50,80])

heigh       = np.array(["short","aver","tall"])
heigh_th    = np.array([130,160,190])

pulse       = np.array(["passive","active","stress"])
pulse_th    = np.array([60,90,120])

calories    = np.array(["low", "mid", "high"])
calories_th = np.array([1000, 2000, 3000])

x_ages = np.arange(101)
y = np.arange(0, 1.00001, .00001)











