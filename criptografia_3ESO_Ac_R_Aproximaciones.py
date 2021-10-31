#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:46:16 2020

@author: sergio
"""
import sys
import subprocess
import numpy as np
import random
import math
import csv
import time
import escribeCabeceraLaTeX
import escribeInicioFichaLaTeX
import escribeFinalFichaLaTeX
from sys import argv
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP

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
            textoOperacion = ponParentesis(A) + "\cdot{}" + ponParentesis(B) + " + \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "} - " + ponParentesis(E) + "\cdot{}" + ponParentesis(F)
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
            textoOperacion = "\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "} - \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "} + " + ponParentesis(E) + "-" + ponParentesis(F)
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
            textoOperacion = "\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}\cdot{}" + ponParentesis(E) + " - \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "}\cdot{}" + ponParentesis(F)
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
            textoOperacion = ponParentesis(E) + "\cdot{}\Big[\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}-" + ponParentesis(C) + "\Big] + " + ponParentesis(F) + "\cdot{}(" + ponParentesis(D) + " - " + ponParentesis(G) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # (A/B+sqrt(C))/E-(D-G)/F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = random.randint(2,maximoValor)
        D = random.randint(2,maximoValor)
        E = random.randrange(-1,2,2)*round(random.uniform(0.5,maximoValor),random.randint(orden+1,orden+3))
        F = random.randrange(-1,2,2)*round(random.uniform(0.5,maximoValor),random.randint(orden+1,orden+3))
        G = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = (A/B+math.sqrt(C))/E-(D-G)/F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            textoOperacion = "\Big[\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}+" + r"\sqrt{" + str(C) + r"}" + r"\Big]:" + ponParentesis(E) + "-(" + ponParentesis(D) + "-" + ponParentesis(G) + "):" + ponParentesis(F)
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

###########################

def generaOperacionesTipo6(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # A*B+(sqrt(C)/D)-E*F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        B = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        C = random.randint(2,maximoValor)
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = A*B+math.sqrt(C)/D-E*F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            textoOperacion = ponParentesis(A) + "\cdot{}" + ponParentesis(B) + " + \dfrac{\sqrt{" + str(C) + "}}{" + ponParentesis(D) + "} - " + ponParentesis(E) + "\cdot{}" + ponParentesis(F)
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo7(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # A/B-(sqrt(C)/D)+E-F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = random.randint(2,maximoValor)
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = A/B-math.sqrt(C)/D+E-F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            textoOperacion = "\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "} - \dfrac{\sqrt{" + str(C) + "}}{" + ponParentesis(D) + "} + " + ponParentesis(E) + "-" + ponParentesis(F)
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo8(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # (sqrt(A)/B)*E-(C/D)*F
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(2,maximoValor)
        B = random.randint(2,maximoValor)
        C = random.randint(1,maximoValor)
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = (math.sqrt(A)/B)*E-(C/D)*F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            textoOperacion = "\dfrac{\sqrt{" + str(A) + "}}{" + ponParentesis(B) + "}\cdot{}" + ponParentesis(E) + " - \dfrac{" + ponParentesis(C) + "}{" + ponParentesis(D) + "}\cdot{}" + ponParentesis(F)
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo9(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # E*(A/B-C)+sqrt(F)*(D-G)
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randint(1,maximoValor)
        B = random.randint(2,maximoValor)
        C = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        D = random.randint(2,maximoValor)
        E = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        F = random.randint(2,maximoValor)
        G = round(random.uniform(-maximoValor,maximoValor),random.randint(orden+1,orden+3))
        
        exacto = E*(A/B-C)+math.sqrt(F)*(D-G)
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            textoOperacion = ponParentesis(E) + "\cdot{}\Big[\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}-" + ponParentesis(C) + "\Big] + \sqrt{" + str(F) + "}\cdot{}(" + ponParentesis(D) + " - " + ponParentesis(G) + ")"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo10(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor):
    # (A/B+C)/E-(sqrt(D)-G)/F
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
        
        exacto = (A/B+C)/E-(math.sqrt(D)-G)/F
        aproximado, ultimasCifras = calculaAproximado(exacto, orden, metodo)
        
        if ultimasCifras == solucion:
            textoOperacion = "\Big[\dfrac{" + ponParentesis(A) + "}{" + ponParentesis(B) + "}+" + ponParentesis(C) + "\Big]:" + ponParentesis(E) + "-(\sqrt{" + str(D) + "}-" + ponParentesis(G) + "):" + ponParentesis(F)
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
    elif tipoOperacion == 5:
        return generaOperacionesTipo6(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 6:
        return generaOperacionesTipo7(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 7:
        return generaOperacionesTipo8(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 8:
        return generaOperacionesTipo9(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)
    elif tipoOperacion == 9:
        return generaOperacionesTipo10(solucion, numeroOperacionesDistintas, metodo, orden, maximoValor)        

codigoAlfabetico = {
    'A': -13,
    'B': -12,
    'C': -11,
    'D': -10,
    'E': -9,
    'F': -8,
    'G': -7,
    'H': -6,
    'I': -5,
    'J': -4,
    'K': -3,
    'L': -2,
    'M': -1,
    'N': 0,
    'Ñ': 1,
    'O': 2,
    'P': 3,
    'Q': 4,
    'R': 5,
    'S': 6,
    'T': 7,
    'U': 8,
    'V': 9,
    'W': 10,
    'X': 11,
    'Y': 12,
    'Z': 13}

start = time.time()

sys.path.insert(0, './')

directorioFichas = "./fichas/"

# El nombre del archivo CSV que contiene los elementos a codificar
# lo pasamos como argumento.
rutaArchivoTXT = argv[1]

# Leemos el archivo de texto txt que contiene los elementos.
# Las anotamos en un array de elementos.
elementos = []
fTXT = open(rutaArchivoTXT, "r")
for x in fTXT:
  elementos.append(x[0:-1])
fTXT.close()

# Aleatorizamos la lista para que, al repartirla en clase, estén desordenadas.
random.shuffle(elementos)

# Creamos el archivo LaTeX y escribimos el preámbulo y el comienzo.
posicionBarra = rutaArchivoTXT.find("/",2) # Buscamos la posición de la segunda barra
nombreArchivoTXT = rutaArchivoTXT[posicionBarra+1:]
rutaArchivoLaTeX = directorioFichas + "criptografia_3ESO_Ac_R_Aproximaciones-" + nombreArchivoTXT[0:len(nombreArchivoTXT)-4] + ".tex"
fLaTeX = open(rutaArchivoLaTeX, "w")
escribeCabeceraLaTeX.escribe(fLaTeX)

numeroTiposOperaciones = 10
numeroOperacionesDistintas = 3
maximoValor = 15

nivel = "3 ESO Matemáticas Académicas"
CE = ["1.11 Emplear las herramientas tecnológicas adecuadas, de forma autónoma, realizando cálculos numéricos, algebraicos o estadísticos, haciendo representaciones gráficas, recreando situaciones matemáticas mediante simulaciones o analizando con sentido crítico situaciones diversas que ayuden a la comprensión de conceptos matemáticos o a la resolución de problemas.","2.1 Utilizar las propiedades de los números racionales para operarlos, utilizando la forma de cálculo y notación adecuada, para resolver problemas de la vida cotidiana, y presentando los resultados con la precisión requerida."]
Est = ["1.11.1 Selecciona herramientas tecnológicas adecuadas y las utiliza para la realización de cálculos numéricos, algebraicos o estadísticos cuando la dificultad de los mismos impide o no aconseja hacerlos manualmente.","2.1.6 Distingue y emplea técnicas adecuadas para realizar aproximaciones por defecto y por exceso de un número en problemas contextualizados, justificando sus procedimientos."]
tituloFicha = r"CRIPTOGRAF\'{I}A R"

for koko in range(len(elementos)):
    escribeInicioFichaLaTeX.escribe(fLaTeX,nivel,CE,Est,tituloFicha)
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que resolver una serie de operaciones con números reales. Cada vez que resuelvas una, tendrás que aproximar el resultado al orden pedido y con el método pedido. Cuando lo hayas hecho, busca el número formado por \textbf{las dos últimas cifras} en la tabla y apunta la letra que les corresponde. Si el resultado es negativo, el número a buscar lo será también."+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"`Red' significa `Redondeo', `Exc' significa `Por exceso' y `Def' significa 'Por defecto'' "+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.75}"+"\n")
    fLaTeX.write(r"\begin{small}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|l|l|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Orden} & \textbf{Método} & \textbf{Aproximación} & \textbf{Letra}\\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")

    # Añadimos al archivo fuente LaTeX las operaciones con enteros para el elemento que toque.
    print(elementos[koko])
    
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            operacion = random.randrange(0, numeroTiposOperaciones)
            metodo = random.randrange(0, 3)
            orden = random.randrange(0, 6)
            operacion = convierteLetraAOperacion(operacion,
                                             numeroOperacionesDistintas,
                                             codigoAlfabetico.get(elementos[koko][papa]),
                                             metodo,
                                             orden,
                                             maximoValor)[0]
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
            fLaTeX.write(r" $" + operacion + r"$ & " + orden + r" & " + metodo + r" & & \\\hline " + "\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{small}"+"\n")
    escribeFinalFichaLaTeX.escribe(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
