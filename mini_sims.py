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
        self.trabalho_nivel = 0

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
            self.fome = max(0, self.fome - 40)
            self.mental += 10
            self.higiene = max(0, self.higiene - 10)
    
    def trabalhar(self):
        if (self.trabalho is None):
            return f"{self.nome} não tem trabalho!"

        if (self.energia < 35):
            return f"{self.nome} está muito cansado para trabalhar!"

        self.energia -= self.trabalho.energia_gasta
        self.mental -= self.trabalho.energia_gasta
        self.dinheiro += self.trabalho.ver_salario(self.trabalho_nivel)
        self.higiene -= self.trabalho.higiene_utilizada
        self.fome = max(0, self.fome - 30)

        return f'''{self.nome} trabalhou como {self.trabalho.ver_cargo(self.trabalho_nivel)}.
        E ganhou {self.trabalho.ver_salario(self.trabalho_nivel)}'''
    
    def tomar_banho(self):
        if (self.higiene == 100):
            return f"{self.nome} já está limpo."
        self.higiene = 100
        self.energia -= 5
    
    def mostrar_status(self):
        if self.trabalho:
            trabalho = self.trabalho.carreira
        else:
            trabalho = "Desempregado"
        return f'''
        👩 {self.nome}
        💤 Energia: {self.energia}
        🍽 Fome: {self.fome}
        💲 Dinheiro: {self.dinheiro}
        🧠 Mental: {self.mental}
        🧼 Higiene: {self.higiene}
        💼 Trabalho: {trabalho}'''
    
    def ser_contratado (self, objeto_trabalho):
        self.trabalho = objeto_trabalho
        self.trabalho_nivel = 1
        return f"{self.nome} foi contratado na carreira de {self.trabalho.carreira} no cargo {self.trabalho.ver_cargo(self.trabalho_nivel)}"
    
    def ser_demitido (self):
        self.trabalho = None
        self.trabalho_nivel = 0
        return f"{self.nome} não tem mais trabalho."
        
class Trabalho:
     # Construtor
    def __init__(self, carreira, cargos, salarios, higiene, energia, mental):
        #Atributos
        self.__carreira = carreira
        self.__cargos = cargos # Lista de cargos possíveis
        self.__salarios = salarios # Lista de salarios
        self.__higiene_utilizada = higiene
        self.__energia_gasta = energia
        self.__mental_utilizado = mental
    
    # Métodos
    @property
    def informacoes(self):
        return f''' Carreira: {self.__carreira}
                    Cargos: {self.__cargos}
                    Salários: {self.__salarios}
                    Higiene: {self.__higiene_utilizada}
                    Energia: {self.__energia_gasta}
                    Mental: {self.__mental_utilizado}'''
    
    @property
    def carreira(self):
        return self.__carreira
    
    @property
    def energia_gasta(self):
        return self.__energia_gasta
    
    @property
    def higiene_utilizada(self):
        return self.__higiene_utilizada
    
    @property
    def mental_utilizado(self):
        return self.__mental_utilizado
    
    def ver_cargo(self, nivel):
        return self.__cargos[nivel-1]
    
    def ver_salario(self, nivel):
        return self.__salarios[nivel-1]

if __name__ == "__main__":
    # Criar um objeto para o trabalho
    carreira = "Artista Pop"
    cargos = ["Cantor de Rua", "Artista Independente", "Pop Star"]
    salarios = [100, 1000, 20000]
    higiene = 30
    energia = 50
    mental = 20

    objeto_trabalho = Trabalho(carreira, cargos, salarios, higiene, energia, mental)
    mensagem = objeto_trabalho.informacoes
    print(mensagem)

    # Criar um objeto personagem
    objeto_personagem = Personagem("Cuca Colonial")
    mensagem = objeto_personagem.ser_contratado(objeto_trabalho)
    print(mensagem)