# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 20:23:01 2021

@author: cleme
"""

import Classes
import tests



start = Classes.build_stop('Arcadium')
end = Classes.build_stop('Ponchy')
timestart = '6:24'
real_time = timestart



plus_court = Classes.best_trajet(start,end)
print('chemin le plus court :')
for i in plus_court:
    print(i)
print()    
time_trajet_court = Classes.get_temps_du_trajet(plus_court,start,end)
print('le temps de trajet est :', time_trajet_court, 'minutes')
  

print('\n------------------\n')
plus_rapide = Classes.get_trajet_rapide(Classes.best_time(start,end), start,end)
print('chemin le plus rapide')
for i in plus_rapide:
    print(i)
print()    
time_trajet_rapide = Classes.get_temps_du_trajet(plus_rapide,start,end)
print('le temps de trajet est :', time_trajet_rapide, 'minutes')
print()   
