from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.player = Screen().textinput(title="Snake", prompt="Enter your name: ")
        self.score = 0
        self.high_score = self.set_high_score()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def set_high_score(self):
        high_score = self.fetch_high_score()
        if high_score is None:
            high_score = self.write_high_score('0')
        return high_score

    # helper function 1 for set_high_score
    def fetch_high_score(self):
        try:
            with open(f"./data/score_{self.player}.txt") as file:
                high_score = file.read()
        except FileNotFoundError:
            return None
        else:
            return high_score

    # helper function 2 for set_high_score
    def write_high_score(self, score):
        if self.player is not None:  # score is not recorded if player is None
            with open(f"./data/score_{self.player}.txt", 'w') as file:
                file.write(str(score))
        return score

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.write_high_score(self.high_score)
        # self.score = 0  # alternative mechanism for restarting the game (part)
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
