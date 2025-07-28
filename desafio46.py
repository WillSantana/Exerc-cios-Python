#46 - Contagem regressiva: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
# Contagem regressiva   
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Bum! Bum! Pooow! Estourou!")
time.sleep(1)
print("Feliz ano novo!")
# Exemplo de contagem regressiva para fogos de artifício
# def contagem_regressiva():
#     for i in range(10, 0, -1):
#         print(i)
#         time.sleep(1)
#     print("Feliz ano novo!")
# contagem_regressiva()