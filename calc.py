import math,array,copy,collections
import utils
import plotting
import ROOT as r
from common import obs,pdf,wimport,pseudoData

def plInterval(dataset, modelconfig, wspace, note, smOnly, cl = None, makePlots = True, poiList = []) :
    assert poiList
    out = {}
    calc = r.RooStats.ProfileLikelihoodCalculator(dataset, modelconfig)
    calc.SetConfidenceLevel(cl)
    lInt = calc.GetInterval()

    assert wspace.var(poiList[0]), "%s not in workspace"%poiList[0]
    out["lowerLimit"] = lInt.LowerLimit(wspace.var(poiList[0]))
    out["upperLimit"] = lInt.UpperLimit(wspace.var(poiList[0]))

    ##doesn't work
    #status = r.std.vector('bool')()
    #status.push_back(False)
    #out["upperLimit"] = lInt.UpperLimit(wspace.var("f"), status.front())
    #out["status"] = status.at(0)

    ##doesn't work
    #status = array.array('c', ["a"])
    #out["upperLimit"] = lInt.UpperLimit(wspace.var("f"), status)
    #out["status"] = ord(status[0])

    ##perhaps works but offers no information
    #out["upperLimit"] = lInt.UpperLimit(wspace.var("f"))
    #out["status"] = lInt.FindLimits(wspace.var("f"), r.Double(), r.Double())

    if makePlots :
        canvas = r.TCanvas()
        canvas.SetTickx()
        canvas.SetTicky()
        psFile = "intervalPlot_%s_%g.pdf"%(note, 100*cl)
        plot = r.RooStats.LikelihoodIntervalPlot(lInt)
        plot.Draw(); print
        canvas.Print(psFile)

    utils.delete(lInt)
    return out

def fcExcl(dataset, modelconfig, wspace, note, smOnly, cl = None, makePlots = True) :
    assert not smOnly

    f = r.RooRealVar("f", "f", 1.0)
    poiValues = r.RooDataSet("poiValues", "poiValues", r.RooArgSet(f))
    r.SetOwnership(poiValues, False) #so that ~FeldmanCousins() can delete it
    points = [1.0]
    for point in [0.0] + points :
        f.setVal(point)
        poiValues.add(r.RooArgSet(f))
        
    out = {}
    calc = r.RooStats.FeldmanCousins(dataset, modelconfig)
    calc.SetPOIPointsToTest(poiValues)
    calc.FluctuateNumDataEntries(False)
    calc.UseAdaptiveSampling(True)
    #calc.AdditionalNToysFactor(4)
    #calc.SetNBins(40)
    #calc.GetTestStatSampler().SetProofConfig(r.RooStats.ProofConfig(wspace, 1, "workers=4", False))
    
    calc.SetConfidenceLevel(cl)
    lInt = calc.GetInterval()

    out["upperLimit"] = lInt.UpperLimit(wspace.var("f"))
    return out

def ts1(wspace = None, data = None, snapSb = None, snapB = None, snapfHat = None, verbose = False) :
        wspace.loadSnapshot(snapSb)
        nll = pdf(wspace).createNLL(data)
        sbLl = -nll.getVal()
        utils.delete(nll)
        
        wspace.loadSnapshot(snapB)
        nll = pdf(wspace).createNLL(data)
        bLl = -nll.getVal()
        utils.delete(nll)

        return -2.0*(sbLl-bLl)

def ts10(wspace = None, data = None, snapSb = None, snapB = None, snapfHat = None, verbose = False) :
        wspace.loadSnapshot(snapSb)
        results = utils.rooFitResults(pdf(wspace), data)
        if verbose :
            print "S+B"
            print "---"            
            results.Print("v")
        sbLl = -results.minNll()
        utils.delete(results)
        
        wspace.loadSnapshot(snapB)
        results = utils.rooFitResults(pdf(wspace), data)
        if verbose :
            print " B "
            print "---"            
            results.Print("v")        
        bLl = -results.minNll()
        utils.delete(results)

        out = -2.0*(sbLl-bLl)
        if verbose : print "TS:",out
        return out

def ts4(wspace = None, data = None, snapSb = None, snapB = None, snapfHat = None, verbose = False) :
        wspace.loadSnapshot(snapB)
        nll = pdf(wspace).createNLL(data)
        bLl = -nll.getVal()
        utils.delete(nll)
        return bLl

def ts40(wspace = None, data = None, snapSb = None, snapB = None, snapfHat = None, verbose = False) :
        wspace.loadSnapshot(snapB)
        results = utils.rooFitResults(pdf(wspace), data)
        if verbose :
            print " B "
            print "---"            
            results.Print("v")        
        out = -results.minNll()
        utils.delete(results)

        if verbose : print "TS:",out
        return out

def ts(testStatType = None, **args) :
    if testStatType==1 : return ts1(**args)
    if testStatType==2 : return ts2(**args)
    if testStatType==3 : return ts3(**args)
    if testStatType==4 : return ts4(**args)

def clsCustom(wspace, data, nToys = 100, smOnly = None, testStatType = None, note = "", plots = True) :
    assert not smOnly

    toys = {}
    for label,f in {"b":0.0, "sb":1.0, "fHat":None}.iteritems() :
        if f!=None :
            wspace.var("f").setVal(f)
            wspace.var("f").setConstant()
        else :
            wspace.var("f").setVal(1.0)
            wspace.var("f").setConstant(False)
        results = utils.rooFitResults(pdf(wspace), data)
        wspace.saveSnapshot("snap_%s"%label, wspace.allVars())
        toys[label] = pseudoData(wspace, nToys)
        utils.delete(results)

    args = {"wspace": wspace, "testStatType": testStatType, "snapSb": "snap_sb", "snapB": "snap_b", "snapfHat": "snap_fHat"}
    obs = ts(data = data, **args)

    out = {}
    values = collections.defaultdict(list)
    for label in ["b", "sb"] :
        for toy in toys[label] : 
            values[label].append(ts(data = toy, **args))
        out["CL%s"%label] = 1.0-utils.indexFraction(obs, values[label])
    if plots : plotting.clsCustomPlots(obs = obs, valuesDict = values, note = "TS%d_%s"%(testStatType, note))

    out["CLs"] = out["CLsb"]/out["CLb"] if out["CLb"] else 9.9
    return out

def cls(dataset = None, modelconfig = None, wspace = None, smOnly = None, cl = None, nToys = None, calculatorType = None, testStatType = None,
        plusMinus = {}, note = "", makePlots = None, nWorkers = None, nPoints = 1, poiMin = 1.0, poiMax = 1.0) :
    assert not smOnly

    wimport(wspace, dataset)
    wimport(wspace, modelconfig)

    #from StandardHypoTestInvDemo.C
    opts = {
        "PlotHypoTestResult": False,
        "WriteResult": False,
        "Optimize": True,
        "UseVectorStore": True,
        "GenerateBinned": False,
        "UseProof": nWorkers>1,
        "Rebuild": False,
        "NWorkers": nWorkers,
        "NToyToRebuild": 100,
        "PrintLevel": 0,
        "InitialFit": -1,
        "RandomSeed": -1,
        "NToysRatio": 2,
        "MaxPOI": -1.0,
        "MassValue": "",
        "MinimizerType": "",
        "ResultFileName": "",
        }

    hypoTestInvTool = r.RooStats.HypoTestInvTool()
    for key,value in opts.iteritems() :
        hypoTestInvTool.SetParameter(key, value)

    ctd = {"frequentist":0, "asymptotic":2, "asymptoticNom":3}
    result = hypoTestInvTool.RunInverter(wspace, #RooWorkspace * w,
                                         "modelConfig", "", #const char * modelSBName, const char * modelBName,
                                         "dataName", ctd[calculatorType], testStatType, #const char * dataName, int type,  int testStatType,
                                         True, nPoints, poiMin, poiMax, #bool useCLs, int npoints, double poimin, double poimax,
                                         nToys, #int ntoys,
                                         True, #bool useNumberCounting = false,
                                         "") #const char * nuisPriorName = 0);

    out = {}
    args = {}
    for iPoint in range(nPoints) :
        s = "" if not iPoint else "_%d"%iPoint
        out["CLb%s"     %s] = result.CLb(iPoint)
        out["CLs+b%s"   %s] = result.CLsplusb(iPoint)
        out["CLs%s"     %s] = result.CLs(iPoint)
        out["CLsError%s"%s] = result.CLsError(iPoint)
        out["PoiValue%s"%s] = result.GetXValue(iPoint)
        args["CLs%s"%s] = out["CLs%s"%s]
    
    if nPoints==1 and poiMin==poiMax :
        for item in ["testStatType", "plusMinus", "note", "makePlots", "nPoints"] :
            args[item] = eval(item)
        args["result"] = result
        args["poiPoint"] = poiMin
        args["testStatisticType"] = testStatType
        q = clsOnePoint(args)
        for key,value in q.iteritems() :
            assert not (key in out),"%s %s"%(key, str(out))
            out[key] = value
    else :
        out["UpperLimit"] = result.UpperLimit()
        out["UpperLimitError"] = result.UpperLimitEstimatedError()
        out["LowerLimit"] = result.LowerLimit()
        out["LowerLimitError"] = result.LowerLimitEstimatedError()
        
    return out

def prunedValues(values, weights) :
    assert values.size()==weights.size(),"%d!=%d"%(values.size(), weights.size())
    blackList = [float("inf"), float("-inf"), float("nan")]
    good = []
    bad = []
    for value,weight in zip(values, weights) :
        if value in blackList :
            bad.append( (value, weight) )
        else :
            good.append( (value, weight) )
    return sorted(good),len(bad)

def tsHisto(name = "", lo = None, hi = None, valuesWeights = [], nBad = 0) :
    xMin = 0.0
    #xMin = lo - (hi-lo)/10.
    xMax = hi + (hi-lo)/10.
    out = r.TH1D(name, ";TS;toys / bin", 100, xMin, xMax)
    out.Sumw2()
    for value,weight in valuesWeights :
        out.Fill(value, weight)
    for i in range(nBad) :
        out.Fill(xMax)
    return out

def clsOnePoint(args) :
    result = args["result"]
    iPoint = result.FindIndex(args["poiPoint"])

    if iPoint<0 :
        print "WARNING: No index for POI value %g.  Will use 0."%args["poiPoint"]
        iPoint = 0

    values = result.GetExpectedPValueDist(iPoint).GetSamplingDistribution()
    q,hist = quantiles(values, args["plusMinus"], histoName = "expected_CLs_distribution",
                       histoTitle = "expected CLs distribution;CL_{s};toys / bin",
                       histoBins = (205, -1.0, 1.05), cutZero = False)

    if args["makePlots"] :
        ps = "cls_%s_TS%d.ps"%(args["note"], args["testStatType"])
        canvas = r.TCanvas()
        canvas.Print(ps+"[")
        
        resultPlot = r.RooStats.HypoTestInverterPlot("HTI_Result_Plot", "", result)
        resultPlot.Draw("CLb 2CL")
        canvas.Print(ps)

        text = r.TText()
        text.SetNDC()

        rootFile = r.TFile(ps.replace(".ps", ".root"), "RECREATE")
        
        for i in range(args["nPoints"]) :
            if False :
                tsPlot = resultPlot.MakeTestStatPlot(i)
                tsPlot.Print("v")
                #tsPlot.SetLogYaxis(True)
                tsPlot.Draw()
            else :
                #following this code:
                #http://root.cern.ch/root/html/RooStats__SamplingDistPlot.html#RooStats__SamplingDistPlot:AddSamplingDistribution
                bDist = result.GetBackgroundTestStatDist(i)
                sbDist = result.GetSignalAndBackgroundTestStatDist(i)
                if (not bDist) or (not sbDist) : continue
                b,nBadB   = prunedValues(bDist.GetSamplingDistribution(),   bDist.GetSampleWeights())
                sb,nBadSb = prunedValues(sbDist.GetSamplingDistribution(), sbDist.GetSampleWeights())
                lo = min(b[ 0][0], sb[ 0][0])
                hi = max(b[-1][0], sb[-1][0])

                bHist = tsHisto("bDist%d"%i,  lo, hi,  b, nBadB)
                bHist.Write()
                sbHist = tsHisto("sbDist%d"%i, lo, hi, sb, nBadSb)
                sbHist.Write()

                h = r.TH1D("testStatisticType%d"%i, "testStatisticType", 1, 0, 1)
                h.SetBinContent(1, args["testStatisticType"])
                h.Write()
                
                htr = result.GetResult(i)
                h = r.TH1D("tsObs%d"%i, "observed TS", 1, 0, 1)
                h.SetBinContent(1, htr.GetTestStatisticData())
                h.Write()
                for base in ["CLb", "CLs", "CLsplusb"] :
                    for error in ["", "Error"] :
                        item = base + error
                        h = r.TH1D("%s%d"%(item, i), item, 1, 0, 1)
                        h.SetBinContent(1, getattr(htr, item)())
                        h.Write()
                
            text.DrawText(0.1, 0.95, "Point %d"%i)
            canvas.Print(ps)

        rootFile.Close()
        leg = plotting.drawDecoratedHisto(quantiles = q, hist = hist, obs = args["CLs"])
        text.DrawText(0.1, 0.95, "Point %d"%iPoint)
        canvas.Print(ps)
        
        canvas.Print(ps+"]")
        utils.ps2pdf(ps)
    return q

def profilePlots(dataset, modelconfig, note) :
    canvas = r.TCanvas()
    canvas.SetTickx()
    canvas.SetTicky()
    psFile = "profilePlots_%s.pdf"%note
    canvas.Print(psFile+"[")

    plots = r.RooStats.ProfileInspector().GetListOfProfilePlots(dataset, modelconfig); print
    for i in range(plots.GetSize()) :
        plots.At(i).Draw("al")
        canvas.Print(psFile)
    canvas.Print(psFile+"]")
    #utils.ps2pdf(psFile)

def limits(wspace, snapName, modelConfig, smOnly, cl, datasets, makePlots = False, poi = ["f"]) :
    out = []
    for i,dataset in enumerate(datasets) :
        wspace.loadSnapshot(snapName)
        #dataset.Print("v")
        interval = plInterval(dataset, modelConfig, wspace, note = "", smOnly = smOnly, cl = cl, makePlots = makePlots, poi = poi)
        out.append(interval["upperLimit"])
    return sorted(out)

def quantiles(values = [], plusMinus = {}, histoName = "", histoTitle = "", histoBins = [], cutZero = None) :
    def histoFromList(l, name, title, bins, cutZero = False) :
        h = r.TH1D(name, title, *bins)
        for item in l :
            if cutZero and (not item) : continue
            h.Fill(item)
        return h
    
    def probList(plusMinus) :
        def lo(nSigma) : return ( 1.0-r.TMath.Erf(nSigma/math.sqrt(2.0)) )/2.0
        def hi(nSigma) : return 1.0-lo(nSigma)
        out = []
        out.append( (0.5, "Median") )
        for key,n in plusMinus.iteritems() :
            out.append( (lo(n), "MedianMinus%s"%key) )
            out.append( (hi(n), "MedianPlus%s"%key)  )
        return sorted(out)

    def oneElement(i, l) :
        return map(lambda x:x[i], l)
    
    pl = probList(plusMinus)
    probs = oneElement(0, pl)
    names = oneElement(1, pl)
    
    probSum = array.array('d', probs)
    q = array.array('d', [0.0]*len(probSum))

    h = histoFromList(values, name = histoName, title = histoTitle, bins = histoBins, cutZero = cutZero)
    h.GetQuantiles(len(probSum), q, probSum)
    return dict(zip(names, q)),h
    
def expectedLimit(dataset, modelConfig, wspace, smOnly, cl, nToys, plusMinus, note = "", makePlots = False) :
    assert not smOnly
    
    #fit to SM-only
    wspace.var("f").setVal(0.0)
    wspace.var("f").setConstant(True)
    results = utils.rooFitResults(pdf(wspace), dataset)

    #generate toys
    toys = pseudoData(wspace, nToys)

    #restore signal model
    wspace.var("f").setVal(1.0)
    wspace.var("f").setConstant(False)

    #save snapshot
    snapName = "snap"
    wspace.saveSnapshot(snapName, wspace.allVars())

    #fit toys
    l = limits(wspace, snapName, modelConfig, smOnly, cl, toys)

    q,hist = quantiles(l, plusMinus, histoName = "upperLimit", histoTitle = ";upper limit on XS factor;toys / bin", histoBins = (50, 1, -1), cutZero = True) #enable auto-range
    nSuccesses = hist.GetEntries()

    obsLimit = limits(wspace, snapName, modelConfig, smOnly, cl, [dataset])[0]

    if makePlots : plotting.expectedLimitPlots(quantiles = q, hist = hist, obsLimit = obsLimit, note = note)
    return q,nSuccesses

def nSigma(quantile = None) :
    return r.TMath.ErfInverse(2.0*quantile - 1.0)*math.sqrt(2.0)

def poisMedian(mu = None) :
    assert mu,mu
    med = mu + 1/3.0# - 0.02/mu
    return int(med)

def poisMode(mu = None) :
    return int(mu)

def poisPull(n = None, mu = None) :
    out = {}

    out["n"] = n
    out["mu"] = mu
    out["median"] = poisMedian(mu)
    out["mode"] = poisMode(mu)

    assert mu,mu
    out["simple"] = (n-mu)/math.sqrt(mu)

    assert float(int(n))==n,n
    out["quantile"] = r.Math.poisson_cdf(int(n), mu)
    out["quantileOfMode"] = r.Math.poisson_cdf(out["mode"], mu)

    out["nSigma"] = nSigma(out["quantile"])
    out["nSigmaOfMode"] = nSigma(out["quantileOfMode"])
    out["nSigmaPrime"] = out["nSigma"] - out["nSigmaOfMode"]
    return out

def printPoisPull(dct = {}) :
    def n(h, f) :
        return max(len(h), int(f[1]))
    headers = ["n",   "mu",    "mode", "simple", "nSigma", "nSigmaPrime", "quantile", "quantileOfMode", "nSigmaOfMode"]
    formats = ["%4d", "%7.2f", "%5d",  "%6.2f",  "%6.2f",  "%6.2f",       "%4.2f",    "%4.2f",          "%6.2f"       ]

    if not dct :
        lst = [h.rjust(n(h,f)) for h,f in zip(headers,formats)]
        s = "  ".join(lst)
        print s
        print "-"*len(s)
    else :
        lst = [(f%dct[h]).rjust(n(h,f)) for h,f in zip(headers,formats)]
        print "  ".join(lst)

def pulls(pdf = None) :
    out = {}
    className = pdf.ClassName()
    pdfName = pdf.GetName()

    if className=="RooProdPdf" :
        pdfList = pdf.pdfList()
        for i in range(pdfList.getSize()) :
            out.update(pulls(pdfList[i]))
    elif className=="RooPoisson" :
        p = r.Poisson(pdf)
        x = p.x.arg().getVal()
        mu = p.mean.arg().getVal()
        out[("Pois", pdfName)] = poisPull(x, mu)
    elif className=="RooGaussian" :
        g = r.Gaussian(pdf)
        x = g.x.arg().getVal()
        mu = g.mean.arg().getVal()
        sigma = g.sigma.arg().getVal()
        assert sigma,sigma
        out[("Gaus", pdfName)] = {"simple": (x-mu)/sigma}
    else :
        assert False,className
    return out

def pullHistoTitle(termType = "", key = "") :
    if termType=="Pois" :
        dct = {"simple":      '(n-#mu)/sqrt(#mu)',
               "nSigma":      'quantile of n in Pois( k | #mu )   [in "sigma"]',
               "nSigmaPrime": 'quantile of n [in "sigma"] - quantile of mode [in "sigma"]',
               }
        return "Poisson terms;;"+dct[key]
    elif termType=="Gaus" :
        return "Gaussian terms;;(x-#mu)/#sigma"
    else :
        assert False,termType

def pullHisto(termType = "", pulls = {}, title = "") :
    p = {}
    for key,value in pulls.iteritems() :
        if key[0]!=termType : continue
        p[key[1]] = value

    h = r.TH1D("%sPulls"%termType, title, len(p), 0.5, 0.5+len(p))
    for i,key in enumerate(sorted(p.keys())) :
        h.SetBinContent(1+i, p[key])
        if termType=="Pois" :
            try:
                sample,sel,nB,iHt = key.split("_")
            except:
                print key
                exit()
            sample = sample.replace(termType,"")
            nB = nB.replace("gt2","3")
            if not int(iHt)%2 :
                label = "%s  %s  %s"%(sample,nB,iHt)
            else :
                label = ""
            h.GetXaxis().SetBinLabel(1+i, label)
        elif termType=="Gaus" :
            h.GetXaxis().SetBinLabel(1+i, key)
    return h

def pullPlots(pdf = None, nParams = None, threshold = 2.0, yMax = 3.5,
              poisKey = ["simple", "nSigma", "nSigmaPrime"][0],
              gausKey = "simple", debug = False,
              note = "", plotsDir = "") :

    pRaw = pulls(pdf)

    if debug :
        printPoisPull()
        for key in sorted(pRaw.keys()) :
            if key[0]!="Pois" : continue
            printPoisPull(pRaw[key])

    p = {}
    for key,value in pRaw.iteritems() :
        if key[0]=="Pois" :
            p[key] = value[poisKey]
        elif key[0]=="Gaus" :
            p[key] = value[gausKey]
        else :
            assert False,key

    canvas = r.TCanvas()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetGridy()

    fileName = "%s/pulls_%s.pdf"%(plotsDir, note)
    canvas.Print(fileName+"[")
    canvas.SetBottomMargin(0.15)

    line = r.TLine()
    line.SetLineColor(r.kBlue)

    total = r.TH1D("total", ";pull;terms / bin", 100, -yMax, yMax)
    chi2 = 0
    nTerms = 0
    for termType in ["Pois", "Gaus"] :
        h = pullHisto(termType, p)
        h.SetTitle(pullHistoTitle(termType, key = eval(termType.lower()+"Key")))
        h.SetStats(False)
        h.SetMarkerStyle(20)
        h.Draw("p")

        assert abs(h.GetMinimum())<yMax,h.GetMinimum()
        assert abs(h.GetMaximum())<yMax,h.GetMaximum()
        h.GetYaxis().SetRangeUser(-yMax, yMax)

        h2 = h.Clone("%s_outliers")
        h2.Reset()
        lines = []
        for iBin in range(1, 1+h.GetNbinsX()) :
            content = h.GetBinContent(iBin)
            chi2 += content*content
            nTerms += 1
            total.Fill(content)
            if abs(content)>threshold :
                h2.SetBinContent(iBin, content)
                l2 = line.DrawLine(iBin, -yMax, iBin, content)
                lines.append(l2)
            else :
                h2.SetBinContent(iBin, -9999)
        h2.SetMarkerColor(r.kBlue)
        h2.Draw("psame")
        canvas.Print(fileName)

    nDof = nTerms-nParams
    print "\"chi2\"  =",chi2
    print "nTerms  =",nTerms
    print "nParams =",nParams
    print "nDof    =",nDof
    print "prob    =",r.TMath.Prob(chi2, nDof)
    total.Draw()
    canvas.Print(fileName)
    canvas.Print(fileName+"]")
