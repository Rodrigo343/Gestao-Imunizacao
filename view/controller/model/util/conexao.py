import sqlite3

class Conexao:

    def getConexao(self):    
        try:
            con = sqlite3.connect("gestao_imunizacao.db")
            return con
        
        except Exception as erro:
            print(erro)
