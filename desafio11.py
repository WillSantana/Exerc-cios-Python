largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'A parede tem dimensões {largura} x {altura} , totalizando {area:.2f}m² de área. Para pintar essa parede, você precisará de {tinta:.2f} litros de tinta.')
