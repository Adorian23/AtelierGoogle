variabila1 = 2
print(variabila1,'rand2')
def functie_1(a,b):
    variabila1 = a+b
    print(variabila1,'rand6')
    global msg
    msg='Hello'
    return variabila1

print(variabila1,'rand9')
suma =functie_1(1,2)
print(msg,'rand 14')
print(suma)
