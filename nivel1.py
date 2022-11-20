#!/usr/bin/python3

import pygame
import sprite_pacman


pygame.init()

# F UNCIONES ENCARGADAS DE CREAR LOS MUROS Y LA COMIDA
def dibuja_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, BLUE, rectangulo)
    #imagen_muro = pygame.image.load('muros.png')
    #muro_nuevo = pygame.transform.scale(imagen_muro,(20,20))
    #superficie.blit(muro_nuevo,rectangulo)

def dibuja_comida(superficie, rectangulo):
    pygame.draw.rect(superficie, BLANCO, rectangulo, 20, 20)

def dibuja_food_special(superficie, rectangulo):
    imagen_food= pygame.image.load('food.png')
    food = pygame.transform.scale(imagen_food,(20,20))
    superficie.blit(food,rectangulo)


# FUNCION QUE LEE EL MAPA(VARIABLE = LISTA) Y FORMA LISTA DE MUROS Y COMIDA
def construir_mapa(mapa):
    muros=[]
    comida=[]
    food_special=[]
    contador_comida = 0
    x=0
    y=0
    # RECORRE LA LISTA MAPA
    for muro in mapa:
        for ladrillo in muro:
            # SI HAY UNA X ES UN MURO Y LO AGREGA A LA LISTA CON SUS COORDENADAS
            if ladrillo == "x":
                # coordernadas y el tamanno donde se ubicaran en el mapa
                muros.append(pygame.Rect(x, y, 20, 20))
                # se mueve a la siguiente columna
                x+= 20

            # SI ES UNA M ES COMIDA NORMAL
            elif ladrillo == "m":
                # coordernadas y el tamanno donde se ubicaran en el mapa
                comida.append(pygame.Rect(x+7, y+10, 7, 7))
                x += 20
                contador_comida += 1
            # SI ES UNA F ES COMIDA ESPECIAL
            elif ladrillo == "f":
                food_special.append(pygame.Rect(x, y, 10, 10))
                x += 20
                contador_comida += 1
            # SI NO ES NINGUN CARACTER SOLO PASA AL SIGUIENTE PIXEL
            else:
                x += 20
        # SE MUEVE DE FILA
        x = 0
        y += 20 # Va corriendo a lo largo de todas la comlumnas
    return muros,comida, contador_comida, food_special


# FUNCION PARA RECORRER LA LISTA DE MUROS
def recorre_lista_muros(superficie, muros):
    for m in muros:
        # LLAMA LA FUNCION PARA CREAR LOS MUROS
        dibuja_muro(superficie, m)


# FUNCION PARA RECORRER LA LISTA DE COMIDA
def recorre_lista_comida(superficie, comida):
    for m in comida:
        # LLAMA LA FUNCION PARA CREAR LA COMIDA
        dibuja_comida(superficie, m)

# FUNCION PARA RECORRER LA LISTA DE COMIDA
def recorre_lista_food_special(superficie, food_special):
    for m in food_special:
        # LLAMA LA FUNCION PARA CREAR LA FOOD SPECIAL
        dibuja_food_special(superficie, m)




#!!!!!!!!!!!!!!!!!!!!!!!!!!1
#PREGUNTAAAAAAAAAAAAAAAAAAAAAAR POR QUE NO FUNCIANA ASI
def eliminar_comida(comida, contador_comida):
    for v_comida in list(comida):
        if pacman.rect.colliderect(v_comida):
            comida.remove(v_comida)
            contador_comida -= 1
    # pygame.mixer.music.load('/home/ranleon/Downloads/pacman_chomp.wav')
    # pygame.mixer.music.play(1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!1
#PREGUNTAAAAAAAAAAAAAAAAAAAAAAR POR QUE NO FUNCIANA ASI
def eliminar_food_especial(food_special, contador_comida):
    for v_comida in list(food_special):
        if pacman.rect.colliderect(v_comida):
            comida.remove(v_comida)
            contador_comida -= 1



def main(contador_comida):
    game_over = False
    reloj = pygame.time.Clock() # variable de tiempo, ejecucion del programa


    while game_over == False:
        reloj.tick(FPS) # ajustando los FPS
        # EVENTO PARA QUE EL EXIT DE LA VENTANA FUNCIONE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


        pacman.handle_event(event)
        ventana_juego.fill(pygame.Color('black'))
        # SCALE DE LA IMAGEN DE PACMAN
        image_nuevo = pygame.transform.scale(pacman.image, (20, 20))
        # IMPRIME LA IMAGEN DE PAGAN CON SU SPRITE DE MOVIMIENTOS
        ventana_juego.blit(image_nuevo, pacman.rect)


        # funciones para crear el mapa
        recorre_lista_muros(ventana_juego, muros)
        recorre_lista_comida(ventana_juego, comida)
        recorre_lista_food_special(ventana_juego, food_special)
        #imprime el texto de la comida
        ventana_juego.blit(texto, (100, 560))

        #RECORRE LA LISTA DE COMIDA
        for v_comida in list(comida):
            # ELIMINA DE LA LISTA DE COMIDA SI PACMAN TOCA LA COMIDA
            if pacman.rect.collidepoint(v_comida.centerx, v_comida.centery):
                comida.remove(v_comida)

                # SONIDI FOOD
                pygame.mixer.music.load('pacman_chomp.wav')
                pygame.mixer.music.play()
                # VA RESTANDO LA COMIDA
                contador_comida -= 1

        #RECORRE LA LISTA DE FOOD SPECIAL
        for v_food_special in list(food_special):
            # ELIMINA DE LA LISTA DE FOOD SPECIAL SI PACMAN TOCA LA COMIDA
            if pacman.rect.collidepoint(v_food_special.centerx, v_food_special.centery):
                food_special.remove(v_food_special)
                # VA RESTANDO LA COMIDA EN EL CONTADOR
                contador_comida -= 1
                # SONIDO ESPECIAL FOOD
                pygame.mixer.music.load('pacman_eatfruit.wav')
                pygame.mixer.music.play()

        #IMPRIME EN PANTALLA EL CONTADOR DE COMIDA
        puntos = fuente1.render(str(contador_comida), True, BLANCO)
        ventana_juego.blit(puntos, (400, 560))



        # for muro in muros :
        #     if pacman.colliderect(muro):
        #         if event.key == pygame.K_LEFT:
        #             self.update('right')


        #termina cuando la comida es 0
        if contador_comida == 0:
            game_over = True

        # pygame.mixer.music.load('/home//Downloads/pacman_beginning.wav')
        # pygame.mixer.music.play(8888888)


        pygame.display.flip()
        pygame.display.update()

    pygame.quit ()

# COLORES
VERDE = (0, 255, 0)
BLANCO= (255, 255, 255)
RED=(255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(8888888)

# VARIABLES
ancho_ventana = 900
alto_ventana = 600
ventana_juego = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("NIVEL 1                   SUERTEEEE")
clock = pygame.time.Clock()
pacman = sprite_pacman.pacman((ancho_ventana/2, alto_ventana/2))
FPS = 50
fuente1 = pygame.font.SysFont("segoe print",40)
texto = fuente1.render("COMIDA DISPONIBLE", True, BLANCO)


# MAPAS

mapa = [
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "xmmmmmmmmmmmfmmmmmmxmmmmmmmmmmmmmmmmmmx",
                "xmxxxxmxxxxxxxxxxxmxmxxxxmxxxxxxxxxxxmx",
                "xmxxxxmxxxxxxxxxxxmxmxxxxmxxxxxxxxxxxmx",
                "xmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmx",
                "xmxxxxmxmxxxxxxmxxxxxxxxxmxmxxxxxxxxxmx",
                "xmmmmmmmmmxmmmmmmmmxmmmmmmmmxmmmmmmmmmx",
                "xmmmmmmmmmxmmmmmmmmxmmmmmmmmxmmmmmmmmmx",
                "xmmmxxmmmmmmmmmmmmmmmmmmmmmmmmmmmxxmmmx",
                "xmfm                               mfmx",
                "xmmm      xxxxxxxx     xxxxxxx     mmmx",
                "xmmm      x                  x     mmmx",
                "xmmm      x                  x     mmmx",
                "xmmm      x                  x     mmmx",
                "xmmm      x                  x     mmmx",
                "xmmm      xxxxxxxxxxxxxxxxxxxx     mmmx",
                "xmmm                               mmmx",
                "xmmm                               mmmx",
                "xmmmmmmmmmfmmmmmmmmxmmmmmmmmmmmfmmmmmmx",
                "xmxxxxmxxxxxxxxxxxmxmxxxxmxxxxxxxxxxxmx",
                "xmxxxxmxxxxxxxxxxxmxmxxxxmxxxxxxxxxxxmx",
                "xmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmx",
                "xmxxxxmxmxxxxxxmxxxxxxxxxmxmxxxxxxxxxmx",
                "xmmmmmmmmmxmmmmmmmmxmmmmmmmmxmmmmmmmmmx",
                "xmmmxxmmmmxmmmmmmmmxmmmmmmmmxmmmmxxmmmx",
                "xmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmx",
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
]
# 900/20= columnas
# 600/20= filas

# COLORES
VERDE = (0, 255, 0)
BLANCO= (255, 255, 255)
RED=(255, 0, 0)
BLUE = (0, 0, 255)

# main
# llamar la funcion de construit mapa primero para que forme la listas
if __name__ == '__main__':
    muros, comida, contador_comida, food_special = construir_mapa(mapa)
    main(contador_comida)
