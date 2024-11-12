from abc import ABC, abstractmethod
from utils import Ray, Color, Vec3, Vec3n, Mat4

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

    @abstractmethod
    def scale(self, factor: Vec3):
        '''
        Scale the object by the given scale factor
        @param factor The factor by which the object is to be scaled
        '''
        pass

    @abstractmethod
    def rotate(self, axis: Vec3n, angle: Vec3):
        '''
        Rotates the current object by an angle about the given axis
        Reference: https://danceswithcode.net/engineeringnotes/quaternions/quaternions.html
        @param axis The axis around which the object should be rotated
        @param angle The x, y and z co-ordinates represents the angle about
        which the object should be rotated.
        '''
        pass

    @abstractmethod
    def translate(self, shift: Vec3):
        '''
        Shifts the object by a given shift value.
        @param shift The distance by which the object moves.
        '''
        pass

    @abstractmethod
    def transform(self, matrix: Mat4):
        '''
        Apply an arbitrary matrix transformation. The matrix is not checked
        if it is positive semidefinite (PSD), and hence if the matrix is not
        PSD, this transformation will quit without warning
        @param matrix The transformation matrix
        '''
        pass

class Sphere(Object):
    ''' The Sphere primitive that can be added to the scene. '''
    def __init__(self, radius=1.,):
        ''' The Sphere constructior.
        @param radius The radius of the sphere.
        @param position The location of the sphere.
        '''
        pass

        ''' TODO H: write all the functions that the Object base class requires '''
