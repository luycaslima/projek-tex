#version 330 

layout(location = 0) in vec3 vertexPosition;
layout (location = 1) in vec2 vertexTexCoord;

//uniform mat4 mvp; //model view projection -> default of raylib

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec2 fragTexCoord;
out vec3 fragPosition;
//out vec2 fragTexCoord;


void main(){

    vec4 projectorCoords = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition,1.0);
    fragPosition = vertexPosition;
    gl_Position = projectorCoords;

    /*
        // this makes sure we don't render the texture also on the back of the object
        vec3 projectorDirection = normalize(projPosition - vWorldPosition.xyz);
        float dotProduct = dot(vNormal, projectorDirection);
        if (dotProduct < 0.0) {
        outColor = vec4(color, 1.0);
        }
    */

    //to no project behind
    float w = max(projectorCoords.w,.0);
    //map from [-1,1 ] to [0,1]
    vec2 uv = (projectorCoords.xy/ w) * 0.5 + 0.5;
    fragTexCoord = uv;

    //vTexCoords = projectionMatrixCamera * viewMatrixCamera * modelMatrix * vec4(position,1.0); 
    
}