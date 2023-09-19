import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = ""

    def add_score(self):
        print("%s gains!" % self.name)
        self.score += 1

    def print_player(self):
        print("%s actual score: %d" % (self.name, self.score))

    def set_choose(self, options):
        self.choice = random.choice(options)


class InitOptions:

    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]


class RockPaperScissors:

    def __init__(self, pc, player):
        self.random = pc
        self.player = player

    def guess(self):
        if self.random.choice == self.player.choice:
            print("This is a tie!")
        else:
            if self.random.choice == "Rock":
                if self.player.choice == "Paper":
                    self.player.add_score()
                elif self.player.choice == "Scissors":
                    self.random.add_score()
            elif self.random.choice == "Paper":
                if self.player.choice == "Scissors":
                    self.player.add_score()
                elif self.player.choice == "Rock":
                    self.random.add_score()
            else:  # Scissors
                if self.player.choice == "Paper":
                    self.random.add_score()
                elif self.player.choice == "Rock":
                    self.player.add_score()
        print("%s chose: %s" % (self.random.name, self.random.choice))
        print("%s chose: %s\n" % (self.player.name, self.player.choice))
        self.player.print_player()
        self.random.print_player()
        print()


class PlayGame:
    def __init__(self, name):
        self.human = Player(name)
        self.pc = Player("MyPc")
        self.init = InitOptions()

    def play(self):
        while self.human.score < 3 and self.pc.score < 3:
            self.pc.set_choose(self.init.options)
            while True:
                choose = input("1. Rock\n2. Paper\n3. Scissors\n")
                if choose == "1" or choose == "2" or choose == "3":
                    break
                print("Wrong choose")
            self.human.choice = self.init.options[int(choose) - 1]
            RockPaperScissors(self.pc, self.human).guess()
        if self.human.score == 3:
            print("YOU WIN!")
        else:
            print("YOU LOST!")


if __name__ == "__main__":
    playerName = input("Type in your name: ")
    PlayGame(playerName).play()
