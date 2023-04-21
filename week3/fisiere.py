"""
r- citim,nu adaugam.Daca fisierul nu exista apare eroare
w-scriem,daca fisierul nu exista il adauga,daca exista ceva scris in fisier il rescrie
a- scriem,daca exista ceva scris in fisier il adauga pe urmatorul rand,nu rescrie,nu apare eroare daca fisierul nu exista
r+ - scriere,citire.Daca fisierul nu exista,apare eroare
"""
# file = open('data2.txt',"r+")
# file.write('Ceva')
# file.close()
#
# file = open('data1.txt','r')
# try:
#     file.write('hello')
# finally:
#     file.close()

with open('data.txt','w') as file:
    file.write('ce faci ')