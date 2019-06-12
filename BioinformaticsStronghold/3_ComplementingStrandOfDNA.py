"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.


"""




def revComplementDNA(pathFile):
    #pathFile = File
    pathFix = pathFile.replace("\\","/")
    f = open(pathFix, "r")
    DNA = f.read()
    revDNA = DNA[::-1]
    replacement1 = revDNA.replace("A", "t")
    replacement2 = replacement1.replace("T", "a")
    replacement3 = replacement2.replace("G", "c")
    replacement4 = replacement3.replace("C", "g")
    return replacement4.upper()
