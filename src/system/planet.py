import math


class Planet(object):

    def __init__(self, n: str):
        self.name = n
        self.avg_dist_from_sun = 0
        self.aphelion = 0
        self.perihelion = 0
        self.orbital_period = 0
        self.number_of_moons = 0
        self.self_loop = 0
        self.avg_temperature = 0
        self.color = None
        self.radius = 0
        self.angle = 0
        self.following_star = None
        self.factor = 0
        self.image = ""
        self.velocity = 0

    def set_average_distance_from_sun(self, distance: int):
        self.avg_dist_from_sun = distance

    def set_aphelion(self, aph: int):
        self.aphelion = aph

    def set_perihelion(self, per: int):
        self.perihelion = per

    def set_orbital_period(self, orbital: float):
        self.orbital_period = orbital

    def set_number_of_moons(self, moons: int):
        self.number_of_moons = moons

    def set_self_loop(self, loops: float):
        self.self_loop = loops

    def set_average_temperature(self, temp: int):
        self.avg_temperature = temp

    def set_color(self, c: str):
        self.color = c

    def set_radius(self, rad: int):
        self.radius = rad

    def set_angle(self, ang: int):
        self.angle = ang

    def set_following_star(self, following):
        self.following_star = following

    def set_factor(self, fact):
        self.factor = fact

    def set_velocity(self, speed:float):
        self.velocity = speed

    def __str__(self):
        return f"~~~~ {self.name} ~~~~\n" \
               f"Average distance from the sun: {self.avg_dist_from_sun}\n" \
               f"Aphelion: {self.aphelion}\n" \
               f"Perihelion: {self.perihelion}\n" \
               f"Orbital Period (in days): {self.orbital_period}\n" \
               f"Number of Moons: {self.number_of_moons}\n" \
               f"Self Loop (in hours): {self.self_loop}\n" \
               f"Average Temperature: {self.avg_temperature}\n" \
               f"Color: {self.color}"

    def move(self) -> tuple:
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        tup = (x, y)
        return tup

    def get_name(self) -> str:
        return self.name

    def distanceToTheSun(self):
        return self.avg_dist_from_sun


