import matplotlib.pyplot as plt

valores = [10, 20, 30, 40, 50]
nomes = ['A', 'B', 'C', 'D', 'E']
plt.bar(nomes, valores, color='blue')
plt.xlabel('Nomes')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Simples')

# Substitua plt.show() por:
plt.savefig('grafico.png')  # Salva como imagem
print("Gráfico salvo como 'grafico.png'")

