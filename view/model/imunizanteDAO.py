import sqlite3

from controller.conexao import Conexao
from imunizante import Imunizante

class ImunizanteDAO():
    def __init__(self):
        conexao = Conexao()
        self.__con = conexao.getConexao()
        self.__cur = None

    def listarImunizantes(self):
        imunizantes = []
        try:
            self.__cur = self.__con.cursor()
            sql = "SELECT * FROM imunizante"

            for row in self.__cur.execute(sql):
                imunizante = Imunizante(row[0],row[1],row[2],row[3])
                imunizantes.append(imunizante)

            return imunizantes

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def inserir(self,imunizante):
        try:

            sql = "INSERT INTO imunizante VALUES(?, ?, ?, ?)" 
        
            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, (imunizante.id, imunizante.lote, imunizante.id_cidade, imunizante.id_empresa))

            self.__con.commit()

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def altera(self,imunizante):
        try:

            sql = "UPDATE imunizante SET lote = (?), id_cidade = (?), id_empresa = (?) WHERE id = (?);" 
        
            self.__cur = self.__con.cursor()

            self.__cur.execute(sql, (imunizante.lote, imunizante.id_cidade, imunizante.id_empresa, imunizante.id))

            self.__con.commit()

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()

    def busca(self,id):
        try:

            sql = "SELECT * FROM imunizante WHERE id = (?)"
        
            self.__cur = self.__con.cursor()

            for row in self.__cur.execute(sql, (id,)):
                imunizante = Imunizante(row[0],row[1],row[2],row[3])

            return imunizante

        except Exception or sqlite3.DatabaseError:
            sqlite3.enable_callback_tracebacks()
    
    def excluir(self,id):
        try:

            sql = "DELETE FROM imunizante WHERE id = (?)"
        
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


if __name__ == '__main__':
    imunizanteDAO = ImunizanteDAO()
    
    imu = Imunizante(1, 200,1,1)

    imunizanteDAO.altera(imu)