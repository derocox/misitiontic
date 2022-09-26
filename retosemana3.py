print("Reto Tres, Aplicación Edades Pensiones")
print("\n")
Edades = [55, 59, 60, 55, 62, 59, 55, 63]
print(Edades)
print("\n")

 

while True:
    print(''' Menu de Opciones
 	1. Añadir edad: 
 	2. Añadir edad, en una posición de la lista: 
 	3. Longitud de la lista edades: 
 	4. Eliminar la última edad: 
 	5. Eliminar una edad: 
 	6. Contar edades: 
 	7. Personas pensionadas: 
 	8. Mostrar edades: 
 	9. Salir: 
	''')
    opcion = input("Ingresa una Opcion: ")
    if opcion == '1':
        NuevaEdad = int(input("Ingrese una Nueva Edad: "))
        Edades.append(NuevaEdad)
        print(Edades)
    elif opcion == '2':
        NuevaEdad = int(input("Ingrese una Nueva Edad: "))
        NuePosi = int(input("Ingrese Posicion"))
        Edades.insert(NuePosi,NuevaEdad)
        if NuePosi != Edades:
            print("posicion Incorrecta")
            print(Edades)
    elif opcion == '3':
        Vlista = len(Edades)
        print("Longitud de la lista es: ",Vlista)
    elif opcion == '4':
        Edades.pop()
        print(Edades)
    elif opcion == '5':
        Eliminar = int(input("Indique la posicion de edad que desea Eliminar"))
        Edades.pop(Eliminar)
        print(Edades)
    elif opcion == '6':
        Edades.pop(Eliminar)
        print("Conteo de Edades Ingresadas : ").count(Edades)
    else:
        print(Edades)


