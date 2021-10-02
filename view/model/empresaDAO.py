import sqlite3

from controller.conexao import Conexao
from empresa import Empresa

class EmpresaDAO():
    def __init__(self):
        conexao = Conexao()
        self.__con = conexao.getConexao()
        self.__cur = None

    def listarEmpresas(self):
        empresas = []
        try:
            self.__cur = self.__con.cursor()
            sql = "SELECT * FROM empresa"

            for row in self.__cur.execute(sql):
                empresa = Empresa(row[0],row[1],row[2],row[3])
                empresas.append(empresa)

            return empresas

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def inserir(self,empresa):
        try:
            sql = "INSERT INTO empresa VALUES(?, ?, ?, ?)" 

            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, (empresa.id, empresa.nome, empresa.cnpj, empresa.imunizante))

            self.__con.commit()

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def altera(self,empresa):

        try:
            sql = "UPDATE empresa SET nome = (?), cnpj = (?), nome_imunizante = (?) WHERE id = (?);" 
        
            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, (empresa.nome, empresa.cnpj, empresa.imunizante, empresa.id))

            self.__con.commit()

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def busca(self,id):

        try:
            sql = "SELECT * FROM empresa WHERE id = (?)"
        
            self.__cur = self.__con.cursor()

            for row in self.__cur.execute(sql, (id,)):
                empresa = Empresa(row[0],row[1],row[2],row[3])

            return empresa

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()
    
    def excluir(self,id):
        try:

            sql = "DELETE FROM empresa WHERE id = (?)"

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
