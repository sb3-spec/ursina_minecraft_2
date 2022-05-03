from re import S, U
from perlin_noise import PerlinNoise
from ursina import Entity, load_model, load_texture, Mesh, Vec3, Vec2
from math import floor


class MeshTerrain:
    def __init__(self):
        self.subsets = []
        self.num_subsets = 1
        self.subwidth = 32
        self.block = load_model('block.obj')
        self.textureAtlas = load_texture('texture_atlas_3.png')
        self.perlin_noise = PerlinNoise(octaves=2, seed=20)
        self.freq = 100
        self.amp = 20
        
        for i in range(self.num_subsets):
            e = Entity(model=Mesh(), texture="white_cube")
            e.texture_scale *= 64 / e.texture.width
            self.subsets.append(e)



    def genBlock(self, x, y, z):
        # Extend or add to the vertices of our model
        model = self.subsets[0].model
        
        model.vertices.extend([ Vec3(x, y, z) + v for v in self.block.vertices])
        
        
        # coordinates for grass in the texture atlas
        uu = 8
        uv = 7
        model.uvs.extend([Vec2(uu, uv) + u for u in self.block.uvs])
        
        model.generate()
        
    def genTerrain(self):
        x = 0
        
        z = 0

        for i in range(self.subwidth * self.subwidth):
            x = floor(i / self.subwidth)
            z = floor(i % self.subwidth)
            y = floor(self.perlin_noise([x/self.freq, z/self.freq]) * self.amp)
            self.genBlock(x, y, z)
    
        