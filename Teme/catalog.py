class Catalog:
    def __init__(self,nume,prenume):
        self.nume=nume
        self.prenume=prenume
        self.materii={}
        self.absente=absente=0

    def absente(self):
        absente+=1

    def stergere(self,nr_absente):
        if self.absente - nr_absente< 0:
            self.absente = 0
        else:
            self.absente -= nr_absente

    def __str__(self):
        return f"{self.nume} {self.prenume} are {self.absente} absente."



class Extensie1(Catalog):
    def adauga_materie(self, nume_materie, note_materie):
        self.materii[nume_materie] = [nr for nr in note_materie if isinstance(nr, (int, float))]

    def afiseaza_materii(self):
        print(f"Lista de materii pentru {self.nume} {self.prenume}:")
        for materie in self.materii.keys():
            print(f"- {materie}")

    def afiseaza_note(self):
        for materie, note in self.materii.items():
            nr_note = len(note)
            if nr_note > 0:
                suma_note = sum(note)
                media = suma_note / nr_note
                print(f"{materie}: {note} - media: {media:.2f}")
            else:
                print(f"{materie}: fără note")


