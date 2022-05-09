from perlin_noise import PerlinNoise
from math import floor

class Perlin:
    def __init__(self):
        
        
        self.octaves = 3
        self.seed = 15
        self.amp = 15
        self.freq = 64
        
        self.noise_gen = PerlinNoise(octaves=self.octaves, seed=self.seed)
    
    def get_height(self, x, z):
        return floor(self.noise_gen([x/self.freq, z/self.freq]) * self.amp)