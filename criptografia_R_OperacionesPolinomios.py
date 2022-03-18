#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:46:16 2020

@author: sergio
"""
import subprocess
import numpy as np
import random
import time
import math
import funcionesBasicas
import sys
from sys import argv
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP
import numpy
from numpy.polynomial import Polynomial as P

#######################################################################################
# INICIO del código común para todas las fichas
#######################################################################################
start = time.time()
sys.path.insert(0, './')
directorioFichas = "./fichas/"
# Creamos el código albético para encriptar.
codigoAlfabetico = funcionesBasicas.creaCodigoAlfabetico()
# Leemos el archivo de texto txt que contiene los elementos y el tema.
tema,elementos = funcionesBasicas.leeElementos(argv)
# Leemos los datos sobre la ficha para crear el archivo LaTeX y cada ficha.
datos = funcionesBasicas.leeDatosCabecera(argv)
# Creamos el archivo LaTeX.
rutaArchivoLaTeX,fLaTeX = funcionesBasicas.creaArchivoLaTeX(datos,argv[2],directorioFichas)
# Escribimos el preámbulo del archivo LaTeX.
funcionesBasicas.escribePreambuloLaTeX(datos,fLaTeX)
#######################################################################################
# FIN del código común para todas las fichas
#######################################################################################

#######################################################################################
# Parámetros
#######################################################################################
numeroOperacionesDistintas = 3
maximoPositivo = int(input("Introduce el máximo positivo: "))
opcion = int(input("¿Solo sumas y multiplicaciones sencillas (0), también multiplicaciones completas (1) o también divisiones (2)?: "))
maximoCoeficiente = 4
#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def compruebaCoeficientes(coeficientes,solucion):
    respuesta = 0

    suma = 0
    for nuku in range(1,len(coeficientes)):
        suma += coeficientes[nuku] * nuku
    suma += coeficientes[0]
    if suma == solucion:
        respuesta = 1
    # Para la división, comprobamos que ninguno es decimal, mediante módulo 1.
    for nuku in range(1,len(coeficientes)):
        if coeficientes[nuku] % 1 != 0:
            respuesta = 0
    return respuesta

def escribePolinomioEnLaTeX(coeficientes,letra):
    # Atencion: No pone los signos de dólar.
    cadena = ""
    for nuku in range(len(coeficientes)):
        if coeficientes[nuku] % 1 != 0:
            # Es un coeficiente no entero
            coeficienteEscrito = str(abs(coeficientes[nuku]))
        else:
            # Es un coeficiente entero
            coeficienteEscrito = str(abs(int(coeficientes[nuku])))
        if nuku == 0:
            if coeficientes[nuku] < 0:
                nuevaCadena = "-" + coeficienteEscrito
            elif coeficientes[nuku] > 0:
                nuevaCadena = "+" + coeficienteEscrito
            else:
                nuevaCadena = ""
        elif nuku == 1:
            if coeficientes[nuku] < 0:
                nuevaCadena = "-" + coeficienteEscrito + letra
            elif coeficientes[nuku] > 0:
                nuevaCadena = "+" + coeficienteEscrito + letra
            else:
                nuevaCadena = ""
        else:
            if coeficientes[nuku] < 0:
                nuevaCadena = "-" + coeficienteEscrito + letra + "^" + str(nuku)
            elif coeficientes[nuku] > 0:
                nuevaCadena = "+" + coeficienteEscrito + letra + "^" + str(nuku)
            else:
                nuevaCadena = ""
        cadena = nuevaCadena + cadena
    if len(cadena) >0 and cadena[0] == "+":
        cadena = cadena[1:] # Para quitar el signo más cuando está al principio.
    return cadena


# Solo sumas y multiplicaciones sencillas -------------------------------------------------------------------------------------------------
def generaOperacionesTipo1(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x,1)+B(x)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1)])
        B = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
#        print(coeficientesRespuesta)
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo2(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x,1)-B(x)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1)])
        B = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo3(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x,1)+B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
   
def generaOperacionesTipo4(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x,1)-B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo5(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x)-B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo6(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x)+B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas    

def generaOperacionesTipo7(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1)+B(x2,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo8(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1)-B(x2,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo9(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1)+B(x3,x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo10(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1)-B(x3,x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo11(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1)+B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo12(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1)-B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo13(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1)+B(x3,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo14(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1)-B(x3,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A-B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo15(numeroOperacionesDistintas, solucion, maximoPositivo):
    # M*A(x,1)+N*B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        M = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        N = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        coeficientesRespuesta = (M*A+N*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            if N < 0:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + str(N) + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            else:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+" + str(N) + "\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo16(numeroOperacionesDistintas, solucion, maximoPositivo):
    # M*A(x,1)-N*B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        M = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        N = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        coeficientesRespuesta = (M*A-N*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            if N < 0:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + str(N) + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            else:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-" + str(N) + "\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo17(numeroOperacionesDistintas, solucion, maximoPositivo):
    # M*A(x2,x,1)+N*B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        M = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        N = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        coeficientesRespuesta = (M*A+N*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            if N < 0:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + str(N) + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            else:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+" + str(N) + "\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas    

def generaOperacionesTipo18(numeroOperacionesDistintas, solucion, maximoPositivo):
    # M*A(x2,x,1)-N*B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        M = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        N = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        coeficientesRespuesta = (M*A-N*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            if N < 0:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + str(N) + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            else:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-" + str(N) + "\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo19(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x,1)+B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo20(numeroOperacionesDistintas, solucion, maximoPositivo):
    # -A(x3,x,1)+B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (-A+B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$-(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas    
    
def generaOperacionesTipo21(numeroOperacionesDistintas, solucion, maximoPositivo):
    # M*A(x2,x,1)+N*B(x3,x)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        M = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        N = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        coeficientesRespuesta = (M*A+N*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            if N < 0:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+(" + str(N) + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            else:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")+" + str(N) + "\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo22(numeroOperacionesDistintas, solucion, maximoPositivo):
    # M*A(x2,x,1)-N*B(x3,x)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        M = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        N = random.randrange(-1,2,2)*random.randrange(2, maximoCoeficiente)
        coeficientesRespuesta = (M*A-N*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            if N < 0:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-(" + str(N) + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            else:
                ejercicio = "$" + str(M) + "\cdot{}(" + escribePolinomioEnLaTeX(A.coef,'x') + ")-" + str(N) + "\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

# También multiplicaciones  -------------------------------------------------------------------------------------------------

def generaOperacionesTipo23(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x,1)*B(x)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1)])
        B = P([0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo24(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x,1)*B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo25(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1)*B(x2,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo26(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,0,x,1)*B(x3,x2,0,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo27(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,0,x,1)*B(x2,0,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo28(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1)*B(x3,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        B = P([random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),0,0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)])
        coeficientesRespuesta = (A*B).coef
        if compruebaCoeficientes(coeficientesRespuesta,solucion):
            ejercicio = "$(" + escribePolinomioEnLaTeX(A.coef,'x') + ")\cdot{}(" + escribePolinomioEnLaTeX(B.coef,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

# Divisiones -------------------------------------------------------------------------------------------------
def generaOperacionesTipo29(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1):B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo30(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1):B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)        
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo31(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1):B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)        
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo32(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1):B(x2,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)        
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
# Las pŕoximas cuatro son las cuatro anteriores. Las copiamos para equilibrar el número de operaciones de división (solo 4)
# frente al resto de operaciones.
def generaOperacionesTipo33(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x2,x,1):B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo34(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1):B(x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)        
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo35(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1):B(x2,x,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)        
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo36(numeroOperacionesDistintas, solucion, maximoPositivo):
    # A(x3,x2,x,1):B(x2,1)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        B = (random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1),0,random.randrange(-1,2,2)*random.randrange(1, maximoPositivo, 1))
        coeficientesCociente, coeficientesResto = numpy.polynomial.polynomial.polydiv(A, B)
        if compruebaCoeficientes(coeficientesCociente,solucion):
#            print(coeficientesCociente,coeficientesResto)        
            ejercicio = "$(" + escribePolinomioEnLaTeX(A,'x') + "):(" + escribePolinomioEnLaTeX(B,'x') + ")$"
            listaOperaciones.append(ejercicio)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


if opcion == 0:
    numeroTiposOperaciones = 22
elif opcion == 1:
    numeroTiposOperaciones = 28
else:
    numeroTiposOperaciones = 36
#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    # Ahora escribimos las instrucciones específicas para esta ficha.
    if opcion != 2:
        # No hay divisiones.
        enunciadoGeneral = r"Para desencriptarlo, tendr\'{a}s que resolver una serie de operaciones con polinomios. Cuando obtengas el polinomio resultante, \textbf{multiplica} el coeficiente de cada término de grado mayor o igual que 1 por su grado. Luego, \textbf{suma} los productos obtenidos y \textbf{añade} el término independiente. El resultado te indicará la letra."
    else:
        # Hay divisiones.
        enunciadoGeneral = r"Para desencriptarlo, tendr\'{a}s que resolver una serie de operaciones con polinomios. Cuando obtengas el polinomio resultante (el cociente en el caso de la división), \textbf{multiplica} el coeficiente de cada término de grado mayor o igual que 1 por su grado. Luego, \textbf{suma} los productos obtenidos y \textbf{añade} el término independiente. El resultado te indicará la letra."
    fLaTeX.write(enunciadoGeneral+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.5}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Polinomio resultante} & \textbf{Suma} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones para cada letra de este elemento.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento, y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán probablemente operaciones diferentes.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
#            print(elementos[koko][papa],operacionesDistintas[papa]+1)
            exec("cadenas = generaOperacionesTipo" + str(operacionesDistintas[papa]+1) + "(numeroOperacionesDistintas, codigoAlfabetico.get(elementos[koko][papa]), maximoPositivo)")
            pot = 2*random.randrange(0,int(len(cadenas)/2))
            fLaTeX.write(cadenas[pot]+r" & & & \\\hline"+"\n")
            #----------------------------------------------  
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
