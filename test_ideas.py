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

import inspect
import re
import sys


def trace_this(func_to_trace):
    def tracer(frame, event, arg):
        if event == 'return':
            print "Return from {}:{} => {}".format(frame.f_code.co_name, frame.f_lineno, arg)
            return
        if event == 'call':
            # The explicit tracer return is needed for trace chaining, so we
            # get calls *and* return values
            return tracer
        return

    def run_with_tracing(*args, **kwargs):
        sys.settrace(tracer)
        func_to_trace(*args, **kwargs)
        sys.settrace(None)

    return run_with_tracing


def inspect_istests_tester(f):
    fisa = ''
    if inspect.ismethod(f):
        fisa += ' method '
    if inspect.isfunction(f):
        fisa += ' function '
    if inspect.isgeneratorfunction(f):
        fisa += ' generator '
    return fisa

def func_decor(f):
    def decorated(funcref):
        f_src = inspect.getsource(f)
        m = re.match('(?P<func>.+?)\((?P<args>.+?\))', f_src)
        # almost right... should we try to use the AST?
        print m.groups()
        #setattr(f, 'isdecorated', True)
        return f

    if inspect.ismethod(f) or inspect.isfunction(f):
        f = decorated(f)

def func1(*args, **kwargs):
    s = "Some arbitrary value"
    return s

def func2(*args, **kwargs):
    return func1("bob", "carol", "alice")

@trace_this
def func3(*args, **kwargs):
    return func2("golden", "monkey")

def func4(*args, **kwargs):
    return func3(1, 2, 3, 4, 5)

class Box(object):
    def open(self, *args, **kwargs):
        return func4(*args, **kwargs)

if __name__ == "__main__":
    b = Box()
    b.open('cows')
