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
numeroOperacionesDistintas = 5
radicandosIrreducibles = [2, 3, 5, 6, 7, 10, 11]

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaOperacionesTipo1(radicandosIrreducibles, solucion, numeroOperaciones, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        radicandoIrreducible1 = radicandosIrreducibles[random.randint(1, len(radicandosIrreducibles)-1)]
        factor1 = random.randint(1, maximoPositivo)
        factor2 = random.randint(1, maximoPositivo)
        if (factor1**2-factor2) == solucion:
            textoOperacion = "$" + "\sqrt{" + str(radicandoIrreducible1*factor1**4) + "}-\sqrt{" + str(radicandoIrreducible1*factor2**2) + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo2(radicandosIrreducibles, solucion, numeroOperaciones, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        radicandoIrreducible1 = radicandosIrreducibles[random.randint(1, len(radicandosIrreducibles)-1)]
        factor1 = random.randint(1, maximoPositivo)
        factor2 = random.randint(1, maximoPositivo)
        factorExterno1 = random.randint(1, maximoPositivo)
        factorExterno2 = random.randint(1, maximoPositivo)
        if (factor1*factorExterno1-factor2*factorExterno2) == solucion:
            textoOperacion = "$" + str(factorExterno1) + "\sqrt{" + str(radicandoIrreducible1*factor1**2) + "}-" + str(factorExterno2) + "\sqrt{" + str(radicandoIrreducible1*factor2**2) + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas
    
def generaOperacionesTipo3(radicandosIrreducibles, solucion, numeroOperaciones, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        radicandoIrreducible1 = radicandosIrreducibles[random.randint(1, len(radicandosIrreducibles)-1)]
        factor1 = random.randint(1, maximoPositivo)
        factor2 = random.randint(1, maximoPositivo)
        factor3 = random.randint(1, maximoPositivo)
        factorExterno1 = random.randint(1, maximoPositivo)
        factorExterno2 = random.randint(1, maximoPositivo)
        factorExterno3 = random.randint(1, maximoPositivo)
        if (factor1*factorExterno1-factor2*factorExterno2+factorExterno3*factor3) == solucion:
            textoOperacion = "$" + str(factorExterno1) + "\sqrt{" + str(radicandoIrreducible1*factor1**2) + "}-" + str(factorExterno2) + "\sqrt{" + str(radicandoIrreducible1*factor2**2) + "}+" + str(factorExterno3) + "\sqrt{" + str(radicandoIrreducible1*factor3**2) + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas        

def generaOperacionesTipo4(radicandosIrreducibles, solucion, numeroOperaciones, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        radicandoIrreducible1 = radicandosIrreducibles[random.randint(1, len(radicandosIrreducibles)-1)]
        factor1 = random.randint(1, maximoPositivo)
        factor2 = random.randint(1, maximoPositivo)
        factor3 = random.randint(1, maximoPositivo)
        factor4 = random.randint(1, maximoPositivo)
        factorExterno1 = random.randint(1, maximoPositivo)
        factorExterno2 = random.randint(1, maximoPositivo)
        factorExterno3 = random.randint(1, maximoPositivo)
        factorExterno4 = random.randint(1, maximoPositivo)
        if (-factor3*factorExterno3+factor4*factorExterno4) != 0 and (factor1*factorExterno1-factor2*factorExterno2)/(-factor3*factorExterno3+factor4*factorExterno4) == solucion:
            textoOperacion = "$" + "\dfrac{" + str(factorExterno1) + "\sqrt{" + str(radicandoIrreducible1*factor1**2) + "}-" + str(factorExterno2) + "\sqrt{" + str(radicandoIrreducible1*factor2**2) + "}}{-" + str(factorExterno3) + "\sqrt{" + str(radicandoIrreducible1*factor3**2) + "}+" + str(factorExterno4) + "\sqrt{" + str(radicandoIrreducible1*factor4**2) + "}" + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo5(radicandosIrreducibles, solucion, numeroOperaciones, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        radicandoIrreducible1 = radicandosIrreducibles[random.randint(1, len(radicandosIrreducibles)-1)]
        factor1 = random.randint(1, int(maximoPositivo/2))
        factor2 = random.randint(1, int(maximoPositivo/2))
        factor3 = random.randint(1, int(maximoPositivo/2))
        factor4 = random.randint(1, int(maximoPositivo/2))
        factorExterno1 = random.randint(1, maximoPositivo)
        factorExterno2 = random.randint(1, maximoPositivo)
        factorExterno3 = random.randint(1, maximoPositivo)
        factorExterno4 = random.randint(1, maximoPositivo)        
        if (-factor3*factorExterno3+factor4) != 0 and (factor1*factorExterno1-factor2)/(-factor3*factorExterno3+factor4) == solucion:
            textoOperacion = "$" + "\dfrac{" + str(factorExterno1) + "\sqrt{" + str(radicandoIrreducible1*factor1**2) + "}-\sqrt{" + str(radicandoIrreducible1*factor2**2) + "}}{-" + str(factorExterno3) + "\sqrt{" + str(radicandoIrreducible1*factor3**2) + "}+\sqrt{" + str(radicandoIrreducible1*factor4**2) + "}" + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas

def generaOperacionesTipo6(radicandosIrreducibles, solucion, numeroOperaciones, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        radicandoIrreducible1 = radicandosIrreducibles[random.randint(1, len(radicandosIrreducibles)-1)]
        factor1 = random.randint(1, int(maximoPositivo/2))
        factor2 = random.randint(1, int(maximoPositivo/2))
        factor3 = random.randint(1, int(maximoPositivo/2))
        factor4 = random.randint(1, int(maximoPositivo/2))
        factorExterno1 = random.randint(1, maximoPositivo)
        factorExterno2 = random.randint(1, maximoPositivo)
        factorExterno3 = random.randint(1, maximoPositivo)
        factorExterno4 = random.randint(1, maximoPositivo)        
        if (-factor3*factorExterno3+factor4) != 0 and (factor1*factorExterno1-factor2)/(-factor3*factorExterno3+factor4) == solucion:
            textoOperacion = "$" + "\dfrac{" + str(factorExterno1) + "\sqrt[3]{" + str(radicandoIrreducible1*factor1**3) + "}-\sqrt[3]{" + str(radicandoIrreducible1*factor2**3) + "}}{-" + str(factorExterno3) + "\sqrt[3]{" + str(radicandoIrreducible1*factor3**3) + "}+\sqrt[3]{" + str(radicandoIrreducible1*factor4**3) + "}" + "}" + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas    


numeroTiposOperaciones = 6
#######################################################################################
# INICIO del código LaTeX específico para esta ficha
#######################################################################################
for koko in range(len(elementos)):
    funcionesBasicas.escribeInicioFichaLaTeX(datos,tema,fLaTeX)
    # Ahora escribimos las instrucciones específicas para esta ficha.
    fLaTeX.write(r"Para desencriptarlo, tendr\'{a}s que simplificar al máximo una serie de expresiones con radicales. Cada vez que la tengas simplificada, busca \textbf{el factor que multiplica al radical} en la tabla y apunta la letra que le corresponde."+"\n")
    fLaTeX.write(r"\vspace{0.75\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{2}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    fLaTeX.write(r"	\textbf{Operación} & \textbf{Resultado} & \textbf{Letra} \\"+"\n")
    fLaTeX.write(r"	\hline"+"\n")
    # Añadimos al archivo fuente LaTeX las operaciones para cada letra de este elemento.
    print(str(koko+1), "de", str(len(elementos)),":", elementos[koko])
    operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones,len(elementos[koko]))
    for papa in range(len(elementos[koko])):
        # Obtenemos el número correspondiente a cada letra del primer elemento, y generamos unas cuantas operaciones que dan ese número como resultado.
        # De ellas nos quedamos con la primera. De esa forma, letras iguales tendrán probablemente operaciones diferentes.
        if codigoAlfabetico.get(elementos[koko][papa]) is not None:
            #----------------------------------------------
            exec("cadenas = generaOperacionesTipo" + str(operacionesDistintas[papa]+1) + "(radicandosIrreducibles, codigoAlfabetico.get(elementos[koko][papa]), numeroOperacionesDistintas, maximoPositivo)")
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
