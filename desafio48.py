#48 - Soma Ímpares Múltiplos de Três: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Exemplo de soma de números ímpares múltiplos de três

#definição da função
# - Aqui é definida uma função chamada `soma_impares_multiplos_de_tres`. 
# - Essa função não recebe parâmetros e será responsável por calcular 
# - a soma e a quantidade de números ímpares múltiplos de 3 no intervalo de 1 a 500.
def soma_impares_multiplos_de_tres():
    
    # - Inicializa as variáveis
    # - `soma`: Variável que acumula a soma dos números que atendem à condição.
    # - `cont`: Variável que conta quantos números atendem à condição.
    soma = 0  # Inicializa a soma
    cont = 0  # Inicializa o contador
    
    # - O loop `for` percorre todos os números de 1  501 (inclusive). 
    # - A variável `i` assume cada valor dentro desse intervalo.?
    for i in range(1, 501):  # Loop de 1 a 500
        
    # - A condição `if` verifica se o número `i` é ímpar e múltiplo de 3.
    # - `i % 2 != 0`: Verifica se o número `i` é ímpar. Um número é ímpar quando o resto da divisão por 2 não é zero.
    # - `i % 3 == 0`: Verifica se o número `i` é múltiplo de 3. Um número é múltiplo de 3 quando o resto da divisão por 3 é igual a zero.
    # - A condição combina essas duas verificações usando o operador lógico `and`. Assim, apenas números que são ímpares **e** múltiplos de 3 passam pela condição.
     if i % 2 != 0 and i % 3 == 0:  # Verifica se o número é ímpar e múltiplo de três
            
            
            # - incrementa o contador `cont` em 1.
            # - Adiciona o número `i` à variável `soma`.
            # - Isso significa que, para cada número que atende à condição,
            # - o contador é atualizado e o número é somado à soma total.
            # - `cont += 1`: Incrementa o contador em 1.
            # - `soma += i`: Adiciona o número `i` à soma total.
            # - O operador `+=` é uma forma abreviada de escrever `soma = soma + i`.
            # - Assim, a cada iteração do loop, se o número `i` atender à condição,
            # - ele é adicionado à soma total e o contador é atualizado.
            cont += 1  # Incrementa o contador
            soma += i  # Adiciona o número à soma 
            
            
            
    # - retorno dos contadores
    # - Após o loop, a função retorna dois valores:
    # - `soma`: A soma total dos números ímpares múltiplos de 3 encontrados.
    # - `cont`: A quantidade total de números que atenderam à condição.
    # - O retorno é feito como uma tupla, permitindo que ambos os valores sejam capturados quando a função for chamada.
    # - A função retorna a soma e a quantidade de números ímpares múltiplos de 3 encontrados no intervalo.
    # - Isso significa que, ao final da execução da função, você terá a soma total e a contagem de números que atenderam à condição.    
    return soma, cont

# - Armazenamento dos valores retornados
# - A função `soma_impares_multiplos_de_tres` é chamada e seus valores retornados são armazenados nas variáveis `soma` e `cont`.
# - `soma`: A soma total dos números ímpares múltiplos de 3 encontrados.
# - `cont`: A quantidade total de números que atenderam à condição.
soma, cont = soma_impares_multiplos_de_tres()


# - O resultado é exibido na tela usando a função `print`.
# - A função `print` exibe a soma total dos números ímpares múltiplos de 3 encontrados no intervalo.
# - A mensagem inclui a quantidade de números que atenderam à condição.
# - A variável `cont` contém a quantidade total de números que atenderam à condição.
print(f"A soma de todos os {cont} valores solicitados é {soma}")  # Exibe a soma total
