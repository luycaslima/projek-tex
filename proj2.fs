#version 330

in vec4 fragTexCoord;
out vec4 fragColor;

uniform sampler2D texture1;

void main(){
    vec3 projectedTexCoord = fragTexCoord.xyz / fragTexCoord.w;

    //fragColor = fragTexCoord;
    fragColor = texture(texture1,projectedTexCoord.xy);
    //fragColor = vec4(1.0, 1.0, 0.0, 1.0); 
}