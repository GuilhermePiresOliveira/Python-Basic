import time

letra = " Python e melhor q java"
string_repetida = letra * 1000

for char in string_repetida:
    print(char, end="", flush=True)  # O argumento 'flush=True' garante que a saída seja exibida imediatamente
    time.sleep(0.1)  # Atraso de 0,5 segundos entre cada caractere

print()  # Pula para a próxima linha após a exibição completa da string
