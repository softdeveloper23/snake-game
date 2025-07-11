from turtle import Turtle

OBJECT_COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.get_current_high_score()
        self.color(OBJECT_COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def get_current_high_score(self):
        try:
            with open("data.txt") as file:
                value = file.read().strip()
                return int(value) if value else 0
        except (FileNotFoundError, ValueError):
            return 0
        
    def new_high_score(self, new_score):
        with open("data.txt", mode="w") as file:
            file.write(str(new_score))


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
