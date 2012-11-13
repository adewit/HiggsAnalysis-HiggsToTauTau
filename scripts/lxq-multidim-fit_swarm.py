#!/usr/bin/env python

from optparse import OptionParser, OptionGroup

## set up the option parser
parser = OptionParser(usage="usage: %prog [options] ARG",
                      description="Script to setup a set of scripts for maxlimum likelihood scan for 2-dim parameters estimates.")
parser.add_option("-n", "--name", dest="name", default="ml-scan", type="string", help="Name of the output scripts. [Default: \"ml-scan\"]")
parser.add_option("--qsub", dest="qsub", default="-j y -o /dev/null", type="string", help="Submission arguments for batch queue. [Default: \"-j y -o /dev/null\"]")
parser.add_option("--njobs", dest="njobs", default="100", type="string", help="Number of jobs for for scan. [Default: \"100\"]")
parser.add_option("--npoints", dest="npoints", default="100", type="string", help="Number of points per job. [Default: \"100\"]")
parser.add_option("--physics-model", dest="fitModel", type="string", default="", help="Physics model for multi-dimensional maximum likelihood. The physics model should be defined by a model name and a path to a python implementation of the model separated by '='. For example 'ggH-qqH-model=PATH-TO-IMPLEMENTATION'. In this case a workspace of the model with given model options will be created with the name 'ggH-qqH-model.root'. It is also possible to pass on only a name of a physics model, like 'ggH-qqH-model'. In this case it will be assumed that the model with name 'ggH-qqH-model' has been created beforehand. [Default: \"\"]")
parser.add_option("--physics-model-options", dest="fitModelOptions", type="string", default="", help="Potential options for the used physics model for multi-dimensional maximum likelihood. More options can be passed on separated by ','. [Default: \"\"]")
parser.add_option("--options", dest="opts", default="", type="string", help="Additional options for limit.py. [Default: \"\"]")
parser.add_option("--collect", dest="collect", default=False,  action="store_true", help="Collect the individual jobs of a single batch submission after completion. [Default: False)")
parser.add_option("--stable", dest="stable", default=False, action="store_true", help="Run maximum likelihood fit with a set of options that lead to stable results. Makes use of the common options --rMin and --rMax to define the boundaries of the fit. [Default: True]")
## check number of arguments; in case print usage
(options, args) = parser.parse_args()

import os

if options.collect :
    os.system("hadd {DIR}/higgsCombine{MODEL}.MultiDimFit.mH{MASS}.root {DIR}/higgsCombine*.MultiDimFit.mH{MASS}-[0-9]*-[0-9]*.root".format(
        DIR=input,
        MASS=input[input.rfind("/")+1:],
        MODEL=options.name
        ))
    os.system("rm {DIR}/higgsCombine*.MultiDimFit.mH{MASS}-[0-9]*-[0-9]*.root".format(
        DIR=input,
        MASS=input[input.rfind("/")+1:]
        ))
else :
    for dir in args:
        ana = dir[:dir.rfind('/')]
        limit = dir[len(ana)+1:]
        jobname = ana[ana.rfind('/')+1:]+'-'+limit
        ## create submission scripts
        os.system("lxq-multidim-fit.py {DIR} {STABLE} --njobs {JOBS} --npoints {POINTS} --physics-model {FITMODEL}  --physics-model-options {FITMODELOPTIONS} -n {NAME}".format(
            DIR = dir,
            STABLE = "--stable" if options.stable else "",
            JOBS = options.njobs,
            POINTS = options.npoints,
            FITMODEL = options.fitModel,
            FITMODELOPTIONS = options.fitModelOptions,
            NAME = options.name
            ))
        ## execute
        os.system("./{NAME}_submit.sh".format(NAME=options.name))
        ## shelve
        os.system("rm {NAME}_submit.sh".format(NAME=options.name))
        os.system("rm -r {NAME}".format(NAME=options.name))