# def fatorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fatorial(n -1)
    
# fatorial_de_5 = fatorial(5)
# print(f"O fatorial de 5 é: {fatorial_de_5}")
# fatorial_de_7 = fatorial(7)
# print(f"O fatorial de 7 é: {fatorial_de_7}")
# fatorial_de_10 = fatorial(10)
# print(f"O fatorial de 10 é: {fatorial_de_10}")

def fatorial(n):
    for i in range(1, n + 1):
        if i == 1:
            resultado = 1
        else:
            resultado *= i
    return resultado

print(f"O fatorial de 5 é: {fatorial(5)}")