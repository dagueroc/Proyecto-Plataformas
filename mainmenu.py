import pygame
import os

# Iniciar
pygame.init()

# centrar el juego
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Resolucion del juego
screen_ancho = 900
screen_altura = 600
screen = pygame.display.set_mode((screen_ancho, screen_altura))


# Para el render del texto
def texto_formato(message, textoFont, textoTamano, textoColor, textoFondo):
    Fontnuevo = pygame.font.Font(textoFont, textoTamano)
    Textonuevo = Fontnuevo.render(message, True, textoFondo, textoColor)

    return Textonuevo


# Colores, se pueden agregar mas de ser necesario
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

# Fuentes para el texto
font1 = "upheavtt.ttf"
font2 = "fuentepac.ttf"

# FPS del juego
clock = pygame.time.Clock()
FPS = 30


# Menu principal
def main_menu():
    # Sonidos del menu
    pygame.mixer.music.load("fondomenu.mp3")
    pygame.mixer.music.play(-1)
    sonido_tecla = pygame.mixer.Sound("tecla.mp3")
    menu = True
    selected = "iniciar"

    # Funcionamiento del menu, dependiendo de las teclas que se usen
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(sonido_tecla)
                if event.key == pygame.K_UP:
                    selected = "iniciar"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "iniciar":
                        print("iniciar")
                        os.system('/usr/bin/python3 nivel1.py')
                        quit()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Interfaz del menu
        # Fondo de pantalla negro, con el formato de las opciones
        screen.fill(negro)
        titulo = texto_formato("Pac-man't", font1, 80, 0, amarillo)
        if selected == "iniciar":
            texto_iniciar = texto_formato(" >JUGAR ", font1, 75, azul, blanco)
        else:
            texto_iniciar = texto_formato("JUGAR", font1, 75, negro, blanco)
        if selected == "quit":
            texto_salir = texto_formato(" >SALIR ", font1, 75, azul, blanco)
        else:
            texto_salir = texto_formato("SALIR", font1, 75, negro, blanco)

        # subtitle_rect=subtitle.get_rect()
        titulo_rect = titulo.get_rect()
        inicio_rect = texto_iniciar.get_rect()
        salir_rect = texto_salir.get_rect()

        # Texto del menu principal
        # screen.blit(subtitle, (screen_ancho/2 - (subtitle_rect[2]/2), 160))
        screen.blit(titulo, (screen_ancho/2 - (titulo_rect[2]/2), 80))
        screen.blit(texto_iniciar, (screen_ancho/2 - (inicio_rect[2]/2), 300))
        screen.blit(texto_salir, (screen_ancho/2 - (salir_rect[2]/2), 390))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Pacman Menu")


# Inicio del menu
main_menu()
pygame.quit()
quit()
