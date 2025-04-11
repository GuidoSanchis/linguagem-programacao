class Animal:
    def fazer_som(self):
        print("O animal fez um som genérico.")
      
class Cachorro(Animal):
    def fazer_som(self):
        print(" Au au!")
      
class Vaca(Animal):
    def fazer_som(self):
        print("Muuuu!")


# programa
animal1 = Cachorro()
animal2 = Gato()

# Chamando os métodos
print("Som do cachorro:")
animal1.fazer_som()

print("\nSom do gato:")
animal2.fazer_som()