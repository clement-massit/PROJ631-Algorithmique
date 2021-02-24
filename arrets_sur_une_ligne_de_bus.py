# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:15:59 2021

@author: cleme
"""

from data import get_liste_horaires
from Test_Gestion_bus import get_path_regular, get_path_holidays



liste_regular_go1 = get_liste_horaires('Meythet_Le_Rabelais')

liste_regular_go2 = get_liste_horaires('Vernod')

#?print(liste_regular_go1,'\n', liste_regular_go2)


#========================================================
#les deux méthodes ci dessous affiche la liste des differents arrets de la ligne 
#depuis un arret donné si c'est en regular ou holidays

#parametre : une ligne(str) et un arret(str)
def get_ligne_from_step_go(ligne,arret):
    path_regular = get_path_regular(ligne)
    
    end_path = []
    for ar in range(len(path_regular)):
        if path_regular[ar] == arret:                               ############################
            end_path = path_regular[ar:-1]                          # A MODIFIER STEP GO STEP BACK#######
    return end_path

#parametre : une ligne(str) et un arret(str)
def get_ligne_from_step_back(ligne,arret):
    path_holidays = get_path_holidays(ligne)
    
    end_path = []
    for ar in range(len(path_holidays)):
        if path_holidays[ar] == arret:
            end_path = path_holidays[ar:-1]
    return end_path

#print(get_ligne_from_step_regular('1_Poisy-ParcDesGlaisins.txt', 'Vernod'))
#========================================================            

#on retourne le prochain arret a partir d'un arret donné
#et depuis une ligne donné
    
def get_next_step(name_arret,ligne):
    next_step = []
    liste_arret = get_path_regular(ligne)
    for ar in range(len(liste_arret)-1):
        if liste_arret[ar] == name_arret:
            next_step.append(liste_arret[ar + 1])
    return next_step





        
        