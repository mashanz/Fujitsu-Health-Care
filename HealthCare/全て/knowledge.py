"""
FUZZY RULE
Table relation betwen INPUTS to decide OUTPUT by Expert/Statistical
Knowladge. It relation output degree calculated by Fuzzy crisp from
input.


WARNING! TEMPLATE MODE STILL SEARCHING MORE RESOURCE
"""

#=====================================================================
#TABLE DIMENTION TEMPLATE
#=====================================================================
#3x1 table
knowladge_31 = ['A','B','C']
#print(knowladge_31[2])

#3x3 table
#[y][x]
knowladge_33 = [
 ['A','B','C'],
 ['D','E','F'],
 ['G','H','I']]
#print(knowladge_33[1][2])

#3x4 table
#[y][x]
knowladge_34 = [
 ['NO','NO','NO','NO'],
 ['OK','NO','NO','NO'],
 ['OK','OK','OK','NO']]
#print(knowladge_33[1][2])

#3x3x3 table
#[y][x][z]
knowladge_333 =[
 [['A','B','C'],['D','E','F'],['G','H','I']],
 [['J','K','L'],['M','N','O'],['P','Q','R']],
 [['S','T','U'],['V','W','X'],['Y','Z','oh my']]]
#print(knowladge_333[0][2][0])

#=====================================================================
#OVERWEIGH DETECTION KNOWLADGE (OD)
#=====================================================================
knowladge_OD =[
#[y][x][z] = [0][i][i]
#+--------------------------------+
#|   for young(heigh and weigh)   |
#+-------+-------+--------+-------+
#|       | under | normal | over  |
#+-------+-------+--------+-------+
#| ligh  |   A   |   B    |   C   | 00i
#| midle |   D   |   E    |   F   | 01i
#| heavy |   G   |   H    |   I   | 02i
#+-------+-------+--------+-------+
 [['A','B','C'],['D','E','F'],['G','H','I']],

#[y][x][z] = [1][i][i]
#+-------------------------------+
#|   for young(heigh and weigh)  |
#+-------+-------+--------+------+
#|       | under | normal | over |
#+-------+-------+--------+------+
#| ligh  |   J   |   K    |   L  | 10i
#| midle |   M   |   N    |   O  | 11i
#| heavy |   P   |   Q    |   R  | 12i
#+-------+-------+--------+------+
 [['J','K','L'],['M','N','O'],['P','Q','R']],

#[y][x][z] = [2][i][i]
#+-------------------------------+
#|   for young(heigh and weigh)  |
#+-------+-------+--------+------+
#|       | under | normal | over |
#+-------+-------+--------+------+
#| ligh  |   S   |   T    |   U  | 20i
#| midle |   V   |   W    |   X  | 21i
#| heavy |   Y   |   Z    |   -  | 22i
#+-------+-------+--------+------+
 [['S','T','U'],['V','W','X'],['Y','Z','-']]]
#print(knowladge_OD[0][2][0])


#=====================================================================
#WEIGH KNOWLADGE (FUZZY0) dummy knowladge
#=====================================================================
#[y][x] = [i][i]
#+--------------------------------+
#|                                |
#+-------+-------+--------+-------+
#|       | young |  adult |  old  |
#+-------+-------+--------+-------+
#| low   |  under|  under |  under| 0i
#|average| normal|  normal| normal| 1i
#| high  |  over |  over  |  over | 2i
#+-------+-------+--------+-------+
knowladge_F0 = [
 ['under','under','normal'],
 ['under','normal','overweigh'],
 ['normal','overweigh','overweigh']]
#print(knowladge_F1[0][1])

#=====================================================================
#PULSE RATE KNOWLADGE (FUZZY1)
#=====================================================================
#[y][x] = [i][i]
#+--------------------------------+
#|                                |
#+-------+-------+--------+-------+
#|       | young |  adult |  old  |
#+-------+-------+--------+-------+
#| low   |  bad  |  bad   |  bad  | 0i
#|average| good  |  good  | good  | 1i
#| high  |  bad  |  bad   |  bad  | 2i
#+-------+-------+--------+-------+
knowladge_F1 = [
 ['low','low','low'],
 ['good','good','good'],
 ['high','high','high']]
#print(knowladge_F1[0][1])

#=====================================================================
#ELEVATORS OR STAIRS KNOWLADGE (FUZZY2)
#=====================================================================
#[y][x] = [i][i]
#+--------------------------------+
#|     (stairs and elevators)     |
#+-------+-------+--------+-------+
#|       | less  |average | often |
#+-------+-------+--------+-------+
#| less  | moore | no_to  | no_to | 0i
#|average| moore | no_to  | no_to | 1i
#| often | moore | moore  | no_to | 2i
#+-------+-------+--------+-------+
knowladge_F2 = [
 ['use more stairs','use more stairs','use more stairs'],
 ['use more stairs',' ',' '],
 ['use more stairs',' ',' ']]
#print(knowladge_F2[0][1])

#=====================================================================
#EXERCISE KNOWLADGE (FUZZY3)
#=====================================================================
#is staying?, so it's time?
#[OD][F1][F2]
#+--------------------------------+
#|     (stairs and elevators)     |
#+-------+-------+--------+-------+
#|       | less  |average | often |
#+-------+-------+--------+-------+
#| less  | not | not  | litle | 0i
#|average| litle | litle  | litle | 1i
#| often | litle | more  | more | 2i
#+-------+-------+--------+-------+
knowladge_F3 = [
 ['not needed exercise','not needed exercise','need little exercise'],
 ['need little exercise','need little exercise','need little exercise'],
 ['need little','need more exercise','need more exercise']]

#=====================================================================
#WALKING/STEPS KNOWLADGE (FUZZY4)
#=====================================================================

#=====================================================================
#CALORIES KNOWLADGE (FUZZY5)
#=====================================================================






