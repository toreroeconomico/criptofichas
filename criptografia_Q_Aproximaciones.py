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
numeroTiposOperaciones = 5
numeroOperacionesDistintas = 1
maximoValor = 15

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def ponParentesis(valor):
    if valor < 0:
        cadena = "(" + str(valor) + ")"
    else:
        cadena= str(valor)
    return cadena    

def calculaAproximado(exacto, orden, metodo):
    if orden == 0:
        step_size = Decimal("1")
    elif orden == 1:
        step_size = Decimal("0.1")
    elif orden == 2:
        step_size = Decimal("0.01")
    elif orden == 3:
        step_size = Decimal("0.001")
    elif orden == 4:
        step_size = Decimal("0.0001")
    elif orden == 5:
        step_size = Decimal("0.00001")
    if metodo == 0:
        aproximado = Decimal(exacto).quantize(step_size, ROUND_HALF_UP)
    elif metodo == 1:
        aproximado = Decimal(exacto).quantize(step_size, ROUND_CEILING)
    elif metodo == 2:
        aproximado = Decimal(exacto).quantize(step_size, ROUND_FLOOR)
    
    kk = str(aproximado).replace('.', '')
    if len(kk) > 2 and aproximado < 0:
        # Entonces quedarse con las dos últimas cifras elimina el signo negativo y hay que ponérselo.
        ultimasCifras = (-1)*int(str(aproximado).replace('.', '')[-2:])
    else:
        ultimasCifras = int(str(aproximado).replace('.', '')[-2:])
    return aproximado,ultimasCifras
    
def generaOperacionesTipo1(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # A*B+(C/D)-E*F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        B = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        C = random.randint(1,maximoValor)
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = A*B+C/D-E*F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            # A*B+(C/D)-E*F
            textoOperacion = r"$" + ponParentesis(A) + "\cdot{}" + ponParentesis(B) + " + \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "} - " + ponParentesis(E) + "\cdot{}" + ponParentesis(F) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo2(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # A/B-(C/D)+E-F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = random.randint(1,maximoValor)
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = A/B-C/D+E-F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            # A/B-(C/D)+E-F
            textoOperacion = r"$" + "\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "} - \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "} + " + ponParentesis(E) + "-" + ponParentesis(F) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo3(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # (A/B)*E-(C/D)*F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = random.randint(1,maximoValor)
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = (A/B)*E-(C/D)*F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            # (A/B)*E-(C/D)*F
            textoOperacion = r"$" + "\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}\cdot{}" + ponParentesis(E) + " - \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "}\cdot{}" + ponParentesis(F) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo4(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # E*(A/B-C)+F*(D-G)
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        G = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = E*(A/B-C)+F*(D-G)
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            # E*(A/B-C)+F*(D-G)
            textoOperacion = r"$" + ponParentesis(E) + "\cdot{}\Big[\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}-" + ponParentesis(C) + "\Big] + " + ponParentesis(F) + "\cdot{}(" + ponParentesis(D) + " - " + ponParentesis(G) + ")" + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # (A/B+C)/E-(D-G)/F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        D = random.randint(2,maximoValor)
        E = random.randrange(-1,2,2)*round(random.uniform(0.5,maximoValor),random.randint(orden+1,orden+3))
        F = random.randrange(-1,2,2)*round(random.uniform(0.5,maximoValor),random.randint(orden+1,orden+3))
        G = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = (A/B+C)/E-(D-G)/F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            # (A/B+C)/E-(D-G)/F
            textoOperacion = r"$" + "\Big[\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}+" + ponParentesis(C) + "\Big]:" + ponParentesis(E) + "-(" + ponParentesis(D) + "-" + ponParentesis(G) + "):" + ponParentesis(F) + r"$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def convierteLetraAOperacion(tipoOperacion, numeroOperacionesDistintas, solucion, metodo, orden, maximoValor):
    if tipoOperacion == 0:
        return generaOperacionesTipo1(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 1:
        return generaOperacionesTipo2(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 2:
        return generaOperacionesTipo3(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 3:
        return generaOperacionesTipo4(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 4:
        return generaOperacionesTipo5(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################

for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que calcular el resultado de una serie de operaciones con números racionales y aproximarlo al orden pedido (O) y con el método pedido (M). Luego, busca en la tabla el número formado por \textbf{las dos últimas cifras} y anota la letra correspondiente. Si el resultado es negativo, el número también."+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"`Red' significa `Redondeo', `Exc' significa `Por exceso' y `Def' significa 'Por defecto'' "+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.5}"+"\n")
    fLaTeX.write(r"\begin{small}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|c|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{O} & \textbf{M} & \textbf{Aproximación} & \textbf{Número} & \textbf{Letra}\\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")

    # Añadimos al archivo fuente LaTeX las operaciones con enteros para el elemento que toque.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            metodo = random.randrange(0, 3)
            orden = random.randrange(0, 6)
            textoOperacion = convierteLetraAOperacion(operacionesDistintas[papa],
                                             numeroOperacionesDistintas,
                                             codigoAlfabetico.get(elementos[koko][papa]),
                                             metodo,
                                             orden,
                                             maximoValor)[0].replace('.',',')
            if metodo == 0:
                metodo = "Red"
            elif metodo == 1:
                metodo = "Exc"
            elif metodo == 2:
                metodo = "Def"
            if orden == 0:
                orden = "U"
            elif orden == 1:
                orden = "d"
            elif orden == 2:
                orden = "c"
            elif orden == 3:
                orden = "m"
            elif orden == 4:
                orden = "dm"
            elif orden == 5:
                orden = "cm"
            fLaTeX.write(textoOperacion + r" & " + orden + r" & " + metodo + r" & & & \\\hline " + "\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{small}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
