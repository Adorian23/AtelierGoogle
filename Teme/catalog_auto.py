
class Masina:
    def __init__(self,marca,tip):
        self.marca=marca
        self.tip=tip

    def met_culoare(self,culoare):
        self.culoare=culoare

    def AfisareCuloare(self):
        print(self.culoare)

class Interior(Masina):
    def __init__(self, marca, tip, scaune_incalzite):
        super().__init__(marca, tip)
        self.scaune_incalzite = scaune_incalzite

class Lumini(Masina):
    def __init__(self, marca, tip, Blocuri_Optice_LED):
        super().__init__(marca, tip)
        self.Blocuri_Optice_LED = Blocuri_Optice_LED


masina_ar =Interior(marca='ARO', tip='M461',scaune_incalzite='Nu')
masina_ar.met_culoare('rosu')

print('Marca:', masina_ar.marca)
print('Tip:', masina_ar.tip)
print('Scaune incalzite:', masina_ar.scaune_incalzite)
masina_ar.AfisareCuloare()



masina_dacia = Lumini(marca='Dacia', tip='1310', Blocuri_Optice_LED='Nu')
masina_dacia.met_culoare('negru')
print('Marca:', masina_dacia.marca)
print('Tip:', masina_dacia.tip)
print('Blocuri Optice LED:', masina_dacia.Blocuri_Optice_LED)
masina_dacia.AfisareCuloare()
