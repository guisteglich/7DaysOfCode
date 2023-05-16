"""
paciente deve ter um nome, um número de identificação e o estado de saúde atual ]
permitir adicionar novos pacientes, remover pacientes e listar todos os pacientes em ordem de chegada
"""


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximoNo = None


class Paciente:
    def __init__(self, nome, id, estado):
        self.nome = nome
        self.id = id
        self.estado = estado
        self.proximoNo = None


class ListaDePacientes:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_paciente(self, nome, id, estado):
        paciente = Paciente(nome, id, estado)

        if self.head == None:
            self.head = paciente
            self.tail = paciente

        else:
            atual = self.head
            while atual.proximoNo != None:
                atual = atual.proximoNo
            atual.proximoNo = paciente  # type: ignore
            self.tail = paciente

        # Melhoria: usar tail para chegar no último elemento, evitando precisar percorrer a lista.

    def remove_paciente(self, nome):
        if self.head == None:
            return print(
                f"Não é possível remover o paciente {nome}, a lista está vazia!"
            )
        else:
            atual = self.head
            pai = self.head

            while atual.nome != nome: # type: ignore
                if atual.proximoNo == None:
                    return print(f"O paciente {nome} não está na lista!")
                pai = atual
                atual = atual.proximoNo # type: ignore
            
            if atual == self.tail:
                self.tail = pai
            pai.proximoNo = atual.proximoNo

    def listar_pacientes(self):
        if self.head == None:
            return print("Não há pacientes para ser listado!")
        atual = self.head
        while atual != None:
            print(f"O paciente {atual.nome} que possui o identificador {atual.id} está com o estado de saúde {atual.estado}.")
            atual = atual.proximoNo

pacientes = ListaDePacientes()

pacientes.add_paciente("Guilherme", "044", "Saudável")
pacientes.add_paciente("Geromel", "03", "Recuperação")

pacientes.listar_pacientes()
        
