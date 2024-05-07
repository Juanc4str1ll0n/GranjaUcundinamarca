print("Bienvenido a la granja Udec")

class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

    def calcular_produccion(self):
        return self.area * self.rendimiento


class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        


class Granja:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo):
        self.cultivos.remove(cultivo)

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, animal):
        self.animales.remove(animal)

    def calcular_produccion_total_cultivos(self):
        produccion_total = 0
        for cultivo in self.cultivos:
            produccion_total += cultivo.calcular_produccion()
        return produccion_total

    def calcular_produccion_total_animales(self):
        return sum(animal.peso for animal in self.animales)

    def calcular_produccion_total_granja(self):
        return self.calcular_produccion_total_cultivos() + self.calcular_produccion_total_animales()

    def calcular_produccion_leche(self, num_vacas):
        litros_por_vaca = 15
        valor_por_litro = 2000
        produccion_total = num_vacas * litros_por_vaca
        ganancias = produccion_total * valor_por_litro
        return produccion_total, ganancias

    def generar_reporte_produccion_total(self):
        print("Producción total de cultivos: ", self.calcular_produccion_total_cultivos())
        print("Producción total de animales: ", self.calcular_produccion_total_animales())
        print("Producción total de la granja: ", self.calcular_produccion_total_granja())


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar cultivo")
    print("2. Eliminar cultivo")
    print("3. Agregar animal")
    print("4. Eliminar animal")
    print("5. Calcular producción de leche")
    print("6. Generar reporte de producción total")
    print("7. Salir")


if __name__ == "__main__":
    granja = Granja()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cultivo: ")
            tipo = input("Tipo de cultivo: ")
            area = float(input("Área de cultivo (en hectáreas): "))
            rendimiento = float(input("Rendimiento por hectárea: "))
            cultivo = Cultivo(nombre, tipo, area, rendimiento)
            granja.agregar_cultivo(cultivo)
            print("Cultivo agregado exitosamente.")
        elif opcion == "2":
            # Implementar eliminación de cultivo
            pass
        elif opcion == "3":
            especie = input("Especie del animal: ")
            raza = input("Raza del animal: ")
            edad = int(input("Edad del animal: "))
            peso = float(input("Peso del animal (en kg): "))
            animal = Animal(especie, raza, edad, peso)
            granja.agregar_animal(animal)
            print("Animal agregado exitosamente.")
        elif opcion == "4":
            # Implementar eliminación de animal
            pass
        elif opcion == "5":
            num_vacas = int(input("Ingrese la cantidad de vacas: "))
            produccion_total, ganancias = granja.calcular_produccion_leche(num_vacas)
            print(f"Bienvenido a la finca de Producción total de leche: {produccion_total} litros")
            print(f"Ganancias por la producción de leche: ${ganancias}")
        elif opcion == "6":
            granja.generar_reporte_produccion_total()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
