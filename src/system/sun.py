class TheSun(object):

    def __init__(self):
        self.name = 'sun'
        self.distance_from_earth = 149597887
        self.speed_central_galaxy_km_in_second = 217
        self.self_loop = 25
        self.temperature = 5511
        self.color = 'red'
        self.image = "GUI/media/sun.gif"

    def __str__(self):
        return f"!~!~!~!~!~ {self.name.title()} !~!~!~!~!~\n" \
               f"Distance from Earth: {self.distance_from_earth}\n" \
               f"Speed Central Galaxy (Km in Seconds): {self.speed_central_galaxy_km_in_second}\n" \
               f"Self Loop (in hours): {self.self_loop}\n" \
               f"Temperature: {self.temperature}\n" \
               f"Color: {self.color}"
