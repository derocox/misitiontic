arreglo = []

arreglo = [1,10,3,20,5]

tamano_arreglo = len(arreglo)


mes = [1,2,3,4,5,6,7,8,9,10,11,12]
dia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
anio = [2021,2022,2023]


print(tamano_arreglo)

x=0
suma=0
buscar = 20


for x in arreglo:
	suma = suma + x
	if x != buscar:
   		 print(x)
   

print (suma)
print (arreglo[3])
