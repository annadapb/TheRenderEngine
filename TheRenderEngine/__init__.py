from constants import *
from primitives import Object
import numpy
from utils import Vec3

class Film:
    ''' The film stores the image after it has been rendered.
    '''
class Mesh:
    ''' The meshes in the scene. '''
class Light:
    ''' The lights in the scene. '''

    def __init__(self, position: Vec3, color=Vec3(1.0, 1.0, 1.0), intensity=1.0, light_type=POINT):
        '''The Light constuctor. Creates a new POINT light by default.
        @param position The position of the light source in the World.
        @param color Vec3 (r, g, b) for the light color (default: white).
        @param intensity The brightness of the light (default: 1.0).
        @param light_type The type of light, can be either `POINT` or other. Defaults to `POINT`
        '''
        self.position = position
        self.color = color
        self.intensity = intensity
        self.light_type = light_type

    def set_position(self, position: Vec3):
        '''Set the position of the light.
        @param position The position of the light source'''
        self.position = position

    def set_color(self, color: Vec3):
        '''Set the color of the light.
        @param color Vec3 (r, g, b) for the light color'''
        self.color = color

    def set_intensity(self, intensity: float):
        '''Set the intensity of the light.
        @param intensity The brightness of the light'''
        self.intensity = intensity

    def __repr__(self):
        '''Return a representation of the light.'''
        return (
            f"Light(type={self.light_type}, "
            f"position={self.position}, "
            f"color={self.color}, "
            f"intensity={self.intensity})"
        )

class Camera:
    '''
    The Camera is when added to a scene makes it renderable. Without a Camera
    a scene cannot be rendered.
    '''

    def __init__(self, position, direction, film: Film,
    up=numpy.array([0, 1, 0]), projection=PERSPECTIVE, clip_start=.1, clip_end=100):
        '''The Camera constuctor. Creates a new camera.
        @param position The position of the camera in the World.
        @param direction The direction the camera is pointing at.
        @param film The camera's film which will store the image.
        @param up The up-axis of the camera. Defaults to Y-up, i.e, [0, 1, 0]. No
        matter the values, the vector will be normalized before it is used.
        @param projection The camera's projection, can be either `PERSPECTIVE` or `ORTHOGRAPHIC`. Defaults to `PERSPECTIVE`
        @param clip_start The nearest cliping distance.
        @param clip_end The nearest cliping distance.
        '''
        ## The position of the camera in the World.
        self.position = position
        ## The direction the camera is pointing at.
        self.direction = direction
        ## The camera's film which will store the image.
        self.film = film
        
        norm = numpy.linalg.norm(up)
        if norm != 0:	# avoid division by zero
            ## The up-axis of the camera. Defaults to Y-up, i.e, [0, 1, 0].
            self.up = up / norm
        else:
            ## The up-axis of the camera. Defaults to Y-up, i.e, [0, 1, 0].
            self.up = up

        ## The camera's projection, can be either `PERSPECTIVE` or `ORTHOGRAPHIC`. Defaults to `PERSPECTIVE`
        self.projection = projection
        ## The nearest cliping distance.
        self.clip_start = clip_start
        ## The nearest cliping distance.
        self.clip_end = clip_end

    def __repr__(self,):
        ''' Returns a representation of the camera.'''
        return (
            f"Camera(position={self.position}, "
            f"direction={self.direction}, "
            f"film={self.film}, "
            f"up={self.up}, "
            f"projection={self.projection}, "
            f"clip_start={self.clip_start}, "
            f"clip_end={self.clip_end})"
        )

    def _render(self, world):
        ''' The main rendering takes place here and the result is stored
        in the film
        '''
        pass
    
class World:
    '''The World encompasses the entire scene, including all the
    object such as objects, lights, and essentially contain atleast one
    camera. Without a camera, the scene cannot be rendered.
    '''

    def __init__(self,):
        '''! The constructor. Create a empty World. Pre-populated world
        is not supported.
        '''

        ## Contains all the objects present in the scene.
        self._objects= dict()
        ## Contains all the lights present in the scene.
        self._lights = dict()
        ## Contains all the cameras present in the scene.
        self._cameras = dict()

    def __repr__(self,):
        ''' Return info about the current scene. '''
        return "Not supported yet."
        # TODO H: Return string of all the lights camera and objects in
        # current scene.

    def add_object(self, obj: Object):
        '''! Adds a objects to the world.
         @param obj The object to be added.
         @return Nothing is returned.
        '''
        pass
        # TODO A: Check if the input is a Object and add it to self._objects

    def add_light(self, light: Light):
        '''! Adds a light to the world.
        @param light The light to be added.
        @return Nothing is returned.
        '''
        pass
        # TODO A: Check if the input is a Light and add it to self._lights
 
    def add_camera(self, camera: Camera):
        '''! Adds a Camera to the world.
        @param camera The camera to be added.
        @return Nothing is returned.
        '''
        pass
        # TODO A: Create a Camera class.
        # TODO H: Check if the input is a Camera and add it to self._cameras

    def render(self, camera:Camera='main'):
        '''! Renders the current scene
        @param camera The index of the camera which should be used to render
        the scene. Defaults to the 'main' camera added to the scene. Returns
        an error is there is no 'main' camera in the scene.
        @return Nothing. The result of the renderer is present in the
        camera film.
        '''
        pass
