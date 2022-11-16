import numpy as np


#class Player_generator():

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

        self.number = np.arange(0, 2**rounds, 1)
        self.number = np.random.choice(self.number, size=(2**rounds))
        self.match(rounds,players)
        
    def match(self,rounds,players):

        if rounds == 0:
            
            print("El campeon es ",players[self.number[0]].name,"con una skill de ",players[self.number[0]].skill)

        else:

            i = 0
            winners = []

            while i<(2**rounds):
                
                skill_player1 = players[self.number[i]].match_skill()
                skill_player2 = players[self.number[(i+1)]].match_skill()
                

                if skill_player1>skill_player2:

                    winners.append(self.number[i])

                elif skill_player2>skill_player1:

                    winners.append(self.number[i+1])

                else:

                    coin = np.random.random()

                    if coin<=0.5:

                        winners.append(self.number[i])

                    else:

                        winners.append(self.number[i+1])

                i = i+2
            self.number = winners
            rounds = rounds-1
        
            self.match(rounds,players)








players = generator(3)
tournament = Bracket(3,players)

