import mysql.connector
from conexao import conectar

# Cliente

def criar_cliente(nome, email, cpf, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO cliente (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, cpf, senha)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente cadastrado com sucesso.")
    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:
            print("Erro: CPF ou email já cadastrado.")
        else:
            print("Erro ao cadastrar cliente:", e)
    cursor.close()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    for cliente in resultados:
        print(cliente)
    cursor.close()
    conexao.close()

def atualizar_cliente(id, novo_nome, novo_email, novo_cpf, nova_senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        UPDATE cliente
        SET nome = %s, email = %s, cpf = %s, senha = %s
        WHERE id = %s
    """
    valores = (novo_nome, novo_email, novo_cpf, nova_senha, id)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente atualizado com sucesso.")
    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:
            print("Erro: CPF ou email já cadastrado.")
        else:
            print("Erro ao atualizar cliente:", e)
    cursor.close()
    conexao.close()

def deletar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM cliente WHERE ID = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    print("Cliente deletado com sucesso.")
    cursor.close()
    conexao.close()

# Funcionário

def criar_funcionario(nome, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO funcionario (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Funcionário cadastrado com sucesso.")
    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:
            print("Erro: Email já cadastrado.")
        else:
            print("Erro ao cadastrar funcionário:", e)
    cursor.close()
    conexao.close()

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionario")
    resultados = cursor.fetchall()
    for funcionario in resultados:
        print(funcionario)
    cursor.close()
    conexao.close()

def atualizar_funcionario(id, novo_nome, novo_email, nova_senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        UPDATE funcionario
        SET nome = %s, email = %s, senha = %s
        WHERE id = %s
    """
    valores = (novo_nome, novo_email, nova_senha, id)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Funcionário atualizado com sucesso.")
    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:
            print("Erro: Email já cadastrado.")
        else:
            print("Erro ao atualizar funcionário:", e)
    cursor.close()
    conexao.close()

def deletar_funcionario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM funcionario WHERE ID = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    print("Funcionário deletado com sucesso.")
    cursor.close()
    conexao.close()

# Produto

from datetime import date;
def criar_produto(nome, estoque, valor):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO produto (nome, data, estoque, valor) VALUES (%s, %s, %s, %s)"

    data_criacao = date.today()
    valores = (nome, data_criacao, estoque, valor)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Produto cadastrado com sucesso.")
    except Exception as e:
        print("Erro ao cadastrar produto:", e)
    cursor.close()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    resultados = cursor.fetchall()
    for produto in resultados:
        print(produto)
    cursor.close()
    conexao.close()

def atualizar_produto(id, novo_nome, novo_estoque, novo_valor):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        UPDATE produto
        SET nome = %s, estoque = %s, valor = %s
        WHERE id = %s
    """
    valores = (novo_nome, novo_estoque, novo_valor, id)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Produto atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar produto:", e)
    cursor.close()
    conexao.close()

def deletar_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM produto WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    print("Produto deletado com sucesso.")
    cursor.close()
    conexao.close()

# Menu

if __name__ == "__main__":
    while True:
        print("\n--- MENU CLIENTE ---")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("\n--- MENU FUNCIONARIO ---")
        print("5 - Cadastrar funcionário")
        print("6 - Listar funcionários")
        print("7 - Atualizar funcionário")
        print("8 - Deletar funcionário")
        print("\n--- MENU PRODUTO ---")
        print("9 - Cadastrar produto")
        print("10 - Listar produtos")
        print("11 - Atualizar produto")
        print("12 - Deletar produto")
        print("\n-----------------------")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            cpf = input("CPF: ")
            senha = input("Senha: ")
            criar_cliente(nome, email, cpf, senha)

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            id = input("ID do cliente a atualizar: ")
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            novo_cpf = input("Novo CPF: ")
            nova_senha = input("Nova senha: ")
            atualizar_cliente(id, novo_nome, novo_email, novo_cpf, nova_senha)

        elif opcao == "4":
            id = input("ID do cliente a deletar: ")
            deletar_cliente(id)

        elif opcao == "5":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            criar_funcionario(nome, email, senha)

        elif opcao == "6":
            listar_funcionarios()

        elif opcao == "7":
            id = input("ID do funcionário a atualizar: ")
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            nova_senha = input("Nova senha: ")
            atualizar_funcionario(id, novo_nome, novo_email, nova_senha)

        elif opcao == "8":
            id = input("ID do funcionário a deletar: ")
            deletar_funcionario(id)

        elif opcao == "9":
            nome = input("Nome do produto: ")
            estoque = int(input("Estoque: "))
            valor = float(input("Valor: "))
            criar_produto(nome, estoque, valor)

        elif opcao == "10":
            listar_produtos()

        elif opcao == "11":
            id = input("ID do produto a atualizar: ")
            novo_nome = input("Novo nome: ")
            novo_estoque = int(input("Novo estoque: "))
            novo_valor = float(input("Novo valor: "))
            atualizar_produto(id, novo_nome, novo_estoque, novo_valor)

        elif opcao == "12":
            id = input("ID do produto a deletar: ")
            deletar_produto(id)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
