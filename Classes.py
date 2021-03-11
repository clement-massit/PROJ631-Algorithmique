# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Enoncé : Gestion d'un réseau de bus


#from data import get_liste_horaires

import manip_data


#=================================================
#lignes de bus: 
#data_file_name = '1_Poisy-ParcDesGlaisins.txt'



    
#==============================================================================  
#CLASSE ARRET    
class Arret:
    def __init__(self,label):
        self.label = label
        
    def get_ligne(self):
        ligne = ''
        for ar in manip_data.get_path_regular(ligne1.get_name_ligne()):
            if self.get_label() == ar:
                ligne = ligne1.get_name_ligne()
                break
        if self.get_label() not in manip_data.get_path_regular(ligne1.get_name_ligne()):
            ligne = ligne2.get_name_ligne()
            #ligne = ligne[0:-4] #pour enlever le .txt a la fin, c'est juste de l'habillage
        #print('''l'arret ''', self.get_label(), 'fait partie de la ligne :')  
        return ligne

        
    def get_label(self):  #retourne le nom d'un arret
        return self.label    
    

    def next_depart(self,time_start):   #retourne le prochain horaire de depart d'un bus sur le meme arret
        liste_horaire = self.horaires_first_path()
       
        time = manip_horaire(time_start)
        
        if time == True:
            ntime = liste_horaire.index(time + 1)
            for m in liste_horaire:
                horaire_compare = manip_horaire(m)
                if horaire_compare > ntime:
                    break
        else:
            for m in liste_horaire:
                horaire_compare = manip_horaire(m)
                if horaire_compare > time:
                    break
        return convert_to_hours_minutes(horaire_compare)
    
    
    def next_depart_sec_path(self,time_start):   #retourne le prochain horaire de depart d'un bus sur le meme arret
        liste_horaire = self.horaires_sec_path()
       
        time = manip_horaire(time_start)
        
        if time == True:
            ntime = liste_horaire.index(time + 1)
            for m in liste_horaire:
                horaire_compare = manip_horaire(m)
                if horaire_compare > ntime:
                    break
        else:
            for m in liste_horaire:
                horaire_compare = manip_horaire(m)
                if horaire_compare > time:
                    break
        return convert_to_hours_minutes(horaire_compare)
    
    #méthode pour recuperer la liste des horaires d'un arret
    # param : name_arret (str)
    
    def horaires_first_path(self):
        '''try:
            with open(start.get_ligne(), 'r', encoding = "utf-8") as f:
                content = f.read()
               
        except OSError:
            # 'File not found' error message.
            print("File not found")'''
            
        dico = manip_data.regular_horaires(start.get_ligne())  #modifier peut etre le start pour avoir les 2 lignes
        
        for cle in dico.keys():        
            if self.get_label() == cle:
                horaires = dico[self.get_label()]
        
        return horaires
    
    
    def horaires_sec_path(self):
        '''try:
            with open(start.get_ligne(), 'r', encoding = "utf-8") as f:
                content = f.read()
               
        except OSError:
            # 'File not found' error message.
            print("File not found")'''
            
        dico = manip_data.regular_horaires(self.get_ligne())  #modifier peut etre le start pour avoir les 2 lignes
        
        for cle in dico.keys():        
            if self.get_label() == cle:
                horaires = dico[self.get_label()]
        
        return horaires
    


def construct_arret(ar):
    return Arret(ar)


'''
#ligne 1   
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


PISCINE_PATINOIRE = Arret('PISCINE-PATINOIRE')
Arcadium = Arret('Arcadium')
Parc_des_Sports = Arret('Parc_des_Sports')  
Place_des_Romains = Arret('Place_des_Romains')
Courier = Arret('Courier')
GARE = Arret('GARE')
Bonlieu = Arret('Bonlieu')
Préfecture_Pâquier = Arret('Préfecture_Pâquier')
Impérial = Arret('Impérial')
Pommaries = Arret('Pommaries')
VIGNIÈRES = Arret('VIGNIÈRES')
CAMPUS = Arret('CAMPUS') 
'''



#==============================================================================
#CLASSE LIGNE       

class Ligne:
    def __init__(self, name_ligne):
        self.name_ligne = name_ligne
    
    def get_name_ligne(self):
        return self.name_ligne  #retourne un str
        
    #les deux méthodes ci dessous affiche la liste des differents arrets de la ligne 
    #depuis un arret donné si c'est en regular ou holidays
    
    #parametre : une ligne(str) et un arret(str)
    def get_ligne_go_steps(self,start,end):
        path_go = manip_data.get_path_regular(self.name_ligne)
        
        index_start = path_go.index(Arret.get_label(start))
        index_end = path_go.index(Arret.get_label(end))
        
        end_path = path_go.copy()
        end_path = path_go[index_start:index_end+1]
    
        return end_path
        
    #parametre : une ligne(str) et un arret(str)
    def get_ligne_back_steps(self,start,end):
        path_back = manip_data.get_path_regular(self.name_ligne)
        path_back.reverse()
      
        index_start = path_back.index(Arret.get_label(start))
        index_end = path_back.index(Arret.get_label(end))
        
        end_path = path_back.copy()
        end_path = path_back[index_start:index_end+1]
        
        return end_path
    
    def existe_dans_ligne(self,arret):
        for arr in manip_data.get_path_regular(self.get_name_ligne()):
            
            if arret == arr:
                return True
        
              
ligne1 = Ligne('1_Poisy-ParcDesGlaisins.txt')
ligne2 = Ligne('2_Piscine-Patinoire_Campus.txt')




#==============================================================================
#HORAIRES
from datetime import timedelta
 #cette fonction prend en parametre un str du type 'hh:mm'   

def manip_horaire(time):
    #cette méthode permet de transformer une heure du type HH:MM en nombre de minutes
    h = time
    if h != '-':
        delta = timedelta(hours = int(h.split(':')[0]), minutes = int(h.split(':')[1]))
        minutes = delta.total_seconds()/60
        return minutes
    else:
        return True

def convert_to_hours_minutes(number):
    #cette méthode transforme un nombre de minutes en HH:MM
    hours = number // 60
    number -= (hours * 60)
    minutes = number 
    return '{:1}:{:02}'.format(int(hours), int(minutes))


#==============================================================================
#PHASE DE TEST
'''
print('Entrez un arret de départ :')
start = construct_arret(input())
print('Entrez un arret darriver :')
end = construct_arret(input())

print('Entrez un horaire de départ (de la forme HH:MM) :')
timestart = input()

'''

def get_index_horaire_du_next_arret(ar,time):  
    #liste des horaires de l'arret
    liste_horaires_ar = Arret(ar).horaires_first_path()
    horaire_next_depart = Arret(ar).next_depart(time)  

    #heure du prochain bus a l'arret ar
    index_depart = liste_horaires_ar.index(horaire_next_depart)

    for h in range(len(liste_horaires_ar)):
    
        if index_depart == liste_horaires_ar[h]:
            break
    return index_depart



def get_index_horaire_du_next_arret_sec_path(ar,time):  
    #liste des horaires de l'arret
    liste_horaires_ar = Arret(ar).horaires_sec_path()
    
    horaire_next_depart = Arret(ar).next_depart_sec_path(time) 
    
    
    #heure du prochain bus a l'arret ar
    index_depart = liste_horaires_ar.index(horaire_next_depart)

    for h in range(len(liste_horaires_ar)):
    
        if index_depart == liste_horaires_ar[h]:
            break
    return index_depart



def get_temps_du_trajet(start,end):  
    #♦liste_horaires_arret = end.horaires_sec_path()

    time_debut = start.next_depart(real_time)
    
    time_fin = timestart
    
    
    minutes_debut = manip_horaire(time_debut)
    minutes_fin = manip_horaire(time_fin)
    time_trajet = minutes_fin - minutes_debut
    
    return round(time_trajet)


#la fonction qu'on va séparé en deux
    



'''
def path_with_mixed_lignes(start,end):
    #First part
    first_ligne = manip_data.get_path_regular(start.get_ligne()) #liste 
    
    index_start = first_ligne.index(start.get_label())    #index de start dans la liste d'arret
    
    
    for ar in first_ligne:
        
        if ligne1.existe_dans_ligne(ar) == True and ligne2.existe_dans_ligne(ar) == True:
            first_index = first_ligne.index(ar)
            break
        
    first_path = first_ligne[index_start:first_index+1]
    

    #Second part
    sec_ligne = manip_data.get_path_regular(end.get_ligne())
    index_end = sec_ligne.index(end.get_label())
    
    for ar in first_ligne:
        
        if first_path[-1] == ar:
            sec_index = sec_ligne.index(ar)
           
            
    sec_path = sec_ligne[sec_index:index_end+1]  # 0 -- +1 ou +1 -- +1
    
    #print(first_path)
    #print(sec_path)
    
    path = first_path + sec_path
    #print(path)
    return path
'''

print('--------------------')




def first_path():  
    try:
        with open(start.get_ligne(), 'r', encoding = "utf-8") as f:
            content = f.read()
           
    except OSError:
        # 'File not found' error message.
        print("File not found")
        
    dico = manip_data.regular_horaires(start.get_ligne())
    ligne = []
    for cle in dico.keys():
        
        ligne.append(cle)
        
    del ligne[0:ligne.index(start.get_label())]
    for ar in ligne:
    
        if ligne1.existe_dans_ligne(ar) == True and ligne2.existe_dans_ligne(ar) == True:
            del ligne[ligne.index(ar)+1 :]
     
    return ligne
      



def sec_path():  
        
    dico = manip_data.regular_horaires(end.get_ligne())
    ligne = []
    for cle in dico.keys():
        
        ligne.append(cle)
        
    liste_arrets = first_path()
    del ligne[ligne.index(end.get_label())+1:]
    for ar in ligne:
        if liste_arrets[-1] == ar:
            del ligne[0:ligne.index(liste_arrets[-1])+1]
     
    return ligne



# ============================================================================
#première partie
start = construct_arret('Vernod')
end = construct_arret('Ponchy')
timestart = '7:21'
real_time = timestart
liste_arrets_first_path = first_path()
liste_arrets_sec_path = sec_path()

print(liste_arrets_first_path)
print(liste_arrets_sec_path)

    
print()



#####   
print('on part de ', start.get_label(), 'il est ', timestart)
print('prochain bus à :', start.next_depart(timestart))
print('------------------------------')

for ar in liste_arrets_first_path:
    
    index_useful = get_index_horaire_du_next_arret(ar,timestart)
    heure_first = Arret(ar).horaires_first_path()[index_useful]
    print('on est a :', ar, '\nil est :', heure_first)
    timestart = heure_first
    

print('----- switch de ligne -----')

for ar in liste_arrets_sec_path:
    
    print('on est a :', ar)
    index_useful = get_index_horaire_du_next_arret_sec_path(ar,timestart)
    heure_sec = Arret(ar).horaires_sec_path()[index_useful]
    print('il est :', heure_sec)
    timestart = heure_sec
    

print('temps \t', get_temps_du_trajet(start,end), 'minutes')
    



