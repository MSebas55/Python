import pandas as pd

nombres = ['Juan', 'Leticia', 'Elías']
edades = [24, 32, 13]

df = pd.DataFrame({'Nombre': nombres, 'Edad': edades})

print(df)

df.index.name = 'ID'

df.to_excel('documento.xlsx')
