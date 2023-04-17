# print("String")
# var1=1
# print("String {}".format(var1))
# input("Adauga o cifra")

# def functie_adunare(param1,):
#     print("print")
#     return param1
#
# functie_adunare(1)

def get_sum(a:int,b: int =3,c:int =3,*args)->int:
    suma =a+b+c
    diferenta=a-b-c
    for i in args:
        suma +=i
    return suma,diferenta

var1,var2 = get_sum(1,-3,-4,8,0,6,7,9,10)
print(suma)

#ctrl+p pentru a vedea cui ii este asignat parametrul
#nu se pune 'a' sau 'b'

