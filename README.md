PyLapse
=======

A simple application to build timelapses using a webcam, Python, V4l2 and ImageMagick


Install
=======

    $ cd pylapse
    $ pip-2.7 -r requirements.txt --upgrade

Or setup a virtualenv environment with...

    $ virtualenv2 venv  ; Maybe you need just virtualenv
    $ venv/bin/activate
    $ pip -r install requirements.txt --upgrade


Install ImageMagick with:

ArchLinux

    # pacman -S imagemagick

Debian/Ubuntu

    # apt-get install imagemagick


Usage
=====

You can define the variables for the captures and video generation in `config.py`.

Then you can create the images with:

    $ python app.py capture

Then you could generate the video with:

    $ python app.py video

You can access the program help:

    $ python app.py -h ; Global help information
    $ python app.py capture -h ; Capture Image Help
    $ python app.py video -h ; Video generation help


Have fun! :-)
