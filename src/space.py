from src.GUI.solar_system_graphics import SolarSystemGraphics
from src.GUI.travel_to_mars_graphics import TravelToMarsGraphics
from src.system.solar_system import SolarSystem
from src.system.hohmann_transfer_orbit import HohmannTransferOrbit
from src.system.spacecraft import Spacecraft


class TheSpace(object):

    def __init__(self):
        self.solar_system = SolarSystem()
        self.spacecraft = Spacecraft(self.solar_system)
        self.hohmann = HohmannTransferOrbit(self.spacecraft)

    def get_solar_system(self) -> SolarSystem:
        return self.solar_system

    def get_hohmann_transfer_orbit(self):
        return self.hohmann

if __name__ == '__main__':
    space = TheSpace()

    # GUI for our Solar System
    SolarSystemGraphics(space.get_solar_system())

    # Hohmann Transfer Orbit - Mission to Mars
    TravelToMarsGraphics(space.get_hohmann_transfer_orbit())

