import sqlite3

from controller.conexao import Conexao
from pessoa import Pessoa

class PessoaDAO():
    def __init__(self):
        conexao = Conexao()
        self.__con = conexao.getConexao()
        self.__cur = None

    def listarPessoas(self):
        pessoas = []
        try:
            self.__cur = self.__con.cursor()
            sql = "SELECT * FROM pessoa"

            for row in self.__cur.execute(sql):
                pessoa = Pessoa(row[0],row[1],row[2],row[3],row[4])
                pessoas.append(pessoa)

            return pessoas

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def inserir(self,pessoa):
        try:
            sql = "INSERT INTO pessoa VALUES(?, ?, ?, ?, ?)" 
        
            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, (pessoa.id, pessoa.nome, pessoa.cpf, pessoa.doses, pessoa.id_imunizante))

            self.__con.commit()
        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def altera(self,pessoa):
        try:
            sql = "UPDATE pessoa SET nome = (?), cpf = (?), doses = (?), id_imunizante = (?) WHERE id = (?);" 
        
            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, ( pessoa.nome, pessoa.cpf, pessoa.doses, pessoa.id_imunizante, pessoa.id))

            self.__con.commit()
        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def busca(self,id):
        try:
            sql = "SELECT * FROM pessoa WHERE id = (?)"
        
            self.__cur = self.__con.cursor()

            for row in self.__cur.execute(sql, (id,)):
                pessoa = Pessoa(row[0],row[1],row[2],row[3])

            return pessoa
        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()
    
    def excluir(self,id):
        try:
            sql = "DELETE FROM pessoa WHERE id = (?)"
        
            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, (id,))

            self.__con.commit()
        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def close(self):
        try:
            self.__con.close()
        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()


    
