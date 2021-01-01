from src.GUI.solar_system_graphics import SolarSystemGraphics
from src.GUI.travel_to_mars_graphics import TravelToMarsGraphics
from src.system.solar_system import SolarSystem


class TheSpace(object):

    def __init__(self):
        self.solar_system = SolarSystem()

    def get_solar_system(self) -> SolarSystem:
        return self.solar_system


if __name__ == '__main__':
    space = TheSpace()

    # GUI for our Solar System
    SolarSystemGraphics(space.get_solar_system())

    # Hohmann Transfer Orbit - Mission to Mars
    TravelToMarsGraphics()
