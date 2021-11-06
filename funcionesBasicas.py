#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:59:22 2021

@author: sergio
"""
import random


#######################################################################################
def creaCodigoAlfabetico():
    codigoAlfabetico = {
        'A': -13,
        'Á': -13,
        'B': -12,
        'C': -11,
        'D': -10,
        'E': -9,
        'É': -9,
        'F': -8,
        'G': -7,
        'H': -6,
        'I': -5,
        'Í': -5,
        'J': -4,
        'K': -3,
        'L': -2,
        'M': -1,
        'N': 0,
        'Ñ': 1,
        'O': 2,
        'Ó': 2,
        'P': 3,
        'Q': 4,
        'R': 5,
        'S': 6,
        'T': 7,
        'U': 8,
        'Ú': 8,        
        'V': 9,
        'W': 10,
        'X': 11,
        'Y': 12,
        'Z': 13}
    return codigoAlfabetico

#######################################################################################   
def leeElementos(argv):
    # El nombre del archivo txt que contiene los elementos a codificar
    # lo hemos pasado como segundo argumento.
    nombreArchivoTxtElementos = argv[2]
    
    elementos = []
    
    #with open(nombreArchivoTxtElementos) as fTxt:
    with open(nombreArchivoTxtElementos, 'r', errors='replace', encoding="utf8") as fTxt:
        # Leemos de golpe todas las líneas del archivo txt.
        lines = fTxt.readlines()
        tema = lines[0] # En la primera línea estará el tema, listo para escribirlo en la ficha.
        # Vamos leyendo los elementos en las líneas siguientes.
        for linea in range(len(lines)-1):
            # Pasamos a mayúsculas cada elemento, quitando el último carácter (retorno de carro).
            elementos.append(lines[linea+1][0:-1].upper()) 
    fTxt.close()
       
    # Aleatorizamos la lista para que, al repartirla en clase, estén desordenadas.
    random.shuffle(elementos)
    return tema,elementos

#######################################################################################   
def leeDatosCabecera(argv):
    # El nombre del archivo txt que contiene los datos de la ficha
    # lo hemos pasado como primer argumento.
    nombreArchivoTxtCabecera = argv[1]
    
    Centro = []
    Nivel = []
    Asignatura = []
    CE = []
    Est = []
    Titulo = []
    Archivo = []
    
    #with open(nombreArchivoTxtCabecera) as fTXT:
    with open(nombreArchivoTxtCabecera, 'r', errors='replace', encoding="utf8") as fTXT:
        # Leemos de golpe todas las líneas del archivo txt.
        lines = fTXT.readlines()
        # Vamos leyendo línea a línea.
        for linea in range(len(lines)):
            posicionComas = lines[linea].find(',')
            texto = lines[linea]
            palabraClave = texto[0:posicionComas]
            if palabraClave == "Centro":
                # En lines[linea] está el nombre del centro.
                Centro.append(texto[posicionComas+1:-1].replace("%","\%"))
            elif palabraClave == "Nivel":
                # En lines[linea] está el nivel (1 ESO, 2 ESO, etc.)
                Nivel.append(texto[posicionComas+1:-1].replace("%","\%"))
            elif palabraClave == "Asignatura":
                # En lines[linea] está la asignatura.
                Asignatura.append(texto[posicionComas+1:-1].replace("%","%"))
            elif palabraClave == "CE":
                # En lines[linea] está un criterio.
                CE.append(texto[posicionComas+1:-1].replace("%","%"))
            elif palabraClave == "Est":
                # En lines[linea] está un estándar.
                Est.append(texto[posicionComas+1:-1].replace("%","%"))
            elif palabraClave == "Título":
                # En lines[linea] está el título para la ficha.
                Titulo.append(texto[posicionComas+1:-1].replace("%","%"))
            elif palabraClave == "Archivo":
                # En lines[linea] está el nombre del archivo LaTeX para la ficha.
                Archivo.append(texto[posicionComas+1:-1].replace("%","%"))                    
    fTXT.close()
    
    datos = {
        "Centro": Centro[0],
        "Nivel": Nivel[0],
        "Asignatura": Asignatura[0],
        "CE": CE,
        "Est": Est,
        "Título": Titulo[0],
        "Archivo": Archivo[0]
    }
    return datos


#######################################################################################   
def creaArchivoLaTeX(datos,archivoElementos,directorioFichas):
    # Creamos el archivo LaTeX en el directorio para las fichas.
    nombreArchivoElementos = archivoElementos[archivoElementos.rfind('/')+1:-4] # Sin la ruta.
    rutaArchivoLaTeX = directorioFichas + datos["Centro"] + r"_" + datos["Archivo"] + r"_" + nombreArchivoElementos + ".tex"
    fLaTeX = open(rutaArchivoLaTeX, "w", encoding="utf8")
    return rutaArchivoLaTeX,fLaTeX

#######################################################################################   
def escribePreambuloLaTeX(datos,fLaTeX):
    fLaTeX.write(r"\documentclass{exam}"+"\n")
    fLaTeX.write(r"\usepackage[margin=0.6in,portrait,a4paper]{geometry}"+"\n")
    fLaTeX.write(r"\renewcommand{\familydefault}{\sfdefault}"+"\n")
    fLaTeX.write(r"\usepackage[scaled=1]{helvet}"+"\n")
    fLaTeX.write(r"\usepackage[helvet]{sfmath}"+"\n")
    fLaTeX.write(r"\usepackage[spanish]{babel}"+"\n")
    fLaTeX.write(r"\selectlanguage{spanish}"+"\n")
    fLaTeX.write(r"\usepackage[utf8]{inputenc}"+"\n")
    fLaTeX.write(r"\usepackage{amsmath}"+"\n")
    fLaTeX.write(r"\usepackage{enumitem}"+"\n")
    fLaTeX.write(r"\usepackage[table]{xcolor}"+"\n")
    fLaTeX.write(r"\usepackage{graphicx}"+"\n")
    fLaTeX.write(r"\usepackage[skins]{tcolorbox}"+"\n")
    fLaTeX.write(r"\usepackage{tabularx}"+"\n")
    fLaTeX.write(r"\usepackage[normalem]{ulem}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\linespread{1.5}"+"\n")
    fLaTeX.write(r"\pagestyle{headandfoot}"+"\n")
    fLaTeX.write(r"\footskip -40pt"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\firstpagefooter{}{}{\includegraphics[width=0.25cm]{logoTwitterGris}\textcolor{lightgray}{\texttt{@toreroeconomico}}}"+"\n")
    fLaTeX.write(r"\runningfooter{}{}{\includegraphics[width=0.25cm]{logoTwitterGris}\textcolor{lightgray}{\texttt{@toreroeconomico}}}"+"\n")
    fLaTeX.write(r"\firstpageheader{\textbf{\textcolor{darkgray}{\large " + datos["Centro"] + r"}}}{}{\textbf{\textcolor{darkgray}{\large Departamento de Matemáticas}}}"+"\n")
    fLaTeX.write(r"\runningheader{\textbf{\textcolor{darkgray}{\large " + datos["Centro"] + r"}}}{}{\textbf{\textcolor{darkgray}{\large Departamento de Matemáticas}}}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\begin{document}"+"\n")
    fLaTeX.write(r""+"\n")

def escribeInicioFichaLaTeX(datos,tema,fLaTeX):
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.25}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{lX}"+"\n")
    fLaTeX.write(r"	\textbf{Nombre y apellidos:} & \textcolor{white}{olakase}\\ "+"\n") 
    fLaTeX.write(r"\end{tabularx} "+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.75}"+"\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|}"+"\n")
    fLaTeX.write(r"	\hline "+"\n")
    fLaTeX.write(r"	\cellcolor{lightgray}{\textbf{\textcolor{black}{\normalsize " + datos["Nivel"] + r" " + datos["Asignatura"] + r"}}} \\\hline "+"\n") 
    for nuja in range(len(datos["CE"])):
        fLaTeX.write(r"	\baselineskip=10pt \cellcolor{white}{\footnotesize\textcolor{darkgray}{\smallsize \textbf{CE} " + datos["CE"][nuja] + r"}} \\\hline"+"\n")
    for nuji in range(len(datos["Est"])):
        fLaTeX.write(r"	\baselineskip=10pt\cellcolor{white}{\footnotesize\textcolor{darkgray}{\smallsize \textbf{Estándar} " + datos["Est"][nuji] + r"}} \\\hline"+"\n")    
    fLaTeX.write(r"\end{tabularx} "+"\n")
    fLaTeX.write(r"\vspace{0.5\baselineskip}"+"\n")    
    fLaTeX.write(r"\begin{center}"+"\n")
    fLaTeX.write(r"	 \begin{tcolorbox}[spartan,height=1cm,valign=center,sharp corners,shadow={0mm}{0mm}{0mm}{white},boxrule=0mm,coltitle=black,colframe=black,colback=lightgray,width=(\textwidth),nobeforeafter]"+"\n")
    if len(datos["Título"]) >= 39:
        fLaTeX.write(r"	     \centering\Large\textbf{" + datos["Título"] + r"}"+"\n")
    else:
        fLaTeX.write(r"	     \centering\huge\textbf{" + datos["Título"] + r"}"+"\n")
    fLaTeX.write(r"\end{tcolorbox}"+"\n")
    fLaTeX.write(r"\end{center}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"En esta ficha se ha encriptado " + tema + r" usando un cifrado de sustituci\'{o}n. Cada letra ha sido sustituida por un n\'{u}mero entero, de acuerdo con la siguiente tabla:"+"\n")
    fLaTeX.write(r"\vspace{-1.0\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1}"+"\n")
    fLaTeX.write(r"\begin{center}"+"\n")
    fLaTeX.write(r"	\begin{scriptsize}"+"\n")
    fLaTeX.write(r"		\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}"+"\n")
    fLaTeX.write(r"			\hline"+"\n")
    fLaTeX.write(r"			A & B & C & D & E & F & G & H & I & J & K & L & M & N & Ñ & O & P & Q & R & S & T & U & V & W & X & Y & Z \\"+"\n")
    fLaTeX.write(r"			\hline"+"\n")
    fLaTeX.write(r"			-13 & -12 & -11 & -10 & -9 & -8 & -7 & -6 & -5 & -4 & -3 & -2 & -1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 \\"+"\n")
    fLaTeX.write(r"			\hline"+"\n")
    fLaTeX.write(r"		\end{tabular}"+"\n")
    fLaTeX.write(r"	\end{scriptsize}"+"\n")
    fLaTeX.write(r"\end{center}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\vspace{0.25\baselineskip}"+"\n")
    
#######################################################################################       
def escribeFinalFichaLaTeX(fLaTeX):
    fLaTeX.write(r"\vspace{0.5\baselineskip}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\noindent\begin{minipage}{1\textwidth}"+"\n")
    fLaTeX.write(r"\begin{center}"+"\n")
    fLaTeX.write(r"   Lo encriptado en esta ficha era:"+"\n")
    fLaTeX.write(r"   \vspace{0.25\baselineskip}"+"\n")
    fLaTeX.write(r"   "+"\n")
    fLaTeX.write(r"	 \begin{tcolorbox}[spartan,height=0.75cm,sharp corners,shadow={0mm}{0mm}{0mm}{white},boxrule=0.1mm,coltitle=white,colframe=black,colback=lightgray,width=(\textwidth),nobeforeafter]"+"\n")
    fLaTeX.write(r"   \end{tcolorbox}"+"\n")
    fLaTeX.write(r"\end{center}"+"\n")
    fLaTeX.write(r"\end{minipage}{"+"\n")
    fLaTeX.write(r"\vspace{\fill}"+"\n")
    fLaTeX.write(r""+"\n")
    fLaTeX.write(r"\newpage"+"\n")    
