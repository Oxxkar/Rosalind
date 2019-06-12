"""
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
"""


def countDNA(pathFile):
    #pathFile = File
    pathFix = pathFile.replace("\\","/")
    f = open(pathFix, "r")
    DNA = f.read()
    print("A:" + str(DNA.count("A")))
    print("C:" + str(DNA.count("C")))
    print("G:" + str(DNA.count("G")))
    print("T:" + str(DNA.count("T")))

    
