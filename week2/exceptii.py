a=input("Alegeti o valoare : ")
try:
    print(int(a))
except ValueError:
    print("S-a intalnit o eroare")
    a=input("Alegeti o alta valoare : ")
print("A trecut de blocul try-except")

# except Exception as e :
# print(e)

