# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:33:46 2024

@author: atcri

PARA INVERTIR UNA CADENA DE ADN, PUEDO PONER cad = cad[::-1]

"""

#El usuario dice la cadena que es
x = input("Introduce una cadena de Nucleótidos: ")
cad = x.upper()

#Comprobamos
if len(cad)%3 == 0:
    cadaa = ''
    
    n = 0
    for n in range(0,len(cad),3):
        print(cad[n]+cad[n+1]+cad[n+2])
        letra1 = cad[n]
        letra2 = cad[n+1]
        letra3 = cad[n+2]
        
        cadena = letra1 + letra2 + letra3

        #Cálculo
        if cadena in ["GGU", "GGC", "GGG", "GGA" ]:
            print('\nGlicina\n\n')
            aa = 'G'

        elif cadena in ["GCU", "GCC", "GCA", "GCG"]:
            print('Alanina')
            aa = 'A'
            
        elif cadena in ["GUA", "GUG", "GUU", "GUC"]:
            print('Valina')
            aa = 'V'
            
        elif cadena in ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]:
            print('Leucina')
            aa = 'L'
            
        elif cadena in ["AUU", "AUC", "AUA"]:
            print('Isoleucina')
            aa = 'I'
            
        elif cadena in ["UUU", "UUC"]:
            print('Fenilalanina')
            aa = 'F'
            
        elif cadena in ["CAU", "CAC"]:
            print('Histidina')
            aa = 'H'
    
        elif cadena in ["UGU", "UGC"]:
            print('Cisteína')
            aa = 'C'

        elif cadena in ["UAU", "UAC"]:
            print('Tirosina')
            aa = 'Y'
            
        elif cadena in ["GAU", "GAC"]:
            print('Ácido Aspártico')
            aa = 'D'
            
        elif cadena in ["AGA", "AGG", "CGU", "CGC", "CGA", "CGG"]:
            print('Arginina')
            aa = 'R'
            
        elif cadena in ["AAA", "AAG"]:
            print('Lisina')
            aa = 'K'
            
        elif cadena in ["GAA", "GAG"]:
            print('Ácido Glutamico')
            aa = 'E'
            
        elif cadena in ["AUG"]:
            print('Metionina')
            aa = 'M'
            
        elif cadena in ["AAU", "AAC"]:
            print('Asparragina')
            aa = 'N'    
            
        elif cadena in ["ACU", "ACA", "ACC", "ACG"]:
            print('Treonina')
            aa = 'T'

        elif cadena in ["CAG", "CAA"]:
            print('Glutamina')
            aa = 'Q'
            
        elif cadena in ['CCA', 'CCU', 'CCG', 'CCC']:
            print('Prolina')
            aa = 'P'
            
        elif cadena in ["AGU", "AGC", "UCU", "UCC", "UCA", "UCG"]:
            print('Serina')
            aa = 'S'
            
        elif cadena in ["UGG"]:
            print('Triptofano')
            aa = 'W'

        elif cadena in ["UAA", "UAG", "UGA"]:
            print('Esa secuencia no codifica un aminoacido,' 
                  'es un codón de terminación o de "Stop"')
            aa = ''

        else:
            print('Esa combinacion no es correcta,' 
                  'prueba a poner mayúsculas o poner letras, 1 a 1 que si sean bases')
            
        
        cadaa = cadaa + aa

elif len(cad)%3 == 1:
    cad_1_sobra = cad + '__'
    cadaa = ''
    
    for n in range(0,len(cad),3):
        print(cad_1_sobra[n]+cad_1_sobra[n+1]+cad_1_sobra[n+2])
        
        cadena = cad_1_sobra[n:n+3]
    
        #Cálculo
        if cadena in ["GGU", "GGC", "GGG", "GGA" ]:
            print('\nGlicina\n\n')
            aa = 'G'

        elif cadena in ["GCU", "GCC", "GCA", "GCG"]:
            print('Alanina')
            aa = 'A'
            
        elif cadena in ["GUA", "GUG", "GUU", "GUC"]:
            print('Valina')
            aa = 'V'
            
        elif cadena in ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]:
            print('Leucina')
            aa = 'L'
            
        elif cadena in ["AUU", "AUC", "AUA"]:
            print('Isoleucina')
            aa = 'I'
            
        elif cadena in ["UUU", "UUC"]:
            print('Fenilalanina')
            aa = 'F'    
            
        elif cadena in ["CAU", "CAC"]:
            print('Histidina')
            aa = 'H'
    
        elif cadena in ["UGU", "UGC"]:
            print('Cisteína')
            aa = 'C'

        elif cadena in ["UAU", "UAC"]:
            print('Tirosina')
            aa = 'Y'
            
        elif cadena in ["GAU", "GAC"]:
            print('Ácido Aspártico')
            aa = 'D'
            
        elif cadena in ["AGA", "AGG", "CGU", "CGC", "CGA", "CGG"]:
            print('Arginina')
            aa = 'R'
            
        elif cadena in ["AAA", "AAG"]:
            print('Lisina')
            aa = 'K'
            
        elif cadena in ["GAA", "GAG"]:
            print('Ácido Glutamico')
            aa = 'E'
            
        elif cadena in ["AUG"]:
            print('Metionina')
            aa = 'M'
            
        elif cadena in ["AAU", "AAC"]:
            print('Asparragina')
            aa = 'N'    
            
        elif cadena in ["ACU", "ACA", "ACC", "ACG"]:
            print('Treonina')
            aa = 'T'

        elif cadena in ["CAG", "CAA"]:
            print('Glutamina')
            aa = 'Q'
            
        elif cadena in ['CCA', 'CCU', 'CCG', 'CCC']:
            print('Prolina')
            aa = 'P'
            
        elif cadena in ["AGU", "AGC", "UCU", "UCC", "UCA", "UCG"]:
            print('Serina')
            aa = 'S'
            
        elif cadena in ["UGG"]:
            print('Triptofano')
            aa = 'W'

        elif cadena in ["UAA", "UAG", "UGA"]:
            print('Esa secuencia no codifica un aminoacido,' 
                  'es un codón de terminación o de "Stop"')
            aa = ''
        
        elif cadena in ["U__", "C__", "G__", "A__"]:
            print("La cadena tiene un codón sin completar, solo se sabe 1 base, podria ser cualquier cosa.")
            aa = ''
            
        else:
            print('Esa combinacion no es correcta,' 
                  'prueba a poner mayúsculas o poner letras, 1 a 1 que si sean bases')
        
        cadaa = cadaa + aa
        
elif len(cad)%3 == 2:
    cad_2_sobra = cad + '_'
    cadaa = ''
    
    n = 0
    for n in range(0,len(cad),3):
        print(cad_2_sobra[n]+cad_2_sobra[n+1]+cad_2_sobra[n+2])
        letra1 = cad_2_sobra[n]
        letra2 = cad_2_sobra[n+1]
        letra3 = cad_2_sobra[n+2]
        
        cadena = letra1 + letra2 + letra3
    
        #Cálculo
        if cadena in ["GGU", "GGC", "GGG", "GGA" ]:
            print('\nGlicina\n\n')
            aa = 'G'

        elif cadena in ["GCU", "GCC", "GCA", "GCG"]:
            print('Alanina')
            aa = 'A'
            
        elif cadena in ["GUA", "GUG", "GUU", "GUC"]:
            print('Valina')
            aa = 'V'
            
        elif cadena in ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]:
            print('Leucina')
            aa = 'L'
            
        elif cadena in ["AUU", "AUC", "AUA"]:
            print('Isoleucina')
            aa = 'I'
            
        elif cadena in ["UUU", "UUC"]:
            print('Fenilalanina')
            aa = 'F'
            
        elif cadena in ["CAU", "CAC"]:
            print('Histidina')
            aa = 'H'
    
        elif cadena in ["UGU", "UGC"]:
            print('Cisteína')
            aa = 'C'

        elif cadena in ["UAU", "UAC"]:
            print('Tirosina')
            aa = 'Y'
            
        elif cadena in ["GAU", "GAC"]:
            print('Ácido Aspártico')
            aa = 'D'
            
        elif cadena in ["AGA", "AGG", "CGU", "CGC", "CGA", "CGG"]:
            print('Arginina')
            aa = 'R'
            
        elif cadena in ["AAA", "AAG"]:
            print('Lisina')
            aa = 'K'
            
        elif cadena in ["GAA", "GAG"]:
            print('Ácido Glutamico')
            aa = 'E'
            
        elif cadena in ["AUG"]:
            print('Metionina')
            aa = 'M'
            
        elif cadena in ["AAU", "AAC"]:
            print('Asparragina')
            aa = 'N'    
            
        elif cadena in ["ACU", "ACA", "ACC", "ACG"]:
            print('Treonina')
            aa = 'T'

        elif cadena in ["CAG", "CAA"]:
            print('Glutamina')
            aa = 'Q'
            
        elif cadena in ['CCA', 'CCU', 'CCG', 'CCC']:
            print('Prolina')
            aa = 'P'
            
        elif cadena in ["AGU", "AGC", "UCU", "UCC", "UCA", "UCG"]:
            print('Serina')
            aa = 'S'
            
        elif cadena in ["UGG"]:
            print('Triptofano')
            aa = 'W'

        elif cadena in ["UAA", "UAG", "UGA"]:
            print('Esa secuencia no codifica un aminoacido,' 
                  'es un codón de terminación o de "Stop"')
            aa = ''
        
        elif cadena in ["UU_", "UA_", "UG_", "UC_", "CC_","CA_", "CG_","CU_", "GU_", "GA_", "GC_", "GG_", "AU_", "AG_", "AC_", "AA_",]:
            print("La cadena tiene un codón sin completar, se saben 2 bases, podria ser cualquier cosa.")
            aa = '(Stop)'
    
        else:
            print('Esa combinacion no es correcta,' 
                  'prueba a poner mayúsculas o poner letras, 1 a 1 que si sean bases')
        
        cadaa = cadaa + aa
        
else:
    print("Lo has bugeado")
    
print("\nLa cadena de proteica en formato de sus siglas es:\n\t",cadaa)



