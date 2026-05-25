lista = []
dicionario = {}

girias_br={
    "gambiarra": "solução imporvisada", "treta": "intendimento pessoal",
    "barbaridade": "ação bruta/mal", "sabor": "pseudobjeto"}
alimentos=dict(
    goiaba="frutas", abobora="legume", grao="feijao")
capitais={
    "Brasil": "Brasília", "Russia": "Moscou",
    "Bolivia": "La Paz", "Italia": "Roma"}
print(capitais["Bolivia"])
capitais["China"]="Xangai"  #adicionar
capitais["China"]="Pequim" #alterar
del capitais["Italia"] #remover
capitais["Laos"]="Vienciana"
print(capitais)
print('='*35)
print(capitais.get("Alemanha"))#Itens inexistentes
paises = capitais.key()
cidades = capitais.values()
print(paises)
print(cidades)
#alterar e percorrer
for pais in capitais:
    print(f"Bem-Vindo ao {pais}")
for pais, cidade in capitais.items():
    print(f"{cidades} é a capital de {pais}")

npc= {
    'nome':'Bouldor',
    'mensagem':'O senhor gostaria de arma ou escudo?',
    'itens': {
        'espada': 100,
        'escudo': 80,
        'adaga': 90
    }
}
