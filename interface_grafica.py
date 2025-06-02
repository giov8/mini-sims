import tkinter as tk
from tkinter import messagebox
from mini_sims import Personagem, Trabalho

class SimsApp:
    # Construtor
    def __init__(self, root):
        # Criando o personagem
        self.personagem = Personagem("Laura Caixão")

        # Titulo da janela
        root.title("Mini Sims")
        # Tamanho da janela
        root.geometry("500x500")

        self.label_status = tk.Label(root, text=self.personagem.mostrar_status(),
                                     font=("Arial", 18), pady=10)
        self.label_status.pack()

        self.btn_comer = tk.Button(root, text="🍔 Comer", command=self.acao_botao_comer)
        self.btn_comer.pack(pady= 5)

        self.btn_trabalhar = tk.Button(root, text="💼 Trabalhar", command=self.acao_botao_trabalhar)
        self.btn_trabalhar.pack(pady= 5)

        self.btn_dormir = tk.Button(root, text="💤 Dormir", command=self.acao_botao_dormir)
        self.btn_dormir.pack(pady= 5)


        self.btn_tomar_banho = tk.Button(root, text="🚿 Tomar banho", command=self.acao_botao_tomar_banho)
        self.btn_tomar_banho.pack(pady= 5)

        self.btn_procurar_emprego = tk.Button(root, text="Procurar emprego", command=self.acao_botao_procurar_emprego)
        self.btn_procurar_emprego.pack(pady= 5)

        self.label_mensagem = tk.Label(root, text="", font=("Arial", 10))
        self.label_mensagem.pack()


    # Método que atualiza os status do personagem
    def atualizar_status(self):
        self.label_status.config(text=self.personagem.mostrar_status())

    # Método que define a ação que acontece quando pressiono o botão "comer"
    def acao_botao_comer(self):
        mensagem = self.personagem.comer()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

        # Método que define a ação que acontece quando pressiono o botão "comer"
    def acao_botao_trabalhar(self):
        mensagem = self.personagem.trabalhar()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

        # Método que define a ação que acontece quando pressiono o botão "comer"
    def acao_botao_dormir(self):
        mensagem = self.personagem.dormir()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

    def acao_botao_tomar_banho(self):
        mensagem = self.personagem.tomar_banho()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
    
    def acao_botao_procurar_emprego(self):
        self.trabalhos = self.criar_trabalhos()
        for trabalho in self.trabalhos:
            mensagem = trabalho.informacoes
            resposta = messagebox.askquestion("Oferta de emprego", message=mensagem)
            if resposta == "yes":
                mensagem_sucesso = f"Parabéns, você foi contratado na carreira de {trabalho.carreira}."
                messagebox.showinfo("Oferta de emprego", mensagem_sucesso)
                self.personagem.ser_contratado(trabalho)
                self.atualizar_status()
                return
        messagebox.showerror("Oferta de emprego", "Não há mais empregos disponíveis")
        self.atualizar_status()
        return    


    def criar_trabalhos(self):
        lista_trabalhos = []
        carreira = "Músico"
        cargos = ["Cantor de Rua", "Artista Independente", "Pop Star"]
        salarios = [100, 1000, 20000]
        higiene = 30
        energia = 50
        mental = 20
        objeto_trabalho = Trabalho(carreira, cargos, salarios, higiene, energia, mental)
        mensagem = objeto_trabalho.informacoes
        # O comando append adiciona um objeto a lista
        lista_trabalhos.append(objeto_trabalho)

        carreira = "Pedreiro"
        cargos = ["Servente", "Pedreiro", "Mestre de Obra"]
        salarios = [200, 300, 1000]
        higiene = 70
        energia = 60
        mental = 10
        objeto_trabalho = Trabalho(carreira, cargos, salarios, higiene, energia, mental)
        mensagem = objeto_trabalho.informacoes
        # O comando append adiciona um objeto a lista
        lista_trabalhos.append(objeto_trabalho)

        carreira = "Desenvolvedor de Software"
        cargos = ["Júnior", "Pleno", "Senior"]
        salarios = [100, 300, 2000]
        higiene = 10
        energia = 50
        mental = 50
        objeto_trabalho = Trabalho(carreira, cargos, salarios, higiene, energia, mental)
        mensagem = objeto_trabalho.informacoes        # O comando append adiciona um objeto a lista
        lista_trabalhos.append(objeto_trabalho)

        return lista_trabalhos

# Rodar o App
if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()
