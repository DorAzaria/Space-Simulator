from src.system.hohmann_transfer_orbit import HohmannTransferOrbit
import matplotlib
import matplotlib.animation as animation
import numpy

class TravelToMarsGraphics(object):

    def __init__(self, hohmann: HohmannTransferOrbit):
        self.hohmann_transfer_orbit = hohmann
        self.mission = hohmann.mission
        self.spacecraft = hohmann.spacecraft
