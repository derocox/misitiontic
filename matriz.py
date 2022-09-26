thislist = [["apple", "1", "cherry"],["blueberry","2","sandia"],["fruta1","3","fruta2"],["fruta3","4","fruta4"]]

def extraerlista(lista):
	for x in lista:
		print(x[0], "---" ,x[2])



def extraernumeros(lista):
	for j in lista:
		print(j[1])


extraerlista(thislist)
extraernumeros(thislist)

