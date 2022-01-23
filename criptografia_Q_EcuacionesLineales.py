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
conDenominadores = input("¿Con denominadores (1) o sin denominadores (0)?: ") 
numeroOperacionesDistintas = 4

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaOperacionesTipo1(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = D
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        if (D-A*C) % (A*B) == 0 and  (D-A*C)/(A*B) == solucion:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo2(solucion, numeroOperacionesDistintas, maximoPositivo):
    # Ax+B = Cx+D
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        if (A-C) != 0:
            if (D-B)/(A-C) == solucion:
                textoOperacion = "$" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + " = "
                else:
                    textoOperacion += str(B) + " = "
                textoOperacion += str(C) + "x"
                if D > 0:
                    textoOperacion += "+" + str(D) + "$"
                else:
                    textoOperacion += str(D) + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo3(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = D(Ex+F)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(1, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(1, maximoPositivo)
        E = random.randrange(1, maximoPositivo)
        F = random.randrange(1, maximoPositivo)
        if (A*B-D*E) != 0:
            if (D*F-A*C)/(A*B-D*E) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + ") = "
                else:
                    textoOperacion += str(C) + ") = "
                textoOperacion += str(D) + "(" + str(E) + "x"
                if F > 0:
                    textoOperacion += "+" + str(F) + ")" + "$"
                else:
                    textoOperacion += str(F) + ")" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo4(solucion, numeroOperacionesDistintas, maximoPositivo):
    # (Ax+B)/C = (Dx+E)/F
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        if F != C and (F*A-C*D) != 0:
            if (C*E-F*B)/(F*A-C*D) == solucion:
                textoOperacion = "$" + "\dfrac{" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
                else:
                    textoOperacion += str(B) + "}{" + str(C) + "} = "
                textoOperacion += "\dfrac{" + str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "}{" + str(F) + "}" + "$"
                else:
                    textoOperacion += str(E) + "}{" + str(F) + "}" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(solucion, numeroOperacionesDistintas, maximoPositivo):
    # (Ax+B)/C = (Dx+E)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = 1
        if (F*A-C*D) != 0:
            if (C*E-F*B)/(F*A-C*D) == solucion:
                textoOperacion = "$" + "\dfrac{" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
                else:
                    textoOperacion += str(B) + "}{" + str(C) + "} = "
                textoOperacion += str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "$"
                else:
                    textoOperacion += str(E) + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = (Dx+E)/F
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        if (A*F*B-D) != 0:
            if (-A*F*C+E)/(A*F*B-D) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + ") = "
                else:
                    textoOperacion += str(C) + ") = "
                textoOperacion += "\dfrac{" + str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "}{" + str(F) + "}" + "$"
                else:
                    textoOperacion += str(E) + "}{" + str(F) + "}" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


#def convierteLetraAOperacion(tipoOperacion, numeroOperacionesDistintas, solucion, maximoPositivo):
#    if tipoOperacion == 0:
#        return generaOperacionesTipo1(solucion, numeroOperacionesDistintas, maximoPositivo)
#    elif tipoOperacion == 1:
#        return generaOperacionesTipo2(solucion, numeroOperacionesDistintas, maximoPositivo)
#    elif tipoOperacion == 2:
#        return generaOperacionesTipo3(solucion, numeroOperacionesDistintas, maximoPositivo)
#    elif tipoOperacion == 3:
#        return generaOperacionesTipo4(solucion, numeroOperacionesDistintas, maximoPositivo)
#    elif tipoOperacion == 4:
#        return generaOperacionesTipo5(solucion, numeroOperacionesDistintas, maximoPositivo)
#    elif tipoOperacion == 5:
#        return generaOperacionesTipo6(solucion, numeroOperacionesDistintas, maximoPositivo)

if conDenominadores == '1':
    numeroTiposOperaciones = 6
else:
    numeroTiposOperaciones = 3

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendrás que resolver las siguientes ecuaciones lineales. Cada vez que resuelvas una, busca la solución en la tabla y anota la letra correspondiente."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{2}"+"\n")
    fLaTeX.write(r"\begin{footnotesize}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Ecuación} & \textbf{Solución} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones para cada letra de este elemento.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento, y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
            exec("cadenas = generaOperacionesTipo" + str(operacionesDistintas[papa]+1) + "(codigoAlfabetico.get(elementos[koko][papa]), numeroOperacionesDistintas, maximoPositivo)")
            pot = 2*random.randrange(0,int(len(cadenas)/2))
            fLaTeX.write(cadenas[pot]+r" & & \\\hline"+"\n")
            #----------------------------------------------  
#            fLaTeX.write(r"\begin{normalsize}"+convierteLetraAOperacion(random.randrange(0, numeroTiposEcuaciones),numeroOperacionesDistintas,
#                                                 codigoAlfabetico.get(elementos[koko][papa]),
#                                                 maximoPositivo)[0] + r"\end{normalsize} & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{footnotesize}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
