lista_operatii=['+','-','*','/']

while True:
    operator_1 = input("Adauga primul operator : ")
    operator_2 = input("Adauga al doilea operator : ")
    operatie = input("Alege operatia pe care doresti sa o executi : ")

    if not operator_1.isdigit() or not operator_2.isdigit():
        print("Operatorii trebuie sa fie cifre!")
        continue
    while operatie in ['C','c']:
        print("Ai sters valorile !")
        operator_1 = input("Adauga primul operator : ")
        operator_2 = input("Adauga al doilea operator : ")
        operatie = input("Alege operatia pe care doresti sa o executi : ")

    if operatie not in lista_operatii:
        print("Operatia aleasa nu este valida!")
        continue


    if int(operator_2)==0 and operatie =="/":
        print("Impartirea la 0 nu este permisa")
        continue

    if operatie =='+':
        print(f"Suma celor doua numere {operator_1}+{operator_2} este {int(operator_1)+int(operator_2)}")
    elif operatie =='-':
        print(f"Diferenta celor doua numere {operator_1}-{operator_2} este {int(operator_1)-int(operator_2)}")
    elif operatie =='*':
        print(f"Produsul celor doua numere {operator_1}*{operator_2} este {int(operator_1)*int(operator_2)}")
    elif operatie =='/':
        print(f"Impartirea celor doua numere {operator_1}/{operator_2} este {int(operator_1)/int(operator_2)}")

    else:
        print("Ceva nu e bine")
    break

