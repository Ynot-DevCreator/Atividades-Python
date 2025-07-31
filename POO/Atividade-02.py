class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
    def descricao(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
    def descricao(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")    
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
    def descricao(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")

motos = [
    Moto("Yamaha", "MT-07", 2022)
]
carros = [
    Carro("Honda", "Civic-Type R", 2020)
]
caminhoes = [
    Caminhao("Scania", "R450", 2023)
]

for carro in carros:
    carro.descricao()
for moto in motos:
    carro.descricao()
for caminhao in caminhoes:
    carro.descricao()