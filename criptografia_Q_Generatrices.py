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

#from decimal import Decimal, ROUND_DOWN, ROUND_UP

#######################################################################################
# Parámetros
#######################################################################################
maximoPositivo = 100
minimoNegativo = -100

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################

def find_prime_facs(n):
  list_of_factors=[]
  i=2
  while n>1:
    if n%i==0:
      list_of_factors.append(i)
      n=n/i
      i=i-1
    i+=1  
  return list_of_factors

def ponParentesis(valor):
    if valor < 0:
        cadena = "(" + str(valor) + ")"
    else:
        cadena= str(valor)
    return cadena    

def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return x
    
def generaOperacionesTipo1(numeradorOperacion, maximoPositivo, minimoNegativo,tipoDecimal):
    seguir = 1
    while seguir == 1:
        Np1 = random.randrange(minimoNegativo, maximoPositivo)
        seguir2 = 1
        while seguir2 == 1:
            Dp1 = random.randrange(minimoNegativo, maximoPositivo)
            if Dp1 != 0:
                seguir2 = 0
        MCD = computeGCD(Np1,Dp1)
    
        Np1Simplificado = int(Np1/MCD)
        Dp1Simplificado = int(Dp1/MCD)
        # Tenemos que verificar que el denominador simplificado no tiene factores primos muy grandes
        # que hagan que el periodo o el anteperiodo sea demasiado grande y se compliquen las cosas.
        factoresPrimosDp1Simplificado = find_prime_facs(Dp1Simplificado)
        # Tenemos que asegurarnos de que el tipo de decimal es el que hemos pedido.

        if Np1Simplificado == numeradorOperacion and len(factoresPrimosDp1Simplificado) > 0 and max(factoresPrimosDp1Simplificado) < 17 and Dp1Simplificado % 49 !=0:
            # Lo de modulo 49 es para evitar números con período demasiado largo.
            if 2 in factoresPrimosDp1Simplificado or 5 in factoresPrimosDp1Simplificado:
                # Quitamos el 2 y el 5 para ver si quedan otros factores primos.
                esta2 = False
                esta5 = False                
                if 2 in factoresPrimosDp1Simplificado:
                    esta2 = True
                if 5 in factoresPrimosDp1Simplificado:
                    esta5 = True
                if esta2 and esta5:
                    factoresPrimosDp1Simplificado.remove(2)
                    factoresPrimosDp1Simplificado.remove(5)
                elif esta2 and not esta5:
                    factoresPrimosDp1Simplificado.remove(2)
                elif esta5 and not esta2:
                    factoresPrimosDp1Simplificado.remove(5)
                if factoresPrimosDp1Simplificado != []:
                    # Quedan factores que no son ni el 2 ni el 5, así que el número generado es DPM.
                    if tipoDecimal == "DPM":
                        seguir = 0        
                else:
                    # No quedan factores que no sean ni el 2 ni el 5, así que el número generado es DE.
                    if tipoDecimal == "DE":
                        seguir = 0
            else:
                # El número generado es DPP.
                if tipoDecimal == "DPP":
                    seguir = 0

            numeroDecimal = "{:.15f}".format(math.trunc(Np1Simplificado*10**15/Dp1Simplificado)/10**15)
            posicionPuntoDecimal = numeroDecimal.find('.')
            textoOperacion = numeroDecimal[0:posicionPuntoDecimal] + "," + numeroDecimal[posicionPuntoDecimal+1:]
    return textoOperacion

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################

for koko in range(len(elementos)):
    contador = 0 # para que el tipo de decimal esté proporcionado en la ficha, o sea, que no abunden los DE, por ejemplo.
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    # Ahora escribimos las instrucciones específicas para esta ficha.
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que obtener la fracción generatriz de los siguientes números decimales. Cuando la tengas, busca \textbf{su numerador} en la tabla y apunta la letra que le corresponde. Si la fracción resultante es negativa, el numerador también. Además, \textbf{indica también el tipo de número decimal que es}."+"\n")
    fLaTeX.write(r""+"\n")    
    fLaTeX.write(r"\vspace{\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")        
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.5}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Número decimal} & \textbf{Fracción generatriz} & \textbf{Tipo de número decimal} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")

    # Añadimos al archivo fuente LaTeX las operaciones con enteros para el elemento que toque.
    print(elementos[koko])
    
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento,
        # y generamos una operación que da ese número como resultado.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            if contador % 3 == 0:
                textoDecimal = generaOperacionesTipo1(codigoAlfabetico.get(elementos[koko][papa]),maximoPositivo, minimoNegativo,"DE")
                contador += 1
            elif contador % 3 == 1:
                textoDecimal = generaOperacionesTipo1(codigoAlfabetico.get(elementos[koko][papa]),maximoPositivo, minimoNegativo,"DPP")
                contador += 1
            elif contador % 3 == 2:
                textoDecimal = generaOperacionesTipo1(codigoAlfabetico.get(elementos[koko][papa]),maximoPositivo, minimoNegativo,"DPM")
                contador += 1
            fLaTeX.write(r" $" + textoDecimal + r"...$ & & & \\\hline"+"\n")
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\vspace{\baselineskip}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
