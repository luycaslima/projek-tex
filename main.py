# import eyejktor as ejk


# def main():
#     p = ejk.Program()
#     p.start()
#     p.loop()
#     p.close_and_cleanup()


# if __name__ == "__main__":
#     main()



from pyray import *
from numpy import  deg2rad, radians

init_window(800, 600, "EYEJKTOR")
set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)
set_target_fps(60)
disable_cursor()


camera = Camera3D([0,2,10],[0,0,0],[0,1,0],45.0,CameraProjection.CAMERA_PERSPECTIVE)


model = load_model("assets/models/model_test.glb")
texture = load_texture("assets/textures/05.png")
shader = load_shader("assets/shaders/projection.vs","assets/shaders/projection.fs")

#model_loc = get_shader_location(shader, "matModel")

texture_loc = get_shader_location(shader,"texture1")
#shader.locs[ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD01] = texture_loc
#set_shader_value(shader,texture_loc,bytes(0),ShaderUniformDataType.SHADER_UNIFORM_INT)

set_shader_value_texture(shader,texture_loc,texture)

#projector 
proj_position = [2.0,4.0,2.0]
proj_target = [0.0,0.0,0.0]
up_vector = [0.0,1.0,0.0]

proj_view = matrix_look_at(proj_position,proj_target,up_vector)
proj_projection = matrix_perspective(deg2rad(45), 800.0/600.0,0.1,100.0)

projector_view_loc = get_shader_location(shader,"projectorViewMatrix") 
projector_proj_loc = get_shader_location(shader,"projectorProjMatrix") 

#texture_matrix_projection = matrix_multiply(proj_projection,proj_view)
#texture_matrix_loc = get_shader_location(shader,"textureMatrix")

for i in range(model.materialCount):
    model.materials[i].shader = shader

mat_model = matrix_identity()

while not window_should_close():
    update_camera(camera,CameraMode.CAMERA_FREE)

    #set_shader_value_matrix(shader, model_loc, mat_model)

    #set_shader_value_matrix(shader, view_loc, mat_view)
    #set_shader_value_matrix(shader, projection_loc, mat_projection)
    
    set_shader_value_matrix(shader,projector_view_loc,proj_view)
    set_shader_value_matrix(shader,projector_proj_loc,proj_projection)

    #set_shader_value_matrix(shader,texture_matrix_loc,texture_matrix_projection)
    
    begin_drawing()
    clear_background(WHITE)

    begin_mode_3d(camera)

    draw_model(model,[0,0,0],1.0,WHITE)
    draw_grid(20,1)

    end_mode_3d()
    end_drawing()

unload_shader(shader)
unload_texture(texture)
unload_model(model)
close_window()