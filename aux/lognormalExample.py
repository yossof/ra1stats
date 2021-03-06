#!/usr/bin/env python

import ROOT as r

def stamp(keep = [], mode = "", gauss = None, lognormal = None, sigmaValue = None) :
    text = r.TLatex()
    text.SetNDC()

    text.SetTextColor(r.kBlack)
    x0 = 0.47
    y0 = 0.88
    s = 0.025
    if mode=="x" :
        keep.append( text.DrawLatex(x0, y0-1*s, "#mu = %3.1f"%mu.getVal()) )
        keep.append( text.DrawLatex(x0, y0-2*s, "#sigma = %4.2f"%sigmaValue) )
        keep.append( text.DrawLatex(x0, y0-3*s, kSpec["stamp"] ) )
    if mode=="mu" :
        keep.append( text.DrawLatex(x0, y0-1*s, "x = %3.1f"%x.getVal()) )
        keep.append( text.DrawLatex(x0, y0-2*s, "#sigma = %4.2f"%sigmaValue) )
        keep.append( text.DrawLatex(x0, y0-3*s, kSpec["stamp"] ) )
    for i,item in enumerate([gauss, lognormal]) :
        name = item.GetName()
        text.SetTextColor(color[name])
        keep.append( text.DrawLatex(x0, y0-s*(4+i), name+"(x|  #mu, %s)"%("#sigma" if item==gauss else "k")) )

def plot(sigmaValues = [], maxes = []) :
    canvas = r.TCanvas()
    canvas.Divide(len(sigmaValues), 1)

    keep = []
    for i,sigmaValue in enumerate(sigmaValues) :
        canvas.cd(1+i)
        #http://www.physics.ucla.edu/~cousins/stats/cousins_lognormal_prior.pdf
        sigma = r.RooRealVar("sigma","width of gaussian", sigmaValue) #fixed
        k     = r.RooRealVar("k","shape param. for log-normal", kSpec["func"](sigmaValue)) #fixed

        gauss     = r.RooGaussian("gauss","gaussian PDF", x, mu, sigma)
        lognormal = r.RooLognormal("lognormal","lognormal PDF", x, mu, k)

        frame = (x if mode=="x" else mu).frame()

        for item in [gauss, lognormal] :
            item.plotOn(frame)
            frame.getAttLine().SetLineColor(color[item.GetName()])

        frame.SetTitle("")
        frame.Draw()
        if maxes : frame.SetMaximum(maxes[i])

        stamp(keep, mode, gauss, lognormal, sigmaValue)

        r.gPad.SetTickx()
        r.gPad.SetTicky()
        #r.gPad.SetLogy()

    canvas.cd(0)
    canvas.Print("llk_vs_%s__%s.pdf"%(mode,kSpec["tag"]))

color = {"gauss":r.kRed, "lognormal":r.kBlue}
kSpec = [{"func":lambda x:1+x, "stamp":"k = 1+#sigma", "tag":"k.onePlus"},
         {"func":lambda x:r.TMath.Exp(x), "stamp":"k = exp(#sigma)", "tag":"k.exp"},
         ][0]

for mode in ["x", "mu"] :
    if mode=="x" :
        x     = r.RooRealVar("x", "observation (x)", 1.0, 0.0, 3.0) #observable
        mu    = r.RooRealVar("mu","mean of gaussian (#mu)", 1.0) #fixed mean

    if mode=="mu" :
        x     = r.RooRealVar("x", "observation (x)", 1.0) #fixed observation
        mu    = r.RooRealVar("mu","mean of gaussian (#mu)", 1.0, 0.0, 3.0) #floating paramter in range [0-3]

    plot(sigmaValues = [0.10, 0.20,  0.26, 0.40 ],
         maxes       = [0.14, 0.075, 0.06, 0.042],
         )
