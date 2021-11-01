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
numeroTiposOperaciones = 6
maximoValor = 10

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################

def countWays(n): 
    # Calcula todas las posibles parejas de números que,
    # multiplicados, dan el valor pasado como argumento.
    count = 0
    i = 1
    parejas = []  
    # Counting number of pairs 
    # upto sqrt(n) - 1 
    if abs(n) > 1:
        while ((i * i)<abs(n)) :  
            if(abs(n) % i == 0): 
                count += 1
                if n<0:
                    parejas.append([int(i),int(n/i)])
                    parejas.append([-int(i),-int(n/i)])
                    parejas.append([int(n/i),int(i)])
                    parejas.append([-int(n/i),-int(i)])
                else:
                    parejas.append([int(i),int(n/i)])
                    parejas.append([-int(i),-int(n/i)])
                    parejas.append([int(n/i),int(i)])
                    parejas.append([-int(n/i),-int(i)])
            i += 1
    elif n == 1:
        count = 1
        parejas.append([int(1),int(1)])
        parejas.append([int(-1),int(-1)])
    elif n == -1:
        count = 1
        parejas.append([int(1),int(-1)])
        parejas.append([int(-1),int(1)])
    else:
        count = 1
        parejas.append([int(0),int(0)])
    return count,parejas
  
def generaEcuacionSinSolucion(maximoValor):
    seguir = 1
    while seguir:
        A = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        B = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if B*B < 4*A*C:
            seguir = 0
    respuesta = "$" + escribePolinomioEnLaTeX(P([C,B,A]).coef) + "=0$"        
    return respuesta

def generaEcuacionesTipo1(solucion, maximoValor):
    # x^2 + (A+B)x + A*B = 0
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    if soluciones[0] == 0 and soluciones[1] != 0:
        if soluciones[1] > 0:
            respuesta = "$x\cdot{}(x-" + str(soluciones[1]) + ")=0$"
        else:
            respuesta = "$x\cdot{}(x+" + str(-soluciones[1]) + ")=0$"    
    elif soluciones[1] == 0 and soluciones[0] != 0:
        if soluciones[0] > 0:
            respuesta = "$x\cdot{}(x-" + str(soluciones[0]) + ")=0$"
        else:
            respuesta = "$x\cdot{}(x+" + str(-soluciones[0]) + ")=0$"    
    else:
        A = P([-soluciones[0],1])
        B = P([-soluciones[1],1])
        respuesta = "$" + escribePolinomioEnLaTeX((A*B).coef) + "=0$"
    return respuesta

def generaEcuacionesTipo2(solucion, maximoValor):
    # x^2 + (A+B)x + A*B+C = C
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    if soluciones[0] == 0 and soluciones[1] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[1] > 0:
            respuesta = "$" + str(C) + "x\cdot{}(x-" + str(soluciones[1]) + ")=0$"
        else:
            respuesta = "$" + str(C) + "x\cdot{}(x+" + str(-soluciones[1]) + ")=0$"
    elif soluciones[1] == 0 and soluciones[0] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[0] > 0:
            respuesta = "$" + str(C) + "x\cdot{}(x-" + str(soluciones[0]) + ")=0$"
        else:
            respuesta = "$" + str(C) + "x\cdot{}(x+" + str(-soluciones[0]) + ")=0$"
    else:
        A = P([-soluciones[0],1])
        B = P([-soluciones[1],1])
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        respuesta = "$" + escribePolinomioEnLaTeX((A*B+P([C,0,0])).coef) + "=" + str(C) + "$"
    return respuesta

def generaEcuacionesTipo3(solucion, maximoValor):
    # Cx^2 + C·(A+B)x + C*A*B = 0
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    if soluciones[0] == 0 and soluciones[1] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[1] > 0:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x-" + str(soluciones[1]*C) + ")=0$"
        else:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x+" + str(-soluciones[1]*C) + ")=0$"
    elif soluciones[1] == 0 and soluciones[0] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[0] > 0:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x-" + str(soluciones[0]*C) + ")=0$"
        else:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x+" + str(-soluciones[0]*C) + ")=0$"
    else:
        A = P([-soluciones[0],1])
        B = P([-soluciones[1],1])
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
    respuesta = "$" + escribePolinomioEnLaTeX((C*A*B).coef) + "=0" + "$"
    return respuesta

def generaEcuacionesTipo4(solucion, maximoValor):
    # Cx^2 + C·(A+B)x + C*A*B+D = D
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    if soluciones[0] == 0 and soluciones[1] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[1] > 0:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x-" + str(soluciones[1]*C) + ")=0$"
        else:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x+" + str(-soluciones[1]*C) + ")=0$"
    elif soluciones[1] == 0 and soluciones[0] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[0] > 0:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x-" + str(soluciones[0]*C) + ")=0$"
        else:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x+" + str(-soluciones[0]*C) + ")=0$"
    else:
        A = P([-soluciones[0],1])
        B = P([-soluciones[1],1])
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
    respuesta = "$" + escribePolinomioEnLaTeX((C*A*B+D).coef) + "=" + str(D) + "$"
    return respuesta

def generaEcuacionesTipo5(solucion, maximoValor):
    # (C+D)x^2 + (C+D)·(A+B)x + (C+D)*A*B = (D)x^2 + (D)·(A+B)x + (D)*A*B
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    if soluciones[0] == 0 and soluciones[1] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[1] > 0:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x-" + str(soluciones[1]*C) + ")=0$"
        else:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x+" + str(-soluciones[1]*C) + ")=0$"    
    elif soluciones[1] == 0 and soluciones[0] != 0:
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        if soluciones[0] > 0:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x-" + str(soluciones[0]*C) + ")=0$"
        else:
            respuesta = "$" + str(D) + "x\cdot{}(" + str(C) + "x+" + str(-soluciones[0]*C) + ")=0$"    
    else:
        A = P([-soluciones[0],1])
        B = P([-soluciones[1],1])
        C = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        D = (-1)**random.randint(1,2)*random.randint(1,maximoValor)
        respuesta = "$" + escribePolinomioEnLaTeX(((C+D)*A*B).coef) + "=" + escribePolinomioEnLaTeX((D*A*B).coef) + "$"
    return respuesta

def generaEcuacionesTipo6(solucion, maximoValor):
    # (x-A)(x-B) = 0
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    if soluciones[0] == 0 and soluciones[1] != 0:
        respuesta = "$x\cdot{}(x-" + str(-soluciones[1]) + ")=0$"
    elif soluciones[1] == 0 and soluciones[0] != 0:
        respuesta = "$x\cdot{}(x-" + str(-soluciones[0]) + ")=0$"
    elif soluciones[1] == 0 and soluciones[0] == 0:
        respuesta = "$" + str((-1)**random.randint(1,2)*random.randint(1,maximoValor)) + "x^2=0$"
    else:
        respuesta = "$(x"
        if soluciones[0] > 0:
            respuesta += str(-soluciones[0]) + ")"
        else:
            respuesta += "+" + str(-soluciones[0]) + ")"
        respuesta += "\cdot{}(x"
        if soluciones[1] > 0:
            respuesta += str(-soluciones[1]) + ")=0$"
        else:
            respuesta += "+" + str(-soluciones[1]) + ")=0$"
    return respuesta

def escribePolinomioEnLaTeX(coeficientes):
    # Atencion: No pone los signos de dólar.
    #coeficientes = np.flip(coeficientes,axis=1) # Da error.
    coeficientes = coeficientes[::-1]
    cadena = ""
    if len(coeficientes) == 1:
        cadena += str(int(coeficientes[0]))
    elif len(coeficientes) == 2:
        cadena += str(int(coeficientes[0])) + "x"
        if coeficientes[1] > 0:
            cadena += "+" + str(int(coeficientes[1]))
        elif coeficientes[1] < 0:
            cadena += str(int(coeficientes[1]))
    elif len(coeficientes) > 2:
        for kuku in range(len(coeficientes)-2):
            if coeficientes[kuku] > 0:
                if coeficientes[kuku] == 1:
                    cadena += "x^{" + str(int(len(coeficientes)-1-kuku)) + "}"
                else:
                    cadena += str(int(coeficientes[kuku])) + "x^{" + str(int(len(coeficientes)-1-kuku)) + "}"
            elif coeficientes[kuku] < 0:
                if coeficientes[kuku] == -1:
                    cadena += "-x^{" + str(int(len(coeficientes)-1-kuku)) + "}"
                else:
                    cadena += str(int(coeficientes[kuku])) + "x^{" + str(int(len(coeficientes)-1-kuku)) + "}"
        kuku = len(coeficientes)-2
        if coeficientes[kuku] > 0:
            cadena += "+" + str(int(coeficientes[kuku])) + "x"
        elif coeficientes[kuku] < 0:
            cadena += str(int(coeficientes[kuku])) + "x"
        if coeficientes[kuku+1] > 0:
            cadena += "+" + str(int(coeficientes[kuku+1]))
        elif coeficientes[kuku+1] < 0:
            cadena += str(int(coeficientes[kuku+1]))
    return cadena           

def convierteLetraAOperacion(tipoOperacion, solucion, maximoValor):
    if tipoOperacion == 0:
        return generaEcuacionesTipo1(solucion, maximoValor)
    elif tipoOperacion == 1:
        return generaEcuacionesTipo2(solucion, maximoValor)
    elif tipoOperacion == 2:
        return generaEcuacionesTipo3(solucion, maximoValor)
    elif tipoOperacion == 3:
        return generaEcuacionesTipo4(solucion, maximoValor)
    elif tipoOperacion == 4:
        return generaEcuacionesTipo5(solucion, maximoValor)
    elif tipoOperacion == 5:
        return generaEcuacionesTipo6(solucion, maximoValor)

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendrás que resolver las siguientes ecuaciones de 2º grado. Cuando tenga soluciones reales, busca \textbf{su producto} en la tabla y anota la letra correspondiente. En caso contrario, es un espacio en blanco."+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\vspace{0.25\baselineskip}"+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.0}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(
        r"	\textbf{Ecuación} & \textbf{Solución 1} & \textbf{Solución 2} & \textbf{Producto} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    print(elementos[koko])
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada par de letras del primer elemento,
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            fLaTeX.write(r"	"+convierteLetraAOperacion(random.randrange(0, numeroTiposOperaciones),
                                             codigoAlfabetico.get(elementos[koko][papa]),
                                             maximoValor)+r" & & & & \\\hline"+"\n")
        else:
            # Para los espacios en blanco generamos ecuaciones sin solución real.
            fLaTeX.write(r"	"+generaEcuacionSinSolucion(maximoValor)+r" & & & &  \\\hline"+"\n")
            
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
