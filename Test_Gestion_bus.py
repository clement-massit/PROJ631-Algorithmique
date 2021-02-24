# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Enoncé : Gestion d'un réseau de bus


#from data import get_liste_horaires

#=================================================
#lignes de bus: 
data_file_name = '1_Poisy-ParcDesGlaisins.txt'


try:
    with open(data_file_name, 'r') as f:
        content = f.read()   
except OSError:
    print('file not found')
    
#=================================================   
#Classe Arret    
class Arret:
    def __init__(self,label,liste_horaire_linge):
        self.label = label
        self.liste_horaire_ligne
        
    
    def get_label(self):  #retourne le nom d'un arret
        return self.label     

    def next_depart(self,time_start):   #retourne le prochain horaire de depart d'un bus sur le meme arret
        horaires = self.get_liste_horaires()
        horaire_next_depart = horaires[time_start + 1]
        return horaire_next_depart
    

 
class Bus:
    def __init__(self,label,start,end):
        self.label = label
        self.start = start
        self.end = end
        
        
        
        

#=================================================
#methode general pour recuperer la ligne de bus sous forme d'une liste
def get_path_regular(lign):
    file = open(lign, 'r')
    content = file.read()
    path_fromtxt = []
    
    splitted_content = content.split('\n\n')      #on split le contenu du txt
    path_fromtxt.append(splitted_content[0])    #on ajoute l'elemnt du txt dans une liste vide
    
    
    string_setup = ''.join(path_fromtxt)    #manipulation de la nouvelle liste en str pour pouvoir la split
    new_path = string_setup.split(' N ')    #split pour avoir la liste de tout les arret d'une ligne
    
    return new_path



def get_path_holidays(lign):
    file = open(lign, 'r')
    content = file.read()
    path_fromtxt = []
    
    splitted_content = content.split('\n\n')      #on split le contenu du txt
    path_fromtxt.append(splitted_content[3])    #on ajoute l'elemnt du txt dans une liste vide
    
    
    string_setup = ''.join(path_fromtxt)    #manipulation de la nouvelle liste en str pour pouvoir la split
    new_path = string_setup.split(' N ')    #split pour avoir la liste de tout les arret d'une ligne
    
    return new_path


#=================================================


#Exemple test pour un bus
start = 'LYCÉE_DE_POISY'
end = 'PARC_DES_GLAISINS'

bus = Bus('1',start,end)




