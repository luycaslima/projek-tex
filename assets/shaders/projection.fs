#version 330 

out vec4 finalColor;

in vec2 fragTexCoord;
in vec4 fragColor;
in vec3 fragNormal;
in vec3 fragPosition;
in vec3 projDirection;

uniform sampler2D projTexture;

void main(){ 
    //vec4 texColor = texture(projTexture,fragTexCoord);
    //finalColor = texColor; 

    // Check if the projected coordinates are within the texture bounds
        if (fragTexCoord.x >= 0.0 && fragTexCoord.x <= 1.0 && fragTexCoord.y >= 0.0 && fragTexCoord.y <= 1.0)
        {
            vec4 texColor = texture(projTexture,fragTexCoord);
            finalColor = texColor; 

        }
        else
        {
            // If outside the bounds, discard the fragment or set a default color
            finalColor = vec4(0,0,0,1.0);  // Or use fragColor = vec4(1.0, 1.0, 1.0, 1.0);
        }
    

    // float dotProduct = -dot(fragNormal, projDirection);
    // if(dotProduct < 0.0){
    //     finalColor = vec4(0,0,0,1.0);
    // }
}
