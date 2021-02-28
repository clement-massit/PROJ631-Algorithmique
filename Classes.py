# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Enoncé : Gestion d'un réseau de bus


#from data import get_liste_horaires
import manip_data
from manip_data import get_path_regular, get_path_holidays


#=================================================
#lignes de bus: 
data_file_name = '1_Poisy-ParcDesGlaisins.txt'


try:
    with open(data_file_name, 'r', encoding = "utf-8") as f:
        content = f.read()   
except OSError:
    print('file not found')
    
#==============================================================================  
#CLASSE ARRET    
class Arret:
    def __init__(self,label):
        self.label = label
        
        #self.ligne_regular = manip_data.regular_path
        #self.ligne_holidays = manip_data.we_holidays_path
                
        
    def get_label(self):  #retourne le nom d'un arret
        return self.label    
    

    def next_depart(self,time_start):   #retourne le prochain horaire de depart d'un bus sur le meme arret
        liste_horaire = self.get_liste_horaires()
     
        time = manip_horaire(time_start)
     
        for m in liste_horaire:
            horaire_compare = manip_horaire(m)
            if horaire_compare > time:
                break
        return convert_to_hours_minutes(horaire_compare)
    
    #méthode pour recuperer la liste des horaires d'un arret
    # param : name_arret (str)
        
    def get_liste_horaires(self):
        reg_go = manip_data.regular_date_go[self.get_label()]
        '''reg_back = manip_data.regular_date_back[label]             #ce sont des dictionnaires
        hol_go = manip_data.we_holidays_date_go[label]
        hol_back = manip_data.we_holidays_date_back[label]'''
        return reg_go   #on récupère la liste d'un arret donné
    
LYCÉE_DE_POISY = Arret('LYCÉE_DE_POISY')
POISY_COLLÈGE = Arret('POISY_COLLÈGE')
Vernod = Arret('Vernod')
Meythet_Le_Rabelais = Arret('Meythet_Le_Rabelais')
Chorus = Arret('Chorus')
Mandallaz = Arret('Mandallaz')
GARE = Arret('GARE')
France_Barattes = Arret('France_Barattes')
CES_Barattes = Arret('C.E.S_Barattes')
VIGNIÈRES = Arret('VIGNIÈRES')
Ponchy = Arret('Ponchy')
PARC_DES_GLAISINS = Arret('PARC_DES_GLAISINS')    

liste_arret = [LYCÉE_DE_POISY,POISY_COLLÈGE,Vernod,Meythet_Le_Rabelais,
               Chorus,Mandallaz,GARE,France_Barattes,CES_Barattes,VIGNIÈRES,Ponchy,PARC_DES_GLAISINS]




    
#==============================================================================
#CLASSE LIGNE       

class Ligne:
    def __init__(self, name_ligne):
        self.name_ligne = name_ligne
        
    #les deux méthodes ci dessous affiche la liste des differents arrets de la ligne 
    #depuis un arret donné si c'est en regular ou holidays
    
    #parametre : une ligne(str) et un arret(str)
    def get_ligne_go_steps(self,start,end):
        path_go = get_path_regular(self.name_ligne)

        index_start = path_go.index(Arret.get_label(start))
        index_end = path_go.index(Arret.get_label(end))
        
        end_path = path_go.copy()
        end_path = path_go[index_start:index_end+1]
    
        return end_path
        
    #parametre : une ligne(str) et un arret(str)
    def get_ligne_back_steps(self,start,end):
        path_back = get_path_regular(self.name_ligne)
        path_back.reverse()
      
        index_start = path_back.index(Arret.get_label(start))
        index_end = path_back.index(Arret.get_label(end))
        
        end_path = path_back.copy()
        end_path = path_back[index_start:index_end+1]
        
        return end_path
    




ligne1 = Ligne('1_Poisy-ParcDesGlaisins.txt')
ligne2 = Ligne('2_Piscine-Patinoire_Campus.txt')

#==============================================================================
#HORAIRES
from datetime import timedelta
 #cette fonction prend en parametre un str du type 'hh:mm'   

def manip_horaire(time):
    h = time
    delta = timedelta(hours = int(h.split(':')[0]), minutes = int(h.split(':')[1]))
    minutes = delta.total_seconds()/60
    return minutes

def convert_to_hours_minutes(number):
    hours = number // 60
  
    number -= (hours * 60)
    minutes = number 
    return '{:1}:{:02}'.format(int(hours), int(minutes))





start = Vernod
end = GARE
timestart = '7:00'

chemin = ligne1.get_ligne_go_steps(start,end)
print('chemin :', chemin)
print('il est ', timestart)
print('prochain bus qui part de ', start.get_label(),' est à ', start.next_depart(timestart))
print()



def get_index_horaire_du_next_arret(ar):    #objet arret
    starthoraire = ar.get_liste_horaires()
    #liste des horaires de l'arret
    horaire_next_depart = ar.next_depart(timestart)
    index_depart = starthoraire.index(horaire_next_depart)
    #heure du prochain depart de l'arret
    for h in range(len(starthoraire)):
    
        if index_depart == starthoraire[h]:
            break
    return index_depart
    
print('index de lhoraire :',start.next_depart(timestart), 'est :', get_index_horaire_du_next_arret(start))

print()

print('il est ', timestart, 'prochain bus à :',start.next_depart(timestart))

for ar in chemin:
    liste = Arret(ar).get_liste_horaires()
    print('on est à ', ar)
    print('départ du bus à :', liste[get_index_horaire_du_next_arret(start)])
    
    
    
#parcour liste de chemin prendre vernod +1 et getindexnextarret(vernod +1)









