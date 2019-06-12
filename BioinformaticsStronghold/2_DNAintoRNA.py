"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t
"""
"""
Funcion simple para transformar DNA en RNA
Agregamos la direccion del archivo del DNA.
El primer replace es para cambiar los slash invertidos de Windows.
Abrir el archivo
Guardar el archivo
Remplazar T por U, guardar.
Regresar

NOTA: en el path file escribir r de raw r"pathfile\fileName"
"""
def DNA2RNA(pathFile):
    pathFix = pathFile.replace("\\","/")
    f = open(pathFix, "r")
    DNA = f.read()
    RNA = DNA.replace("T","U")
    return RNA
