from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from .controller.controllerEmpresa import *
from .controller.controllerImunizante import *
from .controller.controllerPessoa import *

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
    cbImunizante.config(state="normal")
    txtId.delete(0, END)
    txtNome.delete(0, END)
    txtCpf.delete(0, END)
    txtDoses.delete(0, END)
    cbImunizante.delete(0, END)
    cbImunizante.config(state="readonly")
    txtId.config(state="readonly")

def formataImunizante():
    '''
    Carregas o lote dos imunizante e o nome do imunizante para comboBox
    '''
    global imunizantes,empresas
    imunizantes = listaImunizantes()
    empresas = listaEmpresas()
    imunizantesFormatados = []
    imunizantesFormatados.append("")

    for i in imunizantes:
        for j in empresas:
            if i.id_empresa == j.id:
                imunizantesFormatados.append("Lote: {0} Imunizante: {1}".format(i.lote, j.imunizante))
    
    return imunizantesFormatados

def formataImunizanteSalva(pessoa_imunizante):
    '''
    Carregas o lote dos imunizante e o nome do imunizante para tabela
    '''
    imunizantes = listaImunizantes()
    empresas = listaEmpresas()
    dadosTabela = []

    if (pessoa_imunizante != None):
        pessoa_imunizante = int(pessoa_imunizante)
        for i in imunizantes:
            if pessoa_imunizante == i.id:
                for j in empresas:
                    if i.id_empresa == j.id:
                        dadosTabela.append(i.lote)
                        dadosTabela.append(j.imunizante)
        return dadosTabela
    else:
        dadosTabela.append("")
        dadosTabela.append("")
        return dadosTabela

def pegaIdImunizante():
    '''
    Carrega a String da combobox estado, formata para uma lista e pega o lote 
    do imunizante e retorna o id do imunizante que esta no banco, para salvar.
    '''
    if (cbImunizante.get() != "" ):
        for i in imunizantes:
            comboEmpresaFomatada = cbImunizante.get().split()
            if(i.lote == int(comboEmpresaFomatada[1])):
                return i.id
    else:
        return 0

def seleciona():
    '''
    Seleciona todos os dados da linha da tabela e coloca os respectivos valores nos campos
    de edição
    '''
    limpar()
    txtId.config(state="normal")
    cbImunizante.config(state="normal")
    itemSelecionado = tabela.selection()[0]
    itemFormatado = tabela.item(itemSelecionado, "values")
    txtId.insert(0, string=itemFormatado[0])
    txtNome.insert(0, string=itemFormatado[1])
    txtCpf.insert(0, string=itemFormatado[2])
    txtDoses.insert(0, string=itemFormatado[3])
    cbImunizante.insert(0, string="Lote: {0} Imunizante: {1}".format(itemFormatado[4], itemFormatado[5]))
    cbImunizante.config(state="readonly")
    txtId.config(state="readonly")

def carregarDados():
    tabela.delete(*tabela.get_children())
    pessoas = listaPessoas()
    for pessoa in pessoas:
        dadosImunizante = formataImunizanteSalva(pessoa.id_imunizante)
        pessoasFormatada = [pessoa.id, pessoa.nome, pessoa.cpf, pessoa.doses, dadosImunizante[0], dadosImunizante[1]]
        tabela.insert("", "end", values=pessoasFormatada)

def salvar():

    if(editaPessoa(txtId.get(), txtNome.get(), txtCpf.get(), txtDoses.get(), pegaIdImunizante())):
        limpar()
        menssagem("Edição com sucesso")
        carregarDados()
    else:
        menssagem("Cadastro Invalido! Insira corretamente os campos")

def excluir():
    
    if(excluirPessoa(txtId.get())):
        limpar()
        menssagem("Excluido com sucesso")
        carregarDados()
    else:
        menssagem("Erro na exclusao")

def busca():
    tabela.delete(*tabela.get_children())
    pessoas = buscaPessoa(txtPesquisa.get())
    for pessoa in pessoas:
        dadosImunizante = formataImunizanteSalva(pessoa.id_imunizante)
        pessoasFormatada = [pessoa.id, pessoa.nome, pessoa.cpf, pessoa.doses, dadosImunizante[0], dadosImunizante[1]]
        tabela.insert("","end",values=pessoasFormatada)
    
def criaTela():

    global txtNome, txtId, txtCpf, txtDoses, cbImunizante, txtPesquisa
    global lblNome, lblCpf, lblDoses, lblImunizante, lblId, lblTitulo, lblPesquisa
    global tela, tabela

    tela= Tk()
    tela.title("Edição Pessoa")
    tela.geometry("800x400+300+200")
    tela.resizable(width=False, height=False)

    tabela = ttk.Treeview(tela,columns=('id', 'nome', 'cpf', 'doses', 'lote', 'imunizante'), show='headings')
    tabela.column('id', minwidth=0, width=50)
    tabela.column('nome', minwidth=0, width=100)
    tabela.column('cpf', minwidth=0, width=100)
    tabela.column('doses', minwidth=0, width=50)
    tabela.column('lote', minwidth=0, width=50)
    tabela.column('imunizante', minwidth=0, width=100)
    tabela.heading('id', text='ID')
    tabela.heading('nome', text='NOME')
    tabela.heading('cpf', text='CPF')
    tabela.heading('doses', text='DOSES')
    tabela.heading('lote', text='LOTE')
    tabela.heading('imunizante', text='IMUNIZANTE')
    tabela.place(x=10, y=100)
    carregarDados()

    lblForm =  Label(tela, border=2, relief="solid", width=45, height = 19)
    lblForm.place(x=470, y=98)

    lblTitulo = Label(tela, text="Edição de Pessoa", font="Arial 20")
    lblTitulo.place(x=250, y=10)

    lblPesquisa = Label(tela, text="Pesquisa:", font="Arial 12")
    lblPesquisa.place(x=10, y=60)
    txtPesquisa = Entry(tela, width=51, border=1, relief="solid", font="Arial 12")
    txtPesquisa.place(x=90, y=60)

    lblId = Label(tela, text="Id: ", font="Arial 12")
    lblId.place(x=480, y=120)
    txtId = Entry(tela, width=25, border=1, relief="solid", font="Arial 12", state="readonly")
    txtId.place(x=540, y=120)

    lblNome = Label(tela, text="Nome: ", font="Arial 12")
    lblNome.place(x=480, y=160)
    txtNome = Entry(tela, width=25, border=1, relief="solid", font="Arial 12")
    txtNome.place(x=540, y=160)

    lblCpf = Label(tela, text="Cpf: ", font="Arial 12")
    lblCpf.place(x=480, y=200)
    txtCpf = Entry(tela, width=25, border=1, relief="solid", font="Arial 12")
    txtCpf.place(x=540, y=200)

    lblDoses = Label(tela, text="Doses: ", font="Arial 12")
    lblDoses.place(x=480, y=240)
    txtDoses = Entry(tela, width=25, border=1, relief="solid", font="Arial 12")
    txtDoses.place(x=540, y=240)

    lblImunizante = Label(tela, text="Imunizante: ", font="Arial 12")
    lblImunizante.place(x=480, y=270)
    cbImunizante = Combobox(tela, values=formataImunizante(), width=20, font="Arial 12", state="readonly")
    cbImunizante.config(state="normal")
    cbImunizante.insert(0, string="")
    cbImunizante.config(state="readonly")
    cbImunizante.place(x=565, y=270)

    btnpesquisa = Button(tela, text="Pesquisar", command=busca, width=15, border=1, relief="solid")
    btnpesquisa.place(x=560, y=60)

    btnLimpaPesquisa = Button(tela, text="Limpa", command=carregarDados, width=15, border=1, relief="solid")
    btnLimpaPesquisa.place(x=678, y=60)

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






