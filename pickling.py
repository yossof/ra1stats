import os
import utils

import configuration as conf
import histogramProcessing as hp
from inputData import rootToTxt
import signalPoint

import ROOT as r


def histoList(histos={}):
    out = []
    for key, value in histos.iteritems():
        for item in value:
            if not hasattr(item, "GetBinContent"):
                continue
            out.append(item)
    return out


def writeSignalFiles(points=[], outFilesAlso=False):
    args = {}
    
    for model in conf.signal.models():
        args[model.name] = {"eff": hp.effHistos(model),
                            "xs": hp.xsHisto(model),
                            "sumWeightIn": hp.sumWeightInHisto(model),
                            "effUncRel": conf.signal.effUncRel(model.name),
                        }
        toCheck = [args[model.name]["xs"], args[model.name]["sumWeightIn"]]
        toCheck += histoList(args[model.name]["eff"])
        rootToTxt.checkHistoBinning(toCheck)

    for point in points:
        name = point[0]
        signal = signalPoint.signalModel(modelName=name, point3=point[1:], **args[name])
        stem = conf.directories.pickledFileName(*point)
        utils.writeNumbers(fileName=stem+".in", d=signal)
        if not outFilesAlso:
            continue
        utils.writeNumbers(fileName=stem+".out", d=signal)


##merge functions
def mergedFile(model=None):
    tags = [conf.limit.method()]
    if "CLs" in conf.limit.method():
        tags += [conf.limit.calculatorType(),
                 #"TS%d" % conf.limit.testStatistic()
                 ]
    if conf.limit.binaryExclusion():
        tags.append("binaryExcl")
    tags.append(model.name)
    if not model.isSms:
        tags.append(model.xsVariation)

    return "".join([conf.directories.mergedFile()+"/",
                    "_".join(tags + [model.llk] + model.whiteList),
                    ".root"
                    ])


def contents(fileName):
    out = {}
    t = utils.readNumbers(fileName)
    if t:
        signal, results = t
        out.update(results)
        out.update(signal.flattened())
    return out


def mergePickledFiles(printExamples=False):
    examples = {}
    histos = {}
    zTitles = {}

    for model in conf.signal.models():
        name = model.name
        examples[name] = hp.xsHisto(model)
        histos[name] = {}
        zTitles[name] = {}
        if printExamples:
            print "Here are the example binnings for %s:" % name
            for c in ["X", "Y", "Z"]:
                print " ".join(["%s:" % c,
                                str(getattr(examples[name],
                                            "GetNbins%s" % c)()),
                                str(getattr(examples[name],
                                            "Get%saxis" % c)().GetXmin()),
                                str(getattr(examples[name],
                                            "Get%saxis" % c)().GetXmax()),
                                ])

    for name, iX, iY, iZ in hp.points():
        fileName = conf.directories.pickledFileName(name, iX, iY, iZ)+".out"
        if not os.path.exists(fileName):
            print "skipping file", fileName
            continue

        for key, value in contents(fileName).iteritems():
            if key not in histos[name]:
                histos[name][key] = examples[name].Clone(name+"_"+key)
                histos[name][key].Reset()
            histos[name][key].SetBinContent(iX, iY, iZ, value[0])
            zTitles[name][key] = value[1]

        os.remove(fileName)
        os.remove(fileName.replace(".out", ".in"))

    for model in conf.signal.models():
        f = r.TFile(mergedFile(model=model), "RECREATE")
        for key, histo in histos[model.name].iteritems():
            histo.GetZaxis().SetTitle(zTitles[model.name][key])
            histo.Write()
        f.Close()
