from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_MAX_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 2 <= self.HORSE_MAX_SPEED:
            self.speed += 2
        else:
            self.speed = self.HORSE_MAX_SPEED
