#cores no terminal
# \033[style;text;backm
# style: 0 sem estilo, 1 negrito, 4 sublinhado, 7 negativo
# text: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 cinza
# back: 40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 ciano, 47 cinza
# \033[m
# \033[0;33;44m
# \033[1;35;43m
# \033[4;30;45m
# \033[7;30;47m
# \033[m
# \033[0;30;41m
# \033[0;30;42m
# \033[0;30;43m
# \033[0;30;44m
# \033[0;30;45m
# \033[0;30;46m
# \033[0;30;47m
# \033[m
# \033[0;30;41m
# \033[0;31;42m
# \033[0;32;43m
# \033[0;33;44m
# \033[0;34;45m
# \033[0;35;46m
# \033[0;36;47m
# \033[0;37;40m
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[1;32;44mOlá, Mundo!\033[m')
print('\033[1;33;45mOlá, Mundo!\033[m')
print('\033[1;34;46mOlá, Mundo!\033[m')
print('\033[1;35;47mOlá, Mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[1;31m{a}\033[m e \033[1;32m{b}\033[m!!!')

nome = 'Santana'    
cores = {'limpa': '\033[m', 
        'azul': '\033[34m', 
        'amarelo': '\033[33m', 
        'preto': '\033[30m', 
        'branco': '\033[37m', 
        'vermelho': '\033[31m', 
        'verde': '\033[32m', 
        'roxo': '\033[35m', 
        'ciano': '\033[36m'}
print(f'Olá! Muito prazer em te conhecer, {cores["vermelho"]}{nome}{cores["limpa"]}!!!')
print(f'Olá! Muito prazer em te conhecer, {cores["verde"]}{nome}{cores["limpa"]}!!!')
print(f'Olá! Muito prazer em te conhecer, {cores["azul"]}Santana{cores["limpa"]}!!!')