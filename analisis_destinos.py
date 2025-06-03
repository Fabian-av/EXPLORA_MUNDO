import pandas as pd
import matplotlib.pyplot as plt
# Cargar datos
df = pd.read_csv('reservas.csv')
# Agrupar por destino: total de reservas, total de personas y total recaudado
resumen = df.groupby('destino').agg({
    'reserva_id': 'count',
    'personas': 'sum',
    'costo_total': 'sum'
}).rename(columns={
    'reserva_id': 'total_reservas',
    'personas': 'total_personas',
    'costo_total': 'total_ingresos'
})
print("Resumen de desempeño por destino:")
print(resumen)
# Gráfico 1: Reservas por destino
resumen['total_reservas'].plot(kind='bar', title='Reservas por destino', ylabel='Cantidad de reservas', color='skyblue')
plt.tight_layout()
plt.show()
# Gráfico 2: Ingresos por destino

resumen['total_ingresos'].plot(kind='bar', title='Ingresos por destino', ylabel='Pesos colombianos',
color='green')
plt.tight_layout()
plt.show()