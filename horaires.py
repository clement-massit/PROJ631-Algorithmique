# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:18:07 2021

@author: cleme
"""

from manip_data import get_next_steps
from Classes import Arret



#==============================================================================


   
#print('test manip horaire : ')
#print(manip_horaire(liste_horaire[0]))      
   
#==============================================================================

#cette fonction renvoie l'horaire a laquelle on arrivera au prochain arret sur une ligne
#elle prend en parametre une horaire de depart et un arret 
#par exemple on est a Vernod il est 7:15 et on arriver a Meythet_Le_Rabelais a 7h21 
    
def get_next_horaire(timestart, arret):
    #renvoie le ditcionnaire du timestart donné
    horaire_dict = manip_horaire(timestart)
    #renvoie le nom du prochain arret
    next_step = get_next_steps(arret,'1_Poisy-ParcDesGlaisins.txt')
    liste_horaires = Arret.get_liste_horaires(next_step[0])  #on recupere la liste des horaires du prochain arret
    
    h,minutes = [], []      #initialisation
    horaires = {}
    
    while '-' in liste_horaires:            
        liste_horaires.remove('-')      #on remove les - de la liste des horaires
    
    
    for i in range(len(liste_horaires)):        #on ajoute aux listes h et minutes les heures et minutes séparées
        hora = liste_horaires[i].split(':')
        h.append(hora[0]) 
        minutes.append(hora[1])
        
        
    horaires['heure'] = h
    horaires['minutes'] = minutes
    
    
    for i in range(len(liste_horaires)):
        if horaire_dict['heure'][0] <= horaires['heure'][i] and horaire_dict['minutes'][0] <= horaires['minutes'][i] or horaire_dict['heure'][0] < horaires['heure'][i]:
            next_h = horaires['heure'][i]
            next_min = horaires['minutes'][i]
            break
    print()
    
    return [next_h, next_min]

    
    
    

#print('on lance ce fichier')
#print('''Nous partons de: Ponchy''')
#print('''Nous arriverons à :''', get_next_steps('Ponchy','1_Poisy-ParcDesGlaisins.txt')[0])
'''print('Nous arriverons au prochain arret vers :',
      get_next_horaire('7:20','Ponchy')[0], 'h',
      get_next_horaire('7:20','Ponchy')[1], 'min'
      )'''
