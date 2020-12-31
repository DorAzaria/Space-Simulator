from solar_system import SolarSystem


class Spacecraft(object):

    def __init__(self, sys: SolarSystem):
        self.solar_system = sys
        self.planets = sys.get_planets()
        self.mission = {'earth': self.planets['earth'], 'mars': self.planets['mars']}
        self.velocity = 0

    def get_mission(self) -> dict:
        return self.mission

