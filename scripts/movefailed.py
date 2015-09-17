#!/usr/bin/env python

import sys
from optparse import OptionParser
import os
import math
import fnmatch

parser = OptionParser()
def split_callback(option,opt,value,parser):
  setattr(parser.values,option.dest,value.split(','))

#def splitIt(a,n):
#  k, m = len(a) / n, len(a) % n
#  return(a[i*k+min(i,m):(i+1) * k +min(i+1,m)] for i in xrange(n))

parser.add_option("--folder", dest="folder",type='string')
parser.add_option("--is_combination",dest="is_combination",action="store_true",default=False)
#parser.add_option("--tanb", dest="tanb", type='string', action='callback',callback=split_callback)

(options,args) = parser.parse_args()

#tanb=options.tanb
folder=options.folder
nvals = len(fnmatch.filter(os.listdir('.'),'%(folder)s-*'%vars()))

#splittanb = list(splitIt(tanb,nvals))

if options.is_combination :
  for dirn in range(-1,1,0.02) :
    print "Copying from directory %(dirn)f"%vars()
    for nsplit in range(0,nvals-1):
      os.system('cp %(folder)s-%(nsplit)d/%(dirn)f/HypothesisTest_* %(folder)s/%(dirn)f/ '%vars())
#    os.system('hadd %(folder)s/%(dirn)f/HypothesisTest.root %(folder)s/%(dirn)f/HypothesisTest_*' %vars()

else :
  for idirn in range(-80,-20,2) :
    dirn = float(idirn)/100
    print dirn
    if idirn not in [-100,0,100] and idirn not in range(-90,90,10):
      print "mkdirnotused %(dirn).2f"%vars()
      os.system('mkdir %(folder)s/bbb/cmb/%(dirn).2f/notused'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.05.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.10.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.15.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.20.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.25.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.30.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.35.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_0.40.root %(folder)s/bbb/cmb/%(dirn).2f/notused/'%vars())
      os.system('hadd -f %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest.root %(folder)s/bbb/cmb/%(dirn).2f/HypothesisTest_*'%vars())
    elif idirn not in [-100,0,100] :
      print "mkdirnotused %(dirn).1f"%vars()
      os.system('mkdir %(folder)s/bbb/cmb/%(dirn).1f/notused'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.05.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.10.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.15.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.20.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.25.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.30.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.35.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_0.40.root %(folder)s/bbb/cmb/%(dirn).1f/notused/'%vars())
      os.system('hadd -f %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest.root %(folder)s/bbb/cmb/%(dirn).1f/HypothesisTest_*'%vars())
    else :
      print "mkdirnotused %(dirn).0f"%vars()
      os.system('mkdir %(folder)s/bbb/cmb/%(dirn).0f/notused'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.05.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.10.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.15.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.20.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.25.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.30.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.35.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('mv %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_0.40.root %(folder)s/bbb/cmb/%(dirn).0f/notused/'%vars())
      os.system('hadd -f %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest.root %(folder)s/bbb/cmb/%(dirn).0f/HypothesisTest_*'%vars())

