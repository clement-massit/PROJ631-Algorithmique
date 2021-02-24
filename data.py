#!/usr/bin/python3
#-*-coding:utf-8-*-
from Test_Gestion_bus import get_path_regular

data_file_name = '1_Poisy-ParcDesGlaisins.txt'
#data_file_name = '2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r') as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic

slited_content = content.split("\n\n")
#les 2 premières parties du txt
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])

#les 2 dernières parties du txt
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])

#print(regular_path)

#print test arrets avec liste horaires
arrets =[]
for cle,heure in regular_date_go.items():
    arrets.append(cle)
    #print(cle,heure)

#==============================================================================
    
#méthode pour recuperer la liste des horaires d'un arret
# param : name_arret (str)
    
def get_liste_horaires(name_arret):
    reg_go = regular_date_go[name_arret]
    reg_back = regular_date_back[name_arret]
    hol_go = we_holidays_date_go[name_arret]
    hol_back = we_holidays_date_back[name_arret]
    return reg_go   #on récupère la liste d'un arret donné


liste_horaire = get_liste_horaires('PARC_DES_GLAISINS')
#==============================================================================

#on retourne le prochain arret a partir d'un arret donné
#et depuis une ligne donné
    
def get_next_step(name_arret,ligne):
    next_step = []
    liste_arret = get_path_regular(ligne)
    for ar in range(len(liste_arret)-1):
        if liste_arret[ar] == name_arret:
            next_step.append(liste_arret[ar + 1])
    return next_step

#==============================================================================

#cette fonction prend en parametre un str du type 'hh:mm'
    
def manip_horaire(heure_numeric):
    heure = []      #values des heure du dictionnaire
    minutes = []    # values des minutes du dictionnaire
    dict_horaire = {}
    while '-' in heure_numeric:            #script pour remove tous les tirets
        heure_numeric.remove('-')
    
    separated = heure_numeric.split(':')
    heure.append(separated[0])
    minutes.append(separated[1])

    dict_horaire['heure'] = heure
    dict_horaire['minutes'] = minutes
    return dict_horaire
    #return un dictionnaire composé de 2 clés du type 'heure' : 6, 'minutes' : 36'
   
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
    next_step = get_next_step(arret,'1_Poisy-ParcDesGlaisins.txt')
    liste_horaires = get_liste_horaires(next_step[0])  #on recupere la liste des horaires du prochain arret
    
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
    return [next_h,next_min]


print('''Nous partons de: Ponchy''')
print('''Nous arriverons à :''', get_next_step('Ponchy','1_Poisy-ParcDesGlaisins.txt')[0])
print('''Nous arriverons au prochain arret vers :''',
      get_next_horaire('7:20','Ponchy')[0], 'h',
      get_next_horaire('7:20','Ponchy')[1], 'min'
      )



