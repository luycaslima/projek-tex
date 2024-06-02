#version 330 

out vec4 finalColor;

in vec2 fragTexCoord;
in vec4 fragColor;
in vec3 fragNormal;
in vec3 fragPosition;
in vec3 projDirection;

uniform sampler2D projTexture;




void main(){ 
    vec4 texColor = texture(projTexture,fragTexCoord);
    finalColor = texColor; 

    // float dotProduct = -dot(fragNormal, projDirection);
    
    // if(dotProduct < 0.0){
    //     finalColor = vec4(0,0,0,1.0);
    // }

    /*
        // this makes sure we don't render the texture also on the back of the object
        vec3 projectorDirection = normalize(projPosition - vWorldPosition.xyz); //world position is just model * vertexPos
        float dotProduct = dot(vNormal, projectorDirection);
        if (dotProduct < 0.0) {
        outColor = vec4(color, 1.0);
        }
    */
}
