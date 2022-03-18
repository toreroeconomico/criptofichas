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
conDenominadores = input("¿Sin denominadores (0) o con denominadores (1)?: ") 
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
        B = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
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
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
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
        A = random.randrange(2, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(2, maximoPositivo)
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
    # A(Bx+C)+Dx-E = F(Gx+H)-I(Jx+K)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(2, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(2, maximoPositivo)
        E = random.randrange(1, maximoPositivo)
        F = random.randrange(2, maximoPositivo)
        G = random.randrange(2, maximoPositivo)
        H = random.randrange(1, maximoPositivo)
        I = random.randrange(2, maximoPositivo)
        J = random.randrange(1, maximoPositivo)
        K = random.randrange(1, maximoPositivo)
        if (A*B+D-F*G+I*J) != 0:
            if (F*H-I*K-A*C+E)/(A*B+D-F*G+I*J) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x" + "+" + str(C) + ")" + "+" + str(D) + "x" + "-" + str(E) + "=" + str(F) + "(" + str(G) + "x" + "+" + str(H) + ")" + "-" + str(I) + "(" + str(J) + "x" + "+" + str(K) + ")" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo5(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C)+Dx-E = Fx+G-H(Ix-J)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(2, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(2, maximoPositivo)
        E = random.randrange(1, maximoPositivo)
        F = random.randrange(2, maximoPositivo)
        G = random.randrange(1, maximoPositivo)
        H = random.randrange(2, maximoPositivo)
        I = random.randrange(1, maximoPositivo)
        J = random.randrange(1, maximoPositivo)
        if (A*B+D-F+H*I) != 0:
            if (G+H*J-A*C+E)/(A*B+D-F+H*I) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x" + "+" + str(C) + ")" + "+" + str(D) + "x" + "-" + str(E) + "=" + str(F) + "x" + "+" + str(G) + "-" + str(H) + "(" + str(I) + "x" + "-" + str(J) + ")" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

#----------------------------------------------------------------------------------------
# Con denominadores
def generaOperacionesTipo6(solucion, numeroOperacionesDistintas, maximoPositivo):
    # (Ax+B)/C = (Dx+E)/F
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
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

def generaOperacionesTipo7(solucion, numeroOperacionesDistintas, maximoPositivo):
    # (Ax+B)/C = (Dx+E)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
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

def generaOperacionesTipo8(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = (Dx+E)/F
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
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
    
def generaOperacionesTipo9(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C)/D-(x+E) = (Fx+G)/H+Ix
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        G = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        H = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        I = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)                        
        if (H*A*B-D*H-D*F-D*H*I) != 0:
            if (D*G-H*A*C+D*H*E)/(H*A*B-D*H-D*F-D*H*I) == solucion:
                textoOperacion = "$\dfrac{" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + ")}{" + str(D) + "}" + "-(x"
                else:
                    textoOperacion += str(C) + ")}{" + str(D) + "}" + "-(x"
                if E > 0:
                    textoOperacion += "+" + str(E) + ") = "
                else:
                    textoOperacion += str(E) + ") = "
                textoOperacion += "\dfrac{" + str(F) + "x"
                if G > 0:
                    textoOperacion += "+" + str(G) + "}{" + str(H) + "}"
                else:
                    textoOperacion += str(G) + "}{" + str(H) + "}"
                if I > 0:
                    textoOperacion += "+" + str(I) + "x" + "$"
                else:
                    textoOperacion += str(I) + "x" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas    
    
    
##################################################################################
    
def generaIdentidadTipo1(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = D(Ex+F)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        if A*B == D*E and A*C == D*F:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "(" + str(E) + "x"
            if F > 0:
                textoOperacion += "+" + str(F) + "$"
            else:
                textoOperacion += str(F) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaIdentidadTipo2(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = Dx+E
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        if A*B == D and A*C == E:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "$"
            else:
                textoOperacion += str(E) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaIdentidadTipo3(solucion, numeroOperacionesDistintas, maximoPositivo):
    # Ax+B/C = Dx+E/F
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        if A*F == D*C and B*F == E*C:
            textoOperacion = "$\dfrac{" + str(A) + "x"
            if B > 0:
                textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
            else:
                textoOperacion += str(B) + "}{" + str(C) + "} = "
            textoOperacion += "\dfrac{" + str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "}{" + str(F) + "}"
            else:
                textoOperacion += str(E) + "}{" + str(F) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

##################################################################################

def generaSinSolucionTipo1(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = D(Ex+F)
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        if A*B == D*E and A*C != D*F:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "(" + str(E) + "x"
            if F > 0:
                textoOperacion += "+" + str(F) + ")$"
            else:
                textoOperacion += str(F) + ")$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaSinSolucionTipo2(solucion, numeroOperacionesDistintas, maximoPositivo):
    # A(Bx+C) = Dx+E
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        if A*B == D and A*C != E:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "$"
            else:
                textoOperacion += str(E) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaSinSolucionTipo3(solucion, numeroOperacionesDistintas, maximoPositivo):
    # Ax+B/C = Dx+E/F
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        B = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        C = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        D = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        E = random.randrange(-1,2,2)*random.randrange(1, maximoPositivo)
        F = random.randrange(-1,2,2)*random.randrange(2, maximoPositivo)
        if A*F == D*C and B*F != E*C:
            textoOperacion = "$\dfrac{" + str(A) + "x"
            if B > 0:
                textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
            else:
                textoOperacion += str(B) + "}{" + str(C) + "} = "
            textoOperacion += "\dfrac{" + str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "}{" + str(F) + "}"
            else:
                textoOperacion += str(E) + "}{" + str(F) + "}"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    

if conDenominadores == '0':
    numeroTiposOperaciones = 5
else:
    numeroTiposOperaciones = 9

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendrás que resolver las siguientes ecuaciones lineales, buscar su solución en la tabla y anotar la letra correspondiente. Si es una identidad o una ecuación sin solución, anota un espacio en blanco."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{2.35}"+"\n")
    fLaTeX.write(r"\begin{footnotesize}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Ecuación} & \textbf{Solución} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones para cada letra de este elemento.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
#        print(str(operacionesDistintas[papa]+1),elementos[koko][papa])
        # Obtenemos el número correspondiente a cada letra del primer elemento, y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
            exec("cadenas = generaOperacionesTipo" + str(operacionesDistintas[papa]+1) + "(codigoAlfabetico.get(elementos[koko][papa]), numeroOperacionesDistintas, maximoPositivo)")
            pot = 2*random.randrange(0,int(len(cadenas)/2))
            fLaTeX.write(r"\normalsize " + cadenas[pot]+r" & & \\\hline"+"\n")
            #----------------------------------------------  
        else:
            # Es un espacio en blanco, que podemos codificar como identidad o ecuación sin solución.
            if random.randrange(0, 2) == 0:
                if conDenominadores == '0':
                    exec("cadenas = generaIdentidadTipo" + str(random.randrange(1, 3)) + "(0, numeroOperacionesDistintas, maximoPositivo)")
                else:
                    exec("cadenas = generaIdentidadTipo" + str(random.randrange(1, 4)) + "(0, numeroOperacionesDistintas, maximoPositivo)")
            else:
                if conDenominadores == '0':
                    exec("cadenas = generaSinSolucionTipo" + str(random.randrange(1, 3)) + "(0, numeroOperacionesDistintas, maximoPositivo)")            
                else:
                    exec("cadenas = generaSinSolucionTipo" + str(random.randrange(1, 4)) + "(0, numeroOperacionesDistintas, maximoPositivo)")            
            pot = 2*random.randrange(0,int(len(cadenas)/2))
            fLaTeX.write(r"\normalsize " + cadenas[pot]+r" & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{footnotesize}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
