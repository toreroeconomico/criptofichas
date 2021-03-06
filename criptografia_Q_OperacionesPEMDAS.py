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
numeroOperacionesDistintas = 3
maximoPositivo = int(input("Introduce el máximo positivo: "))

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

def generaOperacionesTipo1(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # 4·1/2^2-3^3·2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        Zp1 = generaEnteroAleatorio(-maximoPositivo,maximoPositivo,[0])
        Zp2 = generaEnteroAleatorio(-maximoPositivo,maximoPositivo,[0])
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        if Zp1*(Np1/Dp1)**2+Zp2*(Np2/Dp2)**3 == numeradorOperacion/denominadorOperacion:
            if Zp2 > 0:
                textoOperacion = "$" + str(Zp1) + "\cdot{}" + "\Big(\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}\Big)^2" + "+" + str(Zp2) + "\cdot{}\Big(" + "\dfrac{" + str(Np2) + "}{" + str(Dp2) + "}\Big)^3" + "$"
            else:
                textoOperacion = "$" + str(Zp1) + "\cdot{}" + "\Big(\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}\Big)^2" + "+(" + str(Zp2) + ")\cdot{}\Big(" + "\dfrac{" + str(Np2) + "}{" + str(Dp2) + "}\Big)^3" + "$" 
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo2(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # sqrt(Zp1)/Dp2-(1/2)*Zp2=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        Zp1 = random.randrange(2, min(14,maximoPositivo))**2
        Zp2 = generaEnteroAleatorio(-maximoPositivo,maximoPositivo,[0])
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        if math.sqrt(Zp1)/Dp2-(Np1/Dp1)*Zp2 == numeradorOperacion/denominadorOperacion:
            if Zp2 > 0:
                textoOperacion = "$" + "\dfrac{\sqrt{" + str(Zp1) + "}}{" + str(Dp2) + "}-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}\cdot{}" + str(Zp2) + "$"
            else:
                textoOperacion = "$" + "\dfrac{\sqrt{" + str(Zp1) + "}}{" + str(Dp2) + "}-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}\cdot{}(" + str(Zp2) + ")" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo3(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # sqrt(Zp1)/Dp2+(-1/2)*Zp2^2=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        Zp1 = random.randrange(2, min(14,maximoPositivo))**2
        Zp2 = generaEnteroAleatorio(-maximoPositivo,maximoPositivo,[0])
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        if math.sqrt(Zp1)/Dp2+(-Np1/Dp1)*Zp2**2 == numeradorOperacion/denominadorOperacion:
            textoOperacion = "$" + "\dfrac{\sqrt{" + str(Zp1) + "}}{" + str(Dp2) + "}+" + "\dfrac{(-" + str(Np1) + ")}{" + str(Dp1) + "}\cdot{}(" + str(Zp2) + ")^2" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo4(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # -1/2+2/3-2/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        if -(Np1/Dp1)+(Np2/Dp2)-(Np3/Dp3) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "$" + "-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "+" + "\dfrac{" + \
                str(Np2) + "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # -1/2·((-2)^3/3+2^3/3)=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        if (-Np1/Dp1)*(((-Np2)**3)/Dp2+(Np3**3/Dp3)) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "$" + "-" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\Big[\dfrac{(-" + str(Np2) + ")^3}{" + str(Dp2) + "}+\dfrac{" + str(Np3) + "^3}{" + str(Dp3) + "}\Big]" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # (1/2)^2·2/3-2/3:((-1)/3)^2=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np4, Dp4] = generaParejaNumeradorDenominador(maximoPositivo)
        if ((Np1/Dp1)**2)*(Np2/Dp2)-(Np3/Dp3)/(((-Np4)/Dp4)**2) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "$" + "\Big(\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}\Big)^2" + "\cdot{}" + "\dfrac{" + str(Np2) + "}{" + str(Dp2) + "}" + "-" + "\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}:\Big[\dfrac{(-" + str(Np4) + ")}{" + str(Dp4) + "}\Big]^2" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo7(numeradorOperacion, denominadorOperacion, numeroOperacionesDistintas, maximoPositivo):
    # 1/2·(sqrt(2/3)-2/3):1/3=
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        Zp1 = random.randrange(2, min(14,maximoPositivo))
        Zp2 = generaEnteroAleatorio(2,min(14,maximoPositivo),[Zp1])
        [Np1, Dp1] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np2, Dp2] = generaParejaNumeradorDenominador(maximoPositivo)
        [Np3, Dp3] = generaParejaNumeradorDenominador(maximoPositivo)
        if (Np1/Dp1)*((Zp1/Zp2)-(Np2/Dp2))/(Np3/Dp3) == numeradorOperacion/denominadorOperacion:
            textoOperacion = "$" + "\dfrac{" + str(Np1) + "}{" + str(Dp1) + "}" + "\cdot{}" + "\Big(\sqrt{\dfrac{" + str(Zp1**2) + "}{" + str(Zp2**2) + "}}" + "-" + "\dfrac{" + str(Np2) + "}{" + str(Dp2) + "}\Big):\dfrac{" + str(Np3) + "}{" + str(Dp3) + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

    
numeroTiposOperaciones = 7
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
#        print(elementos[koko][papa],":",str(operacionesDistintas[papa]+1))
        # Obtenemos el número correspondiente a cada letra del primer elemento, y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán probablemente operaciones diferentes.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
            exec("cadenas = generaOperacionesTipo" + str(operacionesDistintas[papa]+1) + "(codigoAlfabetico.get(elementos[koko][papa]), generaDenominador(codigoAlfabetico.get(elementos[koko][papa])), numeroOperacionesDistintas, maximoPositivo)")
            pot = 2*random.randrange(0,int(len(cadenas)/2))
            fLaTeX.write(cadenas[pot]+r" & & \\\hline"+"\n")
            #----------------------------------------------  
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
