from src.system.planet import Planet
import turtle
import time
import math

from src.system.solar_system import SolarSystem


class Graphics(object):

    def __init__(self, sys: SolarSystem):
        self.system = sys
        self.planets = sys.get_planets()
        self.init_animation()

    def init_animation(self):
        mercury = turtle.Turtle()
        mercury.shape('circle')
        mercury.write("mercury")
        mercury.color('white')
        mercury.penup()

        venus = turtle.Turtle()
        venus.shape('circle')
        venus.write("venus")
        venus.color('white')
        venus.penup()

        earth = turtle.Turtle()
        earth.shape('circle')
        earth.shapesize(2, 2)
        earth.write("earth")
        earth.color('white')
        earth.penup()

        mars = turtle.Turtle()
        mars.shape('circle')
        mars.write("mars")
        mars.color('white')
        mars.penup()

        turtles = {'mercury': mercury, 'venus': venus, 'earth': earth, 'mars': mars}
        self.start_animation(turtles)

    def start_animation(self, turtles):

        screen = turtle.Screen()
        screen.title("Solar System")
        screen.setup(800, 800)
        screen.bgpic('GUI/media/background.gif')

        sun = turtle.Turtle()
        screen.addshape("GUI/media/sun.gif")
        screen.addshape("GUI/media/earth.gif")
        screen.addshape("GUI/media/mars.gif")
        screen.addshape("GUI/media/venus.gif")
        screen.addshape("GUI/media/mercury.gif")
        screen.addshape("GUI/media/moon.gif")
        sun.shape("GUI/media/sun.gif")
        turtles['earth'].shape("GUI/media/earth.gif")
        turtles['mars'].shape("GUI/media/mars.gif")
        turtles['venus'].shape("GUI/media/venus.gif")
        turtles['mercury'].shape("GUI/media/mercury.gif")

        moon = turtle.Turtle()
        moon.shape("GUI/media/moon.gif")
        moon.penup()

        angle_moon = 0
        radius_moon = 40

        while (True):
            screen.update()
            for planet in self.system.get_planets().values():
                pair = planet.move()
                if (planet.get_name() in turtles.keys()):
                    turtles[planet.name].goto(sun.xcor() + pair[0], sun.ycor() + pair[1])
                    planet.angle += planet.factor
                    turtles[planet.name].pendown()

            angle_moon += 0.06

            x = radius_moon * math.cos(angle_moon)
            y = radius_moon * math.sin(angle_moon)
            moon.goto(turtles['earth'].xcor() + x, turtles['earth'].ycor() + y)
            time.sleep(0.01)
