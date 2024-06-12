qtd=0
soma=0
media=0
valor=float(input("DIGITE UM VALOR:"))
            
while(valor>0.0):
    soma=soma+valor
    qtd=qtd+1
    #entrada de valores
    valor=float(input("DIGITE UM VALOR:"))

#Caso didite um valor negativo o laço encerra
media=soma/qtd
print("\n total de soma ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores:", media)