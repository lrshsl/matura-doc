

## My ideas (brainstorming):

- PDF
    - data extractor
    - viewer
    - editor
- Markup language
    - to HTML
    - both HTML and CSS
- Images
    - QOI format own implementation
    - WEBP format
    - Raster to vector graphics converter


## Concrete propositions:

1. PDF editor
    - In python
    - Built on top of [borb](https://github.com/jorisschellekens/borb) (problems with semi-commercial license?)
    - Borb would have a nice [book](https://github.com/jorisschellekens/borb-examples/blob/master/README.md)
    - Or in another language with the help of other libraries
    - How it would work:
        - provide an easy command line interface
        - provide a simplistic GUI:
            - Basically just a textarea to run commands
            - Display the resulting pdf next to it

2. Markup + Styling language
    - In any language
    - Source language
        - Plan a simple & flexible syntax
        - Use already existing languages as a base (markdown, HTML, CSS, org)
    - Target language
        - HTML, CSS with bootstrap
    - Write a transpiler using the same techniques as real com-/transpilers
        - I already looked into that area
        - There are many utilities for lexing/parsing etc
            - One could work with regexes/BNF parsers
            - C/C++ : Flex & Bison  (I have some experience with that; It would be at least possible)
            - Rust : I know Rust quite well and I've read that Rust has great libraries for parsing, but I never used them
            - The language Haskell itself is known to be very suitible (don't really know it but would be interested)

3. Raster -> Vector converter
    - The approach:
        - Use AI
        - Test data completely generatable:
            - Generate random SVG (or other vec formats) files
            - Use an existing Vector to Raster converter to get a raster file
            - Give the raster file as input to the AI model
            - The AI model outputs a vector file
            - The score to rate the AI is simply how different the output is from the original SVG file
            - The test data can be deleted afterwards -> Less storage usage
    - Probably in Python/Cython because of the powerfull AI libraries
    - Interesting: [GDAL](https://www.gdal.org/)




## Explanations


### Idea 2: Markup + Styling language

I really enjoy writing in languages like markdown, where one can easily read and write the source code and it can produce a nice looking HTML page or PDF. As soon as you try to add some styling though, you find yourself typing HTML and embedded CSS and all of md's advantages are lost.
Latex has similar problems, it can get very quickly very unreadable.
After a quick google search I didn't really find other markup/styling languages that would be as easy to use as markdown and support an easy way to do some basic styling like changing font, color of bg/fg, centering text etc.
My idea was, to create a own markup language, maybe a superset of markdown, and add some easy to learn and remember styling capabilities to it.
I'm also thinking about adding some more features such as variables (probably just copy-paste variables like in Makefiles) and imports (also basic copy-paste).

A syntax example for what I am thinking about is found in the file [syntax\_example.txt](syntax_example.txt)


### Idea 3

To try to solve the problem with raster to vector graphics converter I had the idea of, instead of writing a complex algorithm what no team ever managed to get working quite well until now, letting an AI find the best-suiting vector elements for a given raster image. I could use any raster file format and target any vector format, since conversions between the same type of format is already very well supported in most mainstream programming languages.

#### The final product
The product of the work would be an AI model that is able to recognise shapes, colors and possibly text in a given image and produce a vector file or a specification of the shapes that would allow to be converted in a vector format.

#### Steps to be done
I would first write a generator to generate random SVG files and then convert them into vector files using [cairosvg](https://cairosvg.org/).

For the AI part, I'd go with [keras](https://keras.io/). Using [tensorflow](https://www.tensorflow.org/) the images from the generator would be filled into the AI model trough an [input pipeline](https://www.tensorflow.org/guide/data), which the model could directly train on.

The whole process would look like that:
1. Generate random vector files
2. Convert them into vector files
3. Train the model
4. Grade the model based on how much the output resembles the original vector file

I would begin with some simple examples to train the model, and then add some more features:
1. Basic shapes
    - Input: raster image with one shape, like a circle, rectangle etc
    - Output would be a number (0 for circle, 1 for rectangle etc)
3. Basic colors
    - Input: raster image with one shape, like a circle, rectangle etc in different colors too
    - Output: five numbers: one for shape others for RGB components of color
2. Multiple shapes on one image
3. Overlapping shapes
4. Noise
..
Until it has the desired accuracy.

> Note:
> I decided to use python because of its powerful libraries, especially in the sector of AI. Another option would be Javascript which has some good machine/deep learning libraries as well and would allow to port my tool easily to the web.
> I will probably (need to) descend to [Cython](https://cython.org/), at least for the generator, because of its speed.




