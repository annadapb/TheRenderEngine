from abc import ABC, abstractmethod
from utils import Ray, Color, Vec3, Vec3n, Mat4, dot
import numpy

class Object(ABC):
    ''' The abstract base class of Object that all inherited class should
    implement.
    '''

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
    def __init__(self, center: Vec3, radius=1.,):
        ''' The Sphere constructior.
        @param center The center position of the sphere in the scene.
        @param radius The radius of the sphere.
        '''
        ## The center position of the sphere in the scene
        self.center = center
        ## The radius of the sphere
        self.radius = radius

    def hit(ray: Ray, center: Vec3, radius) -> float:
        '''Determines the intersection point of a ray with a sphere.
        @param ray: Ray
            The ray to check for intersection, defined by an origin and direction.
        @param center: Vec3
            The center of the sphere.
        @param radius: float
            The radius of the sphere.
        @return: float
            The distance from the ray's origin to the intersection point along the ray's direction.
            Returns -1.0 if there is no intersection.
        '''
        oc = center - ray.origin
        a = dot(ray.dir, ray.dir)
        b = dot(ray.dir, oc)
        c = dot(oc, oc) - (radius * radius)
        disc = (b * b) - (a * c)

        if disc < 0:
            return -1.0
        
        return (-b - numpy.sqrt(disc)) / a
        
