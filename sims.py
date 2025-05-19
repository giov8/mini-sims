import tkinter as tk

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.fome = 0
        self.dinheiro = 50

    def comer(self):
        if self.dinheiro >= 10:
            self.fome = max(self.fome - 30, 0)
            self.dinheiro -= 10
            return f"{self.nome} comeu."
        else:
            return f"{self.nome} está sem dinheiro para comer."

    def dormir(self):
        self.energia = min(self.energia + 50, 100)
        self.fome -= 10
        return f"{self.nome} dormiu e recuperou energia."

    def trabalhar(self):
        if self.energia >= 30:
            self.dinheiro += 40
            self.energia -= 30
            self.fome += 20
            return f"{self.nome} trabalhou e ganhou dinheiro."
        else:
            return f"{self.nome} está cansado demais para trabalhar."

    def status(self):
        return f"{self.nome} | Energia: {self.energia} | Fome: {self.fome} | Dinheiro: R${self.dinheiro}"

# Interface gráfica
class SimsApp:
    def __init__(self, root):
        self.personagem = Personagem("João")

        root.title("Mini Sims")
        root.geometry("400x300")

        self.label_status = tk.Label(root, text=self.personagem.status(), font=("Arial", 12), pady=10)
        self.label_status.pack()

        self.label_log = tk.Label(root, text="", font=("Arial", 10))
        self.label_log.pack()

        btn_comer = tk.Button(root, text="🍔 Comer", command=self.acao_comer)
        btn_comer.pack(pady=5)

        btn_dormir = tk.Button(root, text="😴 Dormir", command=self.acao_dormir)
        btn_dormir.pack(pady=5)

        btn_trabalhar = tk.Button(root, text="💼 Trabalhar", command=self.acao_trabalhar)
        btn_trabalhar.pack(pady=5)

        btn_status = tk.Button(root, text="📊 Ver Status", command=self.atualizar_status)
        btn_status.pack(pady=10)

    def atualizar_status(self):
        self.label_status.config(text=self.personagem.status())

    def acao_comer(self):
        log = self.personagem.comer()
        self.label_log.config(text=log)
        self.atualizar_status()

    def acao_dormir(self):
        log = self.personagem.dormir()
        self.label_log.config(text=log)
        self.atualizar_status()

    def acao_trabalhar(self):
        log = self.personagem.trabalhar()
        self.label_log.config(text=log)
        self.atualizar_status()


# Rodar o app
if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()
