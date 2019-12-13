import pygame
import sys
import random

"""
                            THE PING PONG GAME

The program is just a simple game called "Ping - Pong".

*** SINGLEPLAYER ***

CONTROL SETTINGS:

    A - MOVE LEFT
    D- MOVE RIGHT

RULES:

Player has to bounce the ball with the paddle.
When ball touches the right wall the point will be obtained


*** MULTIPLAYER ***

CONTROL SETTINGS:

    PLAYER 1:                 PLAYER 2:

    W - move up               Up arrow - move up
    S - move down             Down arrow - move down


    To exit press "ESC" button

Rules:

Players have to bounce the object and try to score a goal
Goal is scored when the object touch the right or left side of window.

Written by: Piotr Cajdler

"""


black = pygame.color.Color("black")
white = pygame.color.Color("white")  # color definitions
red = pygame.color.Color("red")
yellow = pygame.color.Color("yellow")
turquoise = (64, 224, 208)
pygame.init()

frame = (720, 480)
scr = pygame.display.set_mode(frame)
window = scr.get_rect()
pygame.display.set_caption("GAME")  # main window

line_start = [int(frame[0]/2), int(frame[1])]
line_end = [int(frame[0]/2), 0]
line_thick = 3

single_paddle = pygame.Rect(0, 0, 20, 70)
paddle1 = pygame.Rect(0, 0, 10, 70)
paddle2 = pygame.Rect(0, 0, 10, 70)  # dimensions of the rectangles
ball = pygame.Rect(0, 0, 20, 20)
step = 5

ball_vec = [-6, 6]

single_paddle.midleft = window.midleft
paddle1.midleft = window.midleft
paddle2.midright = window.midright  # layout
ball.center = window.center

score = 0
home_goal = 0
away_goal = 0

pygame.key.set_repeat(70, 70)
fps = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 42)  # font




def menu(font):
    """
    Module contains main menu of the game
    font is the parameter of this function
    """
    global title, title_box, single, single_box, multi, multi_box
    scr.fill(black)

    title = font.render("PING PONG GAME", True, turquoise)
    title_box = title.get_rect()
    title_box.midtop = window.midtop

    single = font.render("TYPE S FOR SINGLE", True, turquoise)
    single_box = single.get_rect()
    single_box.midbottom = window.midbottom

    multi = font.render("TYPE M FOR MULTI", True, turquoise)
    multi_box = multi.get_rect()
    multi_box.center = window.center

    scr.blit(title, title_box)
    scr.blit(single, single_box)
    scr.blit(multi, multi_box)


"""
***SINGLEPLAYER FUNCTIONS***
"""


def basic():
    """
    Module contains basic parameters of paddle motion and keybinds
    """
    global single_paddle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        single_paddle.move_ip(0, -step)
    if key[pygame.K_DOWN]:
        single_paddle.move_ip(0, step)





def collisons():

    """
    That module contains the behaviour when paddle collide with
    ball and the frame
    """
    global ball, single_paddle, ball_vec
    if single_paddle.top <= window.top:
        single_paddle.top = window.top
    if single_paddle.bottom >= window.bottom:
        single_paddle.bottom = window.bottom
    if ball.colliderect(single_paddle):
        ball_vec[0] = -ball_vec[0]


def singlescore():
    """
    Module showing score
    """
    global scoreboard, scoreboard_box
    scoreboard = font.render(f"{score}", True, yellow)
    scoreboard_box = scoreboard.get_rect()
    scoreboard_box = (int(frame[0] / 2), int(frame[1] / 8))


def points():
    """
    Module counting score and changing the difficulty level
    """
    global ball, score
    if ball.right >= window.right:
        score += 1
        ball_vec[0] = -ball_vec[0]
        if score % 3 == 0 and score != 0:
            ball_vec[0] -= 1
            if score > 39:
                ball_vec[0] += 1


def end():
    """
    Module describe behaviour when game is over
    """
    global ball_vec, ball
    ball_vec = [0, 0]
    ball = pygame.Rect(int(-frame[0] / 2), int(-frame[1]), 0, 0)

    lose = font.render("YOU LOSE", True, red)
    lose_box = lose.get_rect()
    lose_box.center = window.center
    scr.blit(lose, lose_box)

    esc = font.render("PRESS ESC TO EXIT", True, white)
    esc_box = esc.get_rect()
    esc_box.midbottom = window.midbottom
    scr.blit(esc, esc_box)


"""
            ***MULTIPLAYER FUNCTIONS***
"""


def squares_move_or_exit():
    """

    The main task of this module is insert control setting in the game
    and the escape button to exit the game

    """

    global paddle1, paddle2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        paddle1.move_ip(0, step)
    if key[pygame.K_w]:
        paddle1.move_ip(0, -step)
    if key[pygame.K_UP]:
        paddle2.move_ip(0, -step)
    if key[pygame.K_DOWN]:
        paddle2.move_ip(0, step)


def ball_move(ball, ball_vec):
    """
    This module contain code to move the ball about ball vector 'ball_vec'
    and checking if ball collide with main frame
    """
    if ball.top >= window.top:
        ball_vec[1] = -ball_vec[1]
    if ball.bottom <= window.bottom:
        ball_vec[1] = -ball_vec[1]


def square_collisions(ball, paddle1, paddle2):

    """
    This module detects collision between ball and paddles
    The collision changes  moving vector of ball
    """

    if ball.colliderect(paddle1):
        ball_vec[0] = -ball_vec[0]
    if ball.colliderect(paddle2):
        ball_vec[0] = -ball_vec[0]
    if paddle1.top <= window.top:
        paddle1.top = window.top
    if paddle1.bottom >= window.bottom:
        paddle1.bottom = window.bottom
    if paddle2.top <= window.top:
        paddle2.top = window.top
    if paddle2.bottom >= window.bottom:
        paddle2.bottom = window.bottom


def result(ball):
    """
    This module is dedicated to showing the result of the match
    when the ball touch te right or left side of the screen box
    the goal is adding to one side
    """

    global home_goal, away_goal

    if ball.left <= window.left:
        away_goal += 1
        ball.center = window.center
        ball_vec[0] = random.choice([-ball_vec[0], ball_vec[0]])
        ball_vec[1] = random.choice([-ball_vec[1], ball_vec[1]])
        pygame.time.delay(200)
    if ball.right >= window.right:
        ball.center = window.center
        home_goal += 1
        ball_vec[0] = random.choice([-ball_vec[0], ball_vec[0]])
        ball_vec[1] = random.choice([-ball_vec[1], ball_vec[1]])
        pygame.time.delay(200)


def draw_l():

    """
    Module drawing the ball and paddles  (with line)
    """

    pygame.draw.rect(scr, white, paddle1)
    pygame.draw.rect(scr, white, paddle2)
    pygame.draw.rect(scr, white, ball)
    pygame.draw.line(scr, white, line_start, line_end, line_thick)


def draw():
    """
    Module drawing the ball and paddles
    """

    pygame.draw.rect(scr, white, paddle1)
    pygame.draw.rect(scr, white, paddle2)
    pygame.draw.rect(scr, white, ball)


def multifunctions():
    """
    Main funtion for multiplayer containing important fuctions of game
    """

    squares_move_or_exit()
    ball_move(ball, ball_vec)
    square_collisions(ball, paddle1, paddle2)
    result(ball)


def scoring():
    """
    Module in which the score boxes are defined and
    what kind of information should be displayed
    """

    global msg_away, msg_awaybox, msg_home, msg_homebox
    msg_away = font.render(f"{home_goal}", True, turquoise)
    msg_awaybox = msg_away.get_rect()
    msg_awaybox = [int(frame[0] / 4), int(frame[1] / 8)]

    msg_home = font.render(f"{away_goal}", True, turquoise)
    msg_homebox = msg_home.get_rect()
    msg_homebox = [int(frame[0] - frame[0] / 4), int(frame[1] / 8)]


def win1():
    """
    Modules contain behavior of application when  player will win
    """
    global ball_vec, ball
    winp1 = font.render("PLAYER 1 WINS", True, red)
    winp1_box = winp1.get_rect()
    winp1_box.center = window.center
    scr.blit(winp1, winp1_box)
    ball_vec = [0, 0]
    ball = pygame.Rect(int(frame[0] / 2), int(frame[1]), 0, 0)

    esc = font.render("PRESS ESC TO EXIT", True, white)
    esc_box = esc.get_rect()
    esc_box.midbottom = window.midbottom
    scr.blit(esc, esc_box)
    scr.blit(msg_home, msg_homebox)
    scr.blit(msg_away, msg_awaybox)


def win2():
    """
    Modules contain behavior of application when  player will win
    """
    global ball_vec, ball
    winp2 = font.render("PLAYER 2 WINS", True, red)
    winp2_box = winp2.get_rect()
    winp2_box.center = window.center
    scr.blit(winp2, winp2_box)

    ball_vec = [0, 0]
    ball = pygame.Rect(int(frame[0] / 2), frame[1], 0, 0)

    esc = font.render("PRESS ESC TO EXIT", True, white)
    esc_box = esc.get_rect()
    esc_box.midbottom = window.midbottom
    scr.blit(esc, esc_box)
    scr.blit(msg_home, msg_homebox)
    scr.blit(msg_away, msg_awaybox)


def endgoal():
    """
    Module includes functions after reaching 5 goals
    """
    if home_goal == 5:
        scr.fill(black)
        win1()
        draw()
    if away_goal == 5:
        scr.fill(black)
        win2()
        draw()


def game():

    """
    Main function of the game, it includes every functions which are used to play
    """
    global ball
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_m:
                while True:
                    ball = ball.move(ball_vec)
                    multifunctions()
                    scr.fill(black)
                    scoring()
                    scr.blit(msg_home, msg_homebox)
                    scr.blit(msg_away, msg_awaybox)
                    draw_l()
                    endgoal()
                    pygame.display.flip()
                    fps.tick(60)
            if event.key == pygame.K_s:
                while True:
                    ball = ball.move(ball_vec)
                    basic()
                    collisons()
                    points()
                    ball_move(ball, ball_vec)
                    singlescore()
                    scr.fill(black)
                    scr.blit(scoreboard, scoreboard_box)

                    if ball.left <= window.left:
                        end()
                    pygame.draw.rect(scr, white, single_paddle)
                    pygame.draw.rect(scr, white, ball)
                    pygame.display.flip()
                    fps.tick(60)
    pygame.display.flip()


"""
Main loops of the game
"""

if __name__ == "__main__":
    while True:
        menu(font)
        game()
