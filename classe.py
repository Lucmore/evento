class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"


class Evento:
    def __init__(self, nome, data, local):
        self.nome = nome
        self.data = data
        self.local = local
        self.participantes = []


    def adicionar_participante(self, pessoa):
        self.participantes.append(pessoa)

    def remover_participante(self, pessoa):
        self.participantes.remove(pessoa)

    def listar_participantes(self):
        for participante in self.participantes:
            print(participante)
               

    def __str__(self):
        return f"Evento: {self.nome}, Data: {self.data}, Local: {self.local}, Número de participantes: {len(self.participantes)}"
    


    
    
          
