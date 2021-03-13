# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:56:23 2021

@author: cleme
"""
from Classes import Arret, Ligne
import manip_data
try:
    with open(start.get_ligne(), 'r', encoding = "utf-8") as f:
        content = f.read()
               
except OSError:
    # 'File not found' error message.
    print("File not found")
        
class Arc:
    def __init__(self,arc = []):
        self.start = start
        self.end = end
        self.arc = [start,end]
        
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    
start = Arret('GARE')
end = Arret('France_Barattes')

arc = Arc([start,end])



def liste_arcs():
    
    dico = manip_data.regular_horaires(start.get_ligne())
    arcs = []
    liste_arcs = []
    for key in dico.keys():
        arcs.append(key)
    for ar in range(len(arcs)-1):
        print(arcs[ar])
        liste_arcs.append([arcs[ar],arcs[ar+1]])
        
    return arcs
print(liste_arcs())
        
