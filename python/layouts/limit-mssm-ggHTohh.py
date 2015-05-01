import FWCore.ParameterSet.Config as cms

layout = cms.PSet(
    ## dataset
    dataset = cms.string("H#rightarrowhh#rightarrow#tau#taubb, e#tau_{h}+#mu#tau_{h}+#tau_{h}#tau_{h}"),	
    lumi = cms.string("19.7 fb^{-1} (8 TeV)"),
    #dataset = cms.string("CMS Preliminary, H #rightarrow #tau #tau, 18.3 fb^{-1} at 8 TeV"),
    ## extra labels (below legend)
    extra = cms.string(""),	
    #extra = cms.string("gg#rightarrow#phi bb set to zero"),
    ## x-axis title
    xaxis = cms.string("m_{H} [GeV]"),
    ## x-axis title
    yaxis = cms.string("95% CL limit on #sigma(gg#rightarrowH)#timesBR(H#rightarrowhh#rightarrow#tau#taubb) [pb]"),
    ## min for plotting
    min = cms.double(0.01),
    ## max for plotting
    max = cms.double(5.), ## 200. 100000.
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
    verbosity = cms.uint32(0),
    ## define output label
    outputLabel = cms.string("ggHTohh-limit"), 
    ## define masspoints for limit plot
    masspoints = cms.vdouble(
   260.
   ,270.
   ,280.
   ,290.
   ,300.
   ,310.
   ,320.
   ,330.
   ,340.
   ,350.
    ),
    ## SM like limit without the line at sigma=1
    mssm_nolog = cms.bool(True),
    mssm_ = cms.bool(True),
    ## plot expected only
    expectedOnly = cms.bool(False),
    ## mass label for the injected signal print band in different layout for signal injected
    injectedMass=cms.string("125"),    
    ## print band in different layout for signal injected
    injected=cms.bool(False),
)
