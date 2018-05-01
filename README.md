# venndy

## A package for computing sections of and drawing Venn diagrams.

Since computing section without drawing them might be desirable, there are
two separate modules for this - compute.py and draw.py. While there is no
(intended) limit to the computation of sections, drawing is currently limited
to at most five sets as Venn diagrams for more sets are hard to read anyway.

The SVG template for the Venn diagrams are based on Edward's design. I just
drew them in a more angular way. Templates were made using Inkscape and, thus,
can easily be loaded and modified using it.

Example:
![example](docs/_static/venndy_example.png)
