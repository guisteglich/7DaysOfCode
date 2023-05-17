class Jogador:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao


class Jogo:
    def __init__(self):
        self.dict = {}

    def add_jogador(self, nome):
        self.dict[nome] = 0
        return print(f"Adicionado o jogador {nome} ao game.")

    def atualizar_pontuacao(self, nome, pontuacao):
        if nome not in self.dict:
            return print(f"O jogador {nome} Não está no game.")
        self.dict[nome] += pontuacao
        return print(
            f"Atualizada a pontuação do jogador {nome} para {self.dict[nome]} pts."
        )

    def remover_jogador(self, nome):
        if nome not in self.dict:
            return print(f"O jogador {nome} Não está no game.")
        self.dict.pop(nome)
        return print(f"O jogador {nome} foi removido do jogo!")

    def listar_jogadores(self):
        if len(self.dict) < 1:
            return print("Não há jogadores cadastrados no game.")
        ranking = sorted(self.dict.items(), key=lambda x: x[1], reverse=True)
        for chave, valor in ranking:
            print(f"O jogador {chave} possui {valor} pts.")

    def vencedor(self):
        if len(self.dict) < 1:
            return print("Não há jogadores cadastrados no game.")
        ranking = sorted(self.dict.items(), key=lambda x: x[1], reverse=True)
        return print(f"O vencedor é o {ranking[0][0]} com {ranking[0][1]} pts.")


jogo = Jogo()

jogo.add_jogador("Guilherme")
jogo.add_jogador("Geromel")
jogo.add_jogador("Pedro")
jogo.add_jogador("Walter")
jogo.add_jogador("Renato")
jogo.add_jogador("Marcelo")
jogo.add_jogador("Douglas")
jogo.add_jogador("Luan")

jogo.atualizar_pontuacao("Guilherme", 90)
jogo.atualizar_pontuacao("Geromel", 120)
jogo.atualizar_pontuacao("Pedro", 85)
jogo.atualizar_pontuacao("Walter", 50)
jogo.atualizar_pontuacao("Renato", 10)
jogo.atualizar_pontuacao("Pedro", 20)
jogo.remover_jogador("Guilherme")

jogo.listar_jogadores()

jogo.vencedor()
