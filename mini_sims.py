class Personagem:
    # Construtor
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.fome = 100
        self.higiene = 100
        self.mental = 100
        self.dinheiro = 50
        self.trabalho = None

    # Métodos (ações)
    def comer (self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para comer"
        else:
            self.fome = min(100, self.fome + 25)
            self.dinheiro -= 10
            return f"{self.nome} se alimentou"

    def dormir(self):
        if (self.energia == 100):
            return f"{self.nome} não está cansado para dormir."
        
        else:
            self.energia = 100
            self.fome -= 40
            self.mental += 10
            self.higiene -= 10
    
    def trabalhar(self):
        if (self.energia < 35):
            return f"{self.nome} está muito cansado para trabalhar!"

        self.energia -= 30
        self.mental -= 20
        self.dinheiro += 40
        self.higiene -= 30

        return f"{self.nome} trabalhou."
    
    def mostrar_status(self):
        return f'''
        👩 {self.nome}
        💤 Energia: {self.energia}
        🍽 Fome: {self.fome}
        💲 Dinheiro: {self.dinheiro}
        🧠 Mental: {self.mental}
        🧼 Higiene: {self.higiene}'''     


if __name__ == "__main__":
    # Criar um objeto para o personagem
    obj1 = Personagem("Laura Caixão")
    print(obj1.comer())
    print(obj1.fome)
    print(obj1.mostrar_status())