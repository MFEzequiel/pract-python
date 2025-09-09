import pandas as pd

# Datos ficticios de clientes
data = {
    'name': ['Juan Pérez', 'Marta López', 'Luis García', 'Ana Torres', 'Rita'],
    'telefon': ['5551234', '5559876', None, '5554321', None],
    'email': ['juan@mail.com', 'marta@mail.com', 'luis@mail.com', 'ana@mail.com', 'rita@gmail.com'],
    'edad': [28, 34, None, 41, 25],
    'fecha_ingreso': ['2023-04-01', '2022-11-15', None, '2021-06-20', None],
    'activo': [True, False, True, True, True]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir fechas
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'], errors='coerce')

# Guardar como Excel
df.to_excel("clientes_ejemplo.xlsx", index=False)

# Guardar como CSV
df.to_csv("clientes_ejemplo.csv", index=False)

print("✅ Archivos creados correctamente: 'clientes_ejemplo.xlsx' y 'clientes_ejemplo.csv'")