from constants import *
from primitives import Object

class Film:
    ''' The film stores the image after it has been rendered.
    '''
class Mesh:
    ''' The meshes in the scene. '''
class Light:
    ''' The lights in the scene. '''
class Camera:
    '''
    The Camera is when added to a scene makes it renderable. Without a Camera
    a scene cannot be rendered.
    '''

    def __init__(self, position, direction, film: Film,
    up=[0, 1, 0], projection=PERSPECTIVE, clip_start=.1, clip_end=100):
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
        pass
        # TODO H: Create internal variables for the above parameters so that we
        # can use it.
    def __repr__(self,):
        ''' Returns a representation of the camera.'''
        pass
        # TODO H: Add the camera's info string.

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
        # TODO H: Create a Light class.
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

