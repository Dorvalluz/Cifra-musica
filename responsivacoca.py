import pygame
import os
import time

# Inicialização
pygame.init()

# Obtém tamanho da tela do celular
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Geração Coca-Cola")

# Cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Fonte proporcional ao tamanho da tela
font_size = int(screen_height * 0.03)
font = pygame.font.SysFont('Arial', font_size)

# Música
MUSIC_FILE = os.path.join(os.path.dirname(__file__), "coca.mp3")
pygame.mixer.music.load(MUSIC_FILE)

# Texto do letreiro
text = """\n(intro) B D A

\n   \n
       
        B\n   Quando nascemos fomos programados\n
        D             A\n   A receber o que vocês\n\n
        B\n   nos empurraram com os enlatados\n\n
        D            A\n   dos U.S.A., de 9 às 6\n\n
        B\n   Desde pequenos nós comemos lixo\n\n
        D           A\n   Comercial e industrial\n\n
        B\n   Mas agora chegou nossa vez\n\n
        D                        A\nVamos cuspir de volta o lixo em cima de vocês\n
        (refrão)

        B            A           G\n   Somos os filhos da revolução\n
        B             A           G\n   Somos burgueses sem religião\n
        B        A         G\n   Somos o futuro da nação\n
        \n   \n


        A       D    B\nGeração Coca-Cola\n
        (2ª estrofe)\n\
        B\n   Depois de vinte anos na escola\n\
        D                A\n   Não é difícil aprender\n\
        B\n   Todas as manhas do seu jogo sujo\n\
        D                 A\n   Não é assim que tem que ser?\n\
        B\n   Vamos fazer nosso dever de casa\n\
        D             A\n   E aí então, vocês vão ver\n\
        B\n   Suas crianças derrubando reis\n\
        D                      A\nFazer comédia no cinema com as suas leis\n\
        (refrão)\n\n
        B            A           G\n   Somos os filhos da revolução\n\
        B             A           G\n   Somos burgueses sem religião\n\
        B        A         G\n   Somos o futuro da nação\n\
        A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n\
        A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n\
        (solo 2 - 3x)\nG   A   B\n\n
\n chorus  \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   \n
\n   B\n
        Depois de vinte anos na escola\n\n
        D                A\n   Não é difícil aprender\n\n
        B\n   Todas as manhas do seu jogo sujo\n\n
        D                 A\n   Não é assim que tem que ser?\n\n
        B\n   Vamos fazer nosso dever de casa\n\n
        D             A\n   E aí então, vocês vão ver\n\n
        B\n   Suas crianças derrubando reis\n\n
        D                      A\nFazer comédia no cinema com as suas leis\n\n
        (refrão)\n\n
        B            A           G\n   Somos os filhos da revolução\n\n
        B             A           G\n   Somos burgueses sem religião\n\n
        B        A         G\n   Somos o futuro da nação\n\n
        A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n\n
        A       D    B     A       D    B\nGeração Coca-Cola, geração coca-cola\n\n
        (solo 2 - 3x)\nG   A   B\n\n
        Composição: Renato Russo\nElaborado por Dorval Luz"""




# Variáveis de controle
y_pos = screen_height
scrolling = False
scroll_speed = 0.8
paused = False
letreiro_iniciado = False
music_start_time = None
pause_start_time = None
paused_time_total = 0
stop_after_seconds = 138  # 2 minutos e 18 segundos

# Funções
def draw_text():
    global y_pos
    y = y_pos
    for line in text.split('\n'):
        rendered = font.render(line, True, GREEN)
        screen.blit(rendered, (screen_width // 2 - rendered.get_width() // 2, y))
        y += rendered.get_height()

def restart_music():
    pygame.mixer.music.play()
    global y_pos, scrolling, paused, letreiro_iniciado
    global music_start_time, paused_time_total
    y_pos = screen_height
    scrolling = True
    paused = False
    letreiro_iniciado = True
    music_start_time = time.time()
    paused_time_total = 0

def toggle_pause():
    global paused, pause_start_time, paused_time_total
    if paused:
        pygame.mixer.music.unpause()
        paused_time_total += time.time() - pause_start_time
        paused = False
    else:
        pygame.mixer.music.pause()
        pause_start_time = time.time()
        paused = True

def increase_font():
    global font_size
    font_size += 2
    return pygame.font.SysFont('Arial', font_size)

def decrease_font():
    global font_size
    if font_size > 10:
        font_size -= 2
    return pygame.font.SysFont('Arial', font_size)

# Loop principal
def main():
    global scrolling, y_pos, paused, font, letreiro_iniciado
    global music_start_time, paused_time_total
    clock = pygame.time.Clock()
    running = True

    # Botões proporcionais à tela
    btn_width = int(screen_width * 0.25)
    btn_height = int(screen_height * 0.08)
    margin = int(screen_height * 0.03)

    play_button = pygame.Rect(margin, screen_height - btn_height - margin, btn_width, btn_height)
    pause_button = pygame.Rect(margin, screen_height - 2 * (btn_height + margin), btn_width, btn_height)
    stop_button = pygame.Rect(margin, screen_height - 3 * (btn_height + margin), btn_width, btn_height)

    while running:
        screen.fill(BLACK)
        draw_text()

        if scrolling and not paused:
            y_pos -= scroll_speed
            if y_pos < -font.get_height() * len(text.split('\n')):
                y_pos = screen_height

        if music_start_time and not paused:
            elapsed_time = time.time() - music_start_time - paused_time_total
            if elapsed_time >= stop_after_seconds:
                pygame.mixer.music.stop()
                scrolling = False
                paused = False
                y_pos = screen_height
                letreiro_iniciado = False
                music_start_time = None
                paused_time_total = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if play_button.collidepoint(pos):
                    restart_music()
                elif pause_button.collidepoint(pos):
                    toggle_pause()
                elif stop_button.collidepoint(pos):
                    pygame.mixer.music.stop()
                    scrolling = False
                    paused = False
                    y_pos = screen_height
                    letreiro_iniciado = False
                    music_start_time = None
                    paused_time_total = 0
                elif event.button == 4:
                    font = increase_font()
                elif event.button == 5:
                    font = decrease_font()

        # Desenhar botões
        pygame.draw.rect(screen, WHITE, play_button)
        pygame.draw.rect(screen, WHITE, pause_button)
        pygame.draw.rect(screen, WHITE, stop_button)

        screen.blit(font.render("Play", True, BLACK), (play_button.x + 20, play_button.y + 10))
        screen.blit(font.render("Pause", True, BLACK), (pause_button.x + 10, pause_button.y + 10))
        screen.blit(font.render("Stop", True, BLACK), (stop_button.x + 20, stop_button.y + 10))

        pygame.display.flip()
        clock.tick(60)

# Executar
if __name__ == "__main__":
    main()
    pygame.quit()
