produto = float(input('Digite o preço do produto: R$ '))
dav = produto - (produto * 0.10)
dp = produto - (produto * 0.08)
print(f'O produto custa R${produto:.2f}, com 10% de desconto a vista, ele custará R${dav:.2f}')
print(f'O produto custa R${produto:.2f}, com 8% de desconto parcelado, ele custará R${dp:.2f}')