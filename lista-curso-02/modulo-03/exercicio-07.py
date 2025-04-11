#classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f" {self.ano} {self.marca} {self.modelo}")

# Criando dois objetos da classe Carro
carro1 = Carro("BMW", "M3", 2020)
carro2 = Carro("BMW", "X6", 2023)

# Exibindo os detalhes de cada carro
print("Detalhes do primeiro carro:")
carro1.exibir_detalhes()

print("\nDetalhes do segundo carro:")
carro2.exibir_detalhes()