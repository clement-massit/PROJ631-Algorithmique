# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Enoncé : Gestion d'un réseau de bus


#from data import get_liste_horaires

import manip_data

#==============================================================================  
#CLASSE ARRET    
class Arret:
    def __init__(self,label):
        self.label = label
        
    def get_ligne(self):
        ligne = ''
        dico_l1 = manip_data.regular_horaires(ligne1.get_name_ligne())
        dico_l2 = manip_data.regular_horaires(ligne2.get_name_ligne())
        
        for key in dico_l1.keys():
            if self.get_label() not in dico_l2:
                ligne = ligne1.get_name_ligne()
                break
            if self.get_label() not in dico_l1: 
                ligne = ligne2.get_name_ligne()
                break
            else:   
                if start.get_label() == key:
                    ligne = ligne1.get_name_ligne()
                    break
                else:
                    ligne = ligne2.get_name_ligne()
                
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
        dico = manip_data.regular_horaires(self.get_ligne())  
        horaires = dico[self.get_label()]
        
        return horaires
    
    
    '''def horaires_sec_path(self):
        dico = manip_data.regular_horaires(end.get_ligne())  
        horaires = dico[self.get_label()]
    
        
        return horaires'''
    
    def get_index_horaire_du_next_arret(self,time):  
        #liste des horaires de l'arret
        liste_horaires_ar = self.horaires_first_path()
        
        horaire_next_depart = self.next_depart(time)  
       
        #heure du prochain bus a l'arret ar
        index_depart = liste_horaires_ar.index(horaire_next_depart)
    
        for h in range(len(liste_horaires_ar)):
        
            if index_depart == liste_horaires_ar[h]:
                break
        return index_depart
    
    def get_index_horaire_du_next_arret_sec_path(self,time):  
        #liste des horaires de l'arret
        liste_horaires_ar = self.horaires_sec_path()
        
        horaire_next_depart = self.next_depart_sec_path(time) 

        #heure du prochain bus a l'arret ar
        index_depart = liste_horaires_ar.index(horaire_next_depart)
    
        for h in range(len(liste_horaires_ar)):
        
            if index_depart == liste_horaires_ar[h]:
                break
        return index_depart

def construct_arret(ar):
    return Arret(ar)


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
        '''path_go = manip_data.get_path_regular(self.name_ligne)
        
        index_start = path_go.index(Arret.get_label(start))
        index_end = path_go.index(Arret.get_label(end))
        
        end_path = path_go.copy()
        end_path = path_go[index_start:index_end+1]
        '''
        
        first = first_path()
        last = sec_path()

        total = first + last
    
        return total
        
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


def get_last_time(liste,timestart):
    for ar in liste:
        
        index_useful = Arret(ar).get_index_horaire_du_next_arret(timestart)
        heure_first = Arret(ar).horaires_first_path()[index_useful]
        timestart = heure_first
    time_done = timestart
    
    return time_done

def get_temps_du_trajet(liste,start,end):  
    
    #plus court
    time_debut_c = start.next_depart(real_time)
    time_fin_c = get_last_time(liste,timestart)
  
    
    minutes_debut_c = manip_horaire(time_debut_c)
    minutes_fin_c = manip_horaire(time_fin_c)
    
    time_trajet_c = minutes_fin_c - minutes_debut_c
    
    '''#plus rapide
    time_debut_r = start.next_depart(real_time)
    time_fin_r = get_last_time(trajet_sur_une_ligne(start,end),timestart)
  
    
    minutes_debut_r = manip_horaire(time_debut_r)
    minutes_fin_r = manip_horaire(time_fin_r)
    
    time_trajet_r = minutes_fin_r - minutes_debut_r'''
    
    return round(time_trajet_c)



#==============================================================================


# ============================================================================
#   CHEMIN LE PLUS RAPIDE
    
def trajet_sur_une_ligne(start,end):
  
    dico = manip_data.regular_horaires(start.get_ligne())
    chemin = []
    
    for key in dico.keys():
        chemin.append(key)
         
        if key == end.get_label():
            break
        
    del chemin[0:chemin.index(start.get_label())]     
    return chemin





def possible_times(start,end):
    trajet = trajet_sur_une_ligne(start,end)
    other = first_path() + sec_path()
    
    time1 = get_temps_du_trajet(trajet,start,end)
    time2 = get_temps_du_trajet(other,start,end)
    
    return time1,time2

def get_trajet_rapide(time,start,end):
    return trajet_sur_une_ligne(start,end) if time == possible_times(start,end)[0] else first_path() + sec_path()



def best_time(start,end):
    time1 = possible_times(start,end)[0]
    time2 = possible_times(start,end)[1]
    return time1 if time1 < time2 else time2


print(best_time(start,end))
#==============================================================================
#   CHEMIN LE PLUS COURT
def first_path():
        
    dico = manip_data.regular_horaires(start.get_ligne())
    
    chemin = []
    
    
    for cle in dico.keys():
        chemin.append(cle)
        
    del chemin[0:chemin.index(start.get_label())]
  
    for ar in chemin:  
        if ar == end.get_label():
            del chemin[chemin.index(ar)+1:]
            return chemin 
         
        if ligne1.existe_dans_ligne(ar) == True and ligne2.existe_dans_ligne(ar) == True: 
            del chemin[chemin.index(ar)+1:]        
            return chemin 


##changement de ligne
def sec_path():  
    if first_path()[-1] == end.get_label():
        
        return []
 
    #1er switch 
    ligne_at_start = start.get_ligne()
   
    if ligne_at_start == ligne1.get_name_ligne():
        switch = ligne2.get_name_ligne()
    else:
        switch = ligne1.get_name_ligne()
        
   
    dico = manip_data.regular_horaires(switch)
    chemin = []
    for cle in dico.keys():
        chemin.append(cle)
    liste_arret = first_path()
    
    index = chemin.index(liste_arret[-1])
    
    del chemin[0:index+1]
    
    for ar in chemin:
        if ligne1.existe_dans_ligne(ar) == True and ligne2.existe_dans_ligne(ar) == True:
            del chemin[chemin.index(ar)+1:]
    if end.get_label() == chemin[-1]:
        
        return chemin
    
   
    ##reswitch eventuellement
    if end.get_label() != chemin[-1]:
        if end.get_ligne() == Arret(chemin[-1]).get_ligne():
            ligne_at_start = ligne_at_start
            
        else:
            ligne_at_start = switch
            
            
        new_dico = manip_data.regular_horaires(ligne_at_start)
        
        new_list = []
        
        
        for key in new_dico.keys():
            new_list.append(key)
            
            
        
        new_index = new_list.index(first_path()[-1])
        fin_index = new_list.index(end.get_label()) 
       
        for ar in new_list:
        
            if ar == chemin[-1]:
                #print('new_liste quon doit del',new_list,'\n')
                #del new_list[0:new_index]
                #print('\nee', new_list,'\n')
                new_list = new_list[new_index:fin_index+1]
                
                
        
           
        return new_list


def possible_paths(sart,end):
    trajet = trajet_sur_une_ligne(start,end)
   
    other = first_path() + sec_path()
   
    result = []
    for ar in other:
        if ar not in result:
            result.append(ar)
    
    return trajet,result
    
    
    
def best_trajet(start,end):#fonction ok
    paths = possible_paths(start,end)
    
    if len(paths[0]) < len(paths[1]):
        return paths[0]
    else:
        return paths[1]

   
#==============================================================================   


#CONSTRUCTION
start = construct_arret('Arcadium')
end = construct_arret('Ponchy')
timestart = '6:24'
real_time = timestart


#print(best_trajet(start,end))
'''
print('Entrez un arret de départ :')
start = construct_arret(input())
print('Entrez un arret darriver :')
end = construct_arret(input())

print('Entrez un horaire de départ (de la forme HH:MM) :')
timestart = input()


print(start.get_ligne(), end.get_ligne())
print(first_path())
print()
print(sec_path())
print()
'''

print('time start :', timestart)

plus_court = best_trajet(start,end)
print('chemin le plus court :')
for i in plus_court:
    print(i)
print()    
time_trajet_court = get_temps_du_trajet(plus_court,start,end)
print('le temps de trajet est :', time_trajet_court, 'minutes')
  

print('\n------------------\n')
plus_rapide = get_trajet_rapide(best_time(start,end), start,end)
print('chemin le plus rapide')
for i in plus_rapide:
    print(i)
print()    
time_trajet_rapide = get_temps_du_trajet(plus_rapide,start,end)
print('le temps de trajet est :', time_trajet_rapide, 'minutes')
print()   




