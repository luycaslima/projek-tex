import ctypes
from pyray import *
from numpy import  deg2rad

# Initialization
screen_width = 800
screen_height = 600

init_window(screen_width, screen_height, "ProjekTEX")
set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)
set_target_fps(60)
disable_cursor()


# Define the camera to look into our 3d world
camera = Camera3D([4,4,4],[0,0,0],[0,1,0],45.0,CameraProjection.CAMERA_PERSPECTIVE)

# Load texture and shader
texture = load_texture("assets/textures/icon_ferrucio.png")
model = load_model("assets/models/jester_cat.glb")
shader = load_shader("assets/shaders/projection.vs", "assets/shaders/projection.fs")
set_texture_wrap(texture, TextureWrap.TEXTURE_WRAP_CLAMP) #to not repeat

for i in range(model.materialCount):
    model.materials[i].shader = shader

# Get the location of the shader uniforms
model_loc = get_shader_location(model.materials[0].shader, "modelMatrix")
view_loc = get_shader_location(model.materials[0].shader, "viewMatrix")

projector_pos_loc = get_shader_location(model.materials[0].shader, "projPosition")

projection_loc = get_shader_location(model.materials[0].shader, "projectionMatrix")
proj_texture_loc = get_shader_location(model.materials[0].shader, "projTexture")

# Set the texture to the shader
for i in range(model.materialCount):
    #Need this to use custom values on the shader (how to use custom texture paths?)
    model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MAP_ALBEDO] = get_shader_location(model.materials[0].shader, "projTexture")
    #TODO TO PROJECTO FROM THE CAMERA OF THE USER, NEED TO SETUP THIS
    #model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_PROJECTION] = get_shader_location(model.materials[0].shader, "projectionMatrix")
    #model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_VIEW] = get_shader_location(model.materials[0].shader, "viewMatrix")
    #model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_MODEL] = get_shader_location(model.materials[0].shader, "modelMatrix")
    model.materials[i].maps[MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = texture # Set model diffuse texture (IMPORTANT FOR THE SHADER)

#set_shader_value_texture(shader,proj_texture_loc,texture)

#projector  (can be also a 3D camera)
proj_position = [2.0,3.0,2]
#TODO how can i buffer data to the c framework
# proj_pos_array = (ctypes.c_float * len(proj_position))(*proj_position)
# # Convert the ctypes array to a pointer
# proj_position_ptr = ctypes.pointer(proj_pos_array)

proj_target = [0.0,1.0,0.0]
up_vector = [0.0,1.0,0.0]

proj_view = matrix_look_at(proj_position,proj_target,up_vector)
#TODO should it be the size of the image? #the fovy define how big
proj_projection = matrix_perspective(deg2rad(10),256.0/256.0,0.1,100.0) 

#TODO use depth mask for checking where the texture should render?
#rl_enable_depth_test()

# Detect window close button or ESC key
while not window_should_close(): 
    # Update camera
    update_camera(camera, CameraMode.CAMERA_FREE)

    # Draw
    begin_drawing()
    clear_background(RAYWHITE)

    begin_mode_3d(camera)
    
    #set_shader_value_v(model.materials[0].shader,projector_pos_loc,bytes(proj_position_ptr),ShaderUniformDataType.SHADER_UNIFORM_VEC3,0)
    set_shader_value_matrix(model.materials[0].shader, model_loc, matrix_identity())
    set_shader_value_matrix(model.materials[0].shader, view_loc, proj_view)
    set_shader_value_matrix(model.materials[0].shader, projection_loc, proj_projection)
    
    # Draw objects with the shader
    draw_cube_wires(proj_position,.2,.2,.2,RED)
    draw_model(model,[0,1,0],1,WHITE)
    
    draw_grid(10, 1.0)

    end_mode_3d()
    #draw_texture(texture,400,300,(255,255,255,125))

    end_drawing()

# Unload resources
unload_shader(shader)  # Unload shader
unload_texture(texture)  # Unload texture
unload_model(model)
close_window()  # Close window
