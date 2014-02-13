#include "HiggsAnalysis/HiggsToTauTau/interface/PlotLimits.h"


/// This is the core plotting routine that can also be used within
/// root macros. It is therefore not element of the PlotLimits class.
void plottingTanb(TCanvas& canv, TGraphAsymmErrors* plain, TGraphAsymmErrors* plain_low, TGraphAsymmErrors* innerBand, TGraphAsymmErrors* innerBand_low, TGraphAsymmErrors* outerBand, TGraphAsymmErrors* outerBand_low, TGraph* expected, TGraph* expected_low, TGraph* observed, TGraph* observed_low, TGraph* lowerLEP, TGraph* upperLEP, std::map<double, TGraphAsymmErrors*> higgsBands, std::map<std::string, TGraph*> comparisons, std::string& xaxis, std::string& yaxis, std::string& theory, TGraph* injected=0, double min=0., double max=50., bool log=false, bool transparent=false);

void
PlotLimits::plotTanb(TCanvas& canv, TGraphAsymmErrors* innerBand, TGraphAsymmErrors* innerBand_low, TGraphAsymmErrors* outerBand, TGraphAsymmErrors* outerBand_low, TGraph* expected, TGraph* expected_low, TGraph* observed, TGraph* observed_low, const char* directory)
{
  //different MSSM scenarios
  std::string extralabel_ = "";
  const char* model;
  if(theory_=="MSSM m_{h}^{max} scenario") {extralabel_= "mhmax-"; model = "mhmax-mu+200";}
  if(theory_=="MSSM m_{h}^{mod-} scenario") {extralabel_= "mhmodm-"; model = "mhmodm";}
  if(theory_=="MSSM m_{h}^{mod+} scenario") {extralabel_= "mhmodp-"; model = "mhmodp";}
  if(theory_=="MSSM low m_{H} scenario") {extralabel_= "lowmH-"; model = "lowmH";}
  if(theory_=="MSSM light stau scenario") {extralabel_= "lightstau1-"; model = "lightstau1";}
  if(theory_=="MSSM tauphobic scenario") {extralabel_= "tauphobic-"; model = "tauphobic";}

  // set up styles
  SetStyle();

  // create plain background
  TGraphAsymmErrors* plain=0;
  if(observed){
    plain=new TGraphAsymmErrors();
    plain->SetPoint(0, observed->GetX()[0], 100.);
    plain->SetPointEYlow (0, 0);
    plain->SetPointEYhigh(0, 100); 
    for(unsigned int imass=0, ipoint=0; imass<bins_.size(); ++imass){
      if(valid_[imass] && observed->GetX()[ipoint]>10){
	plain->SetPoint(ipoint+1, observed->GetX()[ipoint], observed->GetY()[ipoint]); 
	plain->SetPointEYlow (ipoint+1, 0);
 	plain->SetPointEYhigh(ipoint+1, 100);
	//std::cout << ipoint << " " << observed->GetN() << " " << observed->GetX()[ipoint] << std::endl;
	++ipoint;
      }
    }
    plain->SetPoint(observed->GetN(), observed->GetX()[observed->GetN()-1], 100.);
    plain->SetPointEYlow (observed->GetN(), 0);
    plain->SetPointEYhigh(observed->GetN(), 100); 
  }

  TGraphAsymmErrors* plain_low=0;
  if(observed_low){
    plain_low=new TGraphAsymmErrors();
    plain_low->SetPoint(0, observed_low->GetX()[0], 0.5);
    plain_low->SetPointEYlow (0, 0);
    plain_low->SetPointEYhigh(0, 0); 
    //std::cout << observed_low->GetX()[0] << " " << observed_low->GetN() << std::endl;
    for(int imass=0, ipoint=0; imass<observed_low->GetN(); ++imass){
      if(valid_[imass]){
	plain_low->SetPoint(ipoint+1, observed_low->GetX()[ipoint], observed_low->GetY()[ipoint]); 
	plain_low->SetPointEYlow (ipoint+1, observed_low->GetY()[ipoint]-0.5);
 	plain_low->SetPointEYhigh(ipoint+1, 0);
	//std::cout << ipoint << " " << observed_low->GetN() << " " << observed_low->GetX()[ipoint] << std::endl;
	++ipoint;
	}
    }
    plain_low->SetPoint(observed_low->GetN(), observed_low->GetX()[observed_low->GetN()-1], 0.5);
    plain_low->SetPointEYlow (observed_low->GetN(), 0);
    plain_low->SetPointEYhigh(observed_low->GetN(), 0); 
    //std::cout << observed_low->GetX()[observed_low->GetN()-1] << std::endl;
  }

  // create LEP exclusion plot
  TGraph* upperLEP = new TGraph();
  upperLEPLimits(upperLEP);

  TGraph* lowerLEP = new TGraph();
  lowerLEPLimits(lowerLEP);

  // create plots for additional comparisons
  std::map<std::string, TGraph*> comparisons; TGraph* comp=0;
  if(arXiv_1211_6956_){ comp = new TGraph(), arXiv_1211_6956 (comp); comp->SetName("arXiv_1211_6956" ); comparisons[std::string("ATLAS H#rightarrow#tau#tau (4.8/fb)")] = comp;}
  if(arXiv_1204_2760_){ comp = new TGraph(); arXiv_1204_2760 (comp); comp->SetName("arXiv_1204_2760" ); comparisons[std::string("ATLAS H^{+} (4.6/fb)")               ] = comp;}
  //if(arXiv_1302_2892_){ comp = new TGraph(); arXiv_1302_2892 (comp); comp->SetName("arXiv_1302_2892" ); comparisons[std::string("CMS bbH#rightarrow 3b (4.8/fb)")     ] = comp;}
  if(arXiv_1302_2892_){ comp = new TGraph(); arXiv_1302_2892 (comp); comp->SetName("arXiv_1302_2892" ); comparisons[std::string("CMS #phi#rightarrowb#bar{b}")     ] = comp;}
  if(arXiv_1205_5736_){ comp = new TGraph(); arXiv_1205_5736 (comp); comp->SetName("arXiv_1205_5736" ); comparisons[std::string("CMS H^{+} (2/fb)")                   ] = comp;}
  if(HIG_12_052_     ){ comp = new TGraph(); HIG_12_052_lower(comp); comp->SetName("HIG_12_052_lower"); comparisons[std::string("CMS H^{+} (2-4.9/fb)")               ] = comp;}
  if(HIG_12_052_     ){ comp = new TGraph(); HIG_12_052_upper(comp); comp->SetName("HIG_12_052_upper"); comparisons[std::string("EMPTY")                              ] = comp;}

  // setup contratins from Higgs mass
  std::map<double, TGraphAsymmErrors*> higgsBands;
  if(higgs125_){
    higgsBands[3] = higgsConstraint(directory, 125.5, 3., model); //3.
    //higgsBands[2] = higgsConstraint(directory, 125.5, 2., model);
    //higgsBands[1] = higgsConstraint(directory, 125.5, 1., model);
    //for(unsigned int deltaM=0; deltaM<3; ++deltaM){
    //  higgsBands[3-deltaM] = higgsConstraint(directory, 125., 4-deltaM, model);
    //}
  }
  
  // this one is not supported here (see in macros/plotTanb.C to use this option - requires some manual work)
  TGraph* injected=0;
  // do the plotting 
  plottingTanb(canv, plain, plain_low, innerBand, innerBand_low, outerBand, outerBand_low, expected, expected_low, observed, observed_low, lowerLEP, upperLEP, higgsBands, comparisons, xaxis_, yaxis_, theory_, injected, min_, max_, log_, transparent_);
  /// setup the CMS Preliminary
  CMSPrelim(dataset_.c_str(), "", 0.145, 0.840); // 0.835->0.840
  // TPaveText* cmsprel  = new TPaveText(0.145, 0.835+0.06, 0.145+0.30, 0.835+0.16, "NDC");
//   cmsprel->SetBorderSize(   0 );
//   cmsprel->SetFillStyle(    0 );
//   cmsprel->SetTextAlign(   12 );
//   cmsprel->SetTextSize ( 0.03 );
//   cmsprel->SetTextColor(    1 );
//   cmsprel->SetTextFont (   62 );
//   cmsprel->AddText(dataset_.c_str());
//   cmsprel->Draw();

  // write results to files
  if(png_){
    canv.Print(std::string(output_).append("_").append(extralabel_).append(label_).append(".png").c_str());
  }
  if(pdf_){
    canv.Print(std::string(output_).append("_").append(extralabel_).append(label_).append(".pdf").c_str());
    canv.Print(std::string(output_).append("_").append(extralabel_).append(label_).append(".eps").c_str());
  }
  if(txt_){
    print(std::string(output_).append("_").append(extralabel_).append(label_).c_str(), outerBand, innerBand, expected, observed, "txt");
    print(std::string(output_).append("_").append(extralabel_).append(label_).c_str(), outerBand, innerBand, expected, observed, "tex");
  }
  if(root_){
    TFile* output = new TFile(std::string("limits_").append(extralabel_).append(label_).append(".root").c_str(), "update");
    if(!output->cd(output_.c_str())){
      output->mkdir(output_.c_str());
      output->cd(output_.c_str());
    }
    if(observed){ 
      observed ->Write("observed" );
      if(observed_low) observed_low ->Write("observed_low" );
    }
    expected ->Write("expected" );
    innerBand->Write("innerBand");
    outerBand->Write("outerBand");
    if(expected_low) expected_low ->Write("expected_low" );
    if(innerBand_low) innerBand_low->Write("innerBand_low");
    if(outerBand_low) outerBand_low->Write("outerBand_low");
    // auxiliary graphs
    if(extralabel_=="mhmax-") upperLEP->Write("upperLEP");
    if(extralabel_=="mhmax-") lowerLEP->Write("lowerLEP");
    if(plain) plain->Write("plain");
    if(plain_low) plain_low->Write("plain_low");
    
    for(std::map<std::string, TGraph*>::const_iterator comp=comparisons.begin(); comp!=comparisons.end(); ++comp){
      comp->second->Write();
    }
    output->Close();
  }
  return;
}

