class Livro:
    def __init__(self, titulo, numPaginas):
        self.titulo = titulo
        self.numPaginas = numPaginas


class PilhaDeLivros:
    def __init__(self):
        # self.__capacidade = capacidade
        self.__topo = -1
        self.valores = []

    def push(self, titulo, numPaginas):
        livro = Livro(titulo, numPaginas)
        self.__topo += 1
        self.valores.append(livro)

    def pop(self):
        if self.__topo < 0:
            return print("Não há nada na pilha!")
        rmvd = self.valores.pop()
        self.__topo -= 1
        print(f"O livro {rmvd.titulo} foi removido da pilha.")

    def peek(self):
        if self.__topo < 0:
            return print("Não há livros na pilha!")
        return print(
            f"No topo da pilha está o livro {self.valores[self.__topo].titulo}"
        )


pilha = PilhaDeLivros()

pilha.push("A guerra dos tronos", 1256)
pilha.push("A fúria dos reis", 987)
pilha.peek()
pilha.pop()
pilha.peek()
pilha.push("A tormenta das espadas", 1287)
pilha.peek()
