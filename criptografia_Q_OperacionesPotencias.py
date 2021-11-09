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


maximoPositivo = int(input("Introduce el máximo positivo: "))
facil = int(input("¿Fácil (0) o difícil (1)?: "))
if facil == 0:
    numeroTiposOperaciones = 8
else:
    numeroTiposOperaciones = 4
numeroOperacionesDistintas = 5
minimoNegativo = -maximoPositivo

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaOperacionesTipo1(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # (base^exp1·base^exp2)/(base^exp3·base^exp4) OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        base = random.randrange(round(maximoPositivo/2), maximoPositivo)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)
        if (exp1+exp2-exp3-exp4) == exponenteSolucion:
            textoOperacion = r"\dfrac{" + str(base) + r"^{" + str(exp1) + r"}\cdot{}" + str(base) + r"^{" + str(exp2) + r"}" + r"}{" +  str(base) + r"^{" + str(exp3) + r"}\cdot{}" + str(base) + r"^{" + str(exp4) + r"}" + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo2(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # base1 = factor1·factor2
    # base2 = factor3·factor4
    # (base1^exp1·factor3^exp1·factor4^exp1)/(factor1^exp2·base2^exp2·factor2^exp2) OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        factor2 = random.randrange(2,10)
        factor3 = random.randrange(2,10)
        factor4 = random.randrange(2,10)
        base1 = factor1*factor2
        base2 = factor3*factor4
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        if (exp1-exp2) == exponenteSolucion:
            textoOperacion = r"\dfrac{" + str(base1) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor3) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor4) + r"^{" + str(exp1) + r"}" + r"}{" +  str(factor1) + r"^{" + str(exp2) + r"}\cdot{}" + str(base2) + r"^{" + str(exp2) + r"}\cdot{}" + str(factor2) + r"^{" + str(exp2) + r"}" + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo3(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # (factor1^exp0)^exp1·factor1^exp2)/(factor1^exp3):factor1^exp4 OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        exp0 = random.randrange(2,4)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)
        base1 = factor1**exp0        
        if (exp0*exp1+exp2-exp3-exp4) == exponenteSolucion:
            textoOperacion = r"\dfrac{" + str(base1) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor1) + r"^{" + str(exp2) + r"}}{" +  str(factor1) + r"^{" + str(exp3) + r"}}:" + str(factor1) + r"^{" + str(exp4) + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo4(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # (factor1^3^exp1^exp2)/(factor1^2^exp2^exp3)·factor1^exp1 OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)        
        if (3*exp1*exp2-2*exp2*exp3+exp4) == exponenteSolucion:
            textoOperacion = r"\dfrac{(" + str(factor1**3) + r"^{" + str(exp1) + r"})^{" + str(exp2) + r"}}{(" + str(factor1**2) + r"^{" + str(exp2) + r"})^{" + str(exp3) + "}}\cdot{}" + str(factor1) + r"^{" + str(exp4) + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo5(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # ((factor1^2)^exp1·(factor1^3)^exp2)/((factor1^2)^exp3·factor^exp4) OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)        
        if (2*exp1+3*exp2-2*exp3-exp4) == exponenteSolucion:
            textoOperacion = r"\dfrac{" + str(factor1**2) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor1**3) + r"^{" + str(exp2) + r"}}{" + str(factor1**2) + r"^{" + str(exp3) + r"}\cdot{}" + str(factor1) + r"^{" + str(exp4) + r"}}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # (factor1/factor2)^exp1·(factor1^3/factor2)^exp2)·(factor2/factor1^2)^-exp3
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        factor2 = random.randrange(2,10)        
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(2, maximoPositivo)
        if (exp1+3*exp2+2*exp3) == (2*exp1+2*exp2+exp3) and (exp1+3*exp2+2*exp3) == exponenteSolucion:
            textoOperacion = r"\Big(\dfrac{" + str(factor1) + r"}{" + str(factor2**2) + r"}\Big)^{" + str(exp1) + r"}\cdot{}\Big(\dfrac{" + str(factor1**3) + r"}{" + str(factor2**2) + r"}\Big)^{" + str(exp2) + r"}\cdot{}" + r"\Big(\dfrac{" + str(factor2) + r"}{" + str(factor1**2) + r"}\Big)^{" + str(-exp3) + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas        

def generaOperacionesTipo7(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # (factor1^exp1)/(factor2^exp2)·(1/factor1^exp3)·factor2^-exp4 OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        factor2 = random.randrange(2,10)        
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(2, maximoPositivo)
        exp4 = random.randrange(2, maximoPositivo)
        if (exp1-exp3) == (exp2+exp4) and (exp1-exp3) == exponenteSolucion:
            textoOperacion = r"\dfrac{" + str(factor1) + r"^{" + str(exp1) + r"}}{" + str(factor2) + r"^{" + str(exp2) + r"}}\cdot{}\dfrac{1}{" + str(factor1) + r"^{" + str(exp3) + "}}\cdot{}" + str(factor2) + r"^{" + str(-exp4) + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo8(exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo):
    # (factor1^exp1)/(factor2^exp2)·(1/factor1^2^exp3)·factor2^-exp4 OK
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        factor2 = random.randrange(2,10)        
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(2, maximoPositivo)
        exp4 = random.randrange(2, maximoPositivo)
        if (exp1-2*exp3)==(exp2+exp4) and (exp2+exp4) == exponenteSolucion:
            textoOperacion = r"\dfrac{" + str(factor1) + r"^{" + str(exp1) + r"}}{" + str(factor2) + r"^{" + str(exp2) + r"}}\cdot{}\dfrac{1}{" + str(factor1**2) + r"^{" + str(exp3) + "}}\cdot{}" + str(factor2) + r"^{" + str(-exp4) + r"}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas    

def convierteLetraAOperacion(tipoOperacion, numeroOperacionesDistintas, exponenteSolucion, maximoPositivo, minimoNegativo):
    if tipoOperacion == 0:
        return generaOperacionesTipo1(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 1:
        return generaOperacionesTipo2(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 2:
        return generaOperacionesTipo3(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 3:
        return generaOperacionesTipo4(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 4:
        return generaOperacionesTipo5(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 5:
        return generaOperacionesTipo6(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 6:
        return generaOperacionesTipo7(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 7:
        return generaOperacionesTipo8(exponenteSolucion, numeroOperacionesDistintas, maximoPositivo, minimoNegativo)        
    

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    # Ahora escribimos las instrucciones específicas para esta ficha.
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que resolver una serie de operaciones con potencias. El objetivo en cada una de ellas es reducir la operación a una única potencia. Cuando lo hayas conseguido, busca \textbf{el exponente} en la tabla y apunta la letra que le corresponde."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.75}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Potencia única} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones para cada letra de este elemento.
    print(elementos[koko])
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán
        # probablemente operaciones diferentes.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            fLaTeX.write(r" $"+convierteLetraAOperacion(random.randrange(0,numeroTiposOperaciones),numeroOperacionesDistintas,codigoAlfabetico.get(elementos[koko][papa]),maximoPositivo, minimoNegativo)[0]+r"$ & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
