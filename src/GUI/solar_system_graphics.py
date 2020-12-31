from src.system.planet import Planet
import turtle
import time
import math

from src.system.solar_system import SolarSystem


class SolarSystemGraphics(object):

    def __init__(self, sys: SolarSystem):
        self.system = sys
        self.planets = sys.get_planets()
        self.init_animation()

    def init_animation(self):
        screen = turtle.Screen()
        screen.title("Solar System")
        screen.setup(1000, 1000)
        screen.bgpic('GUI/media/background.gif')
        turtles = {}

        mercury = turtle.Turtle()
        screen.addshape(self.planets['mercury'].image)
        mercury.color('white')
        mercury.penup()
        mercury.shape(self.planets['mercury'].image)
        turtles['mercury'] = mercury

        venus = turtle.Turtle()
        screen.addshape(self.planets['venus'].image)
        venus.color('white')
        venus.penup()
        venus.shape(self.planets['venus'].image)
        turtles['venus'] = venus

        earth = turtle.Turtle()
        screen.addshape(self.planets['earth'].image)
        earth.color('white')
        earth.penup()
        earth.shape(self.planets['earth'].image)
        turtles['earth'] = earth

        mars = turtle.Turtle()
        screen.addshape(self.planets['mars'].image)
        mars.color('white')
        mars.penup()
        mars.shape(self.planets['mars'].image)
        turtles['mars'] = mars

        jupiter = turtle.Turtle()
        screen.addshape(self.planets['jupiter'].image)
        jupiter.color('white')
        jupiter.penup()
        jupiter.shape(self.planets['jupiter'].image)
        turtles['jupiter'] = jupiter

        saturn = turtle.Turtle()
        screen.addshape(self.planets['saturn'].image)
        saturn.color('white')
        saturn.penup()
        saturn.shape(self.planets['saturn'].image)
        turtles['saturn'] = saturn

        uranus = turtle.Turtle()
        screen.addshape(self.planets['uranus'].image)
        uranus.color('white')
        uranus.penup()
        uranus.shape(self.planets['uranus'].image)
        turtles['uranus'] = uranus

        neptune = turtle.Turtle()
        screen.addshape(self.planets['neptune'].image)
        neptune.color('white')
        neptune.penup()
        neptune.shape(self.planets['neptune'].image)
        turtles['neptune'] = neptune

        self.start_animation(turtles, screen)

    def start_animation(self, turtles, screen: turtle):
        sun = turtle.Turtle()
        screen.addshape("GUI/media/sun.gif")
        screen.addshape("GUI/media/moon.gif")
        sun.shape("GUI/media/sun.gif")

        moon = turtle.Turtle()
        moon.shape("GUI/media/moon.gif")
        moon.penup()

        angle_moon = 0
        radius_moon = 20

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

