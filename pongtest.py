import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Configuración de los colores
black = (0, 0, 0)
white = (255, 255, 255)

# Configuración de las paletas
player_width, player_height = 15, 60
enemy_width, enemy_height = 15, 60

player_speed = 7

# Inicialización de las posiciones
player_x, player_y = 20, height // 2 - player_height // 2
enemy_x, enemy_y = width - 20 - enemy_width, height // 2 - enemy_height // 2

# Inicialización de la pelota
ball_size = 15
ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 7, 7

# Función principal del juego
def game():
    global player_y, enemy_y, ball_x, ball_y, ball_speed_x, ball_speed_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < height - player_height:
            player_y += player_speed

        # Movimiento de la pelota
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Rebote en las paredes superior e inferior
        if ball_y <= 0 or ball_y >= height - ball_size:
            ball_speed_y = -ball_speed_y

        # Rebote en las paletas
        if (
            player_x < ball_x + ball_size
            and player_x + player_width > ball_x
            and player_y < ball_y + ball_size
            and player_y + player_height > ball_y
        ) or (
            enemy_x < ball_x + ball_size
            and enemy_x + enemy_width > ball_x
            and enemy_y < ball_y + ball_size
            and enemy_y + enemy_height > ball_y
        ):
            ball_speed_x = -ball_speed_x

        # Movimiento de la paleta del enemigo
        if enemy_y < ball_y and enemy_y < height - enemy_height:
            enemy_y += player_speed
        elif enemy_y > ball_y and enemy_y > 0:
            enemy_y -= player_speed

        # Dibujar en la pantalla
        screen.fill(black)
        pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, white, (enemy_x, enemy_y, enemy_width, enemy_height))
        pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Ejecutar el juego
if __name__ == "__main__":
    game()
