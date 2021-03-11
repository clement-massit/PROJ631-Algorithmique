#!/usr/bin/python3
#-*-coding:utf-8-*-


ligne1 = '1_Poisy-ParcDesGlaisins.txt'
ligne2 = '2_Piscine-Patinoire_Campus.txt.txt'
def regular_horaires(lign):
    
    try:
        with open(lign, 'r', encoding = "utf-8") as f:
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
    
    return regular_date_go




def holidays_horaires(lign):
    try:
        with open(lign, 'r', encoding = "utf-8") as f:
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
    #les 2 dernières parties du txt
    we_holidays_path = slited_content[3]
    we_holidays_date_go = dates2dic(slited_content[4])
    we_holidays_date_back = dates2dic(slited_content[5])
    
    return we_holidays_date_go

#==============================================================================

    #on retourne le prochain arret a partir d'un arret donné
    #et depuis une ligne donné
    
def get_next_steps(name_arret,ligne):
    next_step = []                                              #classe Arret
    liste_arret = get_path_regular(ligne)
    for ar in range(len(liste_arret)-1):
        if liste_arret[ar] == name_arret:
            next_step.append(liste_arret[ar + 1])
    return next_step


#==============================================================================
    
#methode general pour recuperer la ligne de bus sous forme d'une liste
def get_path_regular(lign):
    try:
        with open(lign, 'r', encoding = "utf-8") as f:
            content = f.read()
    except OSError:
        # 'File not found' error message.
        print("File not found")
        
    path_fromtxt = []
    
    splitted_content = content.split('\n\n')      #on split le contenu du txt
    path_fromtxt.append(splitted_content[0])    #on ajoute l'elemnt du txt dans une liste vide
    
    
    string_setup = ''.join(path_fromtxt)    #manipulation de la nouvelle liste en str pour pouvoir la split
    new_path = string_setup.split(' N ')    #split pour avoir la liste de tout les arret d'une ligne
    
    return new_path


def get_path_holidays(lign):
    file = open(lign, 'r', encoding = "utf-8")
    content = file.read()
    path_fromtxt = []
    
    splitted_content = content.split('\n\n')      #on split le contenu du txt
    path_fromtxt.append(splitted_content[3])    #on ajoute l'elemnt du txt dans une liste vide
    
    
    string_setup = ''.join(path_fromtxt)    #manipulation de la nouvelle liste en str pour pouvoir la split
    new_path = string_setup.split(' N ')    #split pour avoir la liste de tout les arret d'une ligne
    
    return new_path


#==============================================================================




