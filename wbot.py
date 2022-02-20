# -*- coding: utf-8 -*-    
from cv2 import cv2
from os import listdir
from random import randint
from random import random
import numpy as np
import mss
import pyautogui
import time
import sys
from pprint import pprint
import yaml

VERSAO_SCRIPT = "1.00"

str_in = """
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣤⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢷⣄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⢠⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⡯⠻⠿⣿⣿⡿⠿⠛⢷⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⣤⣤⠼⠟⠛⠄⠠⣭⡙⠋⠉⠄⠄⠚⠟⠋⠃⠐⠸⢟⣦⠄⠄
        ⠄⠄⠄⠄⢀⣴⣿⡿⠋⠄⢀⣤⣤⣶⠈⢷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⠆⠄
        ⠄⠄⠄⠄⣿⣿⣍⠉⠻⠄⢻⣿⣿⣿⣶⣾⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠨⣾⠄
        ⠄⠄⠄⣸⡿⣩⣟⣿⡦⡲⣿⣿⣿⡿⠙⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢈⠁⠄
        ⠄⠄⠄⣿⣏⣉⠉⠛⠢⠈⣻⣿⣿⡍⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠈⠄⠄
        ⠄⠄⠄⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⢷⠄⡌⠄⠄⠄⠄⠄
        ⠄⠄⠸⠿⣿⣿⣿⡿⠟⠉⠿⠿⠁⠄⠄⠄⠄⠄⠄⢄⠄⠐⠁⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⢠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⣾⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⣠⣿⣿⣷⣴⣶⣶⠄⠄⠄⠄⠄⠄⠄⠄⢀⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    +++++++++++++++++++++++++++++++++++++
    ++++++++++ BOT BOLADO 1.00 ++++++++++
    +++++++++++++++++++++++++++++++++++++

    >> Ctrl + c finaliza o bot.
    
    
    """
print(str_in)

def debug_mousepos():

    print("DEBUGGING MOUSE POSITION")

    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def printScreen(monitorNumber = 0):
    with mss.mss() as sct:
        monitor = sct.monitors[monitorNumber]
        sct_img = np.array(sct.grab(monitor))
        # The screen part to capture
        # monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

        # Grab the data
        return sct_img[:,:,:3]

def getRandomEasing():
    easings = [
        pyautogui.easeInQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInBounce,
        pyautogui.easeInElastic
    ]

    return easings[randint(0, len(easings) -1)]

def addRandomness(n, randomn_factor_size=None):
    if randomn_factor_size is None:
        randomness_percentage = 0.1
        randomn_factor_size = randomness_percentage * n

    random_factor = 2 * random() * randomn_factor_size
    if random_factor > 5:
        random_factor = 5
    without_average_random_factor = n - randomn_factor_size
    randomized_n = int(without_average_random_factor + random_factor)
    # logger('{} with randomness -> {}'.format(int(n), randomized_n))
    return int(randomized_n)

def moveToWithRandomness(x,y,t=None):
    ft = 0.2

    if t is not None:
        ft = t

    pyautogui.moveTo(addRandomness(x,10),addRandomness(y,10),ft+random()/2, getRandomEasing())

def load_images():
    file_names = listdir('./images/')
    targets = {}
    for file in file_names:
        path = 'images/' + file
        targets[remove_suffix(file, '.png')] = cv2.imread(path)

    return targets

def getImagePosition(frame_image, target_image, threshold=0.7):

    result = cv2.matchTemplate(frame_image, target_image, cv2.TM_CCOEFF_NORMED)
    w = target_image.shape[1]
    h = target_image.shape[0]

    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


def leftClick(pos):
    x, y = pos
    moveToWithRandomness(x,y)
    pyautogui.click()

def leftClickDrag(pos):
    x, y = pos
    moveToWithRandomness(x,y)
    pyautogui.dragRel(0, -50, duration=0.2, button='left')

def leftClickMultipleReverse(pos):
    for i in range(len(pos) -1, -1, -1):
        leftClick(pos[i])

def sleep(seconds):
    print("Sleeping for {}\r\n".format(seconds))
    time.sleep(seconds)

def loadYaml(filename):
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)



class Wbot():
    def __init__(self):
        # Tempo entre ações
        pyautogui.PAUSE = 0.2
        self.images = load_images()
        self.currentFrame = None
        self.currentScreen = None
        self.selectionScroll = 0
        self.selectionScrollLimit = 6
        self.selectionAttempts = 0
        self.settings = loadYaml("settings.yaml")

    def run(self):
        print("WBot Run!\n")

        while True:
            print("\r\nWBot Thinking...\r\n")
            sleep(1)

            self.updateCurrentFrame()

            self.actionCloseError()
            self.actionConfirmLose()

            self.detectCurrentScreen()
            print("     Current Screen: {}\r\n".format(self.currentScreen))

            if self.currentScreen == 'login':
                self.actionLogin()
                continue

            if self.currentScreen == 'selection':
                self.actionSelection()
                continue

            if self.currentScreen == 'battle':
                self.actionBattle()
                continue

            if self.currentScreen == 'base':
                self.actionBase()
                continue

            print("     Nothing to do....\r\n")
            continue
            # debug_mousepos()

    def updateCurrentFrame(self):
        print("updateCurrentFrame\n")
        self.currentFrame = printScreen(self.settings['monitorNum'])

    def detectCurrentScreen(self):
        previousScreen = self.currentScreen

        pos = self.getPos('screen_login')
        if pos is not None:
            self.currentScreen = 'login'
            return

        pos = self.getPos('screen_selection')
        if pos is not None:
            self.currentScreen = 'selection'

            if previousScreen != self.currentScreen and previousScreen != 'base':
                self.selectionScroll = 0
                self.selectionAttempts = 0
            return

        pos = self.getPos('battle_btn_surrender')
        if pos is not None:
            self.currentScreen = 'battle'

        pos = self.getPos('screen_base')
        if pos is not None:
            self.currentScreen = 'base'

    def getPos(self, img_name, treshold = 0.7):
        pos = getImagePosition(self.currentFrame, self.images[img_name], treshold)

        if len (pos) == 0:
            return None

        x, y, w, h = pos[0]

        # x = x+w/2
        # y = y+h/2

        #some e divide para retornar o meio da imagem
        return x+w/2, y+h/2

    def getPosMultiple(self, img_name, treshold = 0.7):
        pos = getImagePosition(self.currentFrame, self.images[img_name], treshold)

        if len (pos) == 0:
            return None

        multiplePos = []
        for p in pos:
            x, y, w, h = p
            x = x+w/2
            y = y+h/2
            multiplePos.append([x, y])

        # x = x+w/2
        # y = y+h/2

        #some e divide para retornar o meio da imagem
        return multiplePos

    def actionLogin(self):
        print("     actionWallet\n")
        pos = self.getPos('login_btn_connect_wallet')

        if pos is not None:
            leftClick(pos)

        #Sign meta mask
        while True:
            print("     Looking For Metamask Sign button\n")
            sleep(2)
            self.updateCurrentFrame()
            pos = self.getPos('login_btn_metamask_sign')

            if pos is not None:
                leftClick(pos)

            #Looking for Play buttom
            while True:
                print("     Looking For Play button\n")
                sleep(2)
                self.updateCurrentFrame()
                pos = self.getPos('login_btn_play')

                if pos is not None:
                    leftClick(pos)

                return

    def actionSelection(self):
        #Checa se existem naves a serem removidas antes de qualquer seleção
        if self.selectionAttempts == 0:
            pos = self.getPosMultiple('selection_btn_remove')

            if pos is not None:
                print("     Naves a remover, removendo...\r\n")
                #Click 2 times to be safe
                leftClickMultipleReverse(pos)
                leftClickMultipleReverse(pos)
                return

        posBtnFightBoss = self.getPos('selection_btn_fight_boss')

        pos = self.getPos('selection_lbl_15-15', 0.98)
        #naves full, ir para luta
        if pos is not None:
            print("     Naves FULL, FIGHT\r\n")
            leftClick(posBtnFightBoss)
            return

        #naves não full, selecionar naves 100%
        pos = self.getPosMultiple('selection_btn_fight_full', 0.98)
        if pos is not None:
            print("     Naves não FULL, SELECIONAR {}\r\n".format(self.selectionAttempts))

            self.selectionAttempts += 1
            leftClickMultipleReverse(pos)
            sleep(2)
            return

            # if self.selectionAttempts % 3 != 0:
            #     return

        #Se já scrollou mais que o limite vai base
        if self.selectionScroll >= self.selectionScrollLimit:
            print("     Scroll Limit Reached, going to BASE and back {}/{}".format(self.selectionScroll, self.selectionScrollLimit))
            pos = self.getPos('selection_btn_base')

            if pos is not None:
                leftClick(pos)
                return

        #Scrollar
        pos = self.getPos('selection_btn_scroll')
        if pos is not None:
            print("     Scrolling {}/{}".format(self.selectionScroll, self.selectionScrollLimit))
            leftClickDrag(pos)
            self.selectionScroll +=1
            sleep(2)
        return


    def actionCloseError(self):
        pos = self.getPos('error_btn_close')

        if pos is not None:
            leftClick(pos)

    def actionConfirmLose(self):
        pos = self.getPos('battle_lbl_lose')

        if pos is not None:
            print("     YOU LOSE, confirmando... \r\n")
            pos = self.getPos('battle_btn_confirm')
            leftClick(pos)

        return

    def actionBattle(self):
        pos = self.getPos('battle_lbl_victory')

        if pos is not None:
            print("     VICTORY, confirmando... \r\n")

            pos = self.getPos('battle_btn_confirm_victory')
            if pos is not None:
                leftClick(pos)

        pos = self.getPos('battle_lbl_0-15', 0.8)

        if pos is not None:
            print("     Sem naves para lutar, go to selection... \r\n")

            pos = self.getPos('battle_btn_selection')
            if pos is not None:
                leftClick(pos)


        #Se já deu surrender, confirmar
        pos = self.getPos('battle_lbl_surrender')
        if pos is not None:
            print("     Popup Surrender, confirmar...\r\n")

            pos = self.getPos('battle_btn_confirm_surrender')
            if pos is not None:
                leftClick(pos)

        #Surrender no boss 7
        pos = self.getPos('battle_lbl_boss7', 0.98)
        if pos is not None:
            print("     Boss 7, resetando com surrender...\r\n")

            pos = self.getPos('battle_btn_surrender')
            if pos is not None:
                leftClick(pos)

    def actionBase(self):
        pos = self.getPos('base_btn_spaceship')
        if pos is not None:
            print("     Na tela de Base, indo para spaceships.... \r\n")

            #reset variables
            self.selectionAttempts = 1
            self.selectionScroll = 1
            leftClick(pos)
            return

bot = Wbot()
bot.run()
