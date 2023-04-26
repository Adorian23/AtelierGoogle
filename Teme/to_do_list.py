import json
with open("categorii.txt",'r') as f:
    categorii_disponibile = f.read().splitlines()


to_do_list = {'task': [],
              'data_limita': [],
              'ora' : [],
              'persoana_responsabila': [],
              'categorie': []}
while True:
        valoare_task = input('Introduceti task-ul :')
        valoare_data = input('Introduceti data limita : ')
        valoare_ora = input('Introduceti ora: ')
        valoare_persoana = input('Introduceti persoana responsabila : ')
        valoare_categorie = input('Introduceti categoria : ')

        to_do_list['task'].append(valoare_task)
        to_do_list['data_limita'].append(valoare_data)
        to_do_list['ora'].append(valoare_ora)
        to_do_list['persoana_responsabila'].append(valoare_persoana)
        if valoare_categorie.lower() not in categorii_disponibile:
            print(' !!EROARE !! Categoria nu este disponibila')
            break
        else:
            to_do_list['categorie'].append(valoare_categorie)

        with open("to_do_list.json", "w") as f:
            json.dump(to_do_list, f)
        raspuns= input('Doresti sa mai adaugi date noi? ')
        if raspuns.lower()=='da':
            continue
        else:
            break








