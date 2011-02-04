#!/usr/bin/env python
import sys
import ROOT as r
import configuration as conf
import data,utils

def pwd() :
    return sys.argv[1]

def fileName() :
    return sys.argv[2]

def funcName() :
    return fileName().split("/")[-1].replace(".C+","").replace(".C","")

def libName() :
    return funcName()+"_C.so"

def points() :
    return [(int(sys.argv[i]), int(sys.argv[i+1]), int(sys.argv[i+2])) for i in range(3, len(sys.argv), 3)]

for lib in ["AutoDict_pair_std__string_std__string__cxx.so", "AutoDict_std__map_std__string_std__string__cxx.so", libName()] :
    assert not r.gSystem.Load(lib), "Could not load library %s"%lib

for point in points() :
    getattr(r, funcName())(utils.stdMap(conf.switches(), "string", "int"),
                           utils.stdMap(conf.strings(*point), "string", "string"),
                           utils.stdMap(data.numbers(), "string", "double"),
                           *point
                           )
