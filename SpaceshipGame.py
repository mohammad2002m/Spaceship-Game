from ast import Global
from time import sleep
from turtle import width
import pygame

pygame.font.init()

WIDTH = 900
HEIGHT = 500

SPACESHIP_WIDTH = 45
SPACESHIP_HEIGHT = 45

BORDER_WIDTH = 20
BORDER_HEIGHT = 500

FRAME_RATE = 60
SPEED = 3 
MAX_BULLET = 20 
BULLET_SPEED = 4

WHITE = (255 , 255 , 255)
BLACK = (0 , 0 , 0)
YELLOW = (255 , 255 , 0)
RED = (255 , 0 , 0)


WIN = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Mohammad Alshareef is the best game developer")

BORDER = pygame.Rect(WIDTH / 2 - BORDER_WIDTH / 2  , 0 , BORDER_WIDTH , BORDER_HEIGHT)

BACKGROUND_IMG = pygame.image.load('Assets/space.png')

PLAYER1_IMG = pygame.image.load('Assets/spaceship_red.png')
PLAYER2_IMG = pygame.image.load('Assets/spaceship_yellow.png')

BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

PLAYER1_IMG = pygame.transform.scale(PLAYER1_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
PLAYER2_IMG = pygame.transform.scale(PLAYER2_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

PLAYER1_IMG = pygame.transform.rotate(PLAYER1_IMG, 90)
PLAYER2_IMG = pygame.transform.rotate(PLAYER2_IMG, 270)

PLAYER1 = pygame.Rect(100 , 200 , SPACESHIP_WIDTH , SPACESHIP_HEIGHT)
PLAYER2 = pygame.Rect(800 , 200 , SPACESHIP_WIDTH , SPACESHIP_HEIGHT)


player1_health = 10
player2_health = 10

HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WIN_FONT = pygame.font.SysFont('comicsans', 30)

def Winning(Winner):
    WINNER_TEXT = HEALTH_FONT.render( "The Winner is: " + Winner , 1, WHITE)
    WIN.blit(WINNER_TEXT , (WIDTH / 2 - WINNER_TEXT.get_width() / 2 , HEIGHT / 2 - WINNER_TEXT.get_height() / 2))
    pygame.display.update()


def MovementColisions(PLAYER1_BULLETS, PLAYER2_BULLETS):
        KeysPressed = pygame.key.get_pressed()
        if KeysPressed[pygame.K_a] and PLAYER1.x - SPEED > 0:
            PLAYER1.x -= SPEED
        if KeysPressed[pygame.K_d] and PLAYER1.x + SPEED + SPACESHIP_WIDTH < WIDTH / 2 - BORDER_WIDTH / 2:
            PLAYER1.x += SPEED
        if KeysPressed[pygame.K_w] and PLAYER1.y - SPEED > 0:
            PLAYER1.y -= SPEED
        if KeysPressed[pygame.K_s] and PLAYER1.y + SPEED + SPACESHIP_HEIGHT < 500:
            PLAYER1.y += SPEED

        if KeysPressed[pygame.K_LEFT] and PLAYER2.x - SPEED > WIDTH / 2 + BORDER_WIDTH / 2:
            PLAYER2.x -= SPEED
        if KeysPressed[pygame.K_RIGHT] and PLAYER2.x + SPEED + SPACESHIP_WIDTH < 900:
            PLAYER2.x += SPEED
        if KeysPressed[pygame.K_UP] and PLAYER2.y - SPEED > 0:
            PLAYER2.y -= SPEED
        if KeysPressed[pygame.K_DOWN] and PLAYER2.y + SPEED + SPACESHIP_HEIGHT < 500:
            PLAYER2.y += SPEED


        for bullet in PLAYER1_BULLETS: bullet.x += BULLET_SPEED
        for bullet in PLAYER2_BULLETS: bullet.x -= BULLET_SPEED

        global player1_health , player2_health

        #Handel Collision
        TEMP1 = TEMP2 = []
        for bullet in PLAYER1_BULLETS:
            if PLAYER2.colliderect(bullet):
                PLAYER1_BULLETS.remove(bullet)
                player2_health -= 1

            elif bullet.x >= 900:
                PLAYER1_BULLETS.remove(bullet)

        for bullet in PLAYER2_BULLETS:
            if PLAYER1.colliderect(bullet):
                PLAYER2_BULLETS.remove(bullet)
                player1_health -= 1

            elif bullet.x <= 0:
                PLAYER2_BULLETS.remove(bullet)


def DrawAndRender():
    WIN.blit(BACKGROUND_IMG , (0 , 0))
    pygame.draw.rect(WIN , BLACK , BORDER)

    WIN.blit(PLAYER1_IMG , (PLAYER1.x , PLAYER1.y))
    WIN.blit(PLAYER2_IMG , (PLAYER2.x , PLAYER2.y))

    PLAYER1_HEALTH_TEXT = HEALTH_FONT.render( "Health: " + str(player1_health), 1, WHITE)
    PLAYER2_HEALTH_TEXT = HEALTH_FONT.render( "Health: " + str(player2_health), 1, WHITE)

    WIN.blit(PLAYER1_HEALTH_TEXT, (10, 10))
    WIN.blit(PLAYER2_HEALTH_TEXT, (WIDTH - PLAYER2_HEALTH_TEXT.get_width() - 10, 10))

    for bullet in PLAYER1_BULLETS: pygame.draw.rect(WIN , RED , bullet)
    for bullet in PLAYER2_BULLETS: pygame.draw.rect(WIN , YELLOW , bullet)

    pygame.display.update()
        


def RunTheGame():
    clock = pygame.time.Clock()
    GameRunning = True

    global player1_health , player2_health

    player1_health = 10
    player2_health = 10

    global PLAYER1_BULLETS , PLAYER2_BULLETS

    PLAYER1_BULLETS = []
    PLAYER2_BULLETS = []

    while (GameRunning):
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameRunning = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(PLAYER1_BULLETS) < MAX_BULLET:
                    PLAYER1_BULLETS.append(pygame.Rect(PLAYER1.x , PLAYER1.y + SPACESHIP_HEIGHT / 2 , 5 , 5))

                if event.key == pygame.K_RCTRL and len(PLAYER2_BULLETS) < MAX_BULLET:
                    PLAYER2_BULLETS.append(pygame.Rect(PLAYER2.x , PLAYER2.y + SPACESHIP_HEIGHT / 2 , 5 , 5))
        


        if player1_health <= 0 or player2_health <= 0:
            if player1_health <= 0: Winning("Player2")
            if player2_health <= 0: Winning("Player1")
            sleep(3)
            RunTheGame()


        MovementColisions(PLAYER1_BULLETS , PLAYER2_BULLETS)
        DrawAndRender()

RunTheGame()
