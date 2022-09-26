num = int(input("Digita un numero: "))
num = str(num)
cantidad = len(num)

if cantidad == 1:
    print("unidad")
elif cantidad == 2:
    print("decena")
elif cantidad == 3:
    print("centena")
elif cantidad == 4:
    print("milesima")
elif cantidad == 5:
    print("decena de mil")
elif cantidad == 6:
    print("centena de mil")