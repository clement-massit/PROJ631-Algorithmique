# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


import manip_data

#==============================================================================  
#CLASSE ARRET    
class Arret:
    """
    A stop possesses a label -> the name of the stop
    """
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
    

    def next_depart(self,time_start):
        #return the next timetable of the next stop
        #from the first path (this is for the shortest way)
        
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
    
    
    def next_depart_sec_path(self,time_start):
        #return the next timetable of the next stop
        #from the second path (this is for the shortest way)
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
    
    
    
    def horaires_first_path(self):
        #with this method, we can get the list of timetable from one stop
        # if there are one stop in two ligns, the we can get the correct line
        # with the get_ligne() method
        dico = manip_data.regular_horaires(self.get_ligne())  
        horaires = dico[self.get_label()]
        
        return horaires
    
    
    def get_index_horaire_du_next_arret(self,time):  
        #return the index of timetable (indicated in parameters) of the new stop in the path
        # this one is for the first_path() method (shortest way))
        liste_horaires_ar = self.horaires_first_path()
        
        horaire_next_depart = self.next_depart(time)  
       
        #heure du prochain bus a l'arret ar
        index_depart = liste_horaires_ar.index(horaire_next_depart)
    
        for h in range(len(liste_horaires_ar)):
        
            if index_depart == liste_horaires_ar[h]:
                break
        return index_depart
    
    def get_index_horaire_du_next_arret_sec_path(self,time):
        #same than before but this one is for the second path (shortest way)
     
        liste_horaires_ar = self.horaires_sec_path()
        
        horaire_next_depart = self.next_depart_sec_path(time) 

        #heure du prochain bus a l'arret ar
        index_depart = liste_horaires_ar.index(horaire_next_depart)
    
        for h in range(len(liste_horaires_ar)):
        
            if index_depart == liste_horaires_ar[h]:
                break
        return index_depart


def build_stop(ar): #you can build a stop with this method
    return Arret(ar)


#==============================================================================
#CLASSE LIGNE       

class Ligne:
    """
    a line possesses a label same as the Stop class
    """
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
  

def manip_horaire(time):
    #this method can convert a timetable like HH:MM to a number of minutes
    h = time
    if h != '-':
        delta = timedelta(hours = int(h.split(':')[0]), minutes = int(h.split(':')[1]))
        minutes = delta.total_seconds()/60
        return minutes
    else:
        return True

def convert_to_hours_minutes(number):
    #This is the reverse of the previous method
    #convert a number of minutes into HH:MM
    hours = number // 60
    number -= (hours * 60)
    minutes = number 
    return '{:1}:{:02}'.format(int(hours), int(minutes))


def get_last_time(liste,timestart):
    #Give the last timetable of stop list from a start timetable
    for ar in liste:
        
        index_useful = Arret(ar).get_index_horaire_du_next_arret(timestart)
        heure_first = Arret(ar).horaires_first_path()[index_useful]
        timestart = heure_first
    time_done = timestart
    
    return time_done

def get_temps_du_trajet(liste,start,end):  
    #return the time spent in the bus during the travel
    #shortes
    time_debut = start.next_depart(real_time)
    time_fin= get_last_time(liste,timestart)
  
    
    minutes_debut = manip_horaire(time_debut)
    minutes_fin = manip_horaire(time_fin)
    
    time_trajet = minutes_fin - minutes_debut
    
    
    return round(time_trajet)



#==============================================================================


# ============================================================================
#   FASTEST WAY
    
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



#==============================================================================
#   SHORTEST WAY
def first_path():
    #in order to switch line     
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
start = build_stop('Arcadium')
end = build_stop('Ponchy')
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




