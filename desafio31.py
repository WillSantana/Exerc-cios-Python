distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    preco: float = distancia * 0.50
else:
    preco: float = distancia * 0.45
print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.')
print(f'E o preço da sua passagem será de R${preco:.2f}.')