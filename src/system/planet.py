import math


class Planet(object):

    def __init__(self, v: dict):
        self.name = v['name']
        self.avg_dist_from_sun = v['avg_dist_from_sun']
        self.aphelion = v['aphelion']
        self.perihelion = v['perihelion']
        self.orbital_period = v['orbital_period']
        self.number_of_moons = v['number_of_moons']
        self.self_loop = v['self_loop']
        self.avg_temperature = v['avg_temperature']
        self.color = v['color']
        self.radius = v['radius']
        self.angle = v['angle']
        self.following_star = v['following_star']
        self.factor = v['factor']
        self.image = v['image']
        self.velocity = v['velocity']
        self.mu = v['mu']

    def move(self) -> tuple:
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        tup = (x, y)
        return tup

    def get_name(self) -> str:
        return self.name

    def distanceToTheSun(self):
        return self.avg_dist_from_sun
