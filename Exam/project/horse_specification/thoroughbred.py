from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    HORSE_MAX_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 <= self.HORSE_MAX_SPEED:
            self.speed += 3
        else:
            self.speed = self.HORSE_MAX_SPEED