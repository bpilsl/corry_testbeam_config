"""
Simple script for getting histograms out of .root file and creating a .pdf 
file from them. 


python3 pdf_maker.py --ifile=Histos-<something>.root

Author: Benjamin Schwenker <benjamin.schwenker@phys.uni-goettingen.de>  
"""

import ROOT
import os
import glob
import argparse


selected_keys = [
    "AnalysisDUT/Monopix2_0/local_residuals/residualsX",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsX1pix",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsX2pix",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsX3pix",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsY",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsY1pix",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsY2pix",
    "AnalysisDUT/Monopix2_0/local_residuals/residualsY3pix",
    "AnalysisDUT/Monopix2_0/seedChargeVsColAssoc",
    "AnalysisDUT/Monopix2_0/hitMapAssoc",
    "AnalysisDUT/Monopix2_0/clusterChargeAssociated",
    "AnalysisDUT/Monopix2_0/seedChargeAssociated",
    "AnalysisDUT/Monopix2_0/clusterSizeAssociated",
    "AnalysisDUT/Monopix2_0/clusterWidthRowAssociated",
    "AnalysisDUT/Monopix2_0/clusterWidthColAssociated",
    "AnalysisEfficiency/Monopix2_0/pixelEfficiencyMap_trackPos",
    "AnalysisEfficiency/Monopix2_0/chipEfficiencyMap_trackPos",
    "AnalysisEfficiency/Monopix2_0/distanceTrackHit2D",
    "AnalysisEfficiency/Monopix2_0/eTotalEfficiency",
    "AnalysisEfficiency/Monopix2_0/efficiencyColumns",
    "AnalysisEfficiency/Monopix2_0/efficiencyRows",
]


def make_pdf(filename):
    
    # Open files with reconstructed run data 
    f = ROOT.TFile( filename) 

    pdfName = os.path.splitext( os.path.basename( filename ) )[0] + '.pdf'
    
    c1 = ROOT.TCanvas("c1","",10,10,1100,700)
    c1.SetRightMargin(0.2)
  
    for key in selected_keys: #histofile.GetListOfKeys():

        print(key)
        obj = f.Get(key)
        
        if obj.InheritsFrom("TH1"):
            h1 = obj.Clone()
            c1.Clear()
            c1.cd()
            c1.SetName(key)
            c1.SetTitle(key)
      
            if  h1.InheritsFrom("TH2"): 
                h1.Draw("colz")
            else: 
                h1.Draw()
      
            ROOT.gPad.Modified()
            ROOT.gPad.Update()   
            c1.Print(pdfName+"(","pdf")

        elif obj.InheritsFrom("TEfficiency"):
      
            e  = obj.Clone()
            c1.Clear()
            c1.cd()
            c1.SetName(key)
            c1.SetTitle(key)
            e.Draw()
      
            ROOT.gPad.Modified()
            ROOT.gPad.Update()   
            c1.Print(pdfName+"(","pdf")

  
    c1.Print(pdfName+")","pdf")
    f.Close()

parser = argparse.ArgumentParser(description="Perform plotting of test beam runs")
parser.add_argument('--ifile', dest='ifile', default='*', type=str, help='Input file pattern of runs to process')
args = parser.parse_args()


for inputfilename in glob.glob(args.ifile): 

    # Make a pdf containing all plots 
    make_pdf(inputfilename)

    