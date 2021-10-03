class Estado():
    
    def __init__(self, id = None, nome = None):
        self.id = id
        self.nome = nome
         
    @property  
    def id(self):
        return self.__id
    
    @id.setter  
    def id(self, id):
        self.__id = id

    @property  
    def nome(self):
        return self.__nome
    
    @nome.setter  
    def nome(self, nome):
        self.__nome = nome
    
    def __str__(self):        
        return " Id: {0}\n Nome: {1}".format(self.id, self.nome)