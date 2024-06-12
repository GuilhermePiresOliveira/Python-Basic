notaA=float(input("informe a primeira nota:"))
notaB=float(input("informe a segunda nota:"))

#Calcula media  
mediafinal = (notaA + notaB) /2

#Vefiricação
if mediafinal >= 7.0:
   print("A media: %.1f - APROVADO "% mediafinal)

else:
   print("A media: %.1f - REPROVADO "% mediafinal)
