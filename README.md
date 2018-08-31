# Smart Grid

This repository contains all of the code for the work-in-progress research assignement called "Smart Grid". The smartgrid-website directory contains a django website, the serverTest.py contains mysql code that was written asY a test for learning database management, and the SmartGrid.png/SmartGrid.xml are documentation (ERF diagrams) of the database. To create the diagrams I used draw.io (https://www.draw.io/).

Before looking into using or changing this code I recommend that you have some django experience. Django is not necessarily difficult, there is just a lot to know. If you have never worked with django then looking into the tutorial that the creators of django have put together will be a big help to you. This is tutorial is farily comprehensive and will allow you to understand the structure of the project as well as the code that makes it work.

Here is the django "start" page:
https://www.djangoproject.com/start/

You can find the first tutorial in the series here:
https://docs.djangoproject.com/en/2.0/intro/tutorial01/

**Note that this project uses django 2.0

I also advise that you set up a virtual environment for this project. I really enjoy anaconda environments for python, but most anything will work. Your environment should have the following packages installed:

if you're using conda the following will install when you use the command: conda install django

    ca-certificates: 2018.03.07-0
    certifi:         2018.4.16-py37_0
    django:          2.0.5-py37hd476221_0
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4
    libgcc-ng:       7.2.0-hdf63c60_3
    libstdcxx-ng:    7.2.0-hdf63c60_3
    ncurses:         6.1-hf484d3e_0
    openssl:         1.0.2o-h14c3975_1
    pip:             10.0.1-py37_0
    python:          3.7.0-hc3d631a_0
    pytz:            2018.5-py37_0
    readline:        7.0-ha6073c6_4
    setuptools:      40.0.0-py37_0
    sqlite:          3.24.0-h84994c4_0
    tk:              8.6.7-hc745277_3
    wheel:           0.31.1-py37_0
    xz:              5.2.4-h14c3975_4
    zlib:            1.2.11-ha838bed_2

if you're using conda the following will install when you use the command: conda install mysqlclient

    mysql-connector-c: 6.1.11-hf4847fb_0
    mysqlclient:       1.3.13-py37h14c3975_0

finally:
pip install django-autofixture

Django and the supporting packages are needed just for running the straight django code. mysqlclient allows for manipulation of MySQL databases with python code. Forutnately django takes care of the databasing, but we still need to have the appriopriate packages installed for it to do its work. Finally, django-autofixture is a library that I used for filling the database with random data for testing purposes. This tool was a huge help! Checkout the documentation for auto fixture here:

https://pypi.org/project/django-autofixture/

Thanks! I hope that you find this code useful for big things! Please feel free to contact me if you have any questions. You can reach me at nathanthom@nevada.unr.edu
