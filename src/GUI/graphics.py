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
        venus.color('purple')
        venus.penup()

        earth = turtle.Turtle()
        earth.shape('circle')
        earth.shapesize(2,2)
        earth.write("earth")
        earth.color('blue')
        earth.penup()

        mars = turtle.Turtle()
        mars.shape('circle')
        mars.write("mars")
        mars.color('red')
        mars.penup()

        turtles = {'mercury': mercury, 'venus': venus, 'earth': earth, 'mars': mars}
        self.start_animation(turtles)



    def start_animation(self, turtles):

        win = turtle.Screen()
        win.bgpic('GUI/media/background.gif')
        win.setup(800, 800)
        win.tracer(0)

        sun = turtle.Turtle()
        sun.color('black')
        sun.shape('circle')
        sun.shapesize(5, 5)
        sun.color('yellow')

        moon = turtle.Turtle()
        moon.color('white')
        moon.shape('circle')
        moon.color('gray')
        moon.penup()

        angle_moon = 0
        radius_moon = 40

        while(True):
            win.update()
            for planet in self.system.get_planets().values():
                pair = planet.move()
                if(planet.get_name() in turtles.keys()):
                    turtles[planet.name].goto(sun.xcor()+pair[0], sun.ycor()+pair[1])
                    planet.angle += planet.factor
                    turtles[planet.name].pendown()

            angle_moon += 0.06

            x = radius_moon * math.cos(angle_moon)
            y = radius_moon * math.sin(angle_moon)
            moon.goto(turtles['earth'].xcor()+x, turtles['earth'].ycor()+y)
            time.sleep(0.02)





