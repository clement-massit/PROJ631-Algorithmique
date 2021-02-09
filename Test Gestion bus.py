# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Enoncé : Gestion d'un réseau de bus

from data2py import data2dic

data_file_name = '1_Poisy-ParcDesGlaisins.txt'
try:
    with open(data_file_name, 'r') as f:
        content = f.read()
    
except OSError:
    print('file not found')
    
#Classe Arret a un label    
class Arret:
    def __init__(self,label):
        self.label = label
        
    
    def get_label(self):
        return self.label

    def get_liste_horaire(self):
        regular_date_go = dates2dic(content.plit('\n\n\n'))
        return regular_date_go[self]

 
print('Vernod'.get_liste_horaire())
       
class Bus:
    def __init__(self,label,start,end):
        self.label = label
        self.start = start
        self.end = end
        
    