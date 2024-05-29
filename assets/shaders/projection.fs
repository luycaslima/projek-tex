#version 330 

out vec4 finalColor;

in vec2 fragTexCoord;
in vec4 fragColor;
in vec3 fragNormal;
in vec3 fragPosition;

// uniform sampler2D texture1;
uniform sampler2D projTexture;
uniform vec3 projPosition;

//uniform mat4 modelMatrix;
// uniform mat4 viewMatrix;
// uniform mat4 projectionMatrix;


void main(){ 
    vec4 texColor = texture(projTexture,fragTexCoord);
    finalColor = texColor; //if i set red it works
    
    //vec3 projectorDirection = normalize(projPosition - (modelMatrix * vec4(fragPosition,1.0) ).xyz);
    //float dotProduct = dot(fragNormal, projectorDirection);
    /*if(dotProduct < 0.0){
        finalColor = vec4(0,0,0,1.0);
    }*/
    /*
        // this makes sure we don't render the texture also on the back of the object
        vec3 projectorDirection = normalize(projPosition - vWorldPosition.xyz); //world position is just model * vertexPos
        float dotProduct = dot(vNormal, projectorDirection);
        if (dotProduct < 0.0) {
        outColor = vec4(color, 1.0);
        }
    */
}
