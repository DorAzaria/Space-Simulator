from spacecraft import Spacecraft
import math


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
        earth_distance_to_sun = self.mission['earth'].avg_dist_from_sun
        mars_distance_to_sun = self.mission['mars'].avg_dist_from_sun

        #  the vis-viva equation - velocity of the target orbit
        mu = 3.986
        avg_distance = (earth_distance_to_sun + mars_distance_to_sun) / 2
        self.mission['earth'].velocity = math.sqrt(mu * ((2 / earth_distance_to_sun) - (1 / avg_distance)))
        self.mission['mars'].velocity = math.sqrt(mu * ((2 / mars_distance_to_sun) - (1 / avg_distance)))
