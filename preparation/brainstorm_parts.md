
# Concept

## Steps to be taken


### Data generation

The training data has to be generated. This is the most essential part of my work.
The data consists of images of random shapes, in a vector and a raster presentation, which will allow the model to predict the shapes on the basis of the raster image, convert them to a vector presentation, and compare the result to the original vector image.
The pictures should not be compared using their vector source code, but using the pixel values instead, so that slight variations have proportionally small impact.
Another possibility is to generate an own presentation of what is seen in the image, and generate the raster image based on that representation. The neural network would then predict that internal representation, which would have advantages in performance as well as simplicity, since the model output is already present in a for the model usable form.


#### Progress

Different shapes
- Triangles, rectangles (easiest to generate and describe using their corner points)
- Polygons
- Circles (needs another representation: center, radius, color)
Advanced:
- Text

Different colors
- Brightness (requires only a single channel)
- RGB values
    - From a predefined color palette (can be done using one neuron in the output layer for each color (probability distribution)
    - Continuous (the strength of how strong the neurons fire may have to be considered)

Multiple Shapes per image
- As simple as passing a pointer vs creating a new image to implement
- Requires a much more capable model and / or code around it
    - e. g. a pretrained model that can determine regions with one shape each
    - or a pipeline that feeds the image back to the model after removing the recognised shape





