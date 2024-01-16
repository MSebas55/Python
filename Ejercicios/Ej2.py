# Introducir una fecha y que nos muestre la diferencia en días desde hoy
import datetime as dt

todayDate = dt.datetime.today()

dia = int(input("En que dia naciste?\n"))
mes = int(input("En que mes naciste?\n"))
anio = int(input("En que año naciste?\n"))

fechaNueva = dt.datetime(anio, mes, dia)

fechaResta = todayDate - fechaNueva

print(fechaResta.days)
