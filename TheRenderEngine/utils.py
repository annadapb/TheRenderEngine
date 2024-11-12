class Vec3:
    ''' The class to store 3D vectors. '''
    def __init__(self, x: float, y:float, z:float):
        ''' The vector constructor. Use * to expand pass a list.
        @param x The x component
        @param y The y component
        @param z The z component
        '''
        pass

    def norm(self,) -> float:
        ''' Returns the norm (length of the vector) without changing the vector.
        @return The norm (length) of the vector.
        '''
        pass

    def norm_(self,) -> float:
        ''' Returns the norm (length of the vector) while also normalizing it.
        @return The norm (length) of the vector.
        '''
        pass

class Mat4:
    ''' The class to store a 4x4 transformation matrix '''


class Color:
    ''' A color object that stores a color '''

class Ray:
    ''' A single ray object that has a origin and direction '''
    def __init__(self, origin: Vec3, dir: Vec3n):
        ''' The ray constructor.
        @param origin The origin of the ray
        @param dir The direction towards which the Ray points at.
        '''
        ## The origin of the ray
        self.origin = origin
        ## The direction towards which the Ray points at.
        self.dir = dir

    def at(self, t):
        ''' Compute the location the ray is at after time t.
        @param t The time elapsed.
        @return The location of the ray.
        '''
        return self.origin + self.dir * t

