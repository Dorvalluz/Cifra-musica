# Cifra-musica
"""Cantar e tocar Legiao Urbana - Geração Coca cola - 
inclui um slider que controla o tamanho do texto dinamicamente, utilizado app pydroid3."""

import tkinter as tk
import pygame
import os

# Nome do arquivo de música
MUSIC_FILE = "coca.mp3"

# Função para encontrar o arquivo de música no diretório atual e seus subdiretórios
def find_music_file(filename):
    """Procura o arquivo de música no diretório atual e seus subdiretórios."""
    for root, dirs, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Função para atualizar a posição do texto
def update_text_position():
    global y_pos, scrolling
    if scrolling:
        y_pos -= 1  # Move 1 pixel a cada atualização
        canvas.move(text_id, 0, -1)
        
        if y_pos < -text_height:
            y_pos = window_height
            canvas.coords(text_id, window_width // 2, y_pos)
        
        canvas.after(30, update_text_position)  # Atualiza a cada 30ms

# Função para iniciar ou parar o letreiro e a música
def toggle_scrolling():
    global scrolling, y_pos
    if scrolling:
        scrolling = False
        pygame.mixer.music.stop()
        play_button.config(text="PLAY")
        y_pos = window_height  # Redefine a posição do letreiro
        canvas.coords(text_id, window_width // 2, y_pos)
    else:
        scrolling = True
        pygame.mixer.music.play()
        play_button.config(text="STOP")
        update_text_position()
        root.after(160000, stop_all)  # Para tudo após 2:40 (160 segundos)

# Função para parar música e letreiro após 2:20
def stop_all():
    global scrolling
    scrolling = False
    pygame.mixer.music.stop()
    play_button.config(text="PLAY")
    y_pos = window_height  # Redefine a posição do letreiro
    canvas.coords(text_id, window_width // 2, y_pos)

# Função para atualizar o tamanho da fonte
def update_font_size(size):
    """Atualiza o tamanho da fonte do texto no canvas."""
    global text_id
    current_coords = canvas.coords(text_id)
    canvas.delete(text_id)
    text_id = canvas.create_text(window_width // 2, current_coords[1], text=text, font=("Arial", size), anchor='center')
    global text_height
    text_height = canvas.bbox(text_id)[3] - canvas.bbox(text_id)[1]

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Tenta encontrar o arquivo de música
music_path = find_music_file(MUSIC_FILE)

# Carrega o arquivo de música se for encontrado
if music_path:
    try:
        pygame.mixer.music.load(music_path)
    except pygame.error as e:
        print("Erro ao carregar o arquivo de música:", e)
else:
    print(f"Arquivo de música '{MUSIC_FILE}' não encontrado.")

# Cria a janela principal
root = tk.Tk()
root.title("Letreiro Vertical - Geração Coca-Cola")

# Define as dimensões da janela
window_width = 700
window_height = 1400
root.geometry(f"{window_width}x{window_height}")

# Cria um canvas para desenhar o texto
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Adiciona o texto ao canvas
text = ("\n" * 80 +  # Pula 80 linhas no início
        "B\n   Quando nascemos fomos programados\n"
        "D             A\n   A receber o que vocês\n"
        "B\n   nos empurraram com os enlatados\n"
        "D            A\n   dos U.S.A., de 9 às 6\n"
        "B\n   Desde pequenos nós comemos lixo\n"
        "D           A\n   Comercial e industrial\n"
        "B\n   Mas agora chegou nossa vez\n"
        "D                        A\nVamos cuspir de volta o lixo em cima de vocês\n"
        "(refrão)\n"
        "B            A           G\n   Somos os filhos da revolução\n"
        "B             A           G\n   Somos burgueses sem religião\n"
        "B        A         G\n   Somos o futuro da nação\n"
        "A       D    B\nGeração Coca-Cola\n"
        "(2ª estrofe)\n"
        "B\n   Depois de vinte anos na escola\n"
        "D                A\n   Não é difícil aprender\n"
        "B\n   Todas as manhas do seu jogo sujo\n"
        "D                 A\n   Não é assim que tem que ser?\n"
        "B\n   Vamos fazer nosso dever de casa\n"
        "D             A\n   E aí então, vocês vão ver\n"
        "B\n   Suas crianças derrubando reis\n"
        "D                      A\nFazer comédia no cinema com as suas leis\n"
        "(refrão)\n"
        "B            A           G\n   Somos os filhos da revolução\n"
        "B             A           G\n   Somos burgueses sem religião\n"
        "B        A         G\n   Somos o futuro da nação\n"
        "A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n"
        "A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n"
        "(solo 2 - 3x)\nG   A   B\n"
        "B\n   Depois de vinte anos na escola\n"
        "D                A\n   Não é difícil aprender\n"
        "B\n   Todas as manhas do seu jogo sujo\n"
        "D                 A\n   Não é assim que tem que ser?\n"
        "B\n   Vamos fazer nosso dever de casa\n"
        "D             A\n   E aí então, vocês vão ver\n"
        "B\n   Suas crianças derrubando reis\n"
        "D                      A\nFazer comédia no cinema com as suas leis\n"
        "(refrão)\n"
        "B            A           G\n   Somos os filhos da revolução\n"
        "B             A           G\n   Somos burgueses sem religião\n"
        "B        A         G\n   Somos o futuro da nação\n"
        "A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n"
        "A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n"
        "(solo 2 - 3x)\nG   A   B\n"
        "Composição: Renato Russo\nElaborado por Dorval Luz")

# Centraliza o texto e posiciona-o fora da parte inferior da tela
text_id = canvas.create_text(window_width // 2, window_height, text=text, font=("Arial", 7), anchor='center')

# Calcula a altura do texto
text_height = canvas.bbox(text_id)[3] - canvas.bbox(text_id)[1]

# Inicializa a posição y do texto
y_pos = window_height
scrolling = False

# Cria o botão PLAY/STOP
play_button = tk.Button(root, text="PLAY", command=toggle_scrolling)
play_button.pack(pady=2)

# Cria o slider para alterar o tamanho da fonte
font_slider = tk.Scale(root, from_=7, to=30, orient='horizontal', label='Tamanho da Fonte', command=lambda size: update_font_size(int(size)))
font_slider.pack(pady=2)
font_slider.set(7)  # Tamanho inicial da fonte

# Inicia o loop principal do Tkinter
root.mainloop()
