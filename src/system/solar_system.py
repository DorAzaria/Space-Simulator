from src.system.planet import Planet
from src.system.sun import TheSun
import json


class SolarSystem(object):

    def __init__(self):
        self.planets = {}
        self.sun = TheSun()
        self.number_of_planets = 8
        self.open('system/json_files/solar_system.json')

    def get_planets(self) -> dict:
        return self.planets

    def get_the_sun(self):
        return self.sun

    def save_to_file(self, file_name: str) -> None:

        try:
            with open(file_name, "w") as f:
                json.dump(self.planets, default=lambda o: o.__dict__, indent=4, fp=f)
        except IOError as e:
            print(e)

    def open(self, file_name: str) -> None:
        new_planets = {}
        with open(file_name, "r") as f:
            dict_lot = json.load(f)
            for v in dict_lot.values():
                planet = Planet(v)
                new_planets[v['name']] = planet
        self.planets = new_planets
