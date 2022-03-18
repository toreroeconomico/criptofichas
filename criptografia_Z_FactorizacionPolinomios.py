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
maximoPositivoRaices = input("Introduce el máximo positivo para cada raíz (por defecto, 7): ")
if len(maximoPositivoRaices) == 0:
    maximoPositivoRaices = 7
minimoNegativoRaices = -maximoPositivoRaices
maximoTI = input("Introduce el máximo valor del término independiente, o sea, el producto de todas las raíces (por defecto, 42): ")
if len(maximoTI) == 0:
    maximoTI = 42
maximoPositivoFactorComun = input("Introduce el máximo positivo para el coeficiente del factor común  (por defecto, 15): ")
if len(maximoPositivoFactorComun) == 0:
    maximoPositivoFactorComun = 15
numeroOperacionesDistintas = 3

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def escribePolinomioEnLaTeX(coeficientes):
    # Atencion: No pone los signos de dólar.
    cadena = ""
    for nuku in range(len(coeficientes)):
        if nuku == 0:
            if coeficientes[nuku] < 0:
                nuevaCadena = "-" + str(abs(int(coeficientes[nuku])))
            elif coeficientes[nuku] > 0:
                nuevaCadena = "+" + str(abs(int(coeficientes[nuku])))
            else:
                nuevaCadena = ""
        elif nuku == 1:
            if coeficientes[nuku] < 0:
                nuevaCadena = "-" + str(abs(int(coeficientes[nuku]))) + "x"
            elif coeficientes[nuku] > 0:
                nuevaCadena = "+" + str(abs(int(coeficientes[nuku]))) + "x"
            else:
                nuevaCadena = ""
        else:
            if coeficientes[nuku] < 0:
                nuevaCadena = "-" + str(abs(int(coeficientes[nuku]))) + "x^" + str(nuku)
            elif coeficientes[nuku] > 0:
                nuevaCadena = "+" + str(abs(int(coeficientes[nuku]))) + "x^" + str(nuku)
            else:
                nuevaCadena = ""
        cadena = nuevaCadena + cadena
    if cadena[0] == "+":
        cadena = cadena[1:] # Para quitar el signo más cuando está al principio.
    return cadena
    
def generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices):
    raices = random.sample(range(minimoNegativoRaices, maximoPositivoRaices+1), numeroRaices)
    return raices
    
def generaOperacionesTipo1(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 2 raíces, todas distintas
    numeroRaices = 2
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[0] + raices[1] == resultadoOperacion and abs(raices[0]*raices[1]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo2(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 2 raíces, iguales, para hacerlo por identidad notable
    numeroRaices = 1
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if 2*raices[0] == resultadoOperacion and abs(raices[0]*raices[0]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[0],1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo3(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 2 raíces, opuestas, para hacerlo por identidad notable
    numeroRaices = 1
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[0]- raices[0] == resultadoOperacion and abs(raices[0]*raices[0]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([raices[0],1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas   

def generaOperacionesTipo4(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 3 raíces, todas distintas
    numeroRaices = 3
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[0] + raices[1] + raices[2] == resultadoOperacion and abs(raices[0]*raices[1]*raices[2]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            binomio3 = P([-raices[2],1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo5(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 4 raíces, todas distintas
    numeroRaices = 4
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[0] + raices[1] + raices[2] + raices[3] == resultadoOperacion and abs(raices[0]*raices[1]*raices[2]*raices[3]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            binomio3 = P([-raices[2],1])
            binomio4 = P([-raices[3],1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3*binomio4).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 3 raíces, 2 iguales
    numeroRaices = 2
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if 2*raices[0] + raices[1] == resultadoOperacion and abs(raices[0]*raices[0]*raices[1]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            binomio3 = binomio1
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo7(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 4 raíces, 2 iguales
    numeroRaices = 3
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if 2*raices[0] + raices[1] + raices[2] == resultadoOperacion and abs(raices[0]*raices[0]*raices[1]*raices[2]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            binomio3 = P([-raices[2],1])
            binomio4 = binomio1
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3*binomio4).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo8(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 4 raíces, al menos 1 es 0
    numeroRaices = 3
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[0] + raices[1] + raices[2] == resultadoOperacion:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            binomio3 = P([-raices[2],1])
            binomio4 = P([0,1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3*binomio4).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo9(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 4 raíces, al menos 2 son 0
    numeroRaices = 2
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[0] + raices[1] == resultadoOperacion:
            binomio1 = P([-raices[0],1])
            binomio2 = P([-raices[1],1])
            binomio3 = P([0,1])
            binomio4 = P([0,1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3*binomio4).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo10(resultadoOperacion, numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices):
    # 4 raíces, al menos 2 son opuestas
    numeroRaices = 3
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        coeficienteFactorComun = random.randrange(-1,2,2)*random.randrange(1, maximoPositivoFactorComun)
        raices = generaRaicesDistintas(maximoPositivoRaices,minimoNegativoRaices,numeroRaices)
        if raices[1] + raices[2] == resultadoOperacion and abs(raices[0]*raices[0]*raices[1]*raices[2]) <= maximoTI:
            binomio1 = P([-raices[0],1])
            binomio2 = P([raices[0],1])
            binomio3 = P([-raices[1],1])
            binomio4 = P([-raices[2],1])
            textoOperacion = r"$" + escribePolinomioEnLaTeX((coeficienteFactorComun*binomio1*binomio2*binomio3*binomio4).coef) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

numeroTiposOperaciones = 10
#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que factorizar los siguientes polinomios. Escribe, al lado, cómo queda el polinomio factorizado. Luego, \textbf{suma todas sus raíces}, busca el resultado en la tabla y anota la letra correspondiente."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.75}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Polinomio factorizado} & \textbf{Raíces} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones con enteros para el elemento que toque.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
#        print(elementos[koko][papa],operacionesDistintas[papa]+1)
        ##################################################################################3
        # Hay que poner este parche para evitar que el programa trate de encriptar cualquier letra distinta de la N (asociada al valor 0)
        # con un ejercicio tipo 3, de 2 raíces opuestas, porque en dicho caso, la suma de raíces siempre da 0.
        operacion = operacionesDistintas[papa]+1
        if operacion == 3:
            if codigoAlfabetico.get(elementos[koko][papa]) != 0:
                operacion = 6
        # Hay que poner este parche para evitar que el programa trate de encriptar cualquier letra asociada a valores pares
        # con un ejercicio tipo 2, de 2 raíces iguales, o con el 3, de raíces opuestas, porque en el primer caso la suma de
        # raíces nunca puede ser impar y en el segundo caso, nunca puede ser distinta de 0.
        if operacion == 2:
            if codigoAlfabetico.get(elementos[koko][papa]) % 2 == 1:
                operacion = 6
        # Obtenemos el número correspondiente cada letra del primer elemento,
        # y generamos una operación que da ese número como resultado.
        ##################################################################################3
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
            exec("cadenas = generaOperacionesTipo" + str(operacion) + "(codigoAlfabetico.get(elementos[koko][papa]), numeroOperacionesDistintas, maximoPositivoRaices, minimoNegativoRaices)")
            pot = 2*random.randrange(0,int(len(cadenas)/2))
            fLaTeX.write(cadenas[pot]+r" & & \textcolor{white}{x=-2,x=-2,x=-2,x=-2,x=-2} & \\\hline"+"\n")
            #----------------------------------------------  
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
