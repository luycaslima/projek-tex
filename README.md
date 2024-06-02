# ProjekTEX

A Projective texturing tool for 3D Models made with python and raylib.
The objective of the tool is data augmentation in computer vision models

---

## TO DO LIST

- [ ] Save Camera img in orthographic view
    - to do this paint a texture with everything that is being renderend and then convert to a image with np and pillow
- [ ] make the shader work for orthographic views
- [ ] Get the uv calculations from the shader so we can make the new texture for the model.
- [ ] Try to do this above, if not possible with shaders, and paralize with CUDA for scalability (more than one camera)
- [ ] Make the texture not render when the camera don't see it
  - Dot product method
  - Depth mask method ( Like the Nvidia paper of shadow mapping?)
- [ ] Create a Debug Camera object and Camera Frustum
- [ ] Basic Ui functions
  - [ ] Select camera
  - [ ] Move Camera
  - [ ] Undo/Redo
  - [ ] Orbital movement around the model
  - [ ] Save scene
  - [ ] Add/Remove model
  - [ ] Add/Remove Camera
  - [ ] Add/Remove Texture from the camera
  - [ ] Export Img of the scene
- [ ] Migrate project to C/C++ for better support and documentation of Raylib.
