from classe import *


pessoa1 = Pessoa("João Silva", "joao.silva@example.com", "1234-5678"),
pessoa2 = Pessoa("Maria Souza", "maria.souza@example.com", "8765-4321"),
pessoa3 = Pessoa("Augusto Carrara", "agostinho.carrara@example.com", "3231-5732")

evento1 = Evento("Conferência de Tecnologia", "2024-08-15", "Centro de Convenções")
evento2 = Evento("Workshop de Python", "2024-09-10", "Sala de Conferências")

evento1.adicionar_participante(pessoa1)
evento2.adicionar_participante(pessoa2)

evento = Evento("Conferência de Tecnologia", "2024-08-15", "Centro de Convenções")
pessoa1 = Pessoa("João Silva", "joao.silva@example.com", "1234-5678")
pessoa2 = Pessoa("Maria Souza", "maria.souza@example.com", "8765-4321")

evento.adicionar_participante(pessoa1)
evento.adicionar_participante(pessoa2)

evento.listar_participantes()


