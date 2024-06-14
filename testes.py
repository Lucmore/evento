from classe import *


def test_adicionar_participante():
    pessoa1 = Pessoa("João Silva", "joao.silva@example.com", "1234-5678"),
    pessoa2 = Pessoa("Maria Souza", "maria.souza@example.com", "8765-4321"),
    evento1 = Evento("Conferência de Tecnologia", "2024-08-15", "Centro de Convenções")
    evento1.adicionar_participante(pessoa1)
    evento1.adicionar_participante(pessoa2)
    
    assert len(evento1.participantes) == 2 
  

def test_nao_adicionar_participantes_duplicados():
    pessoa1 = Pessoa("João Silva", "joao.silva@example.com", "1234-5678")
    evento1 = Evento("Conferência de Tecnologia", "2024-08-15", "Centro de Convenções")
    evento1.adicionar_participante(pessoa1)

    
    assert len(evento1.participantes) == 1
   
  
        
def test_remover_participante():
    pessoa1 = Pessoa("João Silva", "joao.silva@example.com", "1234-5678")
    evento1 = Evento("Conferência de Tecnologia", "2024-08-15", "Centro de Convenções")
    evento1.adicionar_participante(pessoa1)
    evento1.remover_participante(pessoa1)
    
    assert len(evento1.participantes) == 0



def test_str_pessoa():
    pessoa1 = Pessoa("João Silva", "joao.silva@example.com", "1234-5678")
    
    assert pessoa1.__str__() == "Nome: João Silva, Email: joao.silva@example.com, Telefone: 1234-5678"

def test_str_evento():
    evento1 = Evento("Conferência de Tecnologia", "2024-08-15", "Centro de Convenções")
    
    
    assert evento1.__str__() == "Evento: Conferência de Tecnologia, Data: 2024-08-15, Local: Centro de Convenções, Número de participantes: 0"
 
    
  
        
      

