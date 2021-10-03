from .model.pessoa import Pessoa
from .model.pessoaDAO import PessoaDAO

def adicionaPessoa(nome, cpf,doses, id_imunizante):

    try:
        cpf = cpf.replace("-","")
        cpf = cpf.replace(".","")
        if nome == "" or  len(cpf) !=11 or doses == "":
            return False
        else:
            if id_imunizante == 0:
                id_imunizante = None
            cpf = int(cpf) 
            doses = int(doses) 
            pessoa = Pessoa(None, nome, int(cpf), int(doses), int(id_imunizante))
            pessoaDAO = PessoaDAO()
            pessoaDAO.inserir(pessoa)
            pessoaDAO.close()
            return True

    except:
        return False

def editaPessoa(id,nome, cpf,doses, id_imunizante):
    
    try:
        cpf = cpf.replace("-","")
        cpf = cpf.replace(".","")
        if id =="" or nome == "" or  len(cpf) !=11 or doses == "":
            return False
        else:
            if id_imunizante == 0:
                id_imunizante = None
            pessoa = Pessoa(int(id), nome, int(cpf), int(doses), int(id_imunizante))
            pessoaDAO = PessoaDAO()
            pessoaDAO.altera(pessoa)
            pessoaDAO.close()
            return True

    except:
        return False

def excluirPessoa(id):
    
    id = int(id)
    try:
        pessoa = Pessoa(id)
        pessoaDAO = PessoaDAO()
        pessoaDAO.excluir(pessoa.id)
        pessoaDAO.close()
        return True

    except:
        return False
        
def listaPessoas():
    pessoaDAO = PessoaDAO()
    pessoas = pessoaDAO.listarPessoas()
    pessoaDAO.close()

    return pessoas

def buscaPessoa(pesquisa):
    pessoaDAO = PessoaDAO()
    pessoas = pessoaDAO.busca(pesquisa)
    pessoaDAO.close()

    return pessoas