#! /usr/bin/env python2

from distutils.core import setup
from glob import glob

setup(
    name = 'Game',
    version = '0.1.0',
    description = 'catch a spastic tree',
    author = 'sophia, Tempel',
    url = 'https://github.com/soapy1/A-Game.git',
    packages = 'game' 
    data_files = [('game/data', glob('data/*'))], 
    scripts = 'game.py',
)
    

