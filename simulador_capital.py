print("*** Simulador de Capital ***")
Ingrese_interes_socio1=float(input("Ingrese el interés del Socio 1 : "))
Ingrese_interes_socio2=float(input("Ingrese el interés del Socio 2 : "))

i1=Ingrese_interes_socio1/100
i2=Ingrese_interes_socio2/100
mes=0

if (i1<0.05 and i2<0.05):
    Ingrese_capital_socio1=int(input("Ingrese Capital del Socio 1: "))
    Ingrese_capital_socio2=int(input("Ingrese Capital del Socio 2: "))
    Ingrese_monto_negocio=int(input("Ingrese Monto del Negocio : "))
    capital_1_2=0 #Debo iniciarlizarla= Declarar la variable y colocar un valor incial.
    while capital_1_2<=Ingrese_monto_negocio:
        Ingrese_capital_socio1=(Ingrese_capital_socio1*i1)+Ingrese_capital_socio1
        Ingrese_capital_socio2=(Ingrese_capital_socio2*i2)+Ingrese_capital_socio2
        capital_1_2=Ingrese_capital_socio1+Ingrese_capital_socio2
        mes=mes+1
    if capital_1_2>Ingrese_monto_negocio: #Identación= Espacio para identificar y orden de lectura al programa.
        print("En el mes "+str(mes)+ " pueden hacer el negocio: "+str(capital_1_2)+ ", es el rendimiento conjunto de la inversión")
else:
    print("Existen algún dato de interés inconsistente, hasta pronto.")