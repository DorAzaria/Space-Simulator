from spacecraft import Spacecraft
import math

from src.system.planet import Planet


class HohmannTransferOrbit(object):

    def __init__(self, sp: Spacecraft):
        """ travel to mars from earth
        using the Hohmann Transfer Orbit """
        self.spacecraft = sp
        self.mission = sp.get_mission()
        self.sun = sp.solar_system.get_the_sun()
        self.init()
        self.velocity = sp.velocity
        self.range = 0

    def init(self):
        earth = self.mission['earth']
        mars = self.mission['mars']
        #  the vis-viva equation - velocity of the target orbit
        earth.velocity = self.vis_viva_equation(earth, mars)
        mars.velocity = self.vis_viva_equation(mars, earth)

    @staticmethod
    def vis_viva_equation(source: Planet, destination: Planet) -> float:
        a = (source.avg_dist_from_sun + destination.avg_dist_from_sun) / 2
        return math.sqrt(source.mu * ((2 / source.avg_dist_from_sun) - (1 / a)))
