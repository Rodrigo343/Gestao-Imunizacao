class Pessoa():
    
    def __init__(self, id = None, nome = None, cpf = None, doses = None, id_imunizante = None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.doses = doses
        self.id_imunizante = id_imunizante

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
    def cpf(self):
        return self.__cpf
    
    @cpf.setter  
    def cpf(self, cpf):
        self.__cpf = cpf

    @property  
    def doses(self):
        return self.__doses
    
    @doses.setter  
    def doses(self, doses):
        self.__doses = doses

    @property  
    def id_imunizante(self):
        return self.__id_imunizante
    
    @id_imunizante.setter  
    def id_imunizante(self, id_imunizante):
        self.__id_imunizante = id_imunizante
    
    def __str__(self):        
        return "Id:{0}\n nome:{1}\n cpf:{2}\n dose: {3}\n imunizante:{4}".format(self.id, self.nome, self.cpf, self.doses, self.id_imunizante)