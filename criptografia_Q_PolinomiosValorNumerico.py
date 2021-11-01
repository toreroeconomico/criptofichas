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
numeroExpresionesDistintas = 11
maximoPositivo = 35
minimoNegativo = -35

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaExpresionesTipo1(solucion, maximoPositivo, minimoNegativo):
    # p + (p+1) + (p+2)
    listaExpresiones = []
    textoOperacion = "$p + (p+1) + (p+2)$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$p="+str(round((solucion-3)/3,2))+"$")
    return listaExpresiones

def generaExpresionesTipo2(solucion, maximoPositivo, minimoNegativo):
    # Ap +B
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        if A != 0:
            seguir = 0
    listaExpresiones = []
    textoOperacion = "$" + str(A) + "b"
    if B < 0:
        textoOperacion += str(B) + "$"
    else:
        textoOperacion += " + " + str(B)+"$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$b="+str(round((solucion-B)/A,2))+"$")
    return listaExpresiones

def generaExpresionesTipo3(solucion, maximoPositivo, minimoNegativo):
    # (Ap +B)(Cp+D)
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        C = random.randrange(minimoNegativo, maximoPositivo)
        D = random.randrange(minimoNegativo, maximoPositivo)
        coefA = A*C
        coefB = A*D+B*C
        coefC = B*D-solucion
        discriminante = coefB*coefB-4*coefA*coefC
        if coefA != 0 and discriminante > 0:
            x1 = (-coefB+math.sqrt(discriminante))/(2*coefA)
            x2 = (-coefB-math.sqrt(discriminante))/(2*coefA)
            if x1 == solucion or x2 == solucion:
                seguir = 0
    listaExpresiones = []
    textoOperacion = "$(" + str(A) + "x"
    if B < 0:
        textoOperacion += str(B) + ")"
    else:
        textoOperacion += " + " + str(B) + ")"
    textoOperacion += "(" + str(C) + "x"
    if D < 0:
        textoOperacion += str(D) + ")$"
    else:
        textoOperacion += " + " + str(D) + ")$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$x="+str(round(x1,2))+"$")
    return listaExpresiones

def generaExpresionesTipo4(solucion, maximoPositivo, minimoNegativo):
    # Ap+Bq
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        p = round(random.uniform(minimoNegativo, maximoPositivo),2)
        if B != 0:
            seguir = 0
    q = round((solucion-A*p)/B,2)
    listaExpresiones = []
    textoOperacion = "$"+str(A)+"p"
    if B < 0:
        textoOperacion += str(B)+"q$"
    else:
        textoOperacion += " + "+str(B)+"q$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$p=" + str(p) + ", q=" + str(q) + "$")
    return listaExpresiones

def generaExpresionesTipo5(solucion, maximoPositivo, minimoNegativo):
    # At+Bu^2+C
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        C = random.randrange(minimoNegativo, maximoPositivo)
        u = round(random.uniform(minimoNegativo, maximoPositivo),2)
        if A != 0:
            seguir = 0
    t = round((solucion-C-B*u*u)/A,2)
    listaExpresiones = []
    textoOperacion = "$"+str(A)+"t"
    if B < 0:
        textoOperacion += str(B)+"u^2"
    else:
        textoOperacion += " + "+str(B)+"u^2"
    if C < 0:
        textoOperacion += str(C) + r"$"
    else:
        textoOperacion += " + " + str(C) + r"$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$t=" + str(t) + ", u=" + str(u) + "$")
    return listaExpresiones

def generaExpresionesTipo6(solucion, maximoPositivo, minimoNegativo):
    # A(t+B)
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        if A != 0:
            seguir = 0
    t = round((solucion-A*B)/A,2)
    listaExpresiones = []
    textoOperacion = "$"+str(A)+"(m"
    if B < 0:
        textoOperacion += str(B)+")$"
    else:
        textoOperacion += " + "+str(B)+")$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$m=" + str(t) + "$")
    return listaExpresiones

def generaExpresionesTipo7(solucion, maximoPositivo, minimoNegativo):
    # p(p+A)/B
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        coefA = 1
        coefB = A
        coefC = -solucion*B
        discriminante = coefB*coefB-4*coefA*coefC
        if B != 0 and coefA != 0 and discriminante > 0:
            x1 = (-coefB+math.sqrt(discriminante))/(2*coefA)
            x2 = (-coefB-math.sqrt(discriminante))/(2*coefA)
            if x1 == solucion or x2 == solucion:
                seguir = 0
    listaExpresiones = []
    textoOperacion = r"$\dfrac{p(p "
    if A < 0:
        textoOperacion += str(A)+")}{" + str(B) + "}$"
    else:
        textoOperacion += " + " + str(A)+")}{" + str(B) + "}$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$p=" + str(x2) + "$")
    return listaExpresiones

def generaExpresionesTipo8(solucion, maximoPositivo, minimoNegativo):
    # Ap(p+B)
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        coefA = A
        coefB = A*B
        coefC = -solucion
        discriminante = coefB*coefB-4*coefA*coefC
        if coefA != 0 and discriminante > 0:
            x1 = (-coefB+math.sqrt(discriminante))/(2*coefA)
            x2 = (-coefB-math.sqrt(discriminante))/(2*coefA)
            if x1 == solucion or x2 == solucion:
                seguir = 0
    listaExpresiones = []
    textoOperacion = r"$" + str(A) + "p(p"
    if B < 0:
        textoOperacion += str(B)+")$"
    else:
        textoOperacion += " + " + str(B) + ")$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$p=" + str(x1) + "$")
    return listaExpresiones

def generaExpresionesTipo9(solucion, maximoPositivo, minimoNegativo):
    # A+xyz+By^2
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        x = round(random.uniform(minimoNegativo, maximoPositivo),2)
        y = round(random.uniform(minimoNegativo, maximoPositivo),2)
        if x != 0 and y != 0:
            z = round((solucion-B*y*y-A)/(x*y),2)
            if abs((A+x*y*z+B*y*y)-solucion) < 0.5:
                seguir = 0
    listaExpresiones = []
    textoOperacion = r"$" + str(A) + " + xyz"
    if B < 0:
        textoOperacion += str(B)+"y^2$"
    else:
        textoOperacion += " + " + str(B) + "y^2$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$x=" + str(x) + ", y=" + str(y) + ", z=" + str(z) + "$")
    return listaExpresiones

def generaExpresionesTipo10(solucion, maximoPositivo, minimoNegativo):
    # (A+p)/(p-2)
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        if (1-solucion) == 0:
            p = (-A-2*solucion)/(1-solucion+random.uniform(0.1,0.2))
        else:
            p = (-A-2*solucion)/(1-solucion)
        pRedondeado = round(p,2)
        if pRedondeado-2 > 0 and abs(round((A+pRedondeado)/(pRedondeado-2),2)-solucion) < 0.5:
            seguir = 0
    listaExpresiones = []
    textoOperacion = r"$\dfrac{" + str(A) + " + p}{p-2}$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$p=" + str(pRedondeado) + "$")
    return listaExpresiones

def generaExpresionesTipo11(solucion, maximoPositivo, minimoNegativo):
    # (Ap^2-Bp)/(Cp^2-Dp)
    seguir = 1
    while seguir == 1:
        A = random.randrange(minimoNegativo, maximoPositivo)
        B = random.randrange(minimoNegativo, maximoPositivo)
        C = random.randrange(minimoNegativo, maximoPositivo)
        D = random.randrange(minimoNegativo, maximoPositivo)
        if (A-solucion*C) == 0:
            p = (B-solucion*D)/(A-solucion*C+random.uniform(0.05,0.1))
        else:
            p = (B-solucion*D)/(A-solucion*C)
        pRedondeado = round(p,2)
        if C*pRedondeado*pRedondeado-D*pRedondeado > 0 and abs(round((A*pRedondeado*pRedondeado-B*pRedondeado)/(C*pRedondeado*pRedondeado-D*pRedondeado),2)-solucion) < 0.5:
            seguir = 0
    listaExpresiones = []
    if B>0:
        textoOperacion = r"$\dfrac{" + str(A) + r" p^2" + "-" + str(abs(B)) + r"p}{" + str(C) + r"p^2"
    else:
        textoOperacion = r"$\dfrac{" + str(A) + r" p^2" + "+" + str(abs(B)) + r"p}{" + str(C) + r"p^2"
    if D<0:
        textoOperacion += r"+" + str(abs(D)) + r"p}$"
    else:
        textoOperacion += r"-" + str(abs(D)) + r"p}$"
    listaExpresiones.append(textoOperacion)
    listaExpresiones.append("$p=" + str(pRedondeado) + "$")
    return listaExpresiones

def convierteLetraAExpresion(tipoOperacion, solucion, maximoPositivo, minimoNegativo):
    # Fracciones
    if tipoOperacion == 0:
        return generaExpresionesTipo1(solucion, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 1:
        return generaExpresionesTipo2(solucion, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 2:
        return generaExpresionesTipo3(solucion, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 3:
        return generaExpresionesTipo4(solucion, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 4:
        return generaExpresionesTipo5(solucion, maximoPositivo, minimoNegativo)
    elif tipoOperacion == 5:
        return generaExpresionesTipo6(solucion, maximoPositivo, minimoNegativo)    
    elif tipoOperacion == 6:
        return generaExpresionesTipo7(solucion, maximoPositivo, minimoNegativo)    
    elif tipoOperacion == 7:
        return generaExpresionesTipo8(solucion, maximoPositivo, minimoNegativo)    
    elif tipoOperacion == 8:
        return generaExpresionesTipo9(solucion, maximoPositivo, minimoNegativo)    
    elif tipoOperacion == 9:
        return generaExpresionesTipo10(solucion, maximoPositivo, minimoNegativo)    
    elif tipoOperacion == 10:
        return generaExpresionesTipo11(solucion, maximoPositivo, minimoNegativo)    

    
#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    fLaTeX.write(r"Para desencriptarlo, tendrás que calcular el valor numérico de las siguientes expresiones algebraicas para los valores dados. Cuando lo hayas calculado, \textbf{redondéalo a las unidades}, búscalo en la tabla y anota la letra correspondiente."+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\vspace{0.5\baselineskip}"+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.5}"+"\n")
    fLaTeX.write(r"\begin{footnotesize}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Expresión algebraica} & \textbf{Valor de las variables} & \textbf{Resultado} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    print(elementos[koko])
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            kuka = random.randrange(0,numeroExpresionesDistintas)
            salidas = convierteLetraAExpresion(kuka,codigoAlfabetico.get(elementos[koko][papa]),maximoPositivo,minimoNegativo)
            fLaTeX.write(r"" + salidas[0] + r" & " + salidas[1] + r" & &  \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{footnotesize}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
