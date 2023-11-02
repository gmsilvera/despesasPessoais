import tkinter as tk
import model as crud
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class Main():
    def __init__ (self, win):
        self.objBD = crud.BancoDeDados()
        self.janela = win

        self.frameFormularioEBotoes = tk.Frame(self.janela)
        self.frameFormularioEBotoes.pack(side="top")
        self.frameFormularioItens = tk.Frame(self.frameFormularioEBotoes, width=200, height=200, relief='flat')
        self.frameFormularioItens.pack(side="left")
        self.frameFormularioTexto = tk.Frame(self.frameFormularioEBotoes, width=200, height=200, relief='flat')
        self.frameFormularioTexto.pack(side="left")

        self.labelNome = tk.Label(self.frameFormularioItens, text="Nome: ")
        self.labelNome.pack(padx=5, pady=5)
        self.entryNome = tk.Entry(self.frameFormularioTexto)
        self.entryNome.pack(padx=5, pady=5)
        
        self.labelDataDespesa = tk.Label(self.frameFormularioItens, text="Data da Despesa: ")
        self.labelDataDespesa.pack(padx=5, pady=5)
        self.entryDataDespesa = DateEntry(self.frameFormularioTexto, width=19, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='YYYY-MM-DD')
        self.entryDataDespesa.pack(padx=5, pady=5)
        
        self.labelValor = tk.Label(self.frameFormularioItens, text="Valor: ")
        self.labelValor.pack(padx=5, pady=5)
        self.entryValor = tk.Entry(self.frameFormularioTexto)
        self.entryValor.pack(padx=5, pady=5)
        
        self.labelMetodoDePagamento = tk.Label(self.frameFormularioItens, text="Metodo de Pagamento: ")
        self.labelMetodoDePagamento.pack(padx=5, pady=5)
        self.entryMetodoDePagamento = tk.Entry(self.frameFormularioTexto)
        self.entryMetodoDePagamento.pack(padx=5, pady=5)
        
        self.labelDescricao = tk.Label(self.frameFormularioItens, text="Descrição: ")
        self.labelDescricao.pack(padx=5, pady=5)
        self.entryDescricao = tk.Entry(self.frameFormularioTexto)
        self.entryDescricao.pack(padx=5, pady=5)
        
        self.labelStatusDeDespesa = tk.Label(self.frameFormularioItens, text="Status da Despesa: ")
        self.labelStatusDeDespesa.pack(padx=5, pady=5)
        self.entryStatusDespesa = tk.Entry(self.frameFormularioTexto)
        self.entryStatusDespesa.pack(padx=5, pady=5)
        
        self.frameButton = tk.Frame(self.frameFormularioEBotoes, width=200, height=200, relief='flat')
        self.frameButton.pack(padx=5, pady=5)
        self.adicionarDespesa = tk.Button(self.frameButton, text="Adicionar Despesa", width=20, command=self.adicionarDespesa)
        self.adicionarDespesa.pack(padx=5, pady=5)
        self.atualizarDespesa = tk.Button(self.frameButton, text="Atualizar Despesa", width=20, command=self.atualizarDespesa)
        self.atualizarDespesa.pack(padx=5, pady=5)
        self.deletarDespesa = tk.Button(self.frameButton, text="Deletar Despesa", width=20, command=self.deletarDespesa)
        self.deletarDespesa.pack(padx=5, pady=5)

        self.treeDespesas = ttk.Treeview(self.janela, columns=("ID", "Nome", "Data Despesa", "Valor", "Metodo de Pagamento", "Descricao", "Status Despesa"), show="headings")
        self.treeDespesas.column("ID", width=10)
        self.treeDespesas.column("Nome", width=80)
        self.treeDespesas.column("Data Despesa", width=100)
        self.treeDespesas.column("Valor", width=80)
        self.treeDespesas.column("Metodo de Pagamento", width=180)
        self.treeDespesas.column("Descricao", width=130)
        self.treeDespesas.column("Status Despesa", width=130)

        self.treeDespesas.heading("ID",text="ID")
        self.treeDespesas.heading("Nome", text="Nome")
        self.treeDespesas.heading("Data Despesa", text="Data Despesa")
        self.treeDespesas.heading("Valor", text="Valor")
        self.treeDespesas.heading("Metodo de Pagamento", text="Metodo de Pagamento")
        self.treeDespesas.heading("Descricao", text="Descricao")
        self.treeDespesas.heading("Status Despesa", text="Status Despesa")
        self.treeDespesas.pack()
        self.exibirDespesas()

    def adicionarDespesa(self):
        try:
            nome = self.entryNome.get()
            dataDespesa = self.entryDataDespesa.get()
            valor = float(self.entryValor.get())
            metodoDePagamento = self.entryMetodoDePagamento.get()
            descricao = self.entryDescricao.get()
            statusDespesa = self.entryStatusDespesa.get()
            self.objBD.insertDespesas(nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa)
            self.exibirDespesas()

            self.entryNome.delete(0,tk.END)
            self.entryDataDespesa.delete(0,tk.END)
            self.entryValor.delete(0,tk.END)
            self.entryMetodoDePagamento.delete(0,tk.END)
            self.entryDescricao.delete(0,tk.END)
            self.entryStatusDespesa.delete(0,tk.END)
            print("Despesa cadastrado com sucesso!")
        except:    
            print("Não foi possivel fazer o cadastro.")

    def exibirDespesas(self):
        try:
            print("Dados disponíveis")
            self.treeDespesas.delete(*self.treeDespesas.get_children())
            self.treeDespesas.get_children()
            despesas = self.objBD.selectData()
            for despesa in despesas:
                self.treeDespesas.insert("", tk.END, values=despesa)            
        except:
            print("Não foi possível exibir os campos.")

    def atualizarDespesa(self):
        try:
            selectitem = self.treeDespesas.focus()
            if not selectitem:
                return
            item = self.treeDespesas.item(selectitem)
            print(item)

            despesa = item["values"]
            id = despesa[0]
            nome = self.entryNome.get()
            dataDespesa = self.entryDataDespesa.get()
            valor = float(self.entryValor.get())
            metodoDePagamento = self.entryMetodoDePagamento.get()
            descricao = self.entryDescricao.get()
            statusDespesa = self.entryStatusDespesa.get()

            self.objBD.updateDespesa(id, nome, dataDespesa, valor, metodoDePagamento, descricao, statusDespesa)
            self.exibirDespesas()
            print("Despesa atulizada com sucesso!")

            self.entryNome.delete(0,tk.END)
            self.entryDataDespesa.delete(0,tk.END)
            self.entryValor.delete(0,tk.END)
            self.entryMetodoDePagamento.delete(0,tk.END)
            self.entryDescricao.delete(0,tk.END)
            self.entryStatusDespesa.delete(0,tk.END)
        except:
            print("Não foi possível atualizar a despesa!")

    def deletarDespesa(self):
        try:
            selectItem = self.treeDespesas.selection()
            if not selectItem:
                return
            item = self.treeDespesas.item(selectItem)
            print(item)
            despesa = item["values"]
            ID = despesa[0]
            self.objBD.deleteDespesa(ID)
            self.exibirDespesas()
            print("Despesa excluído com sucesso!")
        except Exception as e:
            print("Não foi possível fazer a exclusão da despesa.", e)

janela = tk.Tk()
despesas_App = Main(janela)
janela.title("Sistema de Administração de Despesas Pessoais")
janela.geometry("750x550")
janela.mainloop()