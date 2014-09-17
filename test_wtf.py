#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtf import wtf

class Shape(object):
    def __init__(self, pastry=None, **kwargs):
        self.initialized = True
        wtf(to_out=False, to_err=True, wvars=['centroid'])

class Square(Shape):
    def __init__(self, **kwargs):
        super(Square, self).__init__(pastry='Croissant', **kwargs)


if __name__ == "__main__":
    square = Square(centroid=(0,9), mass=3e7)

