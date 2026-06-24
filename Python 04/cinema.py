class Cinema:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.sessoes = []

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)
        if not sessao.cinema:
            raise ValueError("Sessão inválida.")
        
    def quantidade_sessoes(self):
        return len(self.sessoes)
        
    def comprar_ingresso(self, sessao, quantidade):
        if sessao not in self.sessoes:
            raise ValueError("Sessão não encontrada.")
        if quantidade <= 0:
            raise ValueError("Quantidade inválida.")
        if sessao.vagas < quantidade:
            raise ValueError("Não há vagas suficientes.")
        sessao.vagas -= quantidade