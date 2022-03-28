import plotext as plt
from time import time
from colorama import Fore
from os import system as sys
from random import choice as CHOICE

ROLLS = 100000 # How many times to roll the Dice (higher number = greater accuracy)

class DiceAnalysis():

    def __init__(self) -> None:
        self.time  = 0
        self.croll = 0
        self.g     = Fore.GREEN
        self.r     = Fore.RESET
        self.dice  = [1, 2, 3, 4, 5, 6]
        self.posbl = [2,3,4,5,6,7,8,9,10,11,12]
        self.count = [0,0,0,0,0,0,0,0,0,0,0]
        self.dice1 = [0,0,0,0,0,0,0,0,0,0,0]
        self.dice2 = [0,0,0,0,0,0,0,0,0,0,0]


    def Menu(self) -> None:
        sys('cls')
        print(f"""SIMPLE DICE ROLL ANALYSIS\n""")

    def CheckRolls(self, ROLL1, ROLL2) -> None:
        for pos in range(len(self.count)):
            if ROLL1 + ROLL2 == self.posbl[pos]: self.count[pos]+=1
            if ROLL1 == self.posbl[pos]: self.dice1[pos]+=1
            if ROLL2 == self.posbl[pos]: self.dice2[pos]+=1

    def RollDice(self) -> None:
        self.Menu()
        time_checking = time()
        print(f"[{self.g}*{self.r}] Acquiring Data for {self.g}{ROLLS}{self.r} rolls...")

        for i in range(ROLLS):
            ROLL1 = CHOICE(self.dice)
            ROLL2 = CHOICE(self.dice)
            self.CheckRolls(ROLL1, ROLL2) ; self.croll+=1
            print(f"[{self.g}*{self.r}] Rolls Checked -> {self.g}{self.croll}{self.r} ({self.g}{round(time() - time_checking)}s{self.r})", end='\r')
        self.time = round(time() - time_checking)

    def DisplayData(self) -> None:
        self.Menu()
        print(f"[{self.g}*{self.r}] The process took {self.g}{self.time}{self.r}s")
        print(f"[{self.g}*{self.r}] Here's the dataset for {self.g}{ROLLS}{self.r} simulated dice rolls...\n")

        for pos in range(len(self.count)):
            count = self.count[pos]
            percentage = round(count/ROLLS*100)
            print(f"{pos+2}{' ' if pos < 8 else ''} -> {self.g}{count}{self.r} ({percentage}%)")

        input(f'\n[{self.g}+{self.r}] Press any key to show graph...')

    def Graph(self) -> None:
        self.Menu()
        plt.bar(self.posbl, self.count, orientation = "vertical", width = 0.2) # or shorter orientation = 'h'
        plt.title(f"Dice Roll Analysis ({ROLLS} rolls)")
        plt.clc()
        plt.plotsize(100, 2 * len(self.posbl) - 1 + 4)
        plt.show()


Analysis = DiceAnalysis()
Analysis.RollDice()
Analysis.DisplayData()
Analysis.Graph()
