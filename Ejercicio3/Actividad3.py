import json
import pandas as pd
from datetime import datetime

# Leer el archivo JSON
with open('employees.json') as f:
    data = json.load(f)

# Imprimir todos los empleados
print("Todos los empleados:")
for employee in data:
    print(employee)

# Procesar todos los empleados y aplicar los cambios necesarios
for employee in data:
    # Convertir salario a euros
    employee['salary'] = '€' + employee['salary'].replace('$', '')

    # Aumentar el salario en un 10% para empleados menores de 30 años
    if employee['age'] < 30:
        employee['salary'] = str(round(float(employee['salary'].replace('€', '').replace(',', '')) * 1.10, 2)) + '€'

# Filtrar empleados menores de 30 años y no del proyecto 'GRONK' para el DataFrame
filtered_employees = [employee for employee in data if employee['age'] < 30 and employee['proyect'] != 'GRONK']

# Crear DataFrame con los datos filtrados y procesados
df = pd.DataFrame(filtered_employees)

# Obtener el mes y año actual para el nombre del archivo Excel
now = datetime.now()
month_year = now.strftime("%m-%Y")

# Guardar los datos en un archivo Excel
excel_file_name = f"pagos-empleados-{month_year}.xlsx"
df.to_excel(excel_file_name, index=False)

print(f"\nArchivo Excel '{excel_file_name}' generado exitosamente.")
