'''Module for maps!'''

import os.path
searchpath = os.path.join(os.path.dirname(__file__), 'data')

import pygame as pg
from xml.etree import ElementTree as etree


class MapModuleError(Exception): pass
class MapError(MapModuleError): pass


class Map(object):
    '''Class for maps!
    Make sure a display has been opened before attempting to load a map.'''

    def __init__(self, filename):
        self.filename = os.path.join(searchpath, filename)

        xml = etree.parse(self.filename)

        root = xml.getroot()
        # Check that version and orientation are as expected.
        if root.get('version') != '1.0':
            raise MapError('Wrong map version, NOOOOOOO')
        if root.get('orientation') != 'orthogonal':
            raise MapError('Need an orthogonal map, NOOOOOOO')
        # Store basic map dimensions.
        self.width = int(root.get('width'))
        self.height = int(root.get('height'))
        self.tilewidth = int(root.get('tilewidth'))
        self.tileheight = int(root.get('tileheight'))

        # Parse tilesets used by this map.
        # Tile number 0 is always an empty tile.
        self.tileset = [ pg.Surface((0,0)) ]
        for tileset in root.findall('tileset'):
            if tileset.get('source') is not None:
                # If tileset is an external reference, open the file, parse the
                # XML, then pass the element object to the parser.
                self.add_tileset(etree.parse(
                    os.path.join(searchpath, tileset.get('source')) ).getroot())
            else:
                # If embedded, pass element object directly to parser.
                self.add_tileset(tileset)

        # Read layers in order that they appear.
        # Layers are listed from bottom to top.
        self.layers = list()
        for layer in root.findall('layer'):
            if (int(layer.get('width')) != self.width or
                int(layer.get('height')) != self.height):
                raise MapError('Layer different size from map, NOOOOOOO')
            data = layer.find('data')
            if data.get('encoding') != 'csv':
                raise MapError('Layer encoding must be CSV, NOOOOOOO')
            # Find corresponding tile image for each tile.
            self.layers.append( [ [ self.tileset[int(i)]
                for i in filter(str.isdigit, line.split(',')) ]
                for line in filter(None, data.text.split('\n')) ] )

    def add_tileset(self, tileset):
        tilewidth = int(tileset.get('tilewidth'))
        tileheight = int(tileset.get('tileheight'))
        im = tileset.find('image')
        image = pg.image.load( os.path.join(searchpath, im.get('source')))
        # Colorkey is defined in tileset by hexadecimal number.
        # TODO: Support alpha transparency.
        image.set_colorkey( int(im.get('trans'), base=16) )
        image.convert()

        # Split image into tiles.
        # TODO: Support margins, spacing.
        self.tileset.extend([ image.subsurface(x,y, tilewidth,tileheight)
            for y in range(0, image.get_height(), tileheight)
            for x in range(0, image.get_width(), tilewidth) ])


    def draw(self, surface):
        '''Draw the complete map to the given Surface.'''
        for layer in self.layers:
            for j,row in enumerate(layer):
                for i,tile in enumerate(row):
                    surface.blit(tile, (i*self.tilewidth,
                        (j+1)*self.tileheight - tile.get_height()))
