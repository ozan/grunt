Grunt
=====

Grunt make slideshow. Grunt make slideshow from text file.

Installation
------------

    sudo pip install grunt

Example
-------

    $ cat examples/fruit.grunt
    Here is a presentation about fruits
    It starts with some apples ... http://farm4.static.flickr.com/3139/2780642603_920207d6cd_o.jpg
    ... followed by some pears. http://farm1.static.flickr.com/59/214356955_aba23e7b13_o.jpg
    Want something more exotic?
    http://farm3.static.flickr.com/2745/4346213550_43117ec8fc_o.jpg
    http://farm5.static.flickr.com/4023/4405120042_8165106b6e_o.jpg
    (fin) http://farm1.static.flickr.com/176/425537870_7bf42a21cb_o.jpg
    
    $ grunt examples/fruit.grunt > my_fruity_presentation.html
    
    $ head my_fruity_presentation.head
    <!doctype html> 
    <html xmlns="http://www.w3.org/1999/xhtml"> 
      <head> 
        <meta charset="utf-8" /> 
        <title>Here is a presentation about fruits</title> 

        <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.3.0/build/cssreset/reset-min.css">

        <style type="text/css" media="screen">
    
    $ open my_fruity_presentation.html

Grunt not extensible. Grunt not customizable. Grunt only make slideshow.
