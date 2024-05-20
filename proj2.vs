#version 330 

layout(location = 0) in vec3 vertexPosition;
layout(location = 1) in vec3 vertexNormal;
layout(location = 2) in vec3 vertexTexCoord;


uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
uniform mat4 textureMatrix;

out vec4 fragTexCoord;

void main(){
    vec4 worldPosition = model * vec4(vertexPosition,1.0);

    gl_Position = projection * view * model * vec4(vertexPosition, 1.0);
    //gl_Position = projection * view * worldPosition;
    fragTexCoord = textureMatrix * worldPosition;
}