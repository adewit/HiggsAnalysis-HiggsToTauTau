import FWCore.ParameterSet.Config as cms

layout = cms.PSet(
    ## dataset
    #dataset = cms.string("#scale[1.5]{CMS}   h,H,A#rightarrow#tau#tau                     19.7 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)"),
    #dataset = cms.string("#scale[1.5]{CMS} (unpublished), h,H,A#rightarrow#tau#tau, 19.7 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)"),
    #dataset = cms.string("#scale[1.5]{CMS} Preliminary, h,H,A#rightarrow#tau#tau, 19.7 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)"),
    #dataset = cms.string("#scale[1.5]{CMS}   h,H,A#rightarrow#tau#tau                                           18.3 fb^{-1} (8 TeV)"),
    #dataset = cms.string("#scale[1.5]{CMS}   h,H,A#rightarrow#tau#tau                                           19.7 fb^{-1} (8 TeV)"),
    dataset = cms.string("A#rightarrowZh#rightarrow#it{ll}#tau#tau"),
    lumi = cms.string("19.7 fb^{-1} (8 TeV)"),
    prelimtext = cms.string("Unpublished"),    
    ## x-axis title
    xaxis = cms.string("cos(#beta-#alpha)"),
    ## y-axis title
    yaxis = cms.string("#bf{tan#beta}"),
    ## theory label 
    theory = cms.string("2HDM type-II"),
    ## min for plotting
    min = cms.double(0.1),
    ## max for plotting
    max = cms.double(10),
    ## min for plotting
    log = cms.int32(0),
    ## print to png
    png = cms.bool(True),
    ## print to pdf
    pdf = cms.bool(True),
    ## print to txt
    txt = cms.bool(True),
    ## print to root
    root = cms.bool(True),
    ## define verbosity level
    verbosity = cms.uint32(3),
    outputLabel = cms.string("cosba-tanb-azh") ,
    ## define masspoints for limit plot
    masspoints = cms.vdouble(
   -1
   ,-0.98
   ,-0.96
   ,-0.94
   ,-0.92
   ,-0.9
   ,-0.88
   ,-0.86
   ,-0.84
   ,-0.82
   ,-0.8
   ,-0.78
   ,-0.76
   ,-0.74
   ,-0.72
   ,-0.7 
   ,-0.68
   ,-0.66
   ,-0.64
   ,-0.62
   ,-0.6
   ,-0.58
   ,-0.56
   ,-0.54
   ,-0.52
   ,-0.5
   ,-0.48
   ,-0.46
   ,-0.44
   ,-0.42
   ,-0.4
   ,-0.38
   ,-0.36
   ,-0.34
   ,-0.32
   ,-0.3
   ,-0.28
   ,-0.26
   ,-0.24
   ,-0.22
   ,-0.2 
   ,-0.18
   ,-0.16
   ,-0.14
   ,-0.12
   ,-0.1 
   ,-0.08
   ,-0.06
   ,-0.04
   ,-0.02
   ,0 
   ,0.02
   ,0.04
   ,0.06
   ,0.08
   ,0.1
   ,0.12
   ,0.14
   ,0.16
   ,0.18
   ,0.2
   ,0.22
   ,0.24
   ,0.26
   ,0.28
   ,0.3
   ,0.32
   ,0.34
   ,0.36
   ,0.38
   ,0.4
   ,0.42
   ,0.44
   ,0.46
   ,0.48
   ,0.5
   ,0.52
   ,0.54
   ,0.56
   ,0.58
   ,0.6
   ,0.62
   ,0.64
   ,0.66
   ,0.68
   ,0.7
   ,0.72
   ,0.74
   ,0.76
   ,0.78
   ,0.8
   ,0.82
   ,0.84
   ,0.86
   ,0.88
   ,0.9
   ,0.92
   ,0.94
   ,0.96
   ,0.98
   ,1
     ),
    ## is this mssm?
    mssm = cms.bool(True),
    ## is this MSSMvsSM?
    MSSMvsSM = cms.bool(False),
    ## plot in Brazilian colors?
    Brazilian = cms.bool(False),
    ## plot transparent?
    transparent = cms.bool(True),
    ## print the 2-sigma band
    outerband = cms.bool(True),
    ## plot expected only
    expectedOnly = cms.bool(False),
    ## use TGraph2D interpolation 
    FitMethod  = cms.int32(2),
    ## print constraints from mH=125GeV
    higgs125 = cms.bool(True),
    ## add arXiv-1211-6956 (ATLAS) to plot
    arXiv_1211_6956 = cms.bool(False),
    ## add arXiv-1204-2760 (ATLAS) to plot
    arXiv_1204_2760 = cms.bool(False),
    ## add arXiv-1302-2892
    arXiv_1302_2892 = cms.bool(False),
    ## add arXiv-1205-5736
    arXiv_1205_5736 = cms.bool(False),
    ## add HIG-12-052
    HIG_12_052 = cms.bool(False),
)
