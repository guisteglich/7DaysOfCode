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
            ultimo.proximoNo = produto
            self.tail = produto

    def remover_produto(self, nome):
        NotImplemented

    def atualizar_produto(self):
        NotImplemented

    def listar_produtos(self):
        NotImplemented

    def busca(self, nome):
        NotImplemented