import random

while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    soma = dado1 + dado2 + dado3
    print(f"\n1º dado: {dado1}")
    print(f"2º dado: {dado2}")
    print(f"3º dado: {dado3}")
    print(f"Soma total: {soma}")

    if soma < 6:
        print("Atingido!")
        
    elif soma > 6 and soma < 12:
        print("Esquiva com sucesso!")
        
    elif soma > 12 and soma < 18:
        print("Esquiva e possibilidade de Contra-ataque!")

    else:
        print("Resultado máximo!")

    continuar = input("\nDeseja rolar novamente? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando o programa...")
        break