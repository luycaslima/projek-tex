#version 330 

out vec4 finalColor;

in vec2 fragTexCoord;

uniform sampler2D texture1;

void main(){

    vec4 texColor = texture(texture1,fragTexCoord);
    finalColor = texColor; //if i set red it works

}
