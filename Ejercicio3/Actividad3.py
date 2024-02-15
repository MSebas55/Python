import json
import pandas as pd
from datetime import datetime

with open('employees.json') as f:
    data = json.load(f)

print("Todos los empleados:")
for employee in data:
    print(employee)

# Procesar todos los empleados y aplicar los cambios necesarios
for employee in data:
    employee['salary'] = '€' + employee['salary'].replace('$', '')

    # Aumentar el salario en un 10%
    if employee['age'] < 30:
        employee['salary'] = str(round(float(employee['salary'].replace('€', '').replace(',', '')) * 1.10, 2)) + '€'

# Filtrar excepciones
filtered_employees = [employee for employee in data if employee['age'] < 30 and employee['proyect'] != 'GRONK']
df = pd.DataFrame(filtered_employees)

# Obtener el mes y año actual
now = datetime.now()
month_year = now.strftime("%m-%Y")

# Guardar los datos
excel_file_name = f"pagos-empleados-{month_year}.xlsx"
df.to_excel(excel_file_name, index=False)

print(f"\nArchivo Excel '{excel_file_name}' generado exitosamente.")
