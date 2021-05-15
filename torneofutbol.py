#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

fechas_partidos = []
arreglo_partidos = []
partidos = []


def menuprincipal():
    os.system('clear')
    print ("Selecciona una opción")
    print ("\t1 - Registrar Partido")
    print ("\t2 - Ver Resultados")
    print ("\t3 - Tabla Clasificacion")
    print ("\t0 - salir")


def datospartido():
    os.system('clear')
    fecha = input("Fecha del partido >> ")
    partidos.append(fecha)
    nom_rival = input("Nombre rival >> ")
    partidos.append(nom_rival)
    goles_rival = input("Goles Equipo Rival >> ")
    partidos.append(goles_rival)
    goles_unab = input("Goles UNAB >> ")
    partidos.append(goles_unab)
    print("Registro Exitoso")


def ordenamientoFechas(fechasArreglo):
    intercambios = True
    numPasada = len(fechasArreglo)-1
    while numPasada > 0 and intercambios:
       intercambios = False
       for i in range(numPasada):
           if fechasArreglo[i]>fechasArreglo[i+1]:
               intercambios = True
               temp = fechasArreglo[i]
               fechasArreglo[i] = fechasArreglo[i+1]
               fechasArreglo[i+1] = temp
       numPasada = numPasada-1



def resultados(arreglo):    

    for x in arreglo:
        fechas_partidos.append(str(x[0]))
    ordenamientoFechas(fechas_partidos)

    for i in arreglo:
        cadena = i[0] + " - UNAB (" + i[3] + ") VS (" + i[2] + ") " + i[1]
        print(cadena)


def statsUnab(arreglo):
    partidos_jugados = len(arreglo) 
    ganadosunab=0
    perdidosunab=0
    empatadosunab=0
    for partidosunab in arreglo:
        if(partidosunab[3]>partidosunab[2]):
            ganadosunab +=1
        elif(partidosunab[3]<partidosunab[2]):
            perdidosunab +=1
        else:
            empatadosunab +=1
    print("Partidos Jugados UNAB: " + str(partidos_jugados))
    print("Partidos Ganados UNAB: " + str(ganadosunab))
    print("Partidos Empatados UNAB: " + str(empatadosunab))
    print("Partidos Perdidos UNAB: " + str(perdidosunab))
    puntos = ((ganadosunab * 3) + (empatadosunab * 1))
    print("Total Puntos UNAB: " + str(puntos))



while True:
    menuprincipal()
    opcion = input("Selecciona una opción >> ")
    if opcion=="1":
        print ("")
        input("Perfecto vamos a registrar los datos del partido...\nPresiona ENTER para continuar")
        datospartido()
        arreglo_partidos.append(partidos)
        partidos = []
        continuar = input("Presiona 1 para registrar un nuevo partido 2 para volver al menu principal >> ")
        if continuar=="1":
            datospartido()
            arreglo_partidos.append(partidos)
            partidos=[]
        elif continuar=="2":
            input("Presiona ENTER para volver al Menu Principal")
        else:
            input("Opción incorrecta...\nPresiona ENTER para continuar")                
    elif opcion=="2":
        print ("")
        input("********** RESULTADOS **********\nPresiona ENTER para continuar")
        resultados(arreglo_partidos)
        input("\nPresiona ENTER para continuar")
    elif opcion=="3":
        print ("")
        input("********** CLASIFICACION **********\nPresiona ENTER para continuar")
        statsUnab(arreglo_partidos)
        input("\nPresiona ENTER para continuar")
    elif opcion=="0":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\nPresiona ENTER para continuar")