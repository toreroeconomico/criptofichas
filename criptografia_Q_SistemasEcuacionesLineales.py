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
numeroTiposOperaciones = 3
numeroOperacionesDistintas = 3
maximoValor = 30

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
  
def generaSCI(numeroOperacionesDistintas, maximoValor):
    # Ax+By = C
    # A*Dx+B*Dy = C*D
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        if B != 0 and D != 0:
            textoOperacion = r"$\left\{ \begin{array}{ll}" + str(A) + "x"
            if B > 0:
                textoOperacion += "+" + str(B) + "y = " + str(C) + r"&\\"
            else:
                textoOperacion += str(B) + "y = " + str(C) + r"&\\"
            textoOperacion += str(A*D) + "x"
            if B*D > 0:
                textoOperacion += "+" + str(B*D) + "y = " + str(C*D)
            else:
                textoOperacion += str(B*D) + "y = " + str(C*D)
            textoOperacion += r"\end{array} \right.$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaSI(numeroOperacionesDistintas, maximoValor):
    # Ax+By = C
    # A*Dx+B*Dy = C*E
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        if B != 0 and C != 0 and D != 0:
            textoOperacion = r"$\left\{ \begin{array}{ll}" + str(A) + "x"
            if B > 0:
                textoOperacion += "+" + str(B) + "y = " + str(C) + r"&\\"
            else:
                textoOperacion += str(B) + "y = " + str(C) + r"&\\"
            textoOperacion += str(A*D) + "x"
            if B*D > 0:
                textoOperacion += "+" + str(B*D) + "y = " + str(C*E)
            else:
                textoOperacion += str(B*D) + "y = " + str(C*E)
            textoOperacion += r"\end{array} \right.$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaSCDTipo1(solucion, numeroOperacionesDistintas, maximoValor):
    # Ax+By = C = A*solx+B*soly
    # Dx+Ey = F = D*solx+E*soly
    # Solución x = (EC-BF)/(EA-BD)
    # Solución y = C/B-A/B*(EC-BF)/(EA-BD)
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        C = A*soluciones[0] + B*soluciones[1]
        D = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        F = D*soluciones[0] + E*soluciones[1]
        if (E*A-B*D) != 0 and B != 0:
            if (E*C-B*F)/(E*A-B*D) == soluciones[0] and (C/B-A/B*(E*C-B*F)/(E*A-B*D)) == soluciones[1]:
                textoOperacion = r"$\left\{ \begin{array}{ll}" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + "y = " + str(C) + r"&\\"
                else:
                    textoOperacion += str(B) + "y = " + str(C) + r"&\\"
                textoOperacion += str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "y = " + str(F)
                else:
                    textoOperacion += str(E) + "y = " + str(F)
                textoOperacion += r"\end{array} \right.$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaSCDTipo2(solucion, numeroOperacionesDistintas, maximoValor):
    # A(Bx+Cy) = D = A*B*solx+A*C*soly
    # Ex+Fy = G = E*solx + F*soly
    # Solución x = (DF-ACG)/(ABF-ACE)
    # Solución y = D/AC-AB/AC*(DF-ACG)/(ABF-ACE)
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        D = A*B*soluciones[0] + A*C*soluciones[1]
        E = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        F = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        G = E*soluciones[0] + F*soluciones[1]
        if (A*B*F-A*C*E) != 0 and (A*C) != 0:
            if (D*F-A*C*G)/(A*B*F-A*C*E) == soluciones[0] and (D/(A*C)-(A*B)/(A*C)*(D*F-A*C*G)/(A*B*F-A*C*E)) == soluciones[1]:
                textoOperacion = r"$\left\{ \begin{array}{ll}" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + "y) = " + str(D) + r"&\\"
                else:
                    textoOperacion += str(C) + "y) = " + str(D) + r"&\\"
                textoOperacion += str(E) + "x"
                if F > 0:
                    textoOperacion += "+" + str(F) + "y = " + str(G)
                else:
                    textoOperacion += str(F) + "y = " + str(G)
                textoOperacion += r"\end{array} \right.$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaSCDTipo3(solucion, numeroOperacionesDistintas, maximoValor):
    # A(Bx+Cy) = D = A*B*solx + A*C*soly
    # Ex+Fy = G = E*solx + F*soly
    # Solución x = (DF-ACG)/(ABF-ACE)
    # Solución y = D/AC-AB/AC*(DF-ACG)/(ABF-ACE)
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        D = A*B*soluciones[0] + A*C*soluciones[1]
        E = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        F = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        G = E*soluciones[0]+ F*soluciones[1]
        if (A*B*F-A*C*E) != 0 and (A*C) != 0:
            if (D*F-A*C*G)/(A*B*F-A*C*E) == soluciones[0] and (D/(A*C)-(A*B)/(A*C)*(D*F-A*C*G)/(A*B*F-A*C*E)) == soluciones[1]:
#                textoOperacion = r"$\left\{ \begin{array}{ll}" + str(A) + "(" + str(B) + "x"
#                if C > 0:
#                    textoOperacion += "+" + str(C) + "y) = " + str(D) + r"&\\"
#                else:
#                    textoOperacion += str(C) + "y) = " + str(D) + r"&\\"
#                textoOperacion += str(E) + "x"
#                if F > 0:
#                    textoOperacion += "+" + str(F) + "y = " + str(G)
#                else:
#                    textoOperacion += str(F) + "y = " + str(G)
#                textoOperacion += r"\end{array} \right.$"
                
                textoOperacion = r"$\left\{ \begin{array}{ll}" + str(E) + "x"
                if F > 0:
                    textoOperacion += "+" + str(F) + "y = " + str(G) + r"&\\"
                else:
                    textoOperacion += str(F) + "y = " + str(G) + r"&\\"
                textoOperacion += str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + "y) = " + str(D)
                else:
                    textoOperacion += str(C) + "y) = " + str(D)
                textoOperacion += r"\end{array} \right.$"
                
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaSCDTipo4(solucion, numeroOperacionesDistintas, maximoValor):
    # A(Bx+Cy) = D = A*B*solx + A*C*soly
    # E(Fx+Gy) = H = E*F*solx + E*G*soly
    # Solución x = (DEG-ACH)/(EGAB-ACEF)
    # Solución y = D/AC-AB/AC*(DEG-ACH)/(EGAB-ACEF)
    parejasPosibles = countWays(solucion)
    soluciones = parejasPosibles[1][random.randint(0,len(parejasPosibles[1])-1)]
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        D = A*B*soluciones[0] + A*C*soluciones[1]
        E = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        F = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        G = random.randrange(-1,2,2)*random.randrange(1, maximoValor)
        H = E*F*soluciones[0] + E*G*soluciones[1]
        if (E*G*A*B-A*C*E*F) != 0 and A*C != 0:
            if (D*E*G-A*C*H)/(E*G*A*B-A*C*E*F) == soluciones[0] and (D/(A*C)-(A*B)/(A*C)*(D*E*G-A*C*H)/(E*G*A*B-A*C*E*F)) == soluciones[1]:
                textoOperacion = r"$\left\{ \begin{array}{ll}" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + "y) = " + str(D) + r"&\\"
                else:
                    textoOperacion += str(C) + "y) = " + str(D) + r"&\\"
                textoOperacion += str(E) + "(" + str(F) + "x"
                if G > 0:
                    textoOperacion += "+" + str(G) + "y) = " + str(H)
                else:
                    textoOperacion += str(G) + "y) = " + str(H)
                textoOperacion += r"\end{array} \right.$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def convierteLetraAOperacion(tipoOperacion, solucion, numeroOperacionesDistintas, maximoValor):
    if tipoOperacion == 0:
        return generaSCDTipo1(solucion, numeroOperacionesDistintas, maximoValor)
    elif tipoOperacion == 1:
        return generaSCDTipo2(solucion, numeroOperacionesDistintas, maximoValor)
    elif tipoOperacion == 2:
        return generaSCDTipo3(solucion, numeroOperacionesDistintas, maximoValor)
    elif tipoOperacion == 3:
        return generaSCDTipo4(solucion, numeroOperacionesDistintas, maximoValor)
#    elif tipoOperacion == 4:
#        return generaSCDTipo5(solucion, numeroOperacionesDistintas, maximoValor)
#    elif tipoOperacion == 5:
#        return generaSCDTipo6(solucion, numeroOperacionesDistintas, maximoValor)
#    # Ahora vienen las de primer grado
#    elif tipoOperacion == 6:
#        return generaSCDTipo7(solucion, numeroOperacionesDistintas, maximoValor)
#    elif tipoOperacion == 7:
#        return generaSCDTipo8(solucion, numeroOperacionesDistintas, maximoValor)
#    elif tipoOperacion == 8:
#        return generaSCDTipo9(solucion, numeroOperacionesDistintas, maximoValor)
#    elif tipoOperacion == 9:
#        return generaSCDTipo10(solucion, numeroOperacionesDistintas, maximoValor)
  
#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendrás que resolver los siguientes sistemas de ecuaciones lineales. \textbf{Si el sistema es compatible determinado (SCD)}, calcula la solución $(x, y)$, busca su producto en la tabla y anota la letra correspondiente. \textbf{Si el sistema es compatible indeterminado (SCI) o incompatible (SI)}, entonces es un espacio en blanco."+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\vspace{0.25\baselineskip}"+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.00}"+"\n")
    fLaTeX.write(r"\begin{footnotesize}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|c|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(
        r"	\textbf{Sistema} & \textbf{Tipo de sistema} & \textbf{Soluci\'{o}n $x$} & \textbf{Soluci\'{o}n $y$} & \textbf{Producto} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    print(elementos[koko])
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a letra del elemento
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            fLaTeX.write(r"	" + convierteLetraAOperacion(random.randrange(0, numeroTiposOperaciones),
                                             codigoAlfabetico.get(elementos[koko][papa]),numeroOperacionesDistintas,
                                             maximoValor)[random.randrange(0,numeroOperacionesDistintas)] + r" & & & & & \\\hline"+"\n")
        else:
            # Para los espacios en blanco generamos un sistema compatible indeterminado (SCI) o uno incompatible (SI).
            if random.randint(0,1) == 0:
                fLaTeX.write(r"	" + generaSCI(numeroOperacionesDistintas,maximoValor)[random.randrange(0,numeroOperacionesDistintas)] + r" & & & & &  \\\hline"+"\n")
            else:
                fLaTeX.write(r"	" + generaSI(numeroOperacionesDistintas,maximoValor)[random.randrange(0,numeroOperacionesDistintas)] + r" & & & & &  \\\hline"+"\n")    
            
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{footnotesize}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
