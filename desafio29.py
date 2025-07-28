velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voçê excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Voçê deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com Segurança!')