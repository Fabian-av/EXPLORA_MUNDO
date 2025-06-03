print("Bienvenido al cotizador de viajes ExploraMundo")
print("================================================")
destinos = {"Cartagena": 250000, "Medellín": 200000, "Tunja": 30000}
destino = input("Elige un destino que quieres ir (Cartagena, Medellín, Tunja): ")
personas = int(input("Ahora dime el número de personas: "))
dias = int(input("Por ultimo dime la cantidad de días: "))

if destino in destinos:
    total = destinos[destino] * personas * dias
    print(f"Costo total para {personas} personas por {dias} días en {destino}: ${total}")

else:
    print("Destino no disponible.")