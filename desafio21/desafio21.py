import pygame   # Importa a biblioteca pygame
import time     # Importa a biblioteca time

# Inicializa o mixer do  pygame
pygame.mixer.init()

# Carrega o arquivo de música
pygame.mixer.music.load('/home/sti/Área de Trabalho/pysthonprojeto/desafio21/Ira! - Tarde Vazia.mp3')

# Inicia a música
pygame.mixer.music.play()

# Aguarda ate qeu a música termine
while pygame.mixer.music.get_busy():
    time.sleep(1)