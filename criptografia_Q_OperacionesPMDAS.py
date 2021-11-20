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
numeroOperacionesDistintas = 4
maximoPositivo = 40

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaEnteroAleatorio(limiteInferior,limiteSuperior,listaExcluidos):
    seguir = 1
    entero = []
    while seguir == 1:
        entero = random.randrange(limiteInferior, limiteSuperior)
        if entero not in listaExcluidos:
            seguir = 0
    return entero

def generaParejaNumeradorDenominador(maximoPositivo):
    seguir = 1
    while seguir == 1:
        Np1 = random.randrange(1, maximoPositivo)
        Dp1 = random.randrange(1, maximoPositivo)
        if Np1 != Dp1:
            seguir = 0
    return Np1,Dp1        

def generaOperacionesTipo1(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # 4·1/2-3·2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Zp1 = generaEnteroAleatorio(-maximoPositivo,maximoPositivo,[0])
        Zp2 = generaEnteroAleatorio(2,maximoPositivo,[0])
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        if Zp1*(Np1/Dp1)-Zp2*(Np2/Dp2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = str(Zp1) + "\cdot{}" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + \
                "-" + str(Zp2) + "\cdot{}" + "\dfrac{" + str(Np2) + "}{" + str(Dp2) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo2(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # 1/2-2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        if (Np1/Dp1)-(Np2/Dp2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "-" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo3(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # -1/2+2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        Nn1 = random.randrange(-maximoPositivo, -1)
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        if (Nn1/Dp1)+(Np2/Dp2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Nn1) + "}{" + str(Dp1) + "}" + "+" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo4(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # -1/2+2/3-2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        if -(Np1/Dp1)+(Np2/Dp2)-(Np3/Dp3) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "+" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # -1/2·(2/3-2/3)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        if (-Np1/Dp1)*((Np2/Dp2)-(Np3/Dp3)) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\Big(\dfrac{" + str(Np2) + \
                "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}\Big)"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # 1/2·2/3-2/3:1/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np4, Dp4] = generaParejaNumeradorDenominador(maximoPositivo)
        if (Np1/Dp1)*(Np2/Dp2)-(Np3/Dp3)/(Np4/Dp4) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\dfrac{" + str(Np2) + \
                "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}:\dfrac{" + str(Np4) + "}{" + str(Dp4) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo7(numeradorOperacion, denominadorOperacion, numeroOperaciones, maximoPositivo):
    # 1/2·(2/3-2/3):1/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np4, Dp4] = generaParejaNumeradorDenominador(maximoPositivo)
        if (Np1/Dp1)*((Np2/Dp2)-(Np3/Dp3))/(Np4/Dp4) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\Big(\dfrac{" + str(Np2) + \
                "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}\Big):\dfrac{" + str(Np4) + "}{" + str(Dp4) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def convierteLetraAOperacion(tipoOperacion, numeroOperacionesDistintas, numeradorOperacion, denominadorOperacion, maximoPositivo):
    if tipoOperacion == 0:
        return generaOperacionesTipo1(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    elif tipoOperacion == 1:
        return generaOperacionesTipo2(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    elif tipoOperacion == 2:
        return generaOperacionesTipo3(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    elif tipoOperacion == 3:
        return generaOperacionesTipo4(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    elif tipoOperacion == 4:
        return generaOperacionesTipo5(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    elif tipoOperacion == 5:
        return generaOperacionesTipo6(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    elif tipoOperacion == 6:
        return generaOperacionesTipo7(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo)
    
def convierteFraccionALatex(fraccion):
    if fraccion.denominator == 1:
        return ("$" + str(fraccion.numerator) + "$")
    else:
        return ("$\dfrac{" + str(fraccion.numerator) + "}{" + str(fraccion.denominator) + "}$")

def generaDenominador(numerador):
    denominador = []
    if numerador == 0:
        denominador = 1
    else:
        seguir = 1
        while seguir == 1:
            denominador = generaEnteroAleatorio(1, 7, [0])
            if denominador == 1: # Es un número natural.
                seguir = 0
            elif math.gcd(numerador,denominador) == 1: # Son primos entre sí.
                seguir = 0 
    return denominador

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
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        #print(elementos[koko][papa],":",str(operacion+1))
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán
        # probablemente operaciones diferentes.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            fLaTeX.write(r" $"+convierteLetraAOperacion(operacionesDistintas[papa],numeroOperacionesDistintas,codigoAlfabetico.get(elementos[koko][papa]),
                                             generaDenominador(codigoAlfabetico.get(elementos[koko][papa])),
                                             maximoPositivo)[0]+r"$ & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
