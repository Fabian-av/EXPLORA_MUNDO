# ------------------------------
# Plantilla Análisis de Datos (Unidad 4 - analisis.py)
import pandas as pd
import matplotlib.pyplot as plt
# Simulación de reservas
reservas = pd.DataFrame({
"Destino": ["Cartagena", "Medellín", "Cartagena", "Tunja"],
"Personas": [2, 3, 1, 4],
"Días": [5, 3, 2, 7]
})
reservas["Total"] = reservas["Personas"] * reservas["Días"] * 250000
print(reservas.groupby("Destino")["Total"].sum())
reservas.groupby("Destino")["Total"].sum().plot(kind="bar")
plt.title("Ingresos por Destino")

plt.ylabel("COP")
plt.show()