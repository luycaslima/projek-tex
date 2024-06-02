#version 330 

layout(location = 0) in vec3 vertexPosition;
layout (location = 1) in vec2 vertexTexCoord;
layout(location = 2) in vec3 vertexNormal;

uniform mat4 mvp; //model view projection -> default of raylib
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform vec3 projPosition;

out vec2 fragTexCoord;
out vec3 fragPosition;
out vec3 fragNormal;
out vec3 projDirection;


void main(){
    vec4 worldPosition =  modelMatrix * vec4(vertexPosition,1.0);
    projDirection = normalize(projPosition - worldPosition.xyz); //This is for do the dot product in frag shader

    
    vec4 projectorCoords = projectionMatrix * viewMatrix * worldPosition;
    gl_Position = mvp * vec4(vertexPosition,1.0);

    fragPosition = vertexPosition;
    fragNormal = vertexNormal;

    //to not project behind
    float w = max(projectorCoords.w,.0);
    
    //map from [-1,1 ] to [0,1]
    vec2 uv = (projectorCoords.xy/ w) * 0.5 + 0.5;
    uv.y = -uv.y; // should invert because of opengl (left bottom origin whili raylib is top lef)
    fragTexCoord = uv;
}