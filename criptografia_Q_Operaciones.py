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
numeroTiposOperaciones = 7
numeroOperacionesDistintas = 5
maximoPositivo = 60
minimoNegativo = -60

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaOperacionesTipo1(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 4·1/2-3·2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Zp1 = random.randrange(1, maximoPositivo)
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        Zp2 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        if Zp1*(Np1/Dp1)-Zp2*(Np2/Dp2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = str(Zp1) + "\cdot{}" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + \
                "-" + str(Zp2) + "\cdot{}" + "\dfrac{" + str(Np2) + "}{" + str(Dp2) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo2(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 1/2-2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        if (Np1/Dp1)-(Np2/Dp2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "-" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo3(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -1/2+2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Nn1 = random.randrange(minimoNegativo, -1)
        Dp1 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        if (Nn1/Dp1)+(Np2/Dp2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Nn1) + "}{" + str(Dp1) + "}" + "+" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo4(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -1/2+2/3-2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        Np3 = random.randrange(1, maximoPositivo)
        Dp3 = random.randrange(1, maximoPositivo)
        if -(Np1/Dp1)+(Np2/Dp2)-(Np3/Dp3) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "+" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # -1/2·(2/3-2/3)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        Np3 = random.randrange(1, maximoPositivo)
        Dp3 = random.randrange(1, maximoPositivo)
        if (-Np1/Dp1)*((Np2/Dp2)-(Np3/Dp3)) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\Big(\dfrac{" + str(Np2) + \
                "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}\Big)"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 1/2·2/3-2/3:1/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        Np3 = random.randrange(1, maximoPositivo)
        Dp3 = random.randrange(1, maximoPositivo)
        Np4 = random.randrange(1, maximoPositivo)
        Dp4 = random.randrange(1, maximoPositivo)
        if (Np1/Dp1)*(Np2/Dp2)-(Np3/Dp3)/(Np4/Dp4) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\dfrac{" + str(Np2) + \
                "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}:\dfrac{" + str(Np4) + "}{" + str(Dp4) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo7(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # 1/2·(2/3-2/3):1/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        Np2 = random.randrange(1, maximoPositivo)
        Dp2 = random.randrange(1, maximoPositivo)
        Np3 = random.randrange(1, maximoPositivo)
        Dp3 = random.randrange(1, maximoPositivo)
        Np4 = random.randrange(1, maximoPositivo)
        Dp4 = random.randrange(1, maximoPositivo)
        if (Np1/Dp1)*((Np2/Dp2)-(Np3/Dp3))/(Np4/Dp4) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\Big(\dfrac{" + str(Np2) + \
                "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}\Big):\dfrac{" + str(Np4) + "}{" + str(Dp4) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def convierteLetraAOperacion(tipoOperacion, numeroOperacionesDistintas, numeradorOperacion, denominadorOperacion, maximoPositivo, minimoNegativo):
    if tipoOperacion == 0:
        return generaOperacionesTipo1(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 1:
        return generaOperacionesTipo2(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 2:
        return generaOperacionesTipo3(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 3:
        return generaOperacionesTipo4(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 4:
        return generaOperacionesTipo5(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 5:
        return generaOperacionesTipo6(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 6:
        return generaOperacionesTipo7(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    
def convierteFraccionALatex(fraccion):
    if fraccion.denominator == 1:
        return ("$" + str(fraccion.numerator) + "$")
    else:
        return ("$\dfrac{" + str(fraccion.numerator) + "}{" + str(fraccion.denominator) + "}$")
    
def generaDenominador(numerador):
    if numerador == 0:
        return 1
    elif abs(numerador) < 5:
        return 2*abs(numerador)+1
    else:
        return abs(numerador)+random.randrange(-1,2,2)

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    # Ahora escribimos las instrucciones específicas para esta ficha.
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que resolver una serie de operaciones con números racionales. Cada vez que resuelvas una, busca \textbf{el numerador irreducible} en la tabla y apunta la letra que le corresponde. Si la fracción resultante es negativa, considera que el numerador es negativo."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.75}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Resultado} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones para cada letra de este elemento.
    print(elementos[koko])
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán
        # probablemente operaciones diferentes.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            fLaTeX.write(r" $"+convierteLetraAOperacion(random.randrange(0,numeroTiposOperaciones),numeroOperacionesDistintas,codigoAlfabetico.get(elementos[koko][papa]),
                                             generaDenominador(codigoAlfabetico.get(elementos[koko][papa])),
                                             maximoPositivo, minimoNegativo)[0]+r"$ & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
