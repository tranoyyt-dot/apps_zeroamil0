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
    conexao_b = conectar_banco()
    if conexao_b:
        cursor = conexao_b.cursor()
        sql = "SELECT NOME, status FROM atracao"
        try:
            resultado = cursor.fetchall(sql)
            cursor.execute(sql)
        except Error as erro:
            print(f"Erro ao cadastrar: {erro}")
    else:
        for atracao in resultado:
            print(f"{atracao[0]} - {atracao[1]}")
            except Error as erro:
            print(f"Erro ao consultar {erro}")
cadastrar_atracao()
lista_atracao()
