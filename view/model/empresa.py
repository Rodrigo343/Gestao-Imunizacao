class Empresa():
    
    def __init__(self, id = None, nome = None, cnpj = None, imunizante = None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.imunizante = imunizante
         
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

    @property  
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter  
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property  
    def imunizante(self):
        return self.__imunizante
    
    @imunizante.setter  
    def imunizante(self, imunizante):
        self.__imunizante = imunizante
    
    def __str__(self):        
        return " Id: {0}\n Nome: {1}\n CNPJ: {2}\n Imunizante: {3}".format(self.id, self.nome, self.cnpj, self.imunizante)