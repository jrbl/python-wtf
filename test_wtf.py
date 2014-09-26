#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Copyright 2014 Joseph Blaylock <jrbl@jrbl.org>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

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

