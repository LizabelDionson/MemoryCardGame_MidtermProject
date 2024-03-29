import pygame
from graphics import *
from random import *
from time import *
from platform import *


def OsCheck():
    if system() != 'Windows':
        return False


def load_sounds():
    click_sound = pygame.mixer.Sound("sounds/click.wav")
    mismatch_sound = pygame.mixer.Sound("sounds/mismatched.wav")
    match_sound = pygame.mixer.Sound("sounds/matchedpair.wav")
    return click_sound, mismatch_sound, match_sound


def play_click_sound(click_sound):
    click_sound.play()


def play_mismatch_sound(mismatch_sound):
    mismatch_sound.play()


def play_match_sound(match_sound):
    match_sound.play()


def DrawBackButton(win):
    button = Image(Point(70, 40), "images/back_button.png")
    button.draw(win)
    return button


def BackButtonClicked(point, button):
    return point.x > 20 and point.x < 120 and point.y > 20 and point.y < 60


def Welcome(win):
    click_sound = pygame.mixer.Sound("sounds/click.wav")

    background = Image(Point(randint(-200, 1000), randint(-200, 600)), 'images/bg.png')
    background.draw(win)

    img1 = Image(Point(randint(50, 700), randint(-100, 500)), 'images/img1.png')
    img1.draw(win)

    logo = Image(Point(400, 400 / 3), 'images/logo.png')
    logo.draw(win)

    txt1 = Text(Point(400, 210), "Click To Start Game")
    txt1.draw(win)

    win.getMouse()
    play_click_sound(click_sound)

    logo.undraw()
    txt1.undraw()


def GameModePick(win):
    click_sound = pygame.mixer.Sound("sounds/click.wav")

    txt0 = Text(Point(400, 50), "Game Mode")
    txt0.setSize(36)
    txt0.setStyle('bold')
    txt0.draw(win)

    txt = Text(Point(400, 100), "Pick A Game Mode! Images Mode Or Numbers Mode!")
    txt.setSize(15)
    txt.draw(win)

    img1 = Image(Point(200, 200), 'images/imagesmode.png')
    img1.draw(win)

    img2 = Image(Point(600, 200), 'images/numbersmode.png')
    img2.draw(win)

    gamemode = -1

    try:
        while gamemode < 0:
            point = win.getMouse()

            if point:
                if 90 < point.x < 310 and 190 < point.y < 230:
                    gamemode = 0
                    play_click_sound(click_sound)
                elif 470 < point.x < 720 and 190 < point.y < 230:
                    gamemode = 1
                    play_click_sound(click_sound)
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt gracefully by exiting the program
        pygame.quit()
        sys.exit()

    txt0.undraw()
    txt.undraw()
    img1.undraw()
    img2.undraw()

    return gamemode


def Difficult(win):
    click_sound = pygame.mixer.Sound("sounds/click.wav")

    txt0 = Text(Point(400, 50), "Difficulty")
    txt0.setSize(36)
    txt0.setStyle('bold')
    txt0.draw(win)

    txt = Text(Point(400, 100), "Pick A Difficulty! Easy Mode Or Normal Mode Or Hard Mode!")
    txt.setSize(15)
    txt.draw(win)

    img1 = Image(Point(200, 200), 'images/easy.png')
    img1.draw(win)

    img2 = Image(Point(400, 200), 'images/normal.png')
    img2.draw(win)

    img3 = Image(Point(600, 200), 'images/hard.png')
    img3.draw(win)

    difficult = -1

    while difficult < 0:
        point = win.getMouse()
        if (point.x < 250 and point.x > 150 and point.y < 230 and point.y > 150):
            difficult = 16
            pygame.mixer.Sound.play(click_sound)
        else:
            if (point.x < 450 and point.x > 350 and point.y < 230 and point.y > 150):
                difficult = 24
                pygame.mixer.Sound.play(click_sound)
            else:
                if (point.x < 650 and point.x > 550 and point.y < 230 and point.y > 150):
                    difficult = 32
                    pygame.mixer.Sound.play(click_sound)
                else:
                    difficult = -1

    txt0.undraw()
    txt.undraw()
    img1.undraw()
    img2.undraw()
    img3.undraw()

    num_list = [i % (int(difficult / 2)) for i in range(difficult)]
    shuffle(num_list)
    exposed = [False for i in range(difficult)]

    return num_list, exposed, difficult


def Init(win):
    click_sound = pygame.mixer.Sound("sounds/click.wav")

    # Display rules
    background = Image(Point(randint(-200, 1000), randint(-200, 600)), 'images/bg.png')
    background.draw(win)

    rules_title = Text(Point(90, 50), "Rules")
    rules_title.setSize(36)
    rules_title.setStyle('bold')
    rules_title.draw(win)

    rules_text = Text(Point(380, 160),
                      "In turn, the player chooses two cards and turns them face up. \n If they are the same number, then the player wins the pair and earns 1 KEY. \n If they are not the same number, they are turned face down again.\n There are 8 KEYS to earn. Use the least moves and time to win the game. \n Now type in your name to start the game!")
    rules_text.setSize(15)
    rules_text.draw(win)

    # Collect player name
    username = ""
    move = 0
    key = 0

    name_prompt = Text(Point(530 / 1.5, 350), "Player Name: ")
    name_prompt.setSize(14)
    name_prompt.draw(win)

    name_entry = Entry(Point(550 / 1.5 + 130, 350), 15)
    name_entry.setFill('white')
    name_entry.draw(win)

    start_button_bg = Rectangle(Point(750 / 1.5 + 100, 330), Point(850 / 1.5 + 160, 370))
    start_button_bg.setFill('green')
    start_button_bg.setOutline("")
    start_button_bg.draw(win)

    # Display start button text
    start_button = Text(Point(800 / 1.5 + 130, 350), "Start")
    start_button.setFill('white')
    start_button.setStyle('bold')
    start_button.draw(win)

    start_button_anchor = start_button.getAnchor()

    while True:
        click_point = win.getMouse()

        if start_button_anchor.getX() - 50 < click_point.getX() < start_button_anchor.getX() + 50 \
                and start_button_anchor.getY() - 15 < click_point.getY() < start_button_anchor.getY() + 15:
            username = name_entry.getText()
            pygame.mixer.Sound.play(click_sound)

            if not username.strip():
                error_msg = Text(Point(400, 300), "Please enter your name before starting the game.")
                error_msg.setTextColor("red")
                error_msg.setStyle('bold')
                error_msg.draw(win)
                sleep(2)
                error_msg.undraw()
            else:
                name_entry.undraw()
                start_button.undraw()
                start_button_bg.undraw()
                break

    name_prompt.undraw()
    name_entry.undraw()

    starttime = time()

    rules_title.undraw()
    rules_text.undraw()
    background.undraw()

    return username, move, key, starttime


def ReadPicturesNames(t, gamemode):
    if gamemode == 1:
        if t == -1:
            a = 'images/cardback.png'
        else:
            a = 'images/card.png'
    else:
        if gamemode == 0:
            if t != -1:
                a = 'images/card_' + str(t) + '.png'
            else:
                a = 'images/cardback.png'

    return a


def DrawPictures(path, p, win, gamemode):
    img1 = Image(p, ReadPicturesNames(path, gamemode))
    img1.draw(win)


def DrawText(p, win, num_list, clicked_card):
    txt1 = Text(p, num_list[clicked_card - 1])
    txt1.setSize(24)
    txt1.setStyle('bold')
    txt1.draw(win)

    return txt1


def ScoreBoard(win, move, key, user_point):
    move_txt = Text(Point(45, 160), "Moves: ")
    move_txt.setStyle('bold')
    move_txt.draw(win)

    move_txt1 = Text(Point(80, 160), str(move))
    move_txt1.setStyle('bold')
    move_txt1.draw(win)

    key_txt = Text(Point(40, 180), "Key: " + str(key))
    key_txt.setStyle('bold')
    key_txt.draw(win)

    if user_point is not None:
        mouse_txt = Text(Point(105, 200), "Mouse Clicked: " + str(user_point.x) + "," + str(user_point.y))
        mouse_txt.setStyle('bold')
        mouse_txt.draw(win)
    else:
        mouse_txt = None

    return move_txt, key_txt, mouse_txt, move_txt1


def GameBoard(win, username, gamemode, difficult):
    txt1 = Text(Point(80, 40), str(username))
    txt1.setSize(30 - len(username))
    txt1.setStyle('bold')
    txt1.draw(win)

    card_point = []
    card_point1 = []
    card_point2 = []

    if difficult == 32:
        plac = 50
    elif difficult == 24:
        plac = 100
    else:
        plac = 150

    for j in range(int(difficult / 8)):
        for i in range(8):
            x = 225 + ((i + 1) * 60)
            y = plac + (j * 100)
            p = Point(x, y)
            DrawPictures(-1, p, win, gamemode)
            p1 = Point(x + 25, y + 40)
            p2 = Point(x - 25, y - 40)
            card_point.append(p)
            card_point1.append(p1)
            card_point2.append(p2)
    return card_point, card_point1, card_point2


def DecideWhichCard(x, y, card_point1, card_point2, difficult):
    for i in range(difficult):
        if x < card_point1[i].x and x > card_point2[i].x and y < card_point1[i].y and y > card_point2[i].y:
            return i + 1
    return -1


def HasItBeenClickedBefore(clicked_card, exposed):
    return exposed[clicked_card - 1]


def CheckMatches(c1, c2, num_list):
    return num_list[c1] == num_list[c2]


def Result(win, gametime, username, difficult):
    if difficult == 32:
        rank = [i.rstrip('\n') for i in open("playersScores_hard.txt", "r")]
        t = "Hard"
    elif difficult == 24:
        rank = [i.rstrip('\n') for i in open("playersScores_normal.txt", "r")]
        t = "Normal"
    else:
        rank = [i.rstrip('\n') for i in open("playersScores.txt", "r")]
        t = "Easy"

    ranking_txt = Text(Point(400, 30), "Rankings Of " + str(t) + " Mode")
    ranking_txt.setSize(20)
    ranking_txt.setStyle('bold')
    ranking_txt.draw(win)

    current = Text(Point(120, 200), str(t) + " Mode\n" + "Player Time: " + str(round(gametime, 3)) + "s")
    current.setSize(14)
    current.setStyle('bold')
    current.draw(win)

    line = Line(Point(0, 50), Point(801, 50))
    line.draw(win)
    line.setWidth(2)

    rankings = sorted(rank)
    t = 0

    while t < len(rankings) and t < 10:
        txt1 = Text(Point(500, 80 + (t * 30)), "Rank " + str(t + 1) + ": " + str(rankings[t]))
        txt1.setSize(14)
        txt1.draw(win)
        t += 1


def InsertInsideTheTopPlayer(username, gametime, move, difficult):
    if difficult == 32:
        rank_file = open("playersScores_hard.txt ", "a+")
    elif difficult == 24:
        rank_file = open("playersScores_normal.txt ", "a+")
    else:
        rank_file = open("playersScores.txt ", "a+")

    rank_file.write(str(round(gametime, 3)) + "s Name: " + str(username) + " Moves: " + str(move) + "\n")

    rank_file.close()


def Main():
    pygame.init()
    user_point = Point(200, 200)
    counter = 0
    card = []

    win = GraphWin("Memories Card Game", 800, 400)

    Welcome(win)
    gamemode = GameModePick(win)
    num_list, exposed, difficult = Difficult(win)
    username, move, key, starttime = Init(win)
    move_txt, key_txt, mouse_txt, move_txt1 = ScoreBoard(win, move, key, user_point)
    card_point, card_point1, card_point2 = GameBoard(win, username, gamemode, difficult)

    msg = Text(Point(100, 300), "")
    msg.setSize(18)
    msg.setStyle('bold')
    msg.draw(win)

    # Load sounds
    click_sound, mismatch_sound, match_sound = load_sounds()

    while key < int(difficult / 2):
        if counter < 2:
            move_txt.undraw()
            key_txt.undraw()
            mouse_txt.undraw()
            move_txt1.undraw()

            move_txt, key_txt, mouse_txt, move_txt1 = ScoreBoard(win, move, key, user_point)

            user_point = win.getMouse()

            msg.undraw()

            if user_point is not None:
                clicked_card = DecideWhichCard(user_point.x, user_point.y, card_point1, card_point2, difficult)

                if clicked_card is not None and clicked_card > 0:
                    if not HasItBeenClickedBefore(clicked_card, exposed):
                        counter += 1
                        card.append(clicked_card - 1)
                        DrawPictures(2, card_point[clicked_card - 1], win, gamemode)
                        if gamemode == 1:
                            txt1 = DrawText(card_point[clicked_card - 1], win, num_list, clicked_card)
                        else:
                            DrawPictures(num_list[clicked_card - 1], card_point[clicked_card - 1], win, gamemode)
                        exposed[clicked_card - 1] = True
                        play_click_sound(click_sound)
                    else:
                        msg.setText("Bad Choices!\n    Pick Another One!")
                        msg.setTextColor('red')
                        msg.draw(win)


        else:

            check = CheckMatches(card[0], card[1], num_list)
            if check:
                key += 1
                move += 1
                oo = ["Great!", "Nice!", "Cool!", "Awesome!"]
                msg.setText(oo[randint(0, 3)])
                msg.setTextColor('black')
                msg.draw(win)
                play_match_sound(match_sound)

            else:
                sleep(1)
                exposed[card[0]] = False
                exposed[card[1]] = False
                DrawPictures(-1, card_point[card[0]], win, gamemode)
                DrawPictures(-1, card_point[card[1]], win, gamemode)
                oo = ["Sorry!", "Try Again!"]
                msg.setText(oo[randint(0, 1)])
                msg.setTextColor('black')
                msg.draw(win)
                play_mismatch_sound(mismatch_sound)
            move += 1
            card = []
            counter = 0

    background = Image(Point(randint(-200, 1000), randint(-200, 600)), 'images/bg.png')
    background.draw(win)

    endtime = time()
    gametime = endtime - starttime
    InsertInsideTheTopPlayer(username, gametime, move, difficult)
    Result(win, gametime, username, difficult)

    backButton = DrawBackButton(win)

    while True:
        clickPoint = win.getMouse()

        if BackButtonClicked(clickPoint, backButton):
            win.close()
            break

    Main()

    win.getMouse()
    win.close()


Main()
