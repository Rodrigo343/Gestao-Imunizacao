from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from .controller.controllerEmpresa import *

def sair():
    tela.destroy()

def voltar():
    sair()
    from .main import criaTela
    criaTela()

def seleciona():
    limpar()
    txtId.config(state="normal")
    itemSelecionado = tabela.selection()[0]
    itemFormatado = tabela.item(itemSelecionado,"values")
    txtId.insert(0,string=itemFormatado[0])
    txtNome.insert(0,string=itemFormatado[1])
    txtCnpj.insert(0,string=itemFormatado[2])
    txtNomeImunizante.insert(0,string=itemFormatado[3])
    txtId.config(state="readonly")
    

def menssagem(menssage):
    messagebox.showinfo("Menssagem", menssage)

def limpar():
    txtId.config(state="normal")
    txtId.delete(0, END)
    txtNome.delete(0, END)
    txtCnpj.delete(0, END)
    txtNomeImunizante.delete(0, END)
    txtId.config(state="readonly")

def salvar():

    if(editaEmpresa(txtId.get(),txtNome.get(),txtCnpj.get(),txtNomeImunizante.get())):
        limpar()
        menssagem("Cadastrado com sucesso")
        carregarDados()
    else:
        menssagem("Edição Invalido! Insira corretamente os campos")

def excluir():
    
    if(excluirEmpresa(txtId.get())):
        limpar()
        menssagem("Excluido com sucesso")
        carregarDados()
    else:
        menssagem("Erro na exclusao! Ou Empresa cadastrado em Imunizante")

def busca():
    tabela.delete(*tabela.get_children())

    empresas = buscaEmpresa(txtPesquisa.get())
    for empresa in empresas:
        empresaFormatada = [empresa.id, empresa.nome, empresa.cnpj, empresa.imunizante]
        tabela.insert("","end",values=empresaFormatada)

def carregarDados():
    tabela.delete(*tabela.get_children())
    empresas = listaEmpresas()
    for empresa in empresas:
        empresaFormatada = [empresa.id, empresa.nome, empresa.cnpj, empresa.imunizante]
        tabela.insert("","end",values=empresaFormatada)

def criaTela():

    global txtNome,txtId, txtCnpj, txtNomeImunizante, txtPesquisa
    global lblNome, lblCnpj, lblNomeImunizante, lblId,lblTitulo, lblPesquisa
    global tela, tabela
    
    tela= Tk()
    tela.title("Cadastro Empresa")
    tela.geometry("800x400")
    tela.resizable(width=False, height=False)

    tabela = ttk.Treeview(tela,columns=('id','nome','cnpj','imunizante'), show='headings')
    tabela.column('id',minwidth=0,width=100)
    tabela.column('nome',minwidth=0,width=100)
    tabela.column('cnpj',minwidth=0,width=100)
    tabela.column('imunizante',minwidth=0,width=150)
    tabela.heading('id',text='ID')
    tabela.heading('nome',text='NOME')
    tabela.heading('cnpj',text='CNPJ')
    tabela.heading('imunizante',text='IMUNIZANTE')
    tabela.place(x=10, y=130)
    carregarDados()

    lblForm =  Label(tela,border=2, relief="solid", width=45, height = 17)
    lblForm.place(x=470, y=130)

    lblTitulo = Label(tela, text="Cadastro de Empresa",font="Arial 20")
    lblTitulo.place(x=250, y=10)

    lblPesquisa = Label(tela, text="Pesquisa:",font="Arial 12")
    lblPesquisa.place(x=10, y=80)
    txtPesquisa = Entry(tela, width=64, border=1, relief="solid",font="Arial 12")
    txtPesquisa.place(x=90, y=80)

    lblId = Label(tela, text="Id: ",font="Arial 12")
    lblId.place(x=480, y=140)
    txtId = Entry(tela, width=25, border=1, relief="solid",font="Arial 12",state="readonly")
    txtId.place(x=540, y=140)

    lblNome = Label(tela, text="Nome: ",font="Arial 12")
    lblNome.place(x=480, y=180)
    txtNome = Entry(tela, width=25, border=1, relief="solid",font="Arial 12")
    txtNome.place(x=540, y=180)

    lblCnpj = Label(tela, text="Cnpj: ",font="Arial 12")
    lblCnpj.place(x=480, y=220)
    txtCnpj = Entry(tela, width=25, border=1, relief="solid",font="Arial 12")
    txtCnpj.place(x=540, y=220)

    lblNomeImunizante = Label(tela, text="Imunizante: ",font="Arial 12")
    lblNomeImunizante.place(x=480, y=260)
    txtNomeImunizante = Entry(tela, width=22, border=1, relief="solid",font="Arial 12")
    txtNomeImunizante.place(x=570, y=260)

    btnVoltar = Button(tela, text="Pesquisar", command=busca, width=15, border=1, relief="solid")
    btnVoltar.place(x=678, y=80)

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



