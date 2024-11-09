class World:
    '''The World encompasses the entire scene, including all the
    object such as mesh, lights, and essentially contain atleast one
    camera. Without a camera, the scene cannot be rendered.
    '''

    def __init__(self,):
        '''! The constructor. Create a empty World. Pre-populated world
        is not supported.
        '''

        ## Contains all the meshes present in the scene.
        self._meshes = list()
        ## Contains all the lights present in the scene.
        self._lights = list()
        ## Contains all the cameras present in the scene.
        self._cameras = list()

    def __repr__(self,):
        ''' Return info about the current scene. '''
        return "Not supported yet."
        # TODO H: Return string of all the lights camera and meshes in
        # current scene.

    def add_mesh(self, mesh):
        '''! Adds a mesh to the world.
         @param mesh The mesh to be added.
         @return Nothing is returned.
        '''
        pass
        # TODO H: Create a Mesh class.
        # TODO A: Check if the input is a Mesh and add it to self._meshes

    def add_light(self, light):
        '''! Adds a light to the world.
        @param light The light to be added.
        @return Nothing is returned.
        '''
        pass
        # TODO H: Create a Light class.
        # TODO A: Check if the input is a Light and add it to self._lights
 
    def add_camera(self, camera):
        '''! Adds a Camera to the world.
        @param camera The camera to be added.
        @return Nothing is returned.
        '''
        pass
        # TODO A: Create a Camera class.
        # TODO H: Check if the input is a Camera and add it to self._cameras

    def render(self, camera_idx=0):
        '''! Renders the current scene
        @param camera_idx The index of the camera which should be used to render
        the scene. Defaults to the first camera added to the scene.
        @return Nothing. The result of the renderer is present in the
        camera film.
        '''
        pass

