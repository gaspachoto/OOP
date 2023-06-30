from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
import sys

class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self.__get_horse_by_name(horse_name)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
        if horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if horse_race:
            raise Exception(f"Race {race_type} has been already created!")
        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.__find_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if horse and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey and jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        max_speed = -sys.maxsize
        winner_jockey = ''
        winner_horse = ''
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner_jockey = jockey.name
                winner_horse = jockey.horse.name
        return f"The winner of the {race_type} race, with a speed of {max_speed}km/h is {winner_jockey}! Winner's horse: {winner_horse}."

    def __get_horse_by_name(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def __get_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def __get_horse_race_by_type(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

    def __find_horse_by_type(self, horse_type):
        for index in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[index]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        return None