#version 330 

out vec4 finalColor;

in vec2 fragTexCoord;
in vec4 fragColor;
in vec3 fragNormal;
in vec3 fragPosition;

// uniform sampler2D texture1;
uniform sampler2D projTexture;


// uniform mat4 modelMatrix;
// uniform mat4 viewMatrix;
// uniform mat4 projectionMatrix;


void main(){
    //vec4 projectorCoords = projectionMatrix * viewMatrix * modelMatrix * vec4(fragPosition,1.0);
    //projectorCoords /= projectorCoords.w;
    //to no project behind
    //float w = max(projectorCoords.w,0.0);
    
    //map from [-1,1 ] to [0,1]
    //vec2 uv = (projectorCoords.xy /w) * 0.5 + 0.5;

    // Clamp texture coordinates to avoid sampling outside the texture
    //uv = clamp(projectorCoords.xy, 0.0, 1.0);

    vec4 texColor = texture(projTexture,fragTexCoord);
    finalColor = texColor; //if i set red it works
}
