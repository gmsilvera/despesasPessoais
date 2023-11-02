import sqlite3

class BancoDeDados():
    #Construtor.
    def __init__(self):
        self.createTable()
    
    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('database.db')
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados.", error)
    #Criando duas tabelas com uma só função. 
    def createTable(self):
        self.abrirConexao()
        create_despesas_query = """CREATE TABLE IF NOT EXISTS despesas(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        dataDespesa TEXT NOT NULL,
        valor REAL NOT NULL,
        metodoDePagamento TEXT NOT NULL,
        descricao TEXT NOT NULL,
        statusDespesa TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_despesas_query)
            self.connection.commit()
            print("Tabela criada com sucesso.")
        except sqlite3.Error as error:
            print("Falha ao criar tabela.", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexao com sqlite foi fechada.")
    
    #Função para Inserir dados na tabela - DESPESAS.
    def insertDespesas(self, nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa):
        self.abrirConexao()
        insert_despesas_query = """INSERT INTO despesas (nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa) VALUES (?,?,?,?,?,?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_despesas_query, (nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa))
            self.connection.commit()
            print("Dados de despesa cadastrado com sucesso.")
        except sqlite3.Error as error:
            print("Falha ao cadastrar despesa.", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com sqlite foi fechada.")
    
    #Função para (selecionar todos os dados) nas tabelas.
    def selectData(self):
        self.abrirConexao()
        select_query = "SELECT * FROM despesas"
        despesa = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            despesa = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao retornar despesa.", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexao com o sqlite foi fechada")
        return despesa

    #Função Atualizar tabela - DESPESA.
    #A data da despesa não pode ser alterada.
    def updateDespesa(self, id, nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa):
        self.abrirConexao()
        update_despesa_query = """UPDATE despesas SET nome = ?, dataDespesa = ?, valor = ?, metodoDePagamento = ?, descricao = ?, statusDespesa = ? WHERE id = ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_despesa_query, (nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa, id))
            self.connection.commit()
            print("Despesa atualizado com sucesso")
        except sqlite3.Error as error:
            print('Falha ao atualizar despesa.', error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexao com o sqlite foi fechada")
    #Função para (deletar) dados na tabela - DESPESA.
    def deleteDespesa(self, ID):
        self.abrirConexao()
        delete_despesa_query = "DELETE FROM despesas WHERE ID = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_despesa_query,(ID,))
            self.connection.commit()
            print('Despesa deletado com sucesso')
        except sqlite3.Error as error:
            print("Falha ao deletar despesa.")
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print('A conexao com o sqlite foi fechada')