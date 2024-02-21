class Traffic:
    def __init__(self, green: float, red: float, yellow: float, x: float):
        self.green_time = green
        self.red_time = red
        self.yellow_time = yellow
        self.state = "green"
        self.time = 0
        self.x = x

    def update(self, t: float):
        self.time += t
        if self.state == "green":
            if self.time > self.green_time:
                self.time = 0
                self.state = "yellow"
        elif self.state == "yellow":
            if self.time > self.yellow_time:
                self.time = 0
                self.state = "red"
        elif self.state == "red":
            if self.time > self.red_time:
                self.time = 0
                self.state = "green"
