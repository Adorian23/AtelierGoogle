import random
from lista_cuvinte import cuvinte_de_ghicit as lista_cuvinte

cuvant = random.choice(lista_cuvinte).lower()
cuvant_initial=list(cuvant)
""" 
o _ o _ _ _ o _ _
"""
""" litere mici lowercase
    7 incercari
    daca a mai incercat litera nu ii ia din vieti
"""


for index,value in enumerate(cuvant):
    print(cuvant_initial[0],cuvant_initial[-1])
    if cuvant_initial[0] != value and cuvant_initial[-1] != value:
        cuvant_initial[index] = '_'
print("".join(cuvant_initial))
numar_incercari = 1
set_litere_incercate = set()
while numar_incercari <= 3:
    litera_incercata= input("Alege o litera : ").lower()
    if litera_incercata in cuvant_initial:
        print("Litera deja este afisata pe ecran !")
    elif litera_incercata in cuvant:
        for index,value in enumerate(cuvant):
            if litera_incercata == value:
                 cuvant_initial[index] = litera_incercata
    else:
            set_litere_incercate.add(litera_incercata)
            if litera_incercata not in set_litere_incercate:
                numar_incercari +=1
                print(set_litere_incercate)
            if numar_incercari == 3:
                print(f"Imi pare rau dar ai pierdut ! Cuvantul era {cuvant} ")
                break
            print(f"Atentie! Mai ai {3 - numar_incercari} incercari .Ai mai incercat aceasta litera ! Literele incercate sunt {','.join(set_litere_incercate)}")
    if '_' not in cuvant_initial:
        print("Ai castigat ! ")
        break

    print("".join(cuvant_initial))
