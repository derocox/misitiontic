print("SIMULADOR DE CAPITAL")
print("Bienvenidos")
interes1=float(input("Ingrese_interes_socio1: "))
interes2=float(input("Ingrese_interes_socio2: "))
mes=0
if interes1<5 and interes2<5:
	C1=int(input("Ingrese_capital_socio1: "))
	C2=int(input("Ingrese_capital_socio2: "))
	C3=int(input("Ingrese_monto_de_negocio: "))
	capital_1_2=0
	while capital_1_2<=C3:
		C1=C1*(interes1/100)+C1
		C2=C2*(interes2/100)+C2
		capital_1_2=C1+C2
		mes=mes+1
	if capital_1_2>C3:
		print("En el mes ", mes, " pueden hacer el negocio: ", capital_1_2, " es el rendimiento conjunto de la inversión.")
else:
	print("Existe algún dato de interés inconsistente, hasta pronto")


