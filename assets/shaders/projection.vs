#version 330 

layout(location = 0) in vec3 vertexPosition;
layout (location = 1) in vec2 vertexTexCoord;

uniform mat4 mvp; //model view projection -> default of raylib
uniform mat4 matModel;

uniform mat4 projectorViewMatrix;
uniform mat4 projectorProjMatrix;

out vec2 fragTexCoord;
 
void main(){

    //fragTexCoord = model * vec4(vertexPosition,1.0);
    //fragTexCoord = vertexTexCoord;
    gl_Position = mvp * vec4(vertexPosition, 1.0);

    vec4 projectorCoords = projectorProjMatrix * projectorViewMatrix * matModel * vec4(vertexPosition,1.0);
    //to no project behind
    float w = max(projectorCoords.w,0.0);
    //map from [-1,1 ] to [0,1]
    vec2 uv = (projectorCoords.xy/ w) * 0.5 + 0.5;
    fragTexCoord = uv;

    //vTexCoords = projectionMatrixCamera * viewMatrixCamera * modelMatrix * vec4(position,1.0); 
    
}