#!/usr/bin/env python

import ROOT as r
import refXsProcessing as rxs
import os

def setup() :
    r.gROOT.SetBatch(True)
    r.gErrorIgnoreLevel = 2000
    r.gROOT.SetStyle("Plain")
    r.gStyle.SetPalette(1)

def mother(model) :
    return {"T1": "gluino", "T2": "squark"}[model]

def ranges(model) :
    d = {}
    d["smsXRange"] = (400.0, 999.9) #(min, max)
    d["smsYRange"] = (100.0, 975.0)
    d["smsXsZRangeLin"]          = (0.0, 40.0, 40) #(zMin, zMax, nContours)
    d["smsXsZRangeLog"]          = (0.4, 40.0, 40)
    d["smsEffZRange"]            = (0.0, 0.60, 30)
    d["smsLimZRange"]            = (0.0, 40.0, 40)
    d["smsLimLogZRange"]         = (0.1, 80.0, 40)
    d["smsLim_NoThUncLogZRange"] = (0.1, 20.0, 20)

    d["smsEffUncExpZRange"] = (0.0, 0.20, 20)
    d["smsEffUncThZRange"]  = (0.0, 0.50, 50)
    return d

def specs() :
    d = {}
    d["printC"] = True
    d["printTxt"] = False
    d["pruneAndExtrapolateGraphs"] = True
    d["oldBehavior"] = True
    d["yValueToPrune"] = 100.0
    
    dir = "/home/hep/elaird1/60_ra_comparison"
    d["razor"] = {"T1_Eff": ("%s/razor/v2/t1_eff.root"%dir,"hist"),
                  "T2_Eff": ("%s/razor/v2/t2_eff.root"%dir,"hist"),
                  "T1_Lim": ("%s/razor/v2/t1_limit.root"%dir,"hist"),
                  "T2_Lim": ("%s/razor/v2/t2_limit.root"%dir,"hist"),
                  "T1_Lim_NoThUnc": ("%s/razor/v3_noThUnc/t1_limit.root"%dir,"LimitT1"),
                  "T2_Lim_NoThUnc": ("%s/razor/v3_noThUnc/t2_limit.root"%dir,"LimitT2"),
                  "name": "Razor",
                  "shiftX": False,
                  "shiftY": False,
                  }

    d["ra2"] = {"T1_Eff": ("%s/ra2/v2/t1_eff.root"%dir,"DefaultAcceptance"),
                "T2_Eff": ("%s/ra2/v2/t2_eff.root"%dir,"DefaultAcceptance"),
                "T1_Lim": ("%s/ra2/v3/t1_limit.root"%dir,"hlimit_gluino_T1_MHT"),
                "T2_Lim": ("%s/ra2/v3/t2_limit.root"%dir,"hlimit_squark_T2_MHT"),
                "T1_Lim_NoThUnc": ("%s/ra2/v4_NoThUnc/t1_limit.root"%dir,"hlimit_gluino_T1_MHT"),
                "T2_Lim_NoThUnc": ("%s/ra2/v4_NoThUnc/t2_limit.root"%dir,"hlimit_squark_T2_MHT"),
                "T1_EffUncExp": ("%s/ra2/v2/t1_effUncExp.root"%dir,"ExpRelUnc_gluino_T1_MHT"),
                "T2_EffUncExp": ("%s/ra2/v2/t2_effUncExp.root"%dir,"ExpRelUnc_squark_T2_MHT"),
                "T1_EffUncTh":  ("%s/ra2/v2/t1_effUncTh.root"%dir,"theoryUnc_gluino_T1_MHT"),
                "T2_EffUncTh":  ("%s/ra2/v2/t2_effUncTh.root"%dir,"theoryUnc_squark_T2_MHT"),
                "name": "Jets +",
                "name2": "Missing HT",
                "shiftX": False,
                "shiftY": True,
                }

    d["ra1"] = {"T1_Eff": ("%s/ra1/v1/T1_eff.root"%dir,"m0_m12_0"),
                "T2_Eff": ("%s/ra1/v1/T2_eff.root"%dir,"m0_m12_0"),
                "T1_Lim": ("%s/ra1/v1/profileLikelihood_T1_lo_1HtBin_expR_xsLimit.root"%dir,"UpperLimit_2D"),
                "T2_Lim": ("%s/ra1/v1/profileLikelihood_T2_lo_1HtBin_expR_xsLimit.root"%dir,"UpperLimit_2D"),
                "T1_Lim_NoThUnc": ("%s/ra1/v1_noThUnc/profileLikelihood_T1_lo_1HtBin_expR_xsLimit.root"%dir,"UpperLimit_2D"),
                "T2_Lim_NoThUnc": ("%s/ra1/v1_noThUnc/profileLikelihood_T2_lo_1HtBin_expR_xsLimit.root"%dir,"UpperLimit_2D"),
                "T1_EffUncExp": ("%s/ra1/v1/T1_effUncRelExp.root"%dir,"effUncRelExperimental_2D"),
                "T2_EffUncExp": ("%s/ra1/v1/T2_effUncRelExp.root"%dir,"effUncRelExperimental_2D"),
                "T1_EffUncTh":  ("%s/ra1/v1/T1_effUncRelTh.root"%dir,"effUncRelTheoretical_2D"),
                "T2_EffUncTh":  ("%s/ra1/v1/T2_effUncRelTh.root"%dir,"effUncRelTheoretical_2D"),
                "name": "#alpha_{T}",
                "shiftX": True,
                "shiftY": True,
                }

    d["combined"] = {
                "name":  "Hadronic",
                "name2": "Searches",
                }
    return d

def binByBinMin(histos) :
    def minContent(histos, x, y) :
        return min(map(lambda h:h.GetBinContent(h.FindBin(x, y)), histos))

    h = histos[0]
    out = h.Clone("combined_min")
    out.Reset()
    for iBinX in range(1, 1+h.GetNbinsX()) :
        x = h.GetXaxis().GetBinCenter(iBinX)
        for iBinY in range(1, 1+h.GetNbinsY()) :
            y = h.GetYaxis().GetBinCenter(iBinY)
            out.Fill(x, y, minContent(histos, x, y))
    return out
    
def shifted(h, shiftX, shiftY) :
    binWidthX = (h.GetXaxis().GetXmax() - h.GetXaxis().GetXmin())/h.GetNbinsX() if shiftX else 0.0
    binWidthY = (h.GetYaxis().GetXmax() - h.GetYaxis().GetXmin())/h.GetNbinsY() if shiftY else 0.0

    if binWidthX or binWidthY : print "INFO: shifting %s by (%g, %g)"%(h.GetName(), binWidthX, binWidthY)
    out = r.TH2D(h.GetName()+"_shifted","",
                 h.GetNbinsX(), h.GetXaxis().GetXmin() - binWidthX/2.0, h.GetXaxis().GetXmax() - binWidthX/2.0,
                 h.GetNbinsY(), h.GetYaxis().GetXmin() - binWidthY/2.0, h.GetYaxis().GetXmax() - binWidthY/2.0,
                 )

    for iBinX in range(1, 1+h.GetNbinsX()) :
        for iBinY in range(1, 1+h.GetNbinsY()) :
            out.SetBinContent(iBinX, iBinY, h.GetBinContent(iBinX, iBinY))
    return out

def freshHisto(h) :
    out = r.TH2D(h.GetName()+"_fresh","",
                 h.GetNbinsX(), h.GetXaxis().GetXmin(), h.GetXaxis().GetXmax(),
                 h.GetNbinsY(), h.GetYaxis().GetXmin(), h.GetYaxis().GetXmax(),
                 )
    for iBinX in range(1, 1+h.GetNbinsX()) :
        for iBinY in range(1, 1+h.GetNbinsY()) :
            out.SetBinContent(iBinX, iBinY, h.GetBinContent(iBinX, iBinY))
    return out

def fetchHisto(file, dir, histo, name) :
    f = r.TFile(file)
    hOld = f.Get("%s/%s"%(dir, histo))
    assert hOld, "%s %s %s"%(file, dir, histo)
    h = hOld.Clone(name)
    h.SetDirectory(0)
    f.Close()
    return freshHisto(h)

def setRange(var, ranges, histo, axisString) :
    if var not in ranges : return
    nums = ranges[var]
    getattr(histo,"Get%saxis"%axisString)().SetRangeUser(*nums[:2])
    #if len(nums)==3 : r.gStyle.SetNumberContours(nums[2])
    if axisString=="Z" :
        maxContent = histo.GetBinContent(histo.GetMaximumBin())
        if maxContent>nums[1] :
            print "ERROR: histo truncated in Z (maxContent = %g, maxSpecified = %g) %s"%(maxContent, nums[1], histo.GetName())

def adjust(h) :
    h.UseCurrentStyle()
    h.SetStats(False)
    for a,size,offset in zip([h.GetXaxis(), h.GetYaxis(), h.GetZaxis()],
                             [1.5, 1.5,  1.3],
                             [1.0, 1.05, 1.0],
                             ) :
        a.CenterTitle(False)
        a.SetTitleSize(size*a.GetTitleSize())
        a.SetTitleOffset(offset)
    
def printText(h, tag, ana) :
    out = open("%s_%s.txt"%(tag, ana), "w")
    for iBinX in range(1, 1+h.GetNbinsX()) :
        x = h.GetXaxis().GetBinCenter(iBinX)
        for iBinY in range(1, 1+h.GetNbinsY()) :
            y = h.GetYaxis().GetBinCenter(iBinY)
            c = h.GetBinContent(iBinX, iBinY)
            out.write("%g %g %g\n"%(x,y,c))
    out.close()

def plotMulti(model = "", suffix = "", zAxisLabel = "", analyses = [], logZ = False, combined = False) :
    def preparedHistograms(analyses, key, zAxisLabel) :
        out = []
        for ana in analyses :
            d = specs()[ana]
            if key not in d :
                h = None
            else :
                h = fetchHisto(d[key][0], "/", d[key][1], name = "%s_%s"%(tag, ana))
                h = shifted(h, d["shiftX"], d["shiftY"])
                adjust(h)
                h.SetTitle(";m_{%s} (GeV); m_{LSP} (GeV);%s"%(mother(model), zAxisLabel))
            out.append(h)
        return out
    
    rangeDict = ranges(model)
    key = "%s_%s"%(model, suffix)
    tag = "%s%s"%(key, "_logZ" if logZ else "")

    histos = preparedHistograms(analyses, key, zAxisLabel)

    if combined :
        analyses = ["combined"]
        histos = [binByBinMin(histos)]
        
    c = r.TCanvas("canvas_%s"%tag,"canvas", 500*len(analyses), 500)
    c.Divide(len(analyses), 1)

    out = []
    for i,ana in enumerate(analyses) :
        c.cd(i+1)
        r.gPad.SetTopMargin(0.15)
        r.gPad.SetBottomMargin(0.15)
        r.gPad.SetLeftMargin(0.15)
        r.gPad.SetRightMargin(0.15)
        if logZ : r.gPad.SetLogz(True)

        h = histos[i]
        h.Draw("colz")

        if specs()["printTxt"] : printText(h, tag, ana.upper())
        setRange("smsXRange", rangeDict, h, "X")
        setRange("smsYRange", rangeDict, h, "Y")
        setRange("sms%s%sZRange"%(suffix, "Log" if logZ else ""), rangeDict, h, "Z")
        if suffix[:3]=="Lim" :
            stuff = rxs.drawGraphs(rxs.graphs(h, model, "Center", specs()["pruneAndExtrapolateGraphs"], specs()["yValueToPrune"], specs()["oldBehavior"] ))
            out.append(stuff)
        out.append(stampCmsPrel())
        d = specs()[ana]
        out.append(stampName(d["name"], d["name2"] if "name2" in d else ""))
        out.append(h)
    printOnce(c, "%s%s.eps"%(tag, "_combined" if combined else ""))

def epsToPdf(fileName, tight = True) :
    if not tight : #make pdf
        os.system("epstopdf "+fileName)
        os.system("rm       "+fileName)
    else : #make pdf with tight bounding box
        epsiFile = fileName.replace(".eps",".epsi")
        os.system("ps2epsi "+fileName+" "+epsiFile)
        os.system("epstopdf "+epsiFile)
        os.system("rm       "+epsiFile)
        os.system("rm       "+fileName)
    #print "%s has been written."%fileName.replace(".eps",".pdf")

def stampCmsPrel() :
    y = 0.87
    text = r.TLatex()
    text.SetTextSize(0.9*text.GetTextSize())
    text.SetNDC()
    text.SetTextAlign(11)
    text.DrawLatex(0.1, y, "CMS Preliminary")
    text.SetTextAlign(21)
    text.DrawLatex(0.55, y, "L = 35/pb")
    text.SetTextAlign(31)
    text.DrawLatex(0.9, y, "#sqrt{s} = 7 TeV")
    return text

def stampName(name, name2) :
    text = r.TLatex()
    text.SetNDC()
    text.SetTextAlign(11)
    text.SetTextSize(1.0*text.GetTextSize())
    if name2 :
        text.DrawLatex(0.18, 0.66, name)
        text.DrawLatex(0.18, 0.60, name2)
    else :
        text.DrawLatex(0.18, 0.63, name)
    return text

def printOnce(canvas, fileName) :
    canvas.Print(fileName)
    if specs()["printC"] : canvas.Print(fileName.replace(".eps",".C"))
    epsToPdf(fileName)

def go(models, analyses, combined) :
    for model in models :
        #plotMulti(model = model, suffix = "Eff", zAxisLabel = "analysis efficiency", analyses = analyses)
        #plotMulti(model = model, suffix = "EffUncExp", zAxisLabel = "experimental unc.", analyses = analyses)
        #plotMulti(model = model, suffix = "EffUncTh", zAxisLabel = "theoretical unc.", analyses = analyses)
        ##plotMulti(model = model, suffix = "Lim", zAxisLabel = "limit on #sigma (pb)", analyses = analyses, logZ = False)
        #plotMulti(model = model, suffix = "Lim", zAxisLabel = "limit on #sigma (pb)", analyses = analyses, logZ = True, combined = combined)
        plotMulti(model = model, suffix = "Lim_NoThUnc", zAxisLabel = "limit on #sigma (pb)", analyses = analyses, logZ = True, combined = combined)
    return

setup()
go(models = ["T1", "T2"],
   analyses = ["ra1", "ra2", "razor"],
   combined = True,
   )