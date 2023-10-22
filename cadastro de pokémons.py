# pip install psycopg2

import psycopg2
from psycopg2 import sql

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="seu_banco_de_dados",
    user="seu_usuario",
    password="sua_senha",
    host="seu_host"
)

# Criar um cursor para executar operações no banco de dados
cur = conn.cursor()

# Função para adicionar um novo Pokémon
def adicionar_pokemon():
    nome = input("Nome do Pokémon: ")
    tipo = input("Tipo: ")
    nivel = int(input("Nível: "))
    hp = int(input("HP: "))
    ataque = int(input("Ataque: "))
    defesa = int(input("Defesa: "))
    natureza = input("Natureza: ")
    sexo = input("Sexo: ")

    cur.execute(
        "INSERT INTO pokemons (nome, tipo, nivel, hp, ataque, defesa, natureza, sexo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (nome, tipo, nivel, hp, ataque, defesa, natureza, sexo)
    )
    conn.commit()
    print("Pokémon adicionado com sucesso!")

# Função para listar todos os Pokémons
def listar_pokemons():
    cur.execute("SELECT * FROM pokemons")
    pokemons = cur.fetchall()
    for pokemon in pokemons:
        print(pokemon)

# Função para atualizar um Pokémon existente
def atualizar_pokemon():
    id_pokemon = int(input("ID do Pokémon que deseja atualizar: "))
    novo_nivel = int(input("Novo nível: "))
    cur.execute(
        "UPDATE pokemons SET nivel = %s WHERE id = %s",
        (novo_nivel, id_pokemon)
    )
    conn.commit()
    print("Pokémon atualizado com sucesso!")

# Função para remover um Pokémon
def remover_pokemon():
    id_pokemon = int(input("ID do Pokémon que deseja remover: "))
    cur.execute(
        "DELETE FROM pokemons WHERE id = %s",
        (id_pokemon,)
    )
    conn.commit()
    print("Pokémon removido com sucesso!")

# Menu principal
while True:
    print("\nMenu de Cadastro de Pokémons")
    print("1. Adicionar Pokémon")
    print("2. Listar Pokémons")
    print("3. Atualizar Pokémon")
    print("4. Remover Pokémon")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_pokemon()
    elif escolha == "2":
        listar_pokemons()
    elif escolha == "3":
        atualizar_pokemon()
    elif escolha == "4":
        remover_pokemon()
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechar a conexão com o banco de dados
cur.close()
conn.close()
