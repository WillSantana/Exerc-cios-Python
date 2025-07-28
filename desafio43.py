#43 - Índice de Massa Corporal: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: – IMC abaixo de 18.5: Abaixo do Peso; – Entre 18.5 e 25: Peso Ideal; – 25 até 30: Sobrepeso; – 30 até 40: Obesidade; – Acima de 40: Obesidade Mórbida.
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é \033[31m{imc:.1f}\033[m e você está \033[31mABAIXO DO PESO\033[m!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é \033[32m{imc:.1f}\033[m e você está no \033[32mPESO IDEAL\033[m!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é \033[33m{imc:.1f}\033[m e você está com \033[33mSOBREPESO\033[m!')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é \033[34m{imc:.1f}\033[m e você está com \033[34mOBESIDADE\033[m!')
else:
    print(f'Seu IMC é \033[35m{imc:.1f}\033[m e você está com \033[35mOBESIDADE MÓRBIDA\033[m!')