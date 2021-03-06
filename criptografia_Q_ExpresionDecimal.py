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
numeroDecimales = int(input("Introduce el número de decimales que hay que obtener: "))
numeroOperacionesDistintas = 1

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def generaOperacionesTipoUnico(numeroLetra, numeroOperacionesDistintas, maximoPositivo, numeroDecimales):
    contador = 0
    listaOperaciones = []
    if abs(numeroLetra) < 10:
        cadenaLetra = "0" + str(abs(numeroLetra))
    else:
        cadenaLetra = str(abs(numeroLetra))
    while contador < numeroOperacionesDistintas:
        numerador = random.randrange(1, maximoPositivo)
        denominador = random.randrange(2, maximoPositivo)
        resultado = numerador/denominador
        resultadoTruncado1 = truncate(resultado- math.floor(resultado),numeroDecimales)
        posicionPunto = str(resultado).find('.') 
        # Buscamos desde las milésimas hasta la precisión indicada por terminal.
        posicionCadenaLetra = str(resultadoTruncado1).find(cadenaLetra, 1, 1+numeroDecimales)
        if posicionCadenaLetra != -1:
            if numeroLetra < 0:
                textoOperacion = "$\dfrac{-" + str(numerador) + "}{" + str(denominador) + "}$"
            else:
                textoOperacion = "$\dfrac{" + str(numerador) + "}{" + str(denominador) + "}$"
            listaOperaciones.append(textoOperacion)
            listaOperaciones.append(posicionCadenaLetra) # Hay que buscar hasta tantos decimales.
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################

for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    # Ahora escribimos las instrucciones específicas para esta ficha.
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que \textbf{obtener la expresión decimal} de cada una de las fracciones que tienes en la ficha, obteniendo tantos decimales como se indique en cada caso."+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"Cuando la hayas obtenido, apunta el resultado. Luego, \textbf{toma las dos últimas cifras decimales} y busca el número que forman en la tabla para saber qué letra le corresponde. Si el resultado es negativo, el número también."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.75}"+"\n")
    fLaTeX.write(r"\begin{footnotesize}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|c|c|X|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Fracción} & \textbf{Nº de cifras decimales}  & \textbf{Resultado} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones con enteros para el elemento que toque.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    #operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento, y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán probablemente operaciones diferentes.
#        print(elementos[koko][papa])
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
            exec("cadenas = generaOperacionesTipoUnico(codigoAlfabetico.get(elementos[koko][papa]), numeroOperacionesDistintas, maximoPositivo, numeroDecimales)")
            pot = 2*random.randrange(0,len(cadenas)/2)
            fLaTeX.write(cadenas[pot]+r" &" + cadenas[pot+1] +r"& & \\\hline"+"\n")
            #----------------------------------------------  
    fLaTeX.write(r"\end{tabularx}"+"\n")
    fLaTeX.write(r"\end{footnotsize}"+"\n")
    funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=fichas", rutaArchivoLaTeX])
end = time.time()
print(len(elementos), "elementos procesados en", int(end - start), " segundos.")
