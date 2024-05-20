from pyray import *
from numpy import deg2rad
class Program:
    
    def __init__(self):
        self._is_running = False
        self.camera = Camera3D([0,2,10],[0,0,0],[0,1,0],45.0,CameraProjection.CAMERA_PERSPECTIVE)
    
    def start(self):
        init_window(800, 450, "EYEJKTOR")
        set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)
        set_target_fps(60)
        disable_cursor()
        
        self._is_running = True
        
        self.model = Model
        self.texture = Texture2D
        self.shader = Shader
        
        self.projector_position  = [4.0,4.0,4.0]
        self.projector_target = [0,0,0]
        self.projector_up = [0,1,0]

        self._open_files()
        self._set_shader()

    def _open_files(self):
        self.model = load_model("assets/models/model_test.glb")
        self.shader = load_shader("assets/shaders/projection.vs","assets/shaders/projection.fs")
        self.texture= load_texture("assets/textures/red.png")
        
    def _set_shader(self):

        self.shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_MODEL] = get_shader_location(self.shader,"modelMatrix")
        #self.shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_VIEW] = get_shader_location(self.shader,"viewMatrixCamera")
        #self.shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_PROJECTION] = get_shader_location(self.shader,"projectionMatrixCamera")

        self.projector_view_loc = get_shader_location(self.shader,"projectorViewMatrix")
        self.projector_projection_loc = get_shader_location(self.shader,"projectorProjMatrix")
      
        #set texture
        set_shader_value_texture(self.shader, get_shader_location(self.shader,"projectedTexture"),self.texture)


    def loop(self):
        while(self._is_running):
            self._input()
            self._update()
            self._render()
    
    def close_and_cleanup(self):
        unload_model(self.model)
        unload_shader(self.shader)
        unload_texture(self.texture)
        close_window()

    def _input(self):
        pass

    def _update(self):
        self._is_running = not window_should_close()
        update_camera(self.camera,CameraMode.CAMERA_FREE)

        self.projector_view_matrix = matrix_look_at(self.projector_position,self.projector_target,self.projector_up)
        self.projector_projection_matrix = matrix_perspective(deg2rad(45.0), 800.0/450.0, 0.1, 1000.0)
        
        set_shader_value_matrix(self.shader, self.projector_view_loc, self.projector_view_matrix)
        set_shader_value_matrix(self.shader,self.projector_projection_loc,self.projector_projection_matrix)



    def _render(self):
        begin_drawing()
        clear_background(WHITE)

        begin_mode_3d(self.camera)

        self.model.materials[0].shader = self.shader

        draw_model(self.model,[0,0,0],1,WHITE)
       
        draw_grid(20,1.0)
        end_mode_3d()
       
        draw_fps(10,10)
        end_drawing()
        
