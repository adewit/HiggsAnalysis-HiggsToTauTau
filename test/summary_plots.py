from optparse import OptionParser, OptionGroup
from HiggsAnalysis.HiggsToTauTau.LimitsConfig import configuration

## set up the option parser
parser = OptionParser(usage="usage: %prog [options]",
                      description="Script to combine 2011+2012 and high and low pt event categories. This script requires that the script run_macros.py has been executed beforehand and produced resultrs w/o issues.")
## direct options
parser.add_option("-a", "--analysis", dest="analysis", default="sm", type="choice", help="Type of analysis (sm or mssm). Lower case is required. [Default: sm]", choices=["sm", "mssm"])
parser.add_option("-t", "--type", dest="type", default="postfit", type="string", help="Type of plots, prefit or postfit. [Default: \"postfit\"]")
parser.add_option("--mA", dest="mA", default="160", type="float", help="Mass of pseudoscalar mA only needed for mssm. [Default: '160']")
parser.add_option("--tanb", dest="tanb", default="8", type="float", help="Tanb only needed for mssm. [Default: '8']")
parser.add_option("-c", "--config", dest="config", default="", type="string", help="Additional configuration file to be used for the channels, periods and categories. [Default: '']")
parser.add_option("--debug", dest="debug", action="store_true", default=False, help="Debug option to show only scripts which are run without actually running them [Default: False]")
parser.add_option("--add-mutau-soft", dest="add_mutau_soft", action="store_true", default=False, help="Add the soft categories to the mt channel [Default: False]")
parser.add_option("--hww-signal", dest="hwwsig", action="store_true", default=False, help="Add H->WW processes as signal to the em channel [Default: False]")
## check number of arguments; in case print usage
(options, args) = parser.parse_args()

config=configuration(options.analysis, options.config, options.add_mutau_soft)

## a set of pre-defined lists

#categories_sm = [
#    "0jet_low",
#    "0jet_high",
#    "0jet",
#    "1jet_low",
#    "1jet_medium",
#    "1jet_high_lowhiggs",
#    "1jet_high_mediumhiggs",
#    "1jet_high",
    #"1jet",  ## these are not combined at the moment due to different binning in low and high pt
#    "vbf",
#    ]


channels   = {
    "em":"emu",
    "et":"eleTau",
    "mt":"muTau",
    "mm":"mumu",
    "ee":"ee",
    "tt":"tauTau"
    }

extra = {
    "ee"      : "ee",
    "emu"     : "e#mu",
    "eleTau"  : "e#tau_{h}",
    "muTau"   : "#mu#tau_{h}",
    "mumu"    : "#mu#mu",
    "tauTau"   : "#tau_{h}#tau_{h}"
    }

log = {
    "sm":
    {
    ("emu"    , "0jet_low"  ) : ["false",],
    ("emu"    , "0jet_high" ) : ["false",],
    ("emu"    , "0jet"      ) : ["false",],
    ("emu"    , "1jet_low"  ) : ["false",],
    ("emu"    , "1jet_high" ) : ["false",],
    ("emu"    , "1jet"      ) : ["false",],
    ("emu"    , "btag_low"  ) : ["false",],
    ("emu"    , "btag_high" ) : ["false",],
    ("emu"    , "vbf"       ) : ["false",],
    ("muTau"  , "0jet_low"  ) : ["false",],
    ("muTau"  , "0jet_high" ) : ["false",],
    ("muTau"  , "0jet"      ) : ["false",],
    ("muTau"  , "1jet_medium"  ) : ["false",],
    ("muTau"  , "1jet_high_lowhiggs" ) : ["false",],
    ("muTau"  , "1jet_high_mediumhiggs" ) : ["false",],
    ("muTau"  , "1jet_high" ) : ["false",],
    ("muTau"  , "1jet"      ) : ["false",],
    ("muTau"  , "btag_low"  ) : ["false",],
    ("muTau"  , "btag_high" ) : ["false",],
    ("muTau"  , "vbf"       ) : ["false",],
    ("eleTau" , "0jet_low"  ) : ["false",],
    ("eleTau" , "0jet_high" ) : ["false",],
    ("eleTau" , "0jet"      ) : ["false",],
    ("eleTau" , "1jet_medium"  ) : ["false",],
    ("eleTau" , "1jet_high_mediumhiggs" ) : ["false",],
    ("eleTau" , "1jet_high" ) : ["false",],
    ("eleTau" , "1jet"      ) : ["false",],
    ("eleTau" , "btag_low"  ) : ["false",],
    ("eleTau" , "btag_high" ) : ["false",],
    ("eleTau" , "vbf"       ) : ["false",],
    ("mumu"   , "0jet_low"  ) : ["true", ],
    ("mumu"   , "0jet_high" ) : ["true", ],
    ("mumu"   , "0jet"      ) : ["true", ],
    ("mumu"   , "1jet_low"  ) : ["true", ],
    ("mumu"   , "1jet_high" ) : ["true", ],
    ("mumu"   , "1jet"      ) : ["true", ],
    ("mumu"   , "btag_low"  ) : ["false", ],
    ("mumu"   , "btag_high" ) : ["false", ],
    ("mumu"   , "vbf"       ) : ["true",],
    ("ee"   , "0jet_low"  ) : ["true", ],
    ("ee"   , "0jet_high" ) : ["true", ],
    ("ee"   , "0jet"      ) : ["true", ],
    ("ee"   , "1jet_low"  ) : ["true", ],
    ("ee"   , "1jet_high" ) : ["true", ],
    ("ee"   , "1jet"      ) : ["true", ],
    ("ee"   , "vbf"       ) : ["true",],
    },    
    "mssm" :
    {
    ("emu"    , "nobtag"       ) : ["false", "true"],
    ("emu"    , "btag"         ) : ["false", "true"],
    ("muTau"  , "nobtag"       ) : ["false", "true"],
    ("muTau"  , "btag"         ) : ["false", "true"],
    ("muTau"  , "nobtag_low"   ) : ["false", "true"],
    ("muTau"  , "nobtag_medium") : ["false", "true"],
    ("muTau"  , "nobtag_high"  ) : ["false", "true"],
    ("muTau"  , "btag_low"     ) : ["false", "true"],
    ("muTau"  , "btag_high"    ) : ["false", "true"],
    ("eleTau" , "btag"         ) : ["false", "true"],
    ("eleTau" , "nobtag"       ) : ["false", "true"],
    ("eleTau" , "nobtag_low"   ) : ["false", "true"],
    ("eleTau" , "nobtag_medium") : ["false", "true"],
    ("eleTau" , "nobtag_high"  ) : ["false", "true"],
    ("eleTau" , "btag_low"     ) : ["false", "true"],
    ("eleTau" , "btag_high"    ) : ["false", "true"],
    ("mumu"   , "nobtag"       ) : ["false", "true"],
    ("mumu"   , "btag"         ) : ["false", "true"],
    },
    }

max = {    
    "sm":
    {
    ("emu"    , "0jet_low"  ) : ["-1",],
    ("emu"    , "0jet_high" ) : ["-1",],
    ("emu"    , "0jet"      ) : ["-1",],
    ("emu"    , "1jet_low"  ) : ["-1",],
    ("emu"    , "1jet_high" ) : ["-1",],
    ("emu"    , "1jet"      ) : ["-1",],
    ("emu"    , "btag_low"  ) : ["-1",],
    ("emu"    , "btag_high" ) : ["-1",],
    ("emu"    , "vbf"       ) : ["-1",], 
    ("muTau"  , "0jet_low"  ) : ["-1",],
    ("muTau"  , "0jet_high" ) : ["-1",],
    ("muTau"  , "0jet"      ) : ["-1",],
    ("muTau"  , "1jet_medium"  ) : ["-1",],
    ("muTau"  , "1jet_high_lowhiggs" ) : ["-1",],
    ("muTau"  , "1jet_high_mediumhiggs" ) : ["-1",],
    ("muTau"  , "1jet_high" ) : ["-1",],
    ("muTau"  , "1jet"      ) : ["-1",],
    ("muTau"  , "btag_low"  ) : ["-1",],
    ("muTau"  , "btag_high" ) : ["-1",],
    ("muTau"  , "vbf"       ) : ["-1",],
    ("eleTau" , "0jet_low"  ) : ["-1",],
    ("eleTau" , "0jet_high" ) : ["-1",],
    ("eleTau" , "0jet"      ) : ["-1",],
    ("eleTau" , "1jet_medium"  ) : ["-1",],
    ("eleTau" , "1jet_high_mediumhiggs" ) : ["-1",],
    ("eleTau" , "1jet_high" ) : ["-1",],
    ("eleTau" , "1jet"      ) : ["-1",],
    ("eleTau" , "btag_low"  ) : ["-1",],
    ("eleTau" , "btag_high" ) : ["-1",],
    ("eleTau" , "vbf"       ) : ["-1",],
    ("mumu"   , "0jet_low"  ) : ["-1",],
    ("mumu"   , "0jet_high" ) : ["-1",],
    ("mumu"   , "0jet"      ) : ["-1",],
    ("mumu"   , "1jet_low"  ) : ["-1",],
    ("mumu"   , "1jet_high" ) : ["-1",],
    ("mumu"   , "1jet"      ) : ["-1",],
    ("mumu"   , "btag_low"  ) : ["-1",],
    ("mumu"   , "btag_high" ) : ["-1",],
    ("mumu"   , "vbf"       ) : ["-1",],
    ("ee"   , "0jet_low"  ) : ["-1",],
    ("ee"   , "0jet_high" ) : ["-1",],
    ("ee"   , "0jet"      ) : ["-1",],
    ("ee"   , "1jet_low"  ) : ["-1",],
    ("ee"   , "1jet_high" ) : ["-1",],
    ("ee"   , "1jet"      ) : ["-1",],
    ("ee"   , "vbf"       ) : ["-1",],
    },    
    "mssm":
    {
    ("emu"    , "nobtag"       ) : ["1900",  "20000"], 
    ("emu"    , "btag"         ) : ["30",  "2000"], 
    ("muTau"  , "nobtag"       ) : ["4800",  "110000"], 
    ("muTau"  , "btag"         ) : ["60",  "1000"], 
    ("muTau"  , "nobtag_low"   ) : ["-1", "-1"],
    ("muTau"  , "nobtag_medium") : ["-1", "-1"],
    ("muTau"  , "nobtag_high"  ) : ["-1", "-1"],
    ("muTau"  , "btag_low"     ) : ["-1", "-1"],
    ("muTau"  , "btag_high"    ) : ["-1", "-1"],
    ("eleTau" , "nobtag"       ) : ["2100",  "40000"], 
    ("eleTau" , "btag"         ) : ["28",  "3000"], 
    ("eleTau" , "nobtag_low"   ) : ["-1", "-1"],
    ("eleTau" , "nobtag_medium") : ["-1", "-1"],
    ("eleTau" , "nobtag_high"  ) : ["-1", "-1"],
    ("eleTau" , "btag_low"     ) : ["-1", "-1"],
    ("eleTau" , "btag_high"    ) : ["-1", "-1"],
    ("mumu"   , "nobtag"    ) :    ["-1",  "3000000"],
    ("mumu"   , "btag"      ) :    ["-1",  "3000"],
    },
    }

min = {
    "sm":
    {
    ("emu"    , "0jet_low"  ) : ["0",  ],
    ("emu"    , "0jet_high" ) : ["0",  ],
    ("emu"    , "0jet"      ) : ["0",  ],
    ("emu"    , "1jet_low"  ) : ["0",  ],
    ("emu"    , "1jet_high" ) : ["0",  ],
    ("emu"    , "1jet"      ) : ["0",  ],
    ("emu"    , "btag_low"  ) : ["0",  ],
    ("emu"    , "btag_high" ) : ["0",  ],
    ("emu"    , "vbf"       ) : ["0",  ],
    ("muTau"  , "0jet_low"  ) : ["0",  ],
    ("muTau"  , "0jet_high" ) : ["0",  ],
    ("muTau"  , "0jet"      ) : ["0",  ],
    ("muTau"  , "1jet_medium"  ) : ["0",  ],
    ("muTau"  , "1jet_high_lowhiggs" ) : ["0",  ],
    ("muTau"  , "1jet_high_mediumhiggs" ) : ["0",  ],
    ("muTau"  , "1jet_high" ) : ["0",  ],
    ("muTau"  , "1jet"      ) : ["0",  ],
    ("muTau"  , "btag_low"  ) : ["0",  ],
    ("muTau"  , "btag_high" ) : ["0",  ],
    ("muTau"  , "vbf"       ) : ["0",  ],
    ("eleTau" , "0jet_low"  ) : ["0",  ],
    ("eleTau" , "0jet_high" ) : ["0",  ],
    ("eleTau" , "0jet"      ) : ["0",  ],
    ("eleTau" , "1jet_medium"  ) : ["0",  ],
    ("eleTau" , "1jet_high_mediumhiggs" ) : ["0",  ],
    ("eleTau" , "1jet_high" ) : ["0",  ],
    ("eleTau" , "1jet"      ) : ["0",  ],
    ("eleTau" , "btag_low"  ) : ["0",  ],
    ("eleTau" , "btag_high" ) : ["0",  ],
    ("eleTau" , "vbf"       ) : ["0",  ],
    ("mumu"   , "0jet_low"  ) : ["1e-2",  ],
    ("mumu"   , "0jet_high" ) : ["1e-2",  ],
    ("mumu"   , "0jet"      ) : ["1e-2",  ],
    ("mumu"   , "1jet_low"  ) : ["1e-2",  ],
    ("mumu"   , "1jet_high" ) : ["1e-2",  ],
    ("mumu"   , "1jet"      ) : ["1e-2",  ],
    ("mumu"   , "btag_low"  ) : ["0",  ],
    ("mumu"   , "btag_high" ) : ["0",  ],
    ("mumu"   , "vbf"       ) : ["1e-2",  ],  
    ("ee"   , "0jet_low"  ) : ["1e-2",  ],
    ("ee"   , "0jet_high" ) : ["1e-2",  ],
    ("ee"   , "0jet"      ) : ["1e-2",  ],
    ("ee"   , "1jet_low"  ) : ["1e-2",  ],
    ("ee"   , "1jet_high" ) : ["1e-2",  ],
    ("ee"   , "1jet"      ) : ["1e-2",  ],
    ("ee"   , "vbf"       ) : ["1e-2",  ],  
    },    
    "mssm":
    {
    ("emu"    , "nobtag"       ) : ["0", "1e-1"],
    ("emu"    , "btag"         ) : ["0", "1e-3"],
    ("muTau"  , "nobtag"       ) : ["0", "1e-3"],
    ("muTau"  , "btag"         ) : ["0", "1e-4"],
    ("muTau"  , "nobtag_low"   ) : ["0", "1e-3"],
    ("muTau"  , "nobtag_medium") : ["0", "1e-3"],
    ("muTau"  , "nobtag_high"  ) : ["0", "1e-3"],
    ("muTau"  , "btag_low"     ) : ["0", "1e-3"],
    ("muTau"  , "btag_high"    ) : ["0", "1e-3"],
    ("eleTau" , "nobtag"       ) : ["0", "1e-3"],
    ("eleTau" , "btag"         ) : ["0", "1e-4"],
    ("eleTau" , "nobtag_low"   ) : ["0", "1e-3"],
    ("eleTau" , "nobtag_medium") : ["0", "1e-3"],
    ("eleTau" , "nobtag_high"  ) : ["0", "1e-3"],
    ("eleTau" , "btag_low"     ) : ["0", "1e-3"],
    ("eleTau" , "btag_high"    ) : ["0", "1e-3"],
    ("mumu"   , "nobtag"       ) : ["0", "1e-2"],
    ("mumu"   , "btag"         ) : ["0", "1e-4"],
    },
    }


import os

##print in the right Signal label for MSSM
postfit_base = open("{CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit.C".format(CMSSW_BASE=os.environ['CMSSW_BASE']),'r')
postfit_use  = open("{CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C".format(CMSSW_BASE=os.environ['CMSSW_BASE']),'w')
for line in postfit_base :
    line = line.replace("$CMSSW_BASE", os.environ['CMSSW_BASE'])
    line = line.replace("$MA" , str(int(options.mA)))
    line = line.replace("$TANB", str(int(options.tanb)))
    line = line.replace("$HWWBG", "false" if options.hwwsig else "true")
    postfit_use.write(line)
postfit_base.close()
postfit_use.close()


type = options.type

print "C R E A T I N G   S U M M A R Y   P L O T S :"
print "CATEGORIES:", config.comb_categories
print "CHANNELS  :", config.comb_channels
print "PERIODS   :", config.comb_periods

## combine 2011+2012
for per in config.comb_periods:
    for chan in config.comb_channels:
        chn = channels[chan]
        #logarithm = "LOG" if (chn in ["mumu","ee"] or options.analysis == "mssm") else "LIN"
        for cat in config.comb_categories:
            ## check whether the category which is to be processed is one of the "normal" categories
            if len(per.split('_')) == 1:
                if cat not in config.categoryname[chan][per]:
                    ## find all categories whos name contain the pattern {CAT} as substring
                    ## the category must be valid for the corresponding period. For 7TeV and 8TeV it must be valid for 7TeV
                    cat_add = [category for category in config.categoryname[chan][per] if (cat in category and config.categoryname[chan][per].index(category) < len(config.categories[chan][per.split("_")[0]]))]
                    rootfiles_LIN = ["{CHN}_{CAT}_{TYPE}_{PERIOD}_LIN.root".format(CHN=chn, CAT=category, TYPE=type, PERIOD = per) for category in cat_add]
                    rootfiles_LOG = ["{CHN}_{CAT}_{TYPE}_{PERIOD}_LOG.root".format(CHN=chn, CAT=category, TYPE=type, PERIOD = per) for category in cat_add]
                    ## loop over all given configurations
                    for idx in range(len(min[options.analysis][chn,cat])):
                        if rootfiles_LIN:
                            if options.debug:
                                print "hadd -f {CHN}_{CAT}_{TYPE}_{PERIOD}_{LOG}.root {ROOT}".format(CHN=chn, CAT=cat, TYPE=type, LOG="LOG" if log[options.analysis][chn,cat][idx] else "LIN",  PERIOD = per, ROOT=' '.join(rootfiles_LOG) if log[options.analysis][chn,cat][idx]=="true" else ' '.join(rootfiles_LIN))
                                print "root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C+\\(\\\"{CHN}_{CAT}_{TYPE}_{PERIOD}_{LOG}.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",\\\"{EXTRA2}\\\",{MIN},{MAX},{LOG}\)".format(
                                    CMSSW_BASE=os.environ['CMSSW_BASE'],
                                    CHN=chn,
                                    CAT=cat,
                                    TYPE=type,
                                    PERIOD=per,
                                    LIN="LOG" if log[options.analysis][chn,cat][idx]=="true" else "LIN",
                                    ANA=options.analysis.upper(),
                                    LABEL="2011+2012",
                                    EXTRA=extra[chn],
                                    EXTRA2=cat,
                                    MIN=min[options.analysis][chn,cat][idx],
                                    MAX=max[options.analysis][chn,cat][idx],
                                    LOG=log[options.analysis][chn,cat][idx]
                                    )
                            os.system("hadd -f {CHN}_{CAT}_{TYPE}_{PERIOD}_{LOG}.root {ROOT}".format(CHN=chn, CAT=cat, TYPE=type, LOG="LOG" if log[options.analysis][chn,cat][idx] else "LIN", PERIOD = per, ROOT=' '.join(rootfiles_LOG) if log[options.analysis][chn,cat][idx]=="true" else ' '.join(rootfiles_LIN)))
                            os.system("root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C+\\(\\\"{CHN}_{CAT}_{TYPE}_{PERIOD}_{LIN}.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",\\\"{EXTRA2}\\\",{MIN},{MAX},{LOG}\)".format(
                                CMSSW_BASE=os.environ['CMSSW_BASE'],
                                CHN=chn,
                                CAT=cat,
                                TYPE=type,
                                PERIOD=per,
                                LIN="LOG" if log[options.analysis][chn,cat][idx]=="true" else "LIN",
                                ANA=options.analysis.upper(),
                                LABEL="2011+2012",
                                EXTRA=extra[chn],
                                EXTRA2=cat,
                                MIN=min[options.analysis][chn,cat][idx],
                                MAX=max[options.analysis][chn,cat][idx],
                                LOG=log[options.analysis][chn,cat][idx]
                                ))
            ## combine 7TeV and 8TeV if it is requested
            if per == "7TeV_8TeV":
                for idx in range(len(min[options.analysis][chn,cat])):
                    if options.debug:
                        print "hadd -f {CHN}_{CAT}_{TYPE}_7TeV_8TeV_{LOG}.root {CHN}_{CAT}_{TYPE}_7TeV_{LOG}.root {CHN}_{CAT}_{TYPE}_8TeV_{LOG}.root".format(
                            CHN=chn, CAT=cat, TYPE=type, LOG="LOG" if log[options.analysis][chn,cat][idx]=="true" else "LIN")
                        print "root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C+\\(\\\"{CHN}_{CAT}_{TYPE}_7TeV_8TeV_{LIN}.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",\\\"{EXTRA2}\\\",{MIN},{MAX},{LOG}\)".format(
                            CMSSW_BASE=os.environ['CMSSW_BASE'],
                            CHN=chn,
                            CAT=cat,
                            TYPE=type,
                            LIN="LOG" if log[options.analysis][chn,cat][idx]=="true" else "LIN",
                            ANA=options.analysis.upper(),
                            LABEL="2011+2012",
                            EXTRA=extra[chn],
                            EXTRA2=cat,
                            MIN=min[options.analysis][chn,cat][idx],
                            MAX=max[options.analysis][chn,cat][idx],
                            LOG=log[options.analysis][chn,cat][idx]
                            )
                    os.system("hadd -f {CHN}_{CAT}_{TYPE}_7TeV_8TeV_{LOG}.root {CHN}_{CAT}_{TYPE}_7TeV_{LOG}.root {CHN}_{CAT}_{TYPE}_8TeV_{LOG}.root".format(
                        CHN=chn, CAT=cat, TYPE=type, LOG="LOG" if log[options.analysis][chn,cat][idx]=="true" else "LIN"))
                    os.system("root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C+\\(\\\"{CHN}_{CAT}_{TYPE}_7TeV_8TeV_{LIN}.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",\\\"{EXTRA2}\\\",{MIN},{MAX},{LOG}\)".format(
                        CMSSW_BASE=os.environ['CMSSW_BASE'],
                        CHN=chn,
                        CAT=cat,
                        TYPE=type,
                        LIN="LOG" if log[options.analysis][chn,cat][idx]=="true" else "LIN",
                        ANA=options.analysis.upper(),
                        LABEL="2011+2012",
                        EXTRA=extra[chn],
                        EXTRA2=cat,
                        MIN=min[options.analysis][chn,cat][idx],
                        MAX=max[options.analysis][chn,cat][idx],
                        LOG=log[options.analysis][chn,cat][idx]
                        ))
