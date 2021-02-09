#!/usr/bin/python3
#-*-coding:utf-8-*-

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


#méthode pour recuperer la liste des horaires d'un arret
def get_liste_horaires(name_arret):
    reg_go = regular_date_go[name_arret]
    reg_back = regular_date_back[name_arret]
    hol_go = we_holidays_date_go[name_arret]
    hol_back = we_holidays_date_back[name_arret]
    return reg_go   #on récupère la liste d'un arret donné

print(get_liste_horaires('Vernod'))
    
def manip_heure





