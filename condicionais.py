n1 = n2 = 0


n1 = float(input("Digite a primeira nota: "))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print("Aprovado com média: ", media)

elif media >= 5:
    print("Recuperação com média: ", media)
    
else:
    print("Reprovado com média: ", media)
    
print(f"A média das notas {n1} e ({n2} é {media:.2f})")
