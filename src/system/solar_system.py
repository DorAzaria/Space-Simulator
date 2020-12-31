from src.system.planet import Planet
from src.system.sun import TheSun


class SolarSystem(object):

    def __init__(self):
        self.planets = {}
        self.sun = TheSun()
        self.number_of_planets = 8
        self.init_planet()

    def init_planet(self):
        self.planets.__setitem__('mercury', self.set_mercury())
        self.planets.__setitem__('venus', self.set_venus())
        self.planets.__setitem__('earth', self.set_earth())
        self.planets.__setitem__('mars', self.set_mars())
        self.planets.__setitem__('jupiter', self.set_jupiter())
        self.planets.__setitem__('saturn', self.set_saturn())
        self.planets.__setitem__('uranus', self.set_uranus())
        self.planets.__setitem__('neptune', self.set_neptune())

    def get_planets(self) -> dict:
        return self.planets

    def get_the_sun(self):
        return self.sun

    @staticmethod
    def set_mercury() -> Planet:
        planet = Planet('mercury')
        planet.set_average_distance_from_sun(57909176)
        planet.set_aphelion(69817079)
        planet.set_perihelion(46001272)
        planet.set_orbital_period(87.9691)
        planet.set_number_of_moons(0)
        planet.set_self_loop(58.6462)
        planet.set_average_temperature(166)
        planet.set_color('gray')
        planet.set_radius(80)
        planet.set_factor(0.05)
        planet.image = "GUI/media/mercury.gif"
        return planet

    @staticmethod
    def set_venus() -> Planet:
        planet = Planet('venus')
        planet.set_average_distance_from_sun(108208926)
        planet.set_aphelion(108941849)
        planet.set_perihelion(107476002)
        planet.set_orbital_period(224.70069)
        planet.set_number_of_moons(0)
        planet.set_self_loop(243.0185)
        planet.set_average_temperature(463)
        planet.set_color('white')
        planet.set_radius(120)
        planet.set_factor(0.03)
        planet.image = "GUI/media/venus.gif"
        return planet

    @staticmethod
    def set_earth() -> Planet:
        planet = Planet('earth')
        planet.set_average_distance_from_sun(149598023)
        planet.set_aphelion(152097701)
        planet.set_perihelion(147098074)
        planet.set_orbital_period(365.256366)
        planet.set_number_of_moons(1)
        planet.set_self_loop(23.934)
        planet.set_average_temperature(14)
        planet.set_color('blue')
        planet.set_radius(160)
        planet.set_factor(0.01)
        planet.image = "GUI/media/earth.gif"
        return planet

    @staticmethod
    def set_mars() -> Planet:
        planet = Planet('mars')
        planet.set_average_distance_from_sun(227936637)
        planet.set_aphelion(249228730)
        planet.set_perihelion(206644545)
        planet.set_orbital_period(686.971)
        planet.set_number_of_moons(2)
        planet.set_self_loop(24.6229)
        planet.set_average_temperature(-63)
        planet.set_color('red')
        planet.set_radius(200)
        planet.set_factor(0.007)
        planet.image = "GUI/media/mars.gif"
        return planet

    @staticmethod
    def set_jupiter() -> Planet:
        planet = Planet('jupiter')
        planet.set_average_distance_from_sun(778340821)
        planet.set_aphelion(816081455)
        planet.set_perihelion(740742598)
        planet.set_orbital_period(4331.572)
        planet.set_number_of_moons(79)
        planet.set_self_loop(10)
        planet.set_average_temperature(-121)
        planet.set_radius(300)
        planet.set_factor(0.005)
        planet.set_color('orange')
        planet.image = "GUI/media/jupiter.gif"
        return planet

    @staticmethod
    def set_saturn() -> Planet:
        planet = Planet('saturn')
        planet.set_average_distance_from_sun(1426725413)
        planet.set_aphelion(1503983449)
        planet.set_perihelion(1349467375)
        planet.set_orbital_period(10832.327)
        planet.set_number_of_moons(82)
        planet.set_self_loop(10)
        planet.set_average_temperature(-130)
        planet.set_radius(350)
        planet.set_factor(0.003)
        planet.set_color('yellow')
        planet.image = "GUI/media/saturn.gif"
        return planet

    @staticmethod
    def set_uranus() -> Planet:
        planet = Planet('uranus')
        planet.set_average_distance_from_sun(2870972220)
        planet.set_aphelion(3006389405)
        planet.set_perihelion(2735555035)
        planet.set_orbital_period(30799.095)
        planet.set_number_of_moons(27)
        planet.set_self_loop(17)
        planet.set_average_temperature(-220)
        planet.set_radius(400)
        planet.set_factor(0.002)
        planet.set_color('azure')
        planet.image = "GUI/media/uranus.gif"
        return planet

    @staticmethod
    def set_neptune() -> Planet:
        planet = Planet('neptune')
        planet.set_average_distance_from_sun(4498252900)
        planet.set_aphelion(4536874325)
        planet.set_perihelion(4459631496)
        planet.set_orbital_period(60190)
        planet.set_number_of_moons(14)
        planet.set_self_loop(16)
        planet.set_average_temperature(-212)
        planet.set_color('blue')
        planet.set_radius(450)
        planet.set_factor(0.001)
        planet.image = "GUI/media/neptune.gif"
        return planet
