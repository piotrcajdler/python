"""
*** FINAL PROJECT ***
This game is called space invaders.
Your main task is to protect yourself
from enemies. Use space to shot and arrows
to move. Good luck!!


********
CODE OF MY GAME CAN BE COPIED
OR MODYFIED WITHOUT MENTIONING
AUTHOR
********

WRITTEN BY: PIOTR CAJDLER
"""

import pygame
import sys
import pygame.mixer
import random

# COLORS
GREEN = pygame.color.Color("green")
BLACK = pygame.color.Color("black")
YELLOW = pygame.color.Color(255, 232, 31)
WHITE = pygame.color.Color("white")
RED = pygame.color.Color("red")

# GAME CONSTANTS AND DEFINING VARIABLES
pygame.init()
FRAME = (1080, 720)
window = pygame.display.set_mode(FRAME)
pygame.display.set_caption("  GALAXY CIVIL WAR  ")
arena = window.get_rect()
fps = pygame.time.Clock()
ship = pygame.image.load("tie.png")
ship_rect = ship.get_rect()
ship_rect.midbottom = arena.midbottom
STEP = 5
bullet = pygame.image.load("bullet1.png")
bullet_rect = bullet.get_rect()
bullet_rect.center = ship_rect.midtop
game_background = pygame.image.load("space.jpg")
fly = pygame.mixer.Sound("ISD-Fly.wav")
shot = pygame.mixer.Sound("ISD-Laser3.wav")
pygame.mixer.set_num_channels(10)

# PARAMETERS

SHIP_Y = 400
SHIP_Y1 = 401
VEC1NUM = 4
VEC2NUM = 20
SCOREX = 800
SCOREY = 50
ALIEN_STEP_DOWN = 100
EASTEREGGNUM = 75
A1L = -300
A1R = -200
A2R = -400
A2L = -500
A3L = -600
A3R = -700
A4R = -800
A1U = 20
A1D = 200
A2U = 10
A2D = 120
TIME_S = 1000

# ALIENS (X-WINGS) LOCATION

alien1 = pygame.image.load("alien.png")
alien_rect1 = alien1.get_rect()
alien_rect1.center = random.randint(A1L, A1R), random.randint(A1U, A1D)
while alien_rect1.x % 5 == 0 or alien_rect1.x % 2 == 0:
    alien_rect1.x = random.randint(A1L, A1R)

alien2 = pygame.image.load("alien.png")
alien_rect2 = alien2.get_rect()
alien_rect2.center = random.randint(A2R, A1L), random.randint(A1U, A1D)
while alien_rect2.x % 5 == 0 or alien_rect2.x % 2 == 0:
    alien_rect2.x = random.randint(A2R, A1L)

alien3 = pygame.image.load("alien.png")
alien_rect3 = alien3.get_rect()
alien_rect3.center = random.randint(A2L, A2R), random.randint(A1U, A1D)
while alien_rect3.x % 5 == 0 or alien_rect3.x % 2 == 0:
    alien_rect3.x = random.randint(A2L, A2R)

alien4 = pygame.image.load("alien.png")
alien_rect4 = alien4.get_rect()
alien_rect4.center = random.randint(A3L, A2L), random.randint(A1U, A1D)
while alien_rect4.x % 5 == 0 or alien_rect4.x % 2 == 0:
    alien_rect4.x = random.randint(A3L, A2L)

alien5 = pygame.image.load("alien.png")
alien_rect5 = alien5.get_rect()
alien_rect4.center = random.randint(A3R, A3L), random.randint(A1U, A1D)
while alien_rect4.x % 5 == 0 or alien_rect4.x % 2 == 0:
    alien_rect4.x = random.randint(A3R, A3L)

alien6 = pygame.image.load("alien.png")
alien_rect6 = alien6.get_rect()
alien_rect6.center = random.randint(A4R, A3R), random.randint(A1U, A1D)
while alien_rect6.x % 5 == 0 or alien_rect6.x % 2 == 0:
    alien_rect6.x = random.randint(A4R, A3R)

# FONT AND OTHER GAME VARIABLES

font = pygame.font.Font('font.ttf', 48)

alien1_hit = 0
alien2_hit = 0
alien3_hit = 0
alien4_hit = 0
alien5_hit = 0
alien6_hit = 0
score = 0

alien_vec = [2, 0]
alien2_vec = [2, 0]
alien3_vec = [2, 0]
alien4_vec = [2, 0]
alien5_vec = [2, 0]
alien6_vec = [2, 0]


def aliens_location():
    """
    This module contains all ships positions and
    it is used to restart the game
    """
    global alien_rect1, alien_rect2, alien_rect3, alien_rect4
    global alien_rect5, alien_rect6

    alien1 = pygame.image.load("alien.png")
    alien_rect1 = alien1.get_rect()
    alien_rect1.center = random.randint(A1L, A1R), random.randint(A1U, A1D)
    while alien_rect1.x % 5 == 0 or alien_rect1.x % 2 == 0:
        alien_rect1.x = random.randint(A1L, A1R)

    alien2 = pygame.image.load("alien.png")
    alien_rect2 = alien2.get_rect()
    alien_rect2.center = random.randint(A2R, A1L), random.randint(A1U, A1D)
    while alien_rect2.x % 5 == 0 or alien_rect2.x % 2 == 0:
        alien_rect2.x = random.randint(A2R, A1L)

    alien3 = pygame.image.load("alien.png")
    alien_rect3 = alien3.get_rect()
    alien_rect3.center = random.randint(A2L, A2R), random.randint(A1U, A1D)
    while alien_rect3.x % 5 == 0 or alien_rect3.x % 2 == 0:
        alien_rect3.x = random.randint(A2L, A2R)

    alien4 = pygame.image.load("alien.png")
    alien_rect4 = alien4.get_rect()
    alien_rect4.center = random.randint(A3L, A2L), random.randint(A1U, A1D)
    while alien_rect4.x % 5 == 0 or alien_rect4.x % 2 == 0:
        alien_rect4.x = random.randint(A3L, A2L)

    alien5 = pygame.image.load("alien.png")
    alien_rect5 = alien5.get_rect()
    alien_rect4.center = random.randint(A3R, A3L), random.randint(A1U, A1D)
    while alien_rect4.x % 5 == 0 or alien_rect4.x % 2 == 0:
        alien_rect4.x = random.randint(A3R, A3L)

    alien6 = pygame.image.load("alien.png")
    alien_rect6 = alien6.get_rect()
    alien_rect6.center = random.randint(A4R, A3R), random.randint(A1U, A1D)
    while alien_rect6.x % 5 == 0 or alien_rect6.x % 2 == 0:
        alien_rect6.x = random.randint(A4R, A3R)


def main_menu(font):
    """
     This is main menu of the game
     font is parameter of function
     is also has code which allows
     the user use mouse
    """
    global pos, logo
    pos = [0, 0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

        background = pygame.image.load("space.jpg")

        title = font.render("GALAXY CIVIL WAR", True, YELLOW)
        title_box = title.get_rect()
        title_box.midtop = arena.midtop

        logo = pygame.image.load("dest1.png")
        logo_rect = logo.get_rect()
        logo_rect.center = (int(FRAME[0] / 2), int(FRAME[1] / 2) - A2U * STEP)

        multi4 = font.render("PLAY", True, YELLOW)
        multi_box4 = multi4.get_rect()
        multi_box4.midbottom = arena.midbottom

        multi2 = font.render("HOW TO PLAY", True, YELLOW)
        multi_box2 = multi2.get_rect()
        multi_box2.midleft = (int(FRAME[0] / 3), int(5 * arena.height / 7))

        window.blit(background, [0, 0])
        window.blit(title, title_box)
        window.blit(multi4, multi_box4)
        window.blit(logo, logo_rect)
        window.blit(multi2, multi_box2)
        pygame.display.flip()

        if multi_box4.collidepoint(pos):
            gameloop()
        if multi_box2.collidepoint(pos):
            menu_how_to_play(font)


def menu_how_to_play(font):
    """
    Module contains how to play menu of the game
    font is the parameter of this function
    Contains: background, all texts
    """
    global title, title_box, multi, multi_box
    global pos
    pos = [0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
        background = pygame.image.load("space.jpg")

        title = font.render("CONTROLS: ARROWS AND SPACE", True, YELLOW)
        title_box = title.get_rect()
        title_box.midtop = arena.midtop

        multi = font.render("   YOUR OBJECTIVE IS TO DESTROY AS MANY",
                            True, YELLOW)
        multi_box = multi.get_rect()
        multi_box.midleft = (0, int(3 * arena.height / 7))

        multi1 = font.render("   X-WING AS YOU CAN AND HELP THE ",
                             True, YELLOW)
        multi_box1 = multi1.get_rect()
        multi_box1.midleft = (0, int(4 * arena.height / 7))

        multi2 = font.render("   EMPIRE WIN THE GALAXY CIVIL WAR", True,
                             YELLOW)
        multi_box2 = multi2.get_rect()
        multi_box2.midleft = (0, int(5 * arena.height / 7))

        multi4 = font.render("BACK TO MAIN MENU", True, YELLOW)
        multi_box4 = multi4.get_rect()
        multi_box4.midbottom = arena.midbottom

        window.blit(background, [0, 0])
        window.blit(title, title_box)
        window.blit(multi, multi_box)
        window.blit(multi1, multi_box1)
        window.blit(multi2, multi_box2)

        window.blit(multi4, multi_box4)
        pygame.display.flip()

        if multi_box4.collidepoint(pos):
            main_menu(font)


def control_keys():
    """
    This functions is providing
    control keys to our tie fighter
    """
    global bullet_rect
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_rect.center == ship_rect.midtop:
                    pygame.mixer.Channel(1).play(shot)
                bullet_rect = bullet_rect.move(0, 2 * -STEP)
                pygame.display.flip()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship_rect.move_ip(-STEP, 0)
        bullet_rect.move_ip(-STEP, 0)
        if bullet_rect.center != ship_rect.midtop:
            bullet_rect.move_ip(STEP, 0)
    if key[pygame.K_UP]:
        ship_rect.move_ip(0, -STEP)
        bullet_rect.move_ip(0, -STEP)
        if bullet_rect.center != ship_rect.midtop:
            bullet_rect.move_ip(0, STEP)
    if key[pygame.K_RIGHT]:
        ship_rect.move_ip(STEP, 0)
        bullet_rect.move_ip(STEP, 0)
        if bullet_rect.center != ship_rect.midtop:
            bullet_rect.move_ip(-STEP, 0)
    if key[pygame.K_DOWN]:
        ship_rect.move_ip(0, STEP)
        bullet_rect.move_ip(0, STEP)
        if bullet_rect.center != ship_rect.midtop:
            bullet_rect.move_ip(0, -STEP)


def collision():
    """
    Module deicated to prevent flying over the
    arena
    """
    if ship_rect.y < SHIP_Y:
        ship_rect.y = SHIP_Y1
        bullet_rect.center = ship_rect.midtop
    if ship_rect.left <= arena.left:
        ship_rect.left = arena.left + STEP
        bullet_rect.center = ship_rect.midtop
    if ship_rect.right >= arena.right:
        ship_rect.right = arena.right - STEP
        bullet_rect.center = ship_rect.midtop
    if ship_rect.bottom >= arena.bottom:
        ship_rect.bottom = arena.bottom - STEP
        bullet_rect.center = ship_rect.midtop
    if ship_rect.top <= arena.top:
        ship_rect.top = arena.top + STEP
        bullet_rect.center = ship_rect.midtop


def alien1_move():
    """
    Function dedicated to 1st X-Wing and
    here we have all behaviour of it
    """
    global alien_vec, aliens, alien_rect1, score, alien1_hit
    alien_rect1 = alien_rect1.move(alien_vec)

    if alien_rect1.colliderect(bullet_rect):
        alien_rect1.x = random.randint(A2R, A1R)
        while alien_rect1.x % 5 == 0:
            alien_rect1.x = random.randint(A2R, A1L)

        alien_rect1.y = random.randint(A2U, A2D)
        if alien1_hit < VEC1NUM:
            alien_vec[0] = 5
        elif alien1_hit > VEC2NUM:
            alien_vec[0] = A1U
        else:
            alien_vec[0] = A2U
        alien1_hit += 1
        bullet_rect.center = ship_rect.midtop
        score += 1
    if 0 <= alien_rect1.left <= arena.right:
        if alien_rect1.left <= arena.left:
            alien_rect1.left = arena.left
            alien_rect1.y += ALIEN_STEP_DOWN
            alien_vec[0] = -alien_vec[0]
        if alien_rect1.right >= arena.right:
            alien_rect1.right = arena.right
            alien_rect1.y += ALIEN_STEP_DOWN
            alien_vec[0] = -alien_vec[0]


def alien2_move():
    """
    Function dedicated to 2nd X-Wing and
    here we have all behaviour of it
    """
    global alien2_vec, aliens, alien_rect2, score, alien2_hit
    alien_rect2 = alien_rect2.move(alien2_vec)

    if alien_rect2.colliderect(bullet_rect):
        alien_rect2.x = random.randint(A2R, A1R)
        while alien_rect2.x % 5 == 0:
            alien_rect2.x = random.randint(A2R, A1L)

        alien_rect2.y = random.randint(A2U, A2D)
        if alien2_hit < VEC1NUM:
            alien2_vec[0] = 5
        elif alien2_hit > VEC2NUM:
            alien2_vec[0] = A1U
        else:
            alien2_vec[0] = A2U
        alien2_hit += 1
        bullet_rect.center = ship_rect.midtop
        score += 1
    if 0 <= alien_rect2.left <= arena.right:
        if alien_rect2.left <= arena.left:
            alien_rect2.left = arena.left
            alien_rect2.y += ALIEN_STEP_DOWN
            alien2_vec[0] = -alien2_vec[0]
        if alien_rect2.right >= arena.right:
            alien_rect2.right = arena.right
            alien_rect2.y += ALIEN_STEP_DOWN
            alien2_vec[0] = -alien2_vec[0]


def alien4_move():
    """
    Function dedicated to 4th X-Wing and
    here we have all behaviour of it
    """
    global alien_vec, aliens, alien_rect4, score, alien4_hit
    alien_rect4 = alien_rect4.move(alien4_vec)

    if alien_rect4.colliderect(bullet_rect):
        alien_rect4.x = random.randint(A2R, A1R)
        while alien_rect4.x % 5 == 0:
            alien_rect4.x = random.randint(A2R, A1L)

        alien_rect4.y = random.randint(A2U, A2D)
        if alien4_hit < VEC1NUM:
            alien4_vec[0] = 5
        elif alien4_hit > VEC2NUM:
            alien4_vec[0] = A1U
        else:
            alien4_vec[0] = A2U
        alien4_hit += 1
        bullet_rect.center = ship_rect.midtop
        score += 1
    if 0 <= alien_rect4.left <= arena.right:
        if alien_rect4.left <= arena.left:
            alien_rect4.left = arena.left
            alien_rect4.y += ALIEN_STEP_DOWN
            alien4_vec[0] = -alien4_vec[0]
        if alien_rect4.right >= arena.right:
            alien_rect4.right = arena.right
            alien_rect4.y += ALIEN_STEP_DOWN
            alien4_vec[0] = -alien4_vec[0]


def alien3_move():
    """
    Function dedicated to 3rd X-Wing and
    here we have all behaviour of it
    """
    global alien_vec, aliens, alien_rect3, score, alien3_hit
    alien_rect3 = alien_rect3.move(alien3_vec)

    if alien_rect3.colliderect(bullet_rect):
        alien_rect3.x = random.randint(A2R, A1R)
        while alien_rect3.x % 5 == 0:
            alien_rect3.x = random.randint(A2R, A1L)

        alien_rect3.y = random.randint(A2U, A2D)
        if alien3_hit < VEC1NUM:
            alien3_vec[0] = 5
        elif alien3_hit > VEC2NUM:
            alien3_vec[0] = A1U
        else:
            alien3_vec[0] = A2U
        alien3_hit += 1
        bullet_rect.center = ship_rect.midtop
        score += 1
    if 0 <= alien_rect3.left <= arena.right:
        if alien_rect3.left <= arena.left:
            alien_rect3.left = arena.left
            alien_rect3.y += ALIEN_STEP_DOWN
            alien3_vec[0] = -alien3_vec[0]
        if alien_rect3.right >= arena.right:
            alien_rect3.right = arena.right
            alien_rect3.y += ALIEN_STEP_DOWN
            alien3_vec[0] = -alien3_vec[0]


def alien5_move():
    """
    Function dedicated to 5th X-Wing and
    here we have all behaviour of it
    """
    global alien_vec, aliens, alien_rect5, score, alien5_hit
    alien_rect5 = alien_rect5.move(alien5_vec)

    if alien_rect5.colliderect(bullet_rect):
        alien_rect5.x = random.randint(A2R, A1R)
        while alien_rect5.x % 5 == 0:
            alien_rect5.x = random.randint(A2R, A1L)

        alien_rect5.y = random.randint(A2U, A2D)
        if alien5_hit < VEC1NUM:
            alien5_vec[0] = 5
        elif alien5_hit > VEC2NUM:
            alien5_vec[0] = A1U
        else:
            alien5_vec[0] = A2U
        alien5_hit += 1
        bullet_rect.center = ship_rect.midtop
        score += 1
    if 0 <= alien_rect5.left <= arena.right:
        if alien_rect5.left <= arena.left:
            alien_rect5.left = arena.left
            alien_rect5.y += ALIEN_STEP_DOWN
            alien5_vec[0] = -alien5_vec[0]
        if alien_rect5.right >= arena.right:
            alien_rect5.right = arena.right
            alien_rect5.y += ALIEN_STEP_DOWN
            alien5_vec[0] = -alien5_vec[0]


def alien6_move():
    """
    Function dedicated to 6th X-Wing and
    here we have all behaviour of it
    """
    global alien_vec, aliens, alien_rect6, score, alien6_hit
    alien_rect6 = alien_rect6.move(alien6_vec)

    if alien_rect6.colliderect(bullet_rect):
        alien_rect6.x = random.randint(A2R, A1R)
        while alien_rect6.x % 5 == 0:
            alien_rect6.x = random.randint(A2R, A1L)

        alien_rect6.y = random.randint(A2U, A2D)
        if alien6_hit < VEC1NUM:
            alien6_vec[0] = 5
        elif alien6_hit > VEC2NUM:
            alien6_vec[0] = A1U
        else:
            alien6_vec[0] = A2U
        alien6_hit += 1
        bullet_rect.center = ship_rect.midtop
        score += 1
    if 0 <= alien_rect6.left <= arena.right:
        if alien_rect6.left <= arena.left:
            alien_rect6.left = arena.left
            alien_rect6.y += ALIEN_STEP_DOWN
            alien6_vec[0] = -alien6_vec[0]
        if alien_rect6.right >= arena.right:
            alien_rect6.right = arena.right
            alien_rect6.y += ALIEN_STEP_DOWN
            alien6_vec[0] = -alien6_vec[0]


def failure(font):
    """
    This is failure menu
    We can here choose 2 options:
    to play again and go back to main
    font is parameter
    """
    global pos, score, alien1_hit, alien2_hit, alien3_hit, alien4_hit
    global alien5_hit, alien6_hit, alien_vec, alien2_vec, ship
    global alien3_vec, alien4_vec, alien5_vec, alien6_vec
    pos = [0, 0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

        background = pygame.image.load("space.jpg")

        title = font.render("YOU HAVE BEEN DEFEATED", True, RED)
        title_box = title.get_rect()
        title_box.center = arena.center

        multi4 = font.render("MAIN MENU", True, YELLOW)
        multi_box4 = multi4.get_rect()
        multi_box4.midbottom = arena.midbottom

        multi2 = font.render("PLAY AGAIN", True, YELLOW)
        multi_box2 = multi2.get_rect()
        multi_box2.center = (int(FRAME[0] / 2), int(5 * arena.height / 7))

        window.blit(background, [0, 0])
        window.blit(title, title_box)
        window.blit(multi4, multi_box4)
        window.blit(multi2, multi_box2)
        pygame.display.flip()

        aliens_location()
        ship = pygame.image.load("tie.png")
        score = 0
        alien1_hit = 0
        alien2_hit = 0
        alien3_hit = 0
        alien4_hit = 0
        alien5_hit = 0
        alien6_hit = 0

        alien_vec = [2, 0]
        alien2_vec = [2, 0]
        alien3_vec = [2, 0]
        alien4_vec = [2, 0]
        alien5_vec = [2, 0]
        alien6_vec = [2, 0]

        if multi_box2.collidepoint(pos):
            gameloop()
        if multi_box4.collidepoint(pos):
            main_menu(font)


def when_failure():
    """
    Module chcecking when game is over
    """
    global bullet_rect, ship_rect
    if bullet_rect.center == ship_rect.midtop and \
            ship_rect.colliderect(alien_rect1):
        pygame.time.wait(TIME_S)
        failure(font)
    if bullet_rect.center == ship_rect.midtop and \
            ship_rect.colliderect(alien_rect2):
        pygame.time.wait(TIME_S)
        failure(font)
    if bullet_rect.center == ship_rect.midtop and \
            ship_rect.colliderect(alien_rect3):
        pygame.time.wait(TIME_S)
        failure(font)
    if bullet_rect.center == ship_rect.midtop and \
            ship_rect.colliderect(alien_rect4):
        pygame.time.wait(TIME_S)
        failure(font)
    if bullet_rect.center == ship_rect.midtop and \
            ship_rect.colliderect(alien_rect5):
        pygame.time.wait(TIME_S)
        failure(font)
    if bullet_rect.center == ship_rect.midtop and \
            ship_rect.colliderect(alien_rect6):
        pygame.time.wait(TIME_S)
        failure(font)


def all_aliens_move():
    """
    Function with all alien functions
    """
    alien1_move()
    alien2_move()
    alien3_move()
    alien4_move()
    alien5_move()
    alien6_move()


def show_score(font):
    """
    Module showing score
    """
    global score, sco, sco_box

    sco = font.render(f"SCORE: {str(score)}", True, YELLOW)
    sco_box = sco.get_rect()

    sco_box.x = SCOREX
    sco_box.y = SCOREY
    window.blit(sco, sco_box)


def gameloop():
    """
    Main game loop
    This is whole game
    with easter eggs
    and whole behaviours of actors
    player
    """
    global bullet_rect, ship_rect, ship, bullet
    while True:
        if score >= EASTEREGGNUM:
            ship = pygame.image.load("cat.png")
            if bullet_rect.bottom <= arena.top:
                ship = pygame.transform.flip(ship, True, False)
        pygame.mixer.Sound.play(fly)
        if bullet_rect.center != ship_rect.midtop:
            bullet_rect = bullet_rect.move(0, int(2.5 * -STEP))
            if bullet_rect.bottom <= arena.top:
                bullet_rect.center = ship_rect.midtop
                ship = pygame.transform.flip(ship, True, False)
        bullet = pygame.transform.flip(bullet, True, False)
        when_failure()
        control_keys()

        all_aliens_move()
        collision()

        window.blit(game_background, [0, 0])
        show_score(font)
        window.blit(bullet, bullet_rect)
        window.blit(ship, ship_rect)
        window.blit(alien1, alien_rect1)
        window.blit(alien2, alien_rect2)
        window.blit(alien3, alien_rect3)
        window.blit(alien4, alien_rect4)
        window.blit(alien5, alien_rect5)
        window.blit(alien6, alien_rect6)

        fps.tick(80)
        pygame.display.flip()


# GLOBAL SCOPE PROTECTION

if __name__ == "__main__":
    main_menu(font)
