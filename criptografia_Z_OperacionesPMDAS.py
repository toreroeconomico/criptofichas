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
numeroTiposOperaciones = 9
maximoPositivo = 25
minimoNegativo = -25
numeroOperacionesDistintas = 10

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaOperacionesTipo1(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 3·(-5)+(-5)·(-2)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        p1 = random.randrange(1, maximoPositivo)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        n3 = random.randrange(minimoNegativo, -1)
        if p1*n1+n2*n3 == resultadoOperacion:
            textoOperacion = str(p1) + "\cdot{}" + "(" + str(n1) + ")" + "+" + \
                "(" + str(n2) + ")" + "\cdot{}" + "(" + str(n3) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo2(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 3+(-5)+(-5)-(-2)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        p1 = random.randrange(1, maximoPositivo)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        n3 = random.randrange(minimoNegativo, -1)
        if p1+n1+n2-n3 == resultadoOperacion:
            textoOperacion = str(p1) + "+" + "(" + str(n1) + ")" + "+" + \
                "(" + str(n2) + ")" + "-" + "(" + str(n3) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo3(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 3·[7+(-5)-(-4)]+6=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        p1 = random.randrange(1, maximoPositivo)
        p2 = random.randrange(1, maximoPositivo)
        p3 = random.randrange(1, maximoPositivo)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        if p1*(p2+n1-n2)+p3 == resultadoOperacion:
            textoOperacion = str(p1) + "\cdot{}" + r"\big[" + str(p2) + "+" + "(" + str(
                n1) + ")" + "-" + "(" + str(n2) + ")" + r"\big]" + "+" + str(p3)
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo4(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -3-(-5)+4·(-2)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        p1 = random.randrange(1, maximoPositivo)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        n3 = random.randrange(minimoNegativo, -1)
        if n1-n2+p1*n3 == resultadoOperacion:
            textoOperacion = str(n1) + "-" + "(" + str(n2) + ")" + \
                "+" + str(p1) + "\cdot{}" + "(" + str(n3) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo5(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -3+(-5):(-2)+4:5·(-4)+3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        n0 = random.randrange(minimoNegativo, -1)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(3, 4)*n1
        p2 = random.randrange(1, maximoPositivo)
        p3 = random.randrange(1, 2)*p2
        p4 = random.randrange(1, maximoPositivo)
        n3 = random.randrange(minimoNegativo, -1)
        if int(n0+n2/n1+p3/p2*n3+p4) == resultadoOperacion:
            textoOperacion = str(n0) + "+" + "(" + str(n2) + ")" + ":" + "(" + str(
                n1) + ")" + "+" + str(p3) + ":" + str(p2) + "\cdot{}" + "(" + str(n3) + ")" + "+" + str(p4)
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo6(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -3+(-5)·(-2)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        n3 = random.randrange(minimoNegativo, -1)
        if n1+n2*n3 == resultadoOperacion:
            textoOperacion = str(n1) + "+" + "(" + str(n2) + ")" + \
                "\cdot{}" + "(" + str(n3) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo7(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 7+(-5)-(-2)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        p1 = random.randrange(1, maximoPositivo)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        if p1+n1-n2 == resultadoOperacion:
            textoOperacion = str(p1) + "+" + "(" + str(n1) + ")" + \
                "-" + "(" + str(n2) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo8(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -7+4+(-5):(-2)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        n1 = random.randrange(minimoNegativo, -1)
        p1 = random.randrange(1, maximoPositivo)
        n2 = random.randrange(minimoNegativo, -1)
        n3 = random.randrange(2,5)*n2
        if int(n1+p1+n3/n2) == resultadoOperacion:
            textoOperacion = str(n1) + "+" + str(p1) + "+" + "(" + str(n3) + ")" + ":" + "(" + str(n2) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo9(resultadoOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 4·(-7)-(-5)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        p1 = random.randrange(1, maximoPositivo)
        n1 = random.randrange(minimoNegativo, -1)
        n2 = random.randrange(minimoNegativo, -1)
        if p1*n1-n2 == resultadoOperacion:
            textoOperacion = str(p1) + r"\cdot{}" + "(" + str(n1) + ")" + \
                "-" + "(" + str(n2) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def convierteLetraAOperacion(tipoOperacion, numeroOperacionesDistintas, resultadoOperacion, maximoPositivo, minimoNegativo):
    if tipoOperacion == 0:
        return generaOperacionesTipo1(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 1:
        return generaOperacionesTipo2(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 2:
        return generaOperacionesTipo3(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 3:
        return generaOperacionesTipo4(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 4:
        return generaOperacionesTipo5(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 5:
        return generaOperacionesTipo6(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 6:
        return generaOperacionesTipo7(resultadoOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 7:
        return generaOperacionesTipo8(resultadoOperacion, 1, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 8:
        return generaOperacionesTipo9(resultadoOperacion, 1, maximoPositivo, minimoNegativo)


#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que resolver una serie de operaciones con números enteros. Cada vez que resuelvas una, busca \textbf{el resultado} en la tabla y anota la letra que le corresponde."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.75}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Resultado} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")

    # Añadimos al archivo fuente LaTeX las operaciones con enteros para el elemento que toque.
    # print(elementos[koko])
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente cada letra del primer elemento,
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            fLaTeX.write(r"$"+convierteLetraAOperacion(operacionesDistintas[papa],numeroOperacionesDistintas,codigoAlfabetico.get(elementos[koko][papa]), maximoPositivo, minimoNegativo)[0]+r"$ & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
