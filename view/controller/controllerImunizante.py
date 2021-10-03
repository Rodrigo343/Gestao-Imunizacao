from .model.imunizante import Imunizante
from .model.imunizanteDAO import ImunizanteDAO
from .model.pessoaDAO import PessoaDAO

def adicionaImunizante(lote,id_estado,id_empresa):

    try:
        if lote == "" or  id_estado == "" or id_empresa == "":
            return False
        else:

            lote = int(lote) 
            imunizante = Imunizante(None, lote, int(id_estado), int(id_empresa))
            imunizanteDAO = ImunizanteDAO()
            imunizanteDAO.inserir(imunizante)
            imunizanteDAO.close()
            return True

    except:
        return False

def editaImunizante(id,lote,id_estado,id_empresa):

    try:
        if lote == "" or  id_estado == "" or id_empresa == "":
            return False
        else:
            lote = int(lote) 
            imunizante = Imunizante(int(id), lote, int(id_estado), int(id_empresa))
            
            imunizanteDAO = ImunizanteDAO()
            imunizanteDAO.altera(imunizante)
            imunizanteDAO.close()
            return True

    except:
        return False

def excluirImunizante(id):
    
    id = int(id)
    try:

        imunizanteDAO = ImunizanteDAO()
        pessoaDAO = PessoaDAO()
        imunizantePessoa = pessoaDAO.listarPessoas()
        for i in imunizantePessoa:
            if i.id_imunizante != None and int(i.id_imunizante) == id:
                return False

        imunizanteDAO.excluir(id)
        imunizanteDAO.close()
        return True

    except:
        return False

def listaImunizantes():
    imunizanteDAO = ImunizanteDAO()
    imunizantes = imunizanteDAO.listarImunizantes()
    imunizanteDAO.close()

    return imunizantes

def buscaImunizante(pesquisa):

    imunizanteDAO = ImunizanteDAO()
    imunizantes = imunizanteDAO.busca(pesquisa)
    imunizanteDAO.close()

    return imunizantes
        
