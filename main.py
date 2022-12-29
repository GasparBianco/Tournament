import numpy as np
from model import *


def generator(rounds):

    i = 0
    players = []
    names = vars()

    while i<(2**rounds):

        i = i+1

        name = "Player"+ str(i)
        skill = int(np.random.normal(loc=85, scale=6))

        if skill >= 100:
            skill=99

        names[name] = Player(name, skill)
        players.append(names[name])

    return(players)




class Player():

    def __init__(self,name,skill):

        self.name = name
        self.skill = skill


    def match_skill(self):


        rng = np.random.default_rng()
        performance = rng.integers(low=-10, high=10)
        performance = self.skill + performance


        return(performance)


class Bracket():

    def __init__(self,rounds,players):

        self.rounds = rounds
        i = 2**self.rounds
        self.randomizer(i,players)
        self.check(players)

    def randomizer(self,i,players):

        self.players = np.random.choice(players, size = i)


    def check(self,players):

        if len(players) == 1:

            print("El campeon es ",players[0].name,"con una skill de ",players[0].skill)

        else:

            self.round(players)


    def round(self,players):

        i = 0
        self.winners = []

        while i<(2**self.rounds):

            match_players = [self.players[i],self.players[i+1]]
            self.match(match_players)
            i = i+2

        self.players = self.winners
        self.rounds = self.rounds - 1
        self.check(self.players)

    def match(self,players):

        skill_player1 = players[0].match_skill()
        skill_player2 = players[1].match_skill()


        if skill_player1>skill_player2:

            self.winners.append(players[0])

        elif skill_player2>skill_player1:

                self.winners.append(players[1])

        else:

            coin = np.random.random()

            if coin<=0.5:

                self.winners.append(players[0])

            else:

                self.winners.append(players[1])


players = generator(3)
tournament = Bracket(3,players)
