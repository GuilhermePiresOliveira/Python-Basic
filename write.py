arquivo=open('arqText.txt', 'w')

arquivo.write('curso pytron \n')
arquivo.write('write.py')
arquivo.write('PYTHON E MELHOR Q JAVA')
arquivo.close()

#leitura do arquivo texto

leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close()
