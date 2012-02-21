from inputData import orig,mixedMuons,afterAlphaT,afterAlphaT_b,mixedMuons_b,mixedMuons_b_sets

class selection(object) :
    '''Each key appearing in samplesAndSignalEff is used in the likelihood;
    the corresponding value determines whether signal efficiency is considered for that sample.'''

    def __init__(self, name = "", samplesAndSignalEff = {}, data = None, alphaTMinMax = (None, None), 
                 nbTag = None, bTagLower = None, universalSystematics = False, universalKQcd = False, zeroQcd = False) :
        for item in ["name", "samplesAndSignalEff", "data", "alphaTMinMax",
                     "nbTag", "bTagLower", "universalSystematics", "universalKQcd", "zeroQcd"] :
            setattr(self, item, eval(item))

class spec(dict) :
    def __init__(self, simpleOneBin = False, qcdSearch = False) :
        self._selections = []
        self.load()

        #for compatibility; to be rewritten
        d = self

        if simpleOneBin :
            assert False
            d["simpleOneBin"] = {"b":3.0}
            key = max(d["alphaT"].keys())
            d["alphaT"] = {key: {"samples": [("had", True)]} }
        else :
            d["simpleOneBin"] = {}
    
        d["selections"] = self.selections()
        d["REwk"] = ["", "Linear", "FallingExp", "Constant"][0]
        d["RQcd"] = ["Zero", "FallingExp", "FallingExpA"][1]
        d["nFZinv"] = ["All", "One", "Two"][2]
        d["qcdSearch"] = qcdSearch
        d["constrainQcdSlope"] = True
    
    def selections(self) :
        return self._selections

    def add(self, sel = None) :
        self._selections.append(sel)

    def load(self) :
        slices = False
        b = True
        multib = False

        assert sum([slices,b,multib]) == 1
        
        if slices :
            self.add(selection(name = "55",
                               alphaTMinMax = ("55", None),
                               samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               data = afterAlphaT.data_55_v1(),
                               universalSystematics = True,
                               universalKQcd = True,
                               )
                     )
            self.add(selection(name = "53",
                               alphaTMinMax = ("53", "55"),
                               samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               data = afterAlphaT.data_53_v1(),
                               )
                     )
            self.add(selection(name = "52",
                               alphaTMinMax = ("52", "53"),
                               samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               data = afterAlphaT.data_52_v1(),
                               )
                     )
        if b :
            self.add(selection(name = "55b_mixed",
                               alphaTMinMax = ("55", None),
                               samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               data = mixedMuons_b.data_55_v1(),
                               bTagLower = "0",
                               universalSystematics = True,
                               universalKQcd = True,
                               )
                     )

        if multib :
            self.add(selection(name = "55b_0btag",
                               alphaTMinMax = ("55", None),
                               #samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               samplesAndSignalEff = {"had":True, "muon":True, "mumu":False},
                               data = mixedMuons_b_sets.data_55_0btag(),
                               nbTag = "0",
                               universalSystematics = True,
                               universalKQcd = True,
                               )
                     )
            self.add(selection(name = "55b_1btag",
                               alphaTMinMax = ("55", None),
                               #samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               samplesAndSignalEff = {"had":True, "muon":True, "mumu":False},
                               data = mixedMuons_b_sets.data_55_1btag(),
                               nbTag = "1",
                               )
                     )
            self.add(selection(name = "55b_2btag",
                               alphaTMinMax = ("55", None),
                               #samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               samplesAndSignalEff = {"had":True, "muon":True, "mumu":False},
                               data = mixedMuons_b_sets.data_55_2btag(),
                               nbTag = "2",
                               )
                     )
            self.add(selection(name = "55b_gt2btag",
                               alphaTMinMax = ("55", None),
                               #samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                               samplesAndSignalEff = {"had":True, "muon":True, "mumu":False},
                               data = mixedMuons_b_sets.data_55_gt2btag(),
                               bTagLower = "2",
                               )
                     )
        #self.add(selection(name = "2010",
        #                   samplesAndSignalEff = {"had":True, "muon":True, "phot":False},
        #                   data = inputData.data2010(),
        #                   )
        #         )
