nome = str(input('Qual é o seu nome? ')).strip() # Pede para o usuário digitar o nome.
if nome == 'Wilson': # Se o nome for Wilson
    print('Que Nome bonito você tem!')
elif nome == 'Thiago' or nome == 'Pedro' or nome == 'Maria': # Se o nome for Thiago, Pedro ou Maria
    print('Seu nome é bem comum no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana': # Se o nome for Ana, Claudia, Jessica ou Juliana
    print('Belo nome de Mulher')
else: # Se o nome não for Wilson, Thiago,
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')