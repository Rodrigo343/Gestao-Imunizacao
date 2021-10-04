from .model.empresa import Empresa
from .model.empresaDAO import EmpresaDAO
from .model.imunizanteDAO import ImunizanteDAO

def adicionaEmpresa(nome, cnpj, nomeImunizante):

    try:
        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace(".", "")

        if len(cnpj) != 11 or  nome == "" or nomeImunizante == "":
            return False
        else:

            empresa = Empresa(None, nome, int(cnpj), nomeImunizante)
            empresaDAO = EmpresaDAO()
            empresaDAO.inserir(empresa)
            empresaDAO.close()
            return True

    except:
        return False

def editaEmpresa(id, nome, cnpj, nomeImunizante):
    
    try:
        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace(".", "")

        if len(cnpj) != 11 or  nome == "" or nomeImunizante == "" or id == "":
            return False
        else:

            empresa = Empresa(int(id), nome, int(cnpj), nomeImunizante)
            empresaDAO = EmpresaDAO()
            empresaDAO.altera(empresa)
            empresaDAO.close()
            return True

    except:
        return False

def excluirEmpresa(id):
    
    id = int(id)
    try:
        empresaDAO = EmpresaDAO()
        imunizanteDAO = ImunizanteDAO()
        imunizanteEmpresa = imunizanteDAO.listarImunizantes()
        for i in imunizanteEmpresa:
            if i.id_empresa == id:
                return False

        empresaDAO.excluir(id)
        empresaDAO.close()
        return True

    except:
        return False

def listaEmpresas():
    empresaDAO = EmpresaDAO()
    empresas = empresaDAO.listarEmpresas()
    empresaDAO.close()

    return empresas

def buscaEmpresa(pesquisa):
    empresaDAO = EmpresaDAO()
    empresas = empresaDAO.busca(pesquisa)
    empresaDAO.close()

    return empresas



        
