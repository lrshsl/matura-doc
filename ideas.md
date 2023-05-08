

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
        - Use already existing languages as a base (markdown, HTML, CSS)
    - Target language
        - HTML, CSS with bootstrap
    - Write a transpiler using the same techniques as real com-/transpilers
        - I already looked into that area
        - There are many utilities for lexing/parsing etc
            - One could work with regexes/BNF parsers
            - C/C++ : Flex & Bison  (I have some experience with that)
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


