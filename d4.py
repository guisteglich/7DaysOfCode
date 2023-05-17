"""
Nesse desafio decidi por utilizar as ferramentas nativas do python com listas para implementar a fila
Ou seja, append e pop para enfileirar e desenfileirar respectivamente.
"""


class Pedido:
    def __init__(self, numero, nomeCliente, items, valor):
        self.numero = numero
        self.nomeCliente = nomeCliente
        self.items = items
        self.valor = valor


class FilaDePedidos:
    def __init__(self):
        self.valores = []

    def enfileirar(self, pedido):
        self.valores.append(pedido)

    def desenfileirar(self):
        if len(self.valores) < 1:
            return print("Não há nada na fila!")
        pedido_atendido = self.valores.pop(0)
        return print(
            f"O pedido {pedido_atendido.numero} do cliente {pedido_atendido.nomeCliente} com os items {pedido_atendido.items} começou a ser preparado."
        )


pedido1 = Pedido(1, "Guilherme", ["hamburguer"], 10.99)
pedido2 = Pedido(2, "Geromel", ["hamburguer", "pizza"], 25.99)
pedido3 = Pedido(3, "Guilherme", ["coca zero"], 4.99)

fila = FilaDePedidos()

fila.enfileirar(pedido1)
fila.enfileirar(pedido2)
fila.enfileirar(pedido3)

fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
