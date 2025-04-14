import pygame
import tkinter as tk
import os
import time

# Caminho do arquivo de música
MUSIC_FILE = r"C:\Users\Dorval\Desktop\GITHB\Cifra-musica\coca.mp3"

# Texto da música
text = """\n" * 800 + 
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
        "Composição: Renato Russo\nElaborado por Dorval Luz"""

# Inicializa o pygame para o áudio
pygame.mixer.init()

# Cria a janela com Tkinter
root = tk.Tk()
root.title("Letreiro Vertical - Geração Coca-Cola")
root.geometry("900x500")
root.resizable(True, True)  # Permite redimensionamento da janela

# Canvas para o letreiro
canvas = tk.Canvas(root, width=700, height=500, bg="black")
canvas.pack(side="left", fill="both", expand=True)  # O canvas fica à esquerda

# Texto do letreiro (inicialmente invisível)
lyrics = canvas.create_text(350, 800, text=text, font=("Arial", 16), fill="green", justify="center", anchor="center")

# Painel de controle dos botões (lado direito)
panel = tk.Frame(root, width=200, bg="#333333", height=500)
panel.pack(side="right", fill="y")

# Variáveis de controle
scrolling = False
yPos = 500  # Posição inicial do texto (fora da tela)
scroll_speed = 0.1  # Velocidade da rolagem
music_length = 0  # Duração da música em segundos
start_time = None  # Tempo de início da música para controlar o atraso

# Função de rolagem do texto sincronizada com a música (karaoke)
def scroll_text():
    global yPos, music_length
    if scrolling:
        # Atualiza a posição do texto com base no tempo da música
        current_time = pygame.mixer.music.get_pos() / 1000  # Tempo da música em segundos
        yPos = 500 - (current_time / music_length) * 800  # Controla a rolagem com base no tempo da música
        canvas.coords(lyrics, 350, yPos)  # Atualiza a posição do texto

        # Se o texto sair da tela, reinicia a rolagem
        if yPos < -canvas.bbox(lyrics)[3]:
            yPos = 500

        canvas.after(10, scroll_text)

# Função de controle de play/stop
def toggle_scrolling():
    global scrolling, start_time
    if scrolling:
        pygame.mixer.music.pause()
        play_button.config(text="Play")
        stop_button.config(state="normal")  # Habilita o botão de stop
        scrolling = False
    else:
        pygame.mixer.music.play()
        play_button.config(text="Stop")
        stop_button.config(state="normal")  # Habilita o botão de stop
        crolling = True
        start_time = time.time()  # Marca o momento em que a música começa a tocar
        scroll_text()

# Função de controle de pausa
def pause_music():
    global scrolling
    if scrolling:
        pygame.mixer.music.pause()
        pause_button.config(text="Resume")
        scrolling = False
    else:
        pygame.mixer.music.unpause()
        pause_button.config(text="Pause")
        scrolling = True
        scroll_text()

# Função para reiniciar a música e sincronizar o letreiro
def stop_music():
    global scrolling
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    play_button.config(text="Stop")
    stop_button.config(state="disabled")  # Desabilita o botão de stop
    scrolling = True
    scroll_text()

# Função para aumentar o tamanho da fonte
def increase_font_size():
    font_size = int(canvas.itemcget(lyrics, "font").split()[1])
    canvas.itemconfig(lyrics, font=("Arial", font_size + 2))

# Função para diminuir o tamanho da fonte
def decrease_font_size():
    font_size = int(canvas.itemcget(lyrics, "font").split()[1])
    if font_size > 10:
        canvas.itemconfig(lyrics, font=("Arial", font_size - 2))

# Função para mudar o tema (cores)
def change_theme():
    current_color = canvas.itemcget(lyrics, "fill")
    new_color = "white" if current_color == "green" else "green"
    canvas.itemconfig(lyrics, fill=new_color)

# Função para carregar e preparar a música
def load_music():
    global music_length
    if os.path.exists(MUSIC_FILE):
        pygame.mixer.music.load(MUSIC_FILE)
        music_length = pygame.mixer.Sound(MUSIC_FILE).get_length()  # Duração da música
        pygame.mixer.music.set_volume(1.0)

# Função para verificar se o atraso de 11 segundos passou
def check_start_time():
    if start_time and time.time() - start_time >= 11:
        canvas.itemconfig(lyrics, state="normal")  # Torna o letreiro visível após 11 segundos
        toggle_scrolling()  # Inicia a rolagem após 11 segundos

# Botões para controle no painel à direita
play_button = tk.Button(panel, text="Play", command=toggle_scrolling, bg="#555555", fg="white")
play_button.pack(pady=10, fill="x")

increase_font_button = tk.Button(panel, text="A+", command=increase_font_size, bg="#555555", fg="white")
increase_font_button.pack(pady=5, fill="x")

decrease_font_button = tk.Button(panel, text="A-", command=decrease_font_size, bg="#555555", fg="white")
decrease_font_button.pack(pady=5, fill="x")

theme_button = tk.Button(panel, text="Mudar Cores", command=change_theme, bg="#555555", fg="white")
theme_button.pack(pady=5, fill="x")

stop_button = tk.Button(panel, text="Stop", command=stop_music, bg="#555555", fg="white", state="disabled")
stop_button.pack(pady=5, fill="x")

pause_button = tk.Button(panel, text="Pause", command=pause_music, bg="#555555", fg="white")
pause_button.pack(pady=5, fill="x")

# Carregar a música
load_music()

# Iniciar a aplicação
root.after(10, check_start_time)
root.mainloop()
