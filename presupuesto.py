saldo=int(input('Por favor ingrese su saldo actual:$' ))

if saldo<0:
    prestamo=10000-saldo
    print('Se debe hacer el prestamo por $', prestamo)
    
elif saldo>=0 and saldo <20000:
    prestamo=20000-saldo
    print ('El prestamo a solicitar es de $', prestamo)
    
else:
    print('No debe solicitar prestamo')

presupuesto = prestamo-5000-2000
print(f'El presupuesto restante para insumos e incentivos para el personal es de:$' , presupuesto)
print(f'El monto para cada uno de ellos es de:$', presupuesto/2)




