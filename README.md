PGU
===

This is a friendly fork of https://github.com/parogers/pgu made so it can run in py37+

Anyone is wellcomed to chery pick anything they want.

Read more at https://github.com/ccanepa/pgu/issues/1

Not available in Pypi

Vera.ttf is from:

    http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/
    see that site for more information about the font.

Documentation
=============

To build the PGU documentation, run the build.py script found under docs:

    $ cd docs
    $ python build.py
    $ your-favorite-browser index.html

To understand pgu.gui -- read:
    http://www.w3.org/TR/REC-html40/
    (pgu.gui is based heavily on my HTML background)

To understand the pgu.gui default theme -- read:
    http://www.w3.org/TR/REC-CSS2/box.html
    (the theme uses the css 2 box model)

Example scripts can be found in the examples directory.

THANKS
======

* Phil Hassey, which wrote the library
* Peter Rogers, maintainer after Phil left
 
* gal koren -- bugs, draft of html.HTML, suggestions, bug finding, ScrollArea widget, FileDialog, List, Console
* fdarling -- testing, suggestions, bug fixing, code cleanup, menus & slider UI fixes, new Table class, reorganization of pgu.gui into a package
* richard jones -- packaging, suggestions, code cleanup
* jhofmann -- tiled preview in tileedit and PIL support
* Dr. L. Humbert -- gui.Password widget
* illume -- added auto-load features to tile & leveledit
* python -- suggestions, bug finding, bug fixing (unicode)
* Addison Hardy -- added ScrollArea to html5.py
* dang`r`us -- testing, suggestions
* piman -- testing, suggestions
* coca-cola -- testing
* tenoften -- testing
* Joao S. O. Bueno - evolving the code base to Python3 (pygame 1.9.5)
