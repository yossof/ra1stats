#! /usr/bin/env python

import ROOT as r

from collections import Iterable
from array import array

import DataFactory as DF

def print_unpack( item, level = 0, ending_comma = False ) :
    if not isinstance( item, dict) : 
        if not isinstance( item, Iterable ) :
            print "\t"*level,"{item:.4}".format(item=item),
            if ending_comma :
                print ","
            else:
                print
        else :
            s = "(" if isinstance( item,tuple ) else "[" 
            e = ")" if isinstance( item,tuple ) else "]" 
            print "\t"*level,s,
            for i in item :
                print "{i:.4},".format(i=i),
            print e,
            if ending_comma :
                print ","
    else :
        print "\t"*level,"{"
        for key,value in item.iteritems() :
            print "\t"*(level+1),
            keystring = '"%s"' % key
            print '{k:20} : '.format( k=keystring ),
            print_unpack( value, 0, True )
        print "\t"*level,"}"

r.gROOT.SetBatch(1)

std_selections = { "had"  : [ "lumiData", "lumiMc", "WW", "WJets", "Zinv", "t", "ZZ",
                         "DY", "tt", "obs", "WZ" ],
                   "muon" : [ "lumiData", "lumiMc", "Zinv", "WW", "WJets", "t", "ZZ",
                         "DY", "tt", "obs", "WZ" ],
                   "mumu" : [ "lumiData", "lumiMc", "Zinv", "WW", "WJets", "t", "ZZ",
                         "DY", "tt", "obs", "WZ" ],
                 }

may_04_files = ["~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_More_Than_One_btags.root",
                "~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_More_Than_Two_btags.root",
                "~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_More_Than_Zero_btags.root",
                "~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_One_btag.root",
                "~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_Two_btags.root",
                "~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_Zero_btags.root",
                "~/public_html/03_RA1/07_numbers_from_darren/02_04_05_2012/RA1_Stats_Zero_btags_AlphaT_Cut.root",
               ]
names = [ "btag_gt1", "btag_gt2", "btag_gt0", "btag1", "btag2", "btag0", "btag0_aT" ]

selections = [ { rfile : std_selections } for rfile in may_04_files ] 

dsfs = [ DF.DataSliceFactory( selection ) for selection in selections ]
dss  = [ dsf.makeSlice("x",55.5,55.6) for dsf in dsfs ]

slices = dict( zip( names, dss ) )

for name,slice in slices.iteritems() :
    print "="*len(name)
    print name
    print "="*len(name)
    mems = dir( slice )
    for attr_name in mems :
        if not "__" in attr_name :
            attr_data = getattr( slice, attr_name )
            print "{classname}.{obj} = ".format(classname="self", obj=attr_name),
            print_unpack( attr_data,1 )
            print
    print "\n"
