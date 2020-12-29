from src.GUI.graphics import Graphics
from src.system.solar_system import SolarSystem
from src.system.planet import Planet


class TheSpace(object):

    def __init__(self):
        self.solar_system = SolarSystem()

    def get_solar_system(self) -> SolarSystem:
        return self.solar_system


if __name__ == '__main__':
    space = TheSpace()
    ss = space.get_solar_system()
    sun = ss.get_the_sun()
    planets = ss.get_planets()
    graphics = Graphics(ss)
