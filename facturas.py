facturas = {}

facturas.update({'1': ['JUAN','20000']})


print(facturas)

cod_factura = 0
nombre = ''
valor = 0

cod_factura = input('Digita codigo: ')
nombre = input('Digita nombre: ').upper()
valor = input('Digita valor: '+str(nombre))


facturas.update({cod_factura: [nombre,valor]})


print(facturas)

for x, y in facturas.items():
	print(x)
	for j in y:
  		print(j)



