from abc import ABC, abstractmethod
from utils import Ray, Color

class Object(ABC):
    @abstractmethod
    def hit(self, ray: Ray) -> Tuple[bool, float, Color]:
        ''' All objects should provide a hit function. Currently the
        hit method only returns if a ray is hit, the distance hit from
        the ray origin and the color.
        @param ray The ray that hits.
        @return A tuple of bool (if ray hits), float (how far from the
        ray origin did the object hit), and Color (what is the color
        emitted from the surface).
        '''
        pass

class Sphere(Object):
    ''' The Sphere primitive that can be added to the scene. '''
