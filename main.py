import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = ""

    def add_score(self):
        self.score += 1

    def print_player(self):
        print(self.name, self.score)


class RandomChooser:

    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.choice = random.choice(self.options)


class RockPaperScissors:

    def __init__(self, pc, player):
        self.random = pc
        self.player = player

    def guess(self):
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
        print("PC: ", self.random.choice)
        self.player.print_player()
        self.random.print_player()


class PlayGame:
    def __init__(self, name):
        self.human = Player(name)
        self.pc = Player("MyPc")

    def play(self):
        while self.human.score < 3 and self.pc.score < 3:
            self.pc.choice = RandomChooser().choice
            while True:
                choose = input("1. Rock\n2. Paper\n3. Scissors\n")
                if choose == "1" or choose == "2" or choose == "3":
                    break
                print("Wrong choose")
            self.human.choice = RandomChooser().options[int(choose) - 1]
            RockPaperScissors(self.pc, self.human).guess()
            # print("Player: ", self.human.choice)
        if self.human.score == 3:
            print("YOU WIN!")
        else:
            print("YOU LOST!")


if __name__ == "__main__":
    playerName = input("Type in your name: ")
    PlayGame(playerName).play()
