import datetime as dt

todayDate = dt.datetime.today()

anio = int(input("En que año naciste?\n"))
mes = int(input("En que mes naciste?\n"))
dia = int(input("En que dia naciste?\n"))

fechaNueva = dt.datetime(anio, mes, dia)

fechaResta = todayDate - fechaNueva

print(fechaResta.days)
