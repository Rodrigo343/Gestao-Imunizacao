import sqlite3

from .util.conexao import Conexao
from .estado import Estado

class EstadoDAO():
    def __init__(self):
        conexao = Conexao()
        self.__con = conexao.getConexao()
        self.__cur = None

    def listarEstados(self):
        estados = []
        try:
            self.__cur = self.__con.cursor()
            sql = "SELECT * FROM uf;"

            for row in self.__cur.execute(sql):
                estado = Estado(row[0],row[1])
                estados.append(estado)

            return estados

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def close(self):
    
        try:
            self.__con.close()

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()
    
