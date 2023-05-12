'''
#7DaysOfCode.
'''

class ListaDeCompras:
    def __init__(self):
        self.items = []
        self.quantidades = []

    def adicionar_item(self, item, quantidades):
        if quantidades <= 0:
            return print("Somente pode ser adicionado 1 ou mais items, valor inválido!")
        else:
            self.items.append(item)
            self.quantidades.append(quantidades)

            return print(f"Inserido {quantidades} items do produto {item} no estoque")

    def remover_item(self, item):
        indx = self.items.index(item)
        self.items.pop(indx)
        self.quantidades.pop(indx)

        return print(f"Removido o item {item}")

    def listar_itens(self):
        for indx, _ in enumerate(self.items):
            print(
                f"{self.items[indx]} com {self.quantidades[indx]} unidades em estoque"
            )


compras = ListaDeCompras()

compras.adicionar_item("Cebola", 20)
compras.adicionar_item("Tomate", 100)
compras.adicionar_item("Pão de forma", 2)
compras.adicionar_item("Feijão", 12)

compras.remover_item("Tomate")

compras.listar_itens()