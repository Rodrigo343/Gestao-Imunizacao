from .model.estado import Estado
from .model.estadoDAO import EstadoDAO

def listaEstado():

    estados = []
    empresaDAO = EstadoDAO()
    estados = empresaDAO.listarEstados()
    empresaDAO.close()
    return estados



        
