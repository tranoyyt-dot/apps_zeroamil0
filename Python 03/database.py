import mysql.connector
from mysql.connector import Error

def conectar_banco():
    """Estabelece Conexão"""
    try: # tenta conectar
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="parque_cidade"
        )
        if conexao.is_connected():
            print("conectou")
    except Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None

def cadastrar_atracao():
    """Inserir novas atrações no parque"""
    conexao_a = conectar_banco()
    if conexao_a:
        cursor = conexao_a.cursor()
        nome = input("Nome da Atração:")
        status = input("Status (funcionamento/manutenção)")
        sql = "INSERT INTO atracoes (nome, status) VALUES (%s, %s)"
        dados = (nome, status)
        try:
            cursor.execute(sql, dados)
            conexao_a.commit()
            print(f"{nome} cadastrado com sucesso!")
        except Error as erro:
            print(f"Erro ao cadastrar: {erro}")
        finally:
            cursor.close()
            conexao_a.close()

def listar_atracoes():
    """Listar as atrações"""
    conexao_c = conectar_banco()
    if conexao_c:
        cursor = conexao_c.cursor()
        sql = "SELECT NOME, status FROM atracao"
        try:
            resultado = cursor.fetchall(sql)
            cursor.execute(sql)
            if not resultado:
                print("Nenhum resultado encontrado")
            else:
                for atracao in resultado:
                    print(f"{atracao[0]} - {atracao[1]}")
        except Error as erro:
            print(f"Erro ao consultar {erro}")

def listar_atracoes_by_status():
    """Listar as atrações por status"""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        status_buscar = input("Digite o status: ")
        sql = "SELECT nome, status FROM  atracoes WHERE status = %s"
        dados = (status_buscar,)
        try:
            cursor.execute(sql, dados)
            resultados = cursor.fetchall()
            if not resultados:
                print("Nenhuma atração com esse status")
            else:
                for atracao in resultados:
                    print(f"Atração: {atracao[0]}")
        except Error as erro:
            print(f"Erro ao buscar: {erro}")
        finally:
            cursor.close()
            conexao.close()

def cadastrar_bilhetes():
    conexao_b = conectar_banco()
    if conexao_b:
        cursor = conexao_b.cursor()
        nome = input("Digite o nome: ")
        valor = input("Custo do bilhete: ")
        sql = "INSERT INTO bilheteria (nome, valor) VALUES (%s, %s)"
        dados = (nome, valor)
        try:
            cursor.execute(sql, dados)
            conexao_b.commit()
            print(f"{nome} cadastrado com sucesso!")
        except Error as erro:
            print(f"Erro ao cadastrar: {erro}")
        finally:
            cursor.close()
            conexao_b.close()

def listar_bilheteria():
    """Listar os bilhetes"""
    conexao_d = conectar_banco()
    if conexao_d:
        cursor = conexao_d.cursor()
        sql = "SELECT NOME, status FROM bilheteria"
        try:
            resultado = cursor.fetchall(sql)
            cursor.execute(sql)
            if not resultado:
                print("Nenhum resultado encontrado")
            else:
                for atracao in resultado:
                    print(f"{atracao[0]} - {atracao[1]}")
        except Error as erro:
            print(f"Erro ao consultar {erro}")



cadastrar_bilhetes()
cadastrar_atracao()
listar_bilheteria()
listar_atracoes()

while True:
    opcao = input("Escolha uma opção: ")
    match opcao:
        case '1':
            cadastrar_atracao()
        case '2':
            cadastrar_bilhetes()
        case '3':
            listar_atracoes()
        case '4':
            pass
        case '0':
            break