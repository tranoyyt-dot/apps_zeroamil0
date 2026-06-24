from cinema import Cinema

def test_adicionar_sessao():
    cinema = Cinema("CineMax", "Rua A, 123")
    sessao = type('Sessao', (object,), {'cinema': cinema, 'vagas': 100})()  # Mocking a Sessao object
    cinema.adicionar_sessao(sessao)
    assert cinema.quantidade_sessoes() == 1

test_adicionar_sessao()
