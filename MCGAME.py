"""

           **** THIS IS MISSIONARIES AND CANNIBALS GAME ****

Your task is to transport 3 cannibals and 3 missionaries
through the one side of river to another.
You should avoid leaving 2 or 3 cannibals with
less number of missionaries,because it means defeat.

CONTROL: MOUSE
SPACE TO RAFT



Written by: Piotr Cajdler
"""

import sys
import pygame

WHITE = pygame.color.Color("white")
pygame.init()		# constants
FR = (1080, 720)
window = pygame.display.set_mode(FR)
arena = window.get_rect()
pygame.display.set_caption("GAME")  	# main window
step = 5
fpsClock = pygame.time.Clock()
action = "listen"
cann1 = {"file": "cann.png", "class": "c"}
cann2 = {"file": "cann.png", "class": "c"}	  # actors and boat
cann3 = {"file": "cann.png", "class": "c"}
mis1 = {"file": "cabb.png", "class": "m"}
mis2 = {"file": "cabb.png", "class": "m"}
mis3 = {"file": "cabb.png", "class": "m"}
boat = pygame.image.load("boat.png")
boatbox = boat.get_rect()
boatbox.center = (int(FR[0] / 3.2), int(FR[1] / 2))

actors = [cann1, cann2, cann3, mis1, mis2, mis3]

for i, actor in enumerate(actors):
    actor["surf"] = pygame.image.load(actor["file"])
    actor["rect"] = actor["surf"].get_rect()
    actor["rect"].midleft = (0, int((i + 1) * arena.height / 7))  # actor locate

bg = pygame.image.load("river.png")
passengers = []
boat_key = []
font = pygame.font.Font('freesansbold.ttf', 42)


def menu(font):
    """
    Module contains main menu of the game
    font is the parameter of this function
    Contains: background, all texts
    """
    global title, title_box, multi, multi_box

    background = pygame.image.load("background.jpg")

    title = font.render("MISSIONARIES AND CANNIBALS", True, WHITE)
    title_box = title.get_rect()
    title_box.midtop = arena.midtop

    multi = font.render("In this game you have to transport all characters",
                        True, WHITE)
    multi_box = multi.get_rect()
    multi_box.midleft = (0, int(2 * arena.height / 7))

    multi1 = font.render("to the right side of the river, but",
                         True, WHITE)
    multi_box1 = multi1.get_rect()
    multi_box1.midleft = (0, int(3 * arena.height / 7))

    multi2 = font.render("you should avoid leaving bigger number", True, WHITE)
    multi_box2 = multi2.get_rect()
    multi_box2.midleft = (0, int(4 * arena.height / 7))

    multi3 = font.render("of cannibals with missionaries. GOOD LUCK!",
                         True, WHITE)
    multi_box3 = multi3.get_rect()
    multi_box3.midleft = (0, int((5 * arena.height / 7)))

    multi4 = font.render("PRESS SPACE TO PLAY!", True, WHITE)
    multi_box4 = multi4.get_rect()
    multi_box4.midbottom = arena.midbottom

    window.blit(background, [0, 0])
    window.blit(title, title_box)
    window.blit(multi, multi_box)
    window.blit(multi1, multi_box1)
    window.blit(multi2, multi_box2)
    window.blit(multi3, multi_box3)
    window.blit(multi4, multi_box4)

    pygame.display.flip()


def gameloop():
    """
    This is main function
    of the game, it contains
    all behaviours and simple
    whole game
    """
    global action, gamestate, gamegraph
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    while True:
                        if action == "listen":
                            getkey()

                        if action == "failure":
                            failure()
                            sys.exit()
                        if action == "success":
                            success()
                            sys.exit()

                        window.blit(bg, [0, 0])
                        for actor in actors:
                            window.blit(actor["surf"], actor["rect"])
                        window.blit(boat, boatbox)
                        pygame.display.flip()


def listtostring(list):
    """
    Function which makes string
    from the list, it is used
    to specify the gamestate
    """
    global string
    string = ""
    for element in list:
        string += element
    return string


def getkey():
    """
    This giant module contains
    all behaviour of characters
    all the slots and places where
    the characters should be before
    the replacement. Module contains also
    mechanism to go and leave the boat
    and whole control keys
    """
    global action, pos, gamestate, passengers

    pos = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                sys.exit()
            if event.key == pygame.K_SPACE:
                if len(passengers) > 0:
                    action = "listen"
                    ferry()
                    key = listtostring(sorted(boat_key))
                    gamestate = gamegraph[gamestate][key]
                    print(str(gamestate))
                    if gamegraph[gamestate] == "failure":
                        action = "failure"
                    elif gamegraph[gamestate] == "success":
                        action = "success"
                    else:
                        action = "listen"
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for actor in actors:

                if actor["rect"].collidepoint(pos) and actor not in passengers:

                    if len(passengers) < 2:
                        for i in range(7):
                            if actor["rect"].midleft == \
                                    (0,
                                     int((i + 1) * FR[1] / 7)) \
                                    and boatbox.center == (int(FR[0] / 3.2),
                                                           int(FR[1] / 2)):
                                actor["rect"].midleft = (int(FR[0] / 3.2),
                                                         int(FR[1] / 2.5))
                                passengers.append(actor)
                                boat_key.append(actor["class"])
                            elif actor["rect"].midleft == \
                                    (int(arena.width * 0.9),
                                     int((i + 1) * FR[1] / 7)) \
                                    and boatbox.center != \
                                    (int(FR[0] / 3.2),
                                     int(FR[1] / 2)):
                                actor["rect"].midleft = (int(FR[0] * 0.7),
                                                         int(FR[1] / 2.5))
                                passengers.append(actor)
                                boat_key.append(actor["class"])

                if actor["rect"].collidepoint(pos) and actor in passengers:
                    if boatbox.center == \
                            (int(FR[0] / 3.2),
                             int(FR[1] / 2)):
                        if cann1["rect"].midleft == \
                                (int(FR[0] / 3.2), int(FR[1] / 2.5)) \
                                or cann1["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or cann1["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            cann1["rect"].midleft = (0,
                                                     int(FR[1] / 7))

                        elif cann2["rect"].midleft == \
                                (int(FR[0] / 3.2),
                                 int(FR[1] / 2.5)) \
                                or cann2["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or cann2["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            cann2["rect"].midleft = (0,
                                                     int(2 * FR[1] / 7))

                        elif cann3["rect"].midleft == \
                                (int(FR[0] / 3.2),
                                 int(FR[1] / 2.5)) \
                                or cann3["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or cann3["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            cann3["rect"].midleft = (0,
                                                     int(3 * FR[1] / 7))

                        elif mis1["rect"].midleft == \
                                (int(FR[0] / 3.2),
                                 int(FR[1] / 2.5)) \
                                or mis1["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or mis1["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            mis1["rect"].midleft = (0,
                                                    int(4 * FR[1] / 7))

                        elif mis2["rect"].midleft == \
                                (int(FR[0] / 3.2),
                                 int(FR[1] / 2.5)) \
                                or mis2["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or mis2["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            mis2["rect"].midleft = (0, int(5 * FR[1] / 7))
                        elif mis3["rect"].midleft == \
                                (int(FR[0] / 3.2),
                                 int(FR[1] / 2.5)) \
                                or mis3["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or mis3["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            mis3["rect"].midleft = (0,
                                                    int(6 * FR[1] / 7))

                        passengers.remove(actor)
                        boat_key.remove(actor["class"])

                    if boatbox.center != \
                            (int(FR[0] / 3.2),
                             int(FR[1] / 2)):

                        if cann1["rect"].midleft == \
                                (int(FR[0] * 0.7),
                                 int(FR[1] / 2.5)) \
                                or cann1["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or cann1["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            cann1["rect"].midleft = (int(arena.width * 0.9),
                                                     int(1 * FR[1] / 7))

                        elif cann2["rect"].midleft == (int(FR[0] * 0.7),
                                                       int(FR[1] / 2.5)) \
                                or cann2["rect"].midleft == \
                                ((int(FR[0] / 3.2) + ((400 // step) * step)),
                                 int(FR[1] / 2.5)) \
                                or cann2["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            cann2["rect"].midleft = (int(arena.width * 0.9),
                                                     int(2 * FR[1] / 7))

                        elif cann3["rect"].midleft == \
                                (int(FR[0] * 0.7),
                                 int(FR[1] / 2.5)) \
                                or cann3["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or cann3["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            cann3["rect"].midleft = (int(arena.width * 0.9),
                                                     int(3 * FR[1] / 7))

                        elif mis1["rect"].midleft == (int(FR[0] * 0.7),
                                                      int(FR[1] / 2.5)) \
                                or mis1["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or mis1["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            mis1["rect"].midleft = (int(arena.width * 0.9),
                                                    int(4 * FR[1] / 7))

                        elif mis2["rect"].midleft == \
                                (int(FR[0] * 0.7),
                                 int(FR[1] / 2.5)) \
                                or mis2["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or mis1["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            mis2["rect"].midleft = \
                                (int(arena.width * 0.9),
                                 int(5 * FR[1] / 7))

                        elif mis3["rect"].midleft == \
                                (int(FR[0] * 0.7),
                                 int(FR[1] / 2.5)) \
                                or mis3["rect"].midleft == \
                                ((int(FR[0] / 3.2) + (400 // step) * step),
                                 int(FR[1] / 2.5)) \
                                or mis1["rect"].midleft == \
                                ((int(FR[0] * 0.7) - (400 // step) * step),
                                 int(FR[1] / 2.5)):
                            mis3["rect"].midleft = \
                                (int(arena.width * 0.9),
                                 int(6 * FR[1] / 7))
                        passengers.remove(actor)
                        boat_key.remove(actor["class"])


def ferry():
    """
    Function which allows
    passengers to go across the river
    and go back to the left side
    """
    global action, gamestate, boat, boatbox, done
    if boatbox.center == (int(FR[0] / 3.2), int(FR[1] / 2)):
        if len(passengers) >= 1:
            for i in range(400 // step):
                boatbox = boatbox.move(step, 0)
                for actor in passengers:
                    actor["rect"] = actor["rect"].move(step, 0)
                window.blit(bg, [0, 0])
                for actor in actors:
                    window.blit(actor["surf"], actor["rect"])
                window.blit(boat, boatbox)
                pygame.display.flip()
                fpsClock.tick(1000)
        boat = pygame.transform.flip(boat, True, False)

    elif boatbox.center != (int(FR[0] / 3.2), int(FR[1] / 2)):
        if len(passengers) >= 1:
            for i in range(400 // step):
                boatbox = boatbox.move(-step, 0)
                for actor in passengers:
                    actor["rect"] = actor["rect"].move(-step, 0)
                window.blit(bg, [0, 0])
                for actor in actors:
                    window.blit(actor["surf"], actor["rect"])
                window.blit(boat, boatbox)
                pygame.display.flip()
                fpsClock.tick(1000)
        boat = pygame.transform.flip(boat, True, False)


def failure():
    """
    Module contains failure goodbye screen
    """
    myfont = pygame.font.Font('freesansbold.ttf', 48)
    msg = myfont.render("Failure", True, (255, 0, 0))
    msg_box = msg.get_rect()
    msg_box.center = arena.center
    window.blit(msg, msg_box)
    pygame.display.flip()
    pygame.time.wait(1000)


def success():
    """
    Module contains success goodbye screen
    """
    myfont = pygame.font.Font('freesansbold.ttf', 48)
    msg = myfont.render("Success", True, (0, 0, 255))
    msg_box = msg.get_rect()
    msg_box.center = arena.center
    window.blit(msg, msg_box)
    pygame.display.flip()
    pygame.time.wait(1000)


# gamegraph
gamegraph = {
    "cccmmmr-": {"m": "cccmm-mr", "mm": "cccm-mmr",
                 "c": "ccmmm-cr",
                 "cc": "cmmm-ccr", "cm": "ccmm-cmr"},
    "ccmmm-cr": {"c": "cccmmmr-"},
    "cmmm-ccr": {"c": "ccmmmr-c",
                 "cc": "cccmmmr-"},
    "ccmm-cmr": {"c": "cccmmr-m",
                 "m": "ccmmmr-c", "cm": "cccmmmr-"},
    "ccmmmr-c": {"m": "ccmm-cmr",
                 "mm": "ccm-cmmr",
                 "c": "cmmm-ccr",
                 "cc": "mmm-cccr", "cm": "cmm-ccmr"},
    "mmm-cccr": {"c": "cmmmr-cc", "cc": "ccmmmr-c"},
    "cmmmr-cc": {"m": "cmm-ccmr",
                 "mm": "cm-ccmmr", "c": "mmm-cccr", "cm": "mm-cccmr"},
    "cm-ccmmr": {"m": "cmmr-ccm", "mm": "cmmmr-cc",
                 "c": "ccmr-cmm", "cc": "cccmr-mm", "cm": "ccmmr-cm"},
    "ccmmr-cm": {"m": "ccm-cmmr", "mm": "cc-cmmmr",
                 "c": "cmm-ccmr", "cc": "mm-cccmr",
                 "cm": "cm-ccmmr"},
    "cc-cmmmr": {"m": "ccmr-cmm", "mm": "ccmmr-cm",
                 "c": "cccr-mmm", "cm": "cccmr-mm"},
    "cccr-mmm": {"c": "cc-cmmmr", "cc": "c-ccmmmr"},
    "c-ccmmmr": {"m": "cmr-ccmm", "mm": "cmmr-ccm",
                 "c": "ccr-cmmm", "cc": "cccr-mmm",
                 "cm": "ccmr-cmm"},
    "ccr-cmmm": {"c": "c-ccmmmr", "cc": "-cccmmmr"},
    "cmr-ccmm": {"m": "c-ccmmmr", "c": "m-cccmmr",
                 "cm": "-cccmmmr"},
    "cccmm-mr": "failure",
    "cccm-mmr": "failure",
    "cccmmr-m": "failure",
    "ccm-cmmr": "failure",
    "cmm-ccmr": "failure",
    "mm-cccmr": "failure",
    "cmmr-ccm": "failure",
    "cccmr-mm": "failure",
    "ccmr-cmm": "failure",
    "m-cccmmr": "failure",
    "-cccmmmr": "success"}

gamestate = "cccmmmr-"

# game
if __name__ == "__main__":
    menu(font)
    gameloop()
