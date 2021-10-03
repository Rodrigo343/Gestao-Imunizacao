from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from .controller.controllerImunizante import *
from .controller.controllerEmpresa import *
from .controller.controllerEstado import *

def sair():
    tela.destroy()

def voltar():
    sair()
    from .main import criaTela
    criaTela()

def menssagem(menssage):
    messagebox.showinfo("Menssagem", menssage)

def limpar():
    txtId.config(state="normal")
    cbEmpresa.config(state="normal")
    cbEstado.config(state="normal")
    txtId.delete(0, END)
    txtLote.delete(0, END)
    cbEstado.delete(0, END)
    cbEmpresa.delete(0, END)
    cbEmpresa.config(state="readonly")
    cbEstado.config(state="readonly")
    txtId.config(state="readonly")

def formataEstado():
    '''
    Carregas apenas os nomes dos estado para carregar na combobox estado
    '''
    global estados
    estados = listaEstado()
    estadosFormatados = []

    for i in estados:
        estadosFormatados.append(i.nome)
    
    return estadosFormatados

def formataEmpresa():
    '''
    Carregas apenas os nomes das empresas para carregar na combobox empresa
    '''
    global empresas
    empresas = listaEmpresas()
    empresasFormatadas = []

    for i in empresas:
        empresasFormatadas.append(i.nome)
    
    return empresasFormatadas

def formataEstadoSalva(estado):
    '''
    Carregas apenas os nomes dos estados para carregar na tabela
    '''
    global estados
    estados = listaEstado()

    for i in estados:
        if(i.id == estado):
            nome = i.nome
    
    return nome

def formataEmpresaSalva(empresa):
    '''
    Carregas apenas os nomes das empresas para carregar na tabela
    '''
    global empresas
    empresas = listaEmpresas()

    for i in empresas:
        if(i.id == empresa):
            nome = i.nome
    
    return nome

def pegaIdEstado():
    '''
    Carrega o nome do estado selecionado na combobox estado, formata para o id que esta na
    lista estados e retorna o id do estado que esta no banco, para salvar.
    '''
    for i in estados:
        if(i.nome == cbEstado.get()):
            estado = i.id
            return estado

def pegaIdEmpresa():
    '''
    Carrega o nome da empresa selecionada na combobox estado, formata para o id que esta na
    lista cidades e retorna o id da empresa que esta no banco, para salvar.
    '''
    for j in empresas:
        if(j.nome == cbEmpresa.get()):
            empresa = j.id
            return empresa

def seleciona():
    '''
    Seleciona todos os dados da linha da tabela e coloca os respectivos valores nos campos
    de edição
    '''
    limpar()
    txtId.config(state="normal")
    cbEmpresa.config(state="normal")
    cbEstado.config(state="normal")
    itemSelecionado = tabela.selection()[0]
    itemFormatado = tabela.item(itemSelecionado,"values")
    txtId.insert(0,string=itemFormatado[0])
    txtLote.insert(0,string=itemFormatado[1])
    cbEstado.insert(0,string=itemFormatado[2])
    cbEmpresa.insert(0,string=itemFormatado[3])
    cbEmpresa.config(state="readonly")
    cbEstado.config(state="readonly")
    txtId.config(state="readonly")

def carregarDados():
    tabela.delete(*tabela.get_children())
    imunizantes = listaImunizantes()
    for imunizante in imunizantes:
        imunizanteFormatada = [imunizante.id, imunizante.lote, formataEstadoSalva(imunizante.id_estado), formataEmpresaSalva(imunizante.id_empresa)]
        tabela.insert("","end",values=imunizanteFormatada)

def salvar():

    if(editaImunizante(txtId.get(),txtLote.get(),pegaIdEstado(),pegaIdEmpresa())):
        limpar()
        menssagem("Cadastrado com sucesso")
        carregarDados()
    else:
        menssagem("Edição Invalido! Insira corretamente os campos")

def excluir():
    
    if(excluirImunizante(txtId.get())):
        limpar()
        menssagem("Excluido com sucesso")
        carregarDados()
    else:
        menssagem("Erro na exclusao! Ou Imunizante cadastrado em pessoa")

def busca():
    tabela.delete(*tabela.get_children())

    imunizantes = buscaImunizante(txtPesquisa.get())
    for imunizante in imunizantes:
        imunizanteFormatada = [imunizante.id, imunizante.lote, formataEstadoSalva(imunizante.id_estado), formataEmpresaSalva(imunizante.id_empresa)]
        tabela.insert("","end",values=imunizanteFormatada)
    
def criaTela():

    global txtLote,txtId, cbEstado, cbEmpresa, txtPesquisa
    global lblLote, lblEstado, lblEmpresa, lblId,lblTitulo, lblPesquisa
    global tela, tabela

    tela= Tk()
    tela.title("Edição Imunizante")
    tela.geometry("800x400")
    tela.resizable(width=False, height=False)

    tabela = ttk.Treeview(tela,columns=('id','lote','cidade','empresa'), show='headings')
    tabela.column('id',minwidth=0,width=100)
    tabela.column('lote',minwidth=0,width=100)
    tabela.column('cidade',minwidth=0,width=100)
    tabela.column('empresa',minwidth=0,width=150)
    tabela.heading('id',text='ID')
    tabela.heading('lote',text='LOTE')
    tabela.heading('cidade',text='CIDADE')
    tabela.heading('empresa',text='EMPRESA')
    tabela.place(x=10, y=130)
    carregarDados()

    lblForm =  Label(tela,border=2, relief="solid", width=45, height = 17)
    lblForm.place(x=470, y=130)

    lblTitulo = Label(tela, text="Edição de Imunizante",font="Arial 20")
    lblTitulo.place(x=250, y=10)

    lblPesquisa = Label(tela, text="Pesquisa:",font="Arial 12")
    lblPesquisa.place(x=10, y=80)
    txtPesquisa = Entry(tela, width=51, border=1, relief="solid",font="Arial 12")
    txtPesquisa.place(x=90, y=80)

    lblId = Label(tela, text="Id: ",font="Arial 12")
    lblId.place(x=480, y=140)
    txtId = Entry(tela, width=25, border=1, relief="solid",font="Arial 12",state="readonly")
    txtId.place(x=540, y=140)

    lblLote = Label(tela, text="Lote: ",font="Arial 12")
    lblLote.place(x=480, y=180)
    txtLote = Entry(tela, width=25, border=1, relief="solid",font="Arial 12")
    txtLote.place(x=540, y=180)

    lblEstado = Label(tela, text="Estado: ",font="Arial 12")
    lblEstado.place(x=480, y=220)
    cbEstado = Combobox(tela, values=formataEstado(), width=23,font="Arial 12",state="readonly")
    cbEstado.place(x=540, y=220)

    lblEmpresa = Label(tela, text="Empresa: ",font="Arial 12")
    lblEmpresa.place(x=480, y=260)
    cbEmpresa = Combobox(tela, values=formataEmpresa(), width=20,font="Arial 12",state="readonly")
    cbEmpresa.place(x=570, y=260)

    btnpesquisa = Button(tela, text="Pesquisar", command=busca, width=15, border=1, relief="solid")
    btnpesquisa.place(x=560, y=80)

    btnLimpaPesquisa = Button(tela, text="Limpa", command=carregarDados, width=15, border=1, relief="solid")
    btnLimpaPesquisa.place(x=678, y=80)

    btnSalvar = Button(tela, text="Salvar", command=salvar, width=15, border=1, relief="solid")
    btnSalvar.place(x=500, y=300)

    btnLimpar = Button(tela, text="Limpar", command=limpar, width=15, border=1, relief="solid")
    btnLimpar.place(x=650, y=300)

    btnLimpar = Button(tela, text="Selecionar", command=seleciona, width=15, border=1, relief="solid")
    btnLimpar.place(x=500, y=330)

    btnVoltar = Button(tela, text="Excluir", command=excluir, width=15, border=1, relief="solid")
    btnVoltar.place(x=650, y=330)

    btnVoltar = Button(tela, text="Voltar", command=voltar, width=15, border=1, relief="solid")
    btnVoltar.place(x=500, y=360)

    btnSair = Button(tela, text="Sair", command=sair, width=15, border=1, relief="solid")
    btnSair.place(x=650, y=360)

    tela.mainloop()






