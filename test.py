from pyray import *
from numpy import  deg2rad

# Initialization
screen_width = 800
screen_height = 600

init_window(screen_width, screen_height, "pyray [shaders] example - projection texturing")
set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)
set_target_fps(60)
disable_cursor()

# Define the camera to look into our 3d world
camera = Camera3D([4,4,4],[0,0,0],[0,1,0],45.0,CameraProjection.CAMERA_PERSPECTIVE)

# Load texture and shader
texture = load_texture("assets/textures/icon_ferrucio.png")
model = load_model("assets/models/jester_cat.glb")
shader = load_shader("assets/shaders/projection.vs", "assets/shaders/projection.fs")


for i in range(model.materialCount):
    model.materials[i].shader = shader

# Get the location of the shader uniforms
model_loc = get_shader_location(model.materials[0].shader, "modelMatrix")
view_loc = get_shader_location(model.materials[0].shader, "viewMatrix")
projector_pos_loc = get_shader_location(model.materials[0].shader, "projPosition")
projection_loc = get_shader_location(model.materials[0].shader, "projectionMatrix")
proj_texture_loc = get_shader_location(model.materials[0].shader, "projTexture")

# Set the texture to the shader
#set_shader_value(shader,proj_texture_loc,bytes(1),ShaderUniformDataType.SHADER_UNIFORM_INT)
#shader.locs[ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD01] = proj_texture_loc
for i in range(model.materialCount):
    #Need this to use custom values on the shader
    model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MAP_ALBEDO] = get_shader_location(model.materials[0].shader, "projTexture")
    #TODO TO PROJECTO FROM THE CAMERA OF THE USER, NEED TO SETUP THIS
    #model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_PROJECTION] = get_shader_location(model.materials[0].shader, "projectionMatrix")
    #model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_VIEW] = get_shader_location(model.materials[0].shader, "viewMatrix")
    #model.materials[i].shader.locs[ShaderLocationIndex.SHADER_LOC_MATRIX_MODEL] = get_shader_location(model.materials[0].shader, "modelMatrix")

    model.materials[i].maps[MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = texture # Set model diffuse texture (IMPORTANT FOR THE SHADER)


# for i in range(model.materialCount):
#     model.materials[i].shader = shader

#set_shader_value_texture(shader,proj_texture_loc,texture)

#projector 
proj_position = [2.0,3.0,2]
proj_target = [0.0,1.0,0.0]
up_vector = [0.0,1.0,0.0]

proj_view = matrix_look_at(proj_position,proj_target,up_vector)
proj_projection = matrix_perspective(deg2rad(10),256.0/256.0,0.1,100.0) #TODO should it be the size of the image? #the fovy define how big


# Main game loop
while not window_should_close():  # Detect window close button or ESC key
    # Update camera
    update_camera(camera, CameraMode.CAMERA_FREE)

    # Draw
    begin_drawing()
    clear_background(RAYWHITE)

    begin_mode_3d(camera)
    

    #set_shader_value_v(model.materials[0].shader,projector_pos_loc,proj_projection,ShaderUniformDataType.SHADER_UNIFORM_VEC3,0)
    set_shader_value_matrix(model.materials[0].shader, model_loc, matrix_identity())
    set_shader_value_matrix(model.materials[0].shader, view_loc, proj_view)
    set_shader_value_matrix(model.materials[0].shader, projection_loc, proj_projection)
    
    # Draw objects with the shader
    # Use shader
    #[begin_shader_mode(shader)
    draw_cube_wires(proj_position,.2,.2,.2,RED)
    draw_model(model,[0,1,0],1,WHITE)
    #end_shader_mode()
    #draw_cube_wires(Vector3(0.0, 1.0, 0.0), 2.0, 2.0, 2.0, BLACK)
    draw_grid(10, 1.0)

    end_mode_3d()
    #draw_texture(texture,400,300,(255,255,255,125))
    draw_text("Move with keys: W, A, S, D", 10, 40, 20, DARKGRAY)

    end_drawing()

# Unload resources
unload_shader(shader)  # Unload shader
unload_texture(texture)  # Unload texture
unload_model(model)
close_window()  # Close window and OpenGL context
