class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade
        self.anterior = None
        self.proximoNo = None


class ListaDeProdutos:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_produto(self, nome, codigo, preco, quantidade):
        produto = Produto(nome, codigo, preco, quantidade)
        if self.head == None:
            self.head = produto
            self.tail = produto
        else:
            ultimo = self.tail
            produto.anterior = ultimo
            ultimo.proximoNo = produto
            self.tail = produto

    def remover_produto(self, nome):
        atual = self.head
        while atual.nome != nome:
            if atual.proximoNo == None:
                return print(f"O produto {nome} não está presente em estoque.")
            pai = atual
            atual = atual.proximoNo
        pai.proximoNo = atual.proximoNo

    def atualizar_produto(self, nome, preco, quantidade=""):
        prd = self.busca(nome)
        if quantidade != "":
            prd[0].preco = preco
            prd[0].quantidade = quantidade
        prd[0].preco = preco

    def listar_produtos(self):
        if self.head == None:
            return print("Não há nada no estoque!")
        atual = self.head
        while atual != None:
            print(
                f"O código {atual.codigo} pertence ao produto {atual.nome} que custa {atual.preco} e possui {atual.quantidade} un. em estoque."
            )
            atual = atual.proximoNo

    def busca(self, nome):
        if self.head == None:
            return print("Não há nada em estoque!")
        atual = self.head
        while atual.nome != nome:
            if atual.proximoNo == None:
                print(f"O produto {nome} não existe em estoque.")
            atual = atual.proximoNo
        return atual, (
            print(
                f"O produto {atual.nome} custa {atual.preco} e há {atual.quantidade} un. em estoque com o código {atual.codigo}"
            ),
        )


produtos = ListaDeProdutos()
produtos.add_produto("Cebola", "001", 3.99, 100)
produtos.add_produto("Tomate", "002", 8.99, 10)
produtos.add_produto("Laranja", "201", 6.99, 111)
produtos.add_produto("Banana", "451", 3.90, 1)

produtos.listar_produtos()

produtos.busca("Laranja")

produtos.atualizar_produto("Laranja", 7.0, 87)
produtos.busca("Laranja")

produtos.remover_produto("Banana")
produtos.listar_produtos()
