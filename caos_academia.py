import random

class Academia:
    def __init__(self):
        self.halteres = [_ for _ in range(10, 37) if _ % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar()
    
    def reiniciar(self):
        self.porta_halteres = {_:_ for _ in self.halteres}
    
    def disponiveis(self):
        return [_ for _ in self.porta_halteres.values() if _ != 0]
    
    def espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]
    
    def pega_halt(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_pos = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_pos] = 0
        return peso
    
    def devolve_halt(self, halt_pos, peso):
        self.porta_halteres[halt_pos] = peso
    
    def caos(self):
        valor_caos = [i for i,j in self.porta_halteres.items() if i != j]
        return len(valor_caos)/len(self.porta_halteres)
    
class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1 - organizado | 2 - desorganizado
        self.academia = academia
        self.peso = 0

    def inicia_treino(self):
        lista_peso = self.academia.disponiveis()
        if lista_peso:
            self.peso = random.choice(lista_peso)
            self.academia.pega_halt(self.peso)
        else:
            academia.reiniciar()
    
    def finaliza_treino(self):
        lista_peso = self.academia.disponiveis()
        if lista_peso:
            if self.tipo == 1:
                if self.peso in lista_peso:
                    self.academia.devolve_halt(self.peso, self.peso)
                else:
                    halt_pos = random.choice(lista_peso)
                    self.academia.devolve_halt(halt_pos, self.peso)
            elif self.tipo == 2:
                halt_pos = random.choice(lista_peso)
                self.academia.devolve_halt(halt_pos, self.peso)
            self.peso = 0
        else:
            academia.reiniciar()

academia = Academia()

usuarios = [Usuario(1, academia) for _ in range(10)]
usuarios += [Usuario(2, academia)]

lista_caos = []
for k in range(50):
    academia.reiniciar()
    for _ in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.inicia_treino()
        for user in usuarios:
            user.finaliza_treino()
    lista_caos += [academia.caos()]

for u in usuarios:
    print(u.tipo)
print("\n")
print(lista_caos)
print("\n")
print(academia.porta_halteres)