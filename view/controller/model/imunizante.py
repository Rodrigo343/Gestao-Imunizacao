class Imunizante():
    
    def __init__(self, id = None, lote = None, id_estado = None, id_empresa = None):
        self.id = id
        self.lote = lote
        self.id_estado = id_estado
        self.id_empresa = id_empresa
         
    @property  
    def id(self):
        return self.__id
    
    @id.setter  
    def id(self, id):
        self.__id = id

    @property  
    def lote(self):
        return self.__lote
    
    @lote.setter  
    def lote(self, lote):
        self.__lote = lote

    @property  
    def id_estado(self):
        return self.__id_uf
    
    @id_estado.setter  
    def id_estado(self, id_estado):
        self.__id_uf = id_estado

    @property  
    def id_empresa(self):
        return self.__id_empresa
    
    @id_empresa.setter  
    def id_empresa(self, id_empresa):
        self.__id_empresa = id_empresa
    
    def __str__(self):        
        return "Id:{0}\n Lote:{1}\n Cidade:{2}\n Empresa: {3}".format(self.id, self.lote, self.id_estado, self.id_empresa)