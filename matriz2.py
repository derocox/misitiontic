thislist = [["producto1", "10000", "descripcion1"],["producto2","20000","descripcion2"]]

def busquedaproductos(lista):
	for i in range(len(lista)):
		if i==0:
  			print("Producto: ", lista[i])


def busquedavalores(lista):
	for i in range(len(lista)):
		if i==1:
			print("Valor: ", lista[i])




def busqueda_param(lista, texto, posicion):
	for i in range(len(lista)):
                if i==posicion:
                        print(texto, ": ", lista[i])



for listainterna in thislist:
	print(listainterna)
	busqueda_param(listainterna, "producto", 0)
	busqueda_param(listainterna, "valor", 1)
	








