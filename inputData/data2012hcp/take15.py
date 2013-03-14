from data import data
import utils

assert False,"these numbers contain mistakes"

def common1(x) :
    x._lumi =  	{
        "mumu"  : 1.139e+04,
        "muon"  : 1.139e+04,
        "mcPhot": 1.157e+04,
        "phot"  : 1.157e+04,
        "mcHad" : 1.166e+04,
        "had"   : 1.166e+04,
        "mcMuon": 1.139e+04,
        "mcMumu": 1.139e+04,
	}

    x._triggerEfficiencies = {
        "hadBulk":       (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "muon":          (0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880),
        "phot":          (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "mumu":          (0.950, 0.960, 0.960, 0.970, 0.970, 0.970, 0.980, 0.980),
        }

    x._htBinLowerEdges = (275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0)
    x._htMaxForPlot    = 975.0
    x._htMeans         = (298.0, 348.0, 416.0, 517.0, 617.0, 719.0, 819.0, 1044.)

    x._observations["nPhot"] = tuple([None, None]+list(x._observations["nPhot"][2:]))

def common(x) :
    common1(x)

    #systBins = tuple([0]*4+[1]*2+[2]*2)
    systBins = tuple([0,1]+[2]*2+[3]*2+[4]*2)
    name = x.__class__.__name__

    if "ge2j" in name :
        systMagnitudes = (0.10, 0.10, 0.20, 0.20, 0.30)
        #x._observations["nHadBulk"] = (630453600, 286166200, 209611400, 69777150, 26101500, 20182300, 4745175, 4776350)
        x._triggerEfficiencies["had"] = (0.870, 0.986, 0.994, 1.000, 1.000, 1.000, 1.000, 1.000)
    elif "le3j" in name :
        #systMagnitudes = (0.10, 0.20, 0.20)
        systMagnitudes = (0.10, 0.10, 0.20, 0.20, 0.20)
        x._triggerEfficiencies["had"] = (0.891, 0.987, 0.990, 1.000, 1.000, 1.000, 1.000, 1.000)
        x._observations["nHadBulk"] = (487992800, 202369400, 134976100, 36965375, 12292400,  8301900, 1925125, 1768325)
    elif "ge4j" in name :
        #systMagnitudes = (0.10, 0.20, 0.30)
        systMagnitudes = (0.10, 0.10, 0.20, 0.20, 0.30)
        x._triggerEfficiencies["had"] = (0.837, 0.982, 0.997, 1.000, 1.000, 1.000, 1.000, 1.000)
        x._observations["nHadBulk"] = (142460800,  83796800,  74635300, 32811775, 13809100, 11880400, 2820050, 3008025)

    if "ge4b" in name :
        x._mergeBins = (0, 1, 2, 2, 2, 2, 2, 2)
        systMagnitudes = (0.25,)
        systBins = (0, 0, 0)
    else :
        x._mergeBins = None

    x._systBins = {
        "sigmaPhotZ": systBins,
        "sigmaMuonW": systBins,
        "sigmaMumuZ": systBins,
        }

    x._fixedParameters = {
        "sigmaPhotZ": systMagnitudes,
        "sigmaMuonW": systMagnitudes,
        "sigmaMumuZ": systMagnitudes,
        "k_qcd_nom":2.96e-2,
        "k_qcd_unc_inp":utils.quadSum([0.61e-2, 0.463e-2])
        }

class data_0b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 283.1, 198.9, 110.7, 51.6, 26.46, 19.68, ) ,
		"mcHad"              :   ( 1265.0, 497.6, 387.5, 252.0, 121.3, 56.22, 24.35, 20.55, ) ,
		"mcTtw"              :   ( 805.1, 316.8, 249.1, 153.3, 70.05, 32.76, 12.65, 12.09, ) ,
		"mcMuon"             :   ( 1803.0, 519.3, 900.1, 694.5, 375.5, 198.8, 105.4, 144.7, ) ,
		"mcZinv"             :   ( 460.1, 180.8, 138.5, 98.7, 51.23, 23.45, 11.7, 8.459, ) ,
		"mcMumu"             :   ( 132.7, 38.74, 64.05, 53.49, 33.04, 18.5, 10.43, 15.34, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 75.36, 9.632, 21.28, 9.732, 7.121, 5.205, 3.83, 4.704, ) ,
		"mcMumuErr"          :   ( 3.983, 2.685, 1.479, 1.098, 0.8711, 0.673, 0.4906, 0.5891, ) ,
		"mcHadErr"           :   ( 42.89, 20.1, 7.289, 5.447, 3.781, 2.503, 1.569, 1.549, ) ,
		"mcZinvErr"          :   ( 7.119, 4.249, 3.338, 2.57, 1.848, 1.213, 0.8688, 0.7011, ) ,
		"mcTtwErr"           :   ( 42.3, 19.65, 6.48, 4.802, 3.299, 2.19, 1.307, 1.381, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 15.38, 12.79, 9.295, 6.562, 4.45, 3.567, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 277.0, 180.0, 80.0, 44.0, 20.0, 17.0, ) ,
		"nHad"               :   ( 1012.0, 453.0, 373.0, 271.0, 112.0, 55.0, 15.0, 26.0, ) ,
		"nMuon"              :   ( 1398.0, 455.0, 639.0, 449.0, 263.0, 149.0, 61.0, 86.0, ) ,
		"nMumu"              :   ( 127.0, 22.0, 55.0, 56.0, 32.0, 11.0, 7.0, 7.0, ) ,
	}

        common(self)


class data_0b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 2452.0, 853.3, 300.1, 118.0, 44.62, 40.71, ) ,
		"mcHad"              :   ( 7002.0, 3006.0, 2097.0, 645.0, 225.3, 74.81, 29.83, 22.34, ) ,
		"mcTtw"              :   ( 3615.0, 1461.0, 1012.0, 293.9, 94.37, 28.89, 12.18, 8.185, ) ,
		"mcMuon"             :   ( 1.221e+04, 6671.0, 6183.0, 2567.0, 1094.0, 512.3, 262.3, 329.3, ) ,
		"mcZinv"             :   ( 3387.0, 1545.0, 1085.0, 351.1, 130.9, 45.92, 17.65, 14.16, ) ,
		"mcMumu"             :   ( 1272.0, 724.9, 707.5, 311.1, 135.7, 66.42, 34.76, 44.12, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 143.6, 41.61, 35.97, 28.38, 14.26, 9.924, 7.021, 7.967, ) ,
		"mcMumuErr"          :   ( 10.11, 6.551, 5.032, 2.631, 1.728, 1.197, 0.8743, 0.9885, ) ,
		"mcHadErr"           :   ( 114.2, 34.6, 17.31, 8.913, 5.286, 2.92, 1.827, 1.514, ) ,
		"mcZinvErr"          :   ( 19.28, 12.69, 9.374, 4.94, 3.043, 1.768, 1.102, 0.9782, ) ,
		"mcTtwErr"           :   ( 112.6, 32.19, 14.55, 7.419, 4.322, 2.324, 1.458, 1.156, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 46.93, 26.18, 15.97, 10.18, 5.706, 5.729, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 2387.0, 799.0, 245.0, 89.0, 31.0, 19.0, ) ,
		"nHad"               :   ( 6219.0, 2893.0, 1971.0, 557.0, 181.0, 59.0, 17.0, 27.0, ) ,
		"nMuon"              :   ( 9750.0, 5208.0, 4684.0, 1819.0, 776.0, 300.0, 150.0, 194.0, ) ,
		"nMumu"              :   ( 1344.0, 712.0, 629.0, 207.0, 120.0, 44.0, 21.0, 27.0, ) ,
	}

        common(self)


class data_1b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 46.48, 31.98, 15.58, 10.47, 5.646, 3.609, ) ,
		"mcHad"              :   ( 664.2, 263.2, 213.9, 121.7, 49.87, 21.72, 9.32, 8.294, ) ,
		"mcTtw"              :   ( 590.1, 234.0, 189.9, 105.0, 42.65, 17.19, 6.669, 6.528, ) ,
		"mcMuon"             :   ( 1603.0, 579.4, 894.0, 652.8, 335.5, 164.8, 83.23, 96.1, ) ,
		"mcZinv"             :   ( 74.11, 29.19, 24.0, 16.7, 7.216, 4.531, 2.651, 1.766, ) ,
		"mcMumu"             :   ( 33.57, 9.361, 18.28, 15.42, 9.121, 5.095, 2.337, 3.692, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 13.4, 6.264, 8.021, 6.499, 4.597, 3.238, 2.272, 2.37, ) ,
		"mcMumuErr"          :   ( 1.182, 0.5989, 0.7896, 0.6875, 0.5165, 0.4206, 0.2248, 0.3294, ) ,
		"mcHadErr"           :   ( 8.222, 4.665, 3.65, 2.619, 1.638, 0.9964, 0.6346, 0.6439, ) ,
		"mcZinvErr"          :   ( 1.383, 0.8047, 0.6673, 0.5017, 0.3055, 0.2519, 0.1991, 0.1515, ) ,
		"mcTtwErr"           :   ( 8.105, 4.595, 3.588, 2.57, 1.609, 0.964, 0.6025, 0.6258, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 2.754, 2.184, 1.404, 1.389, 0.9489, 0.64, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 58.0, 43.0, 17.0, 10.0, 7.0, 3.0, ) ,
		"nHad"               :   ( 510.0, 236.0, 209.0, 95.0, 48.0, 12.0, 13.0, 6.0, ) ,
		"nMuon"              :   ( 1378.0, 417.0, 598.0, 445.0, 206.0, 109.0, 55.0, 49.0, ) ,
		"nMumu"              :   ( 31.0, 7.0, 21.0, 15.0, 11.0, 3.0, 3.0, 4.0, ) ,
	}

        common(self)


class data_1b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 241.9, 82.58, 24.66, 14.29, 6.582, 4.958, ) ,
		"mcHad"              :   ( 1170.0, 515.7, 367.3, 95.68, 27.11, 10.53, 4.195, 2.685, ) ,
		"mcTtw"              :   ( 824.1, 355.6, 252.4, 59.18, 15.53, 5.092, 1.799, 1.023, ) ,
		"mcMuon"             :   ( 2931.0, 1856.0, 1535.0, 556.7, 211.8, 89.05, 41.63, 47.02, ) ,
		"mcZinv"             :   ( 346.1, 160.1, 115.0, 36.5, 11.58, 5.44, 2.396, 1.662, ) ,
		"mcMumu"             :   ( 175.5, 104.3, 95.87, 40.94, 16.38, 7.791, 3.624, 4.609, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 17.37, 11.44, 10.13, 6.102, 3.521, 2.158, 1.482, 1.523, ) ,
		"mcMumuErr"          :   ( 2.445, 1.843, 1.545, 0.8632, 0.5053, 0.311, 0.2208, 0.2477, ) ,
		"mcHadErr"           :   ( 12.12, 5.733, 4.329, 1.953, 0.9982, 0.5438, 0.2979, 0.197, ) ,
		"mcZinvErr"          :   ( 2.853, 1.885, 1.379, 0.6869, 0.3836, 0.2463, 0.1948, 0.1212, ) ,
		"mcTtwErr"           :   ( 11.78, 5.414, 4.103, 1.828, 0.9215, 0.4849, 0.2253, 0.1554, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 6.211, 3.277, 1.613, 1.533, 0.9816, 0.7512, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 292.0, 95.0, 27.0, 9.0, 4.0, 4.0, ) ,
		"nHad"               :   ( 1158.0, 466.0, 325.0, 96.0, 22.0, 8.0, 4.0, 1.0, ) ,
		"nMuon"              :   ( 2662.0, 1583.0, 1221.0, 411.0, 155.0, 51.0, 27.0, 26.0, ) ,
		"nMumu"              :   ( 183.0, 108.0, 102.0, 43.0, 18.0, 6.0, 2.0, 5.0, ) ,
	}

        common(self)


class data_2b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 5.677, 3.732, 2.579, 1.081, 0.4858, 0.2612, ) ,
		"mcHad"              :   ( 281.5, 112.9, 90.2, 53.3, 21.58, 7.965, 2.768, 3.126, ) ,
		"mcTtw"              :   ( 270.7, 109.0, 86.71, 51.14, 20.79, 7.421, 2.48, 2.958, ) ,
		"mcMuon"             :   ( 1026.0, 368.0, 557.0, 395.6, 203.1, 93.67, 46.19, 50.32, ) ,
		"mcZinv"             :   ( 10.86, 3.914, 3.491, 2.164, 0.7854, 0.5438, 0.2879, 0.1677, ) ,
		"mcMumu"             :   ( 13.36, 3.125, 7.02, 5.294, 2.916, 1.607, 0.423, 0.7882, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 7.11, 4.307, 5.281, 4.406, 3.069, 2.061, 1.37, 1.371, ) ,
		"mcMumuErr"          :   ( 0.8526, 0.3455, 0.5415, 0.4437, 0.3081, 0.2675, 0.08825, 0.1363, ) ,
		"mcHadErr"           :   ( 3.414, 2.237, 2.011, 1.533, 0.9361, 0.5313, 0.3008, 0.3227, ) ,
		"mcZinvErr"          :   ( 0.5781, 0.312, 0.2633, 0.1762, 0.1059, 0.07946, 0.0336, 0.0202, ) ,
		"mcTtwErr"           :   ( 3.365, 2.215, 1.994, 1.523, 0.9301, 0.5254, 0.2989, 0.3221, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 1.022, 0.7835, 0.6874, 0.2984, 0.08509, 0.04625, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 12.0, 12.0, 6.0, 1.0, 2.0, 2.0, ) ,
		"nHad"               :   ( 199.0, 108.0, 82.0, 56.0, 24.0, 5.0, 1.0, 2.0, ) ,
		"nMuon"              :   ( 825.0, 274.0, 389.0, 274.0, 148.0, 66.0, 26.0, 17.0, ) ,
		"nMumu"              :   ( 9.0, 4.0, 4.0, 7.0, 3.0, 1.0, 0.0, 2.0, ) ,
	}

        common(self)


class data_2b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 17.03, 4.351, 0.9665, 1.064, 0.4697, 0.2132, ) ,
		"mcHad"              :   ( 202.6, 95.48, 69.61, 16.44, 4.318, 1.179, 0.2653, 0.1273, ) ,
		"mcTtw"              :   ( 172.5, 81.31, 60.53, 13.62, 3.548, 0.8108, 0.1399, 0.04993, ) ,
		"mcMuon"             :   ( 988.5, 628.0, 506.9, 164.7, 58.27, 22.43, 8.701, 8.127, ) ,
		"mcZinv"             :   ( 30.12, 14.17, 9.078, 2.82, 0.7692, 0.3684, 0.1254, 0.07733, ) ,
		"mcMumu"             :   ( 40.96, 19.55, 16.12, 5.905, 2.229, 0.68, 0.3243, 0.3478, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 7.395, 5.935, 5.359, 3.049, 1.762, 1.049, 0.6331, 0.5666, ) ,
		"mcMumuErr"          :   ( 1.46, 0.9268, 0.7821, 0.4472, 0.2631, 0.08818, 0.08505, 0.08186, ) ,
		"mcHadErr"           :   ( 2.957, 2.057, 1.815, 0.8685, 0.4516, 0.1735, 0.04751, 0.01847, ) ,
		"mcZinvErr"          :   ( 0.9821, 0.6499, 0.438, 0.2166, 0.1121, 0.06318, 0.02195, 0.01394, ) ,
		"mcTtwErr"           :   ( 2.789, 1.952, 1.761, 0.841, 0.4375, 0.1615, 0.04213, 0.01211, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 2.192, 0.795, 0.2294, 0.4257, 0.1815, 0.04364, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 28.0, 5.0, 1.0, 1.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 221.0, 105.0, 58.0, 12.0, 5.0, 1.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 876.0, 498.0, 403.0, 120.0, 32.0, 7.0, 3.0, 4.0, ) ,
		"nMumu"              :   ( 45.0, 26.0, 15.0, 4.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.2692, 0.197, 0.1258, 0.05233, 0.02156, 0.00939, ) ,
		"mcHad"              :   ( 28.35, 11.54, 9.161, 6.222, 2.847, 1.022, 0.3579, 0.5172, ) ,
		"mcTtw"              :   ( 27.82, 11.35, 8.957, 6.11, 2.813, 0.9822, 0.3425, 0.5085, ) ,
		"mcMuon"             :   ( 113.9, 38.98, 61.5, 46.84, 27.02, 12.69, 6.419, 7.541, ) ,
		"mcZinv"             :   ( 0.5303, 0.1863, 0.2046, 0.1129, 0.03416, 0.03933, 0.01544, 0.008698, ) ,
		"mcMumu"             :   ( 0.9856, 0.1842, 0.4255, 0.3526, 0.1904, 0.1108, 0.027, 0.05084, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.9162, 0.5366, 0.695, 0.624, 0.5069, 0.3325, 0.2285, 0.2491, ) ,
		"mcMumuErr"          :   ( 0.2027, 0.02304, 0.03687, 0.03394, 0.02401, 0.0226, 0.007629, 0.01121, ) ,
		"mcHadErr"           :   ( 0.4112, 0.2749, 0.2479, 0.2219, 0.153, 0.08548, 0.05256, 0.06852, ) ,
		"mcZinvErr"          :   ( 0.03774, 0.01984, 0.03259, 0.01309, 0.006605, 0.01073, 0.002833, 0.001811, ) ,
		"mcTtwErr"           :   ( 0.4095, 0.2741, 0.2457, 0.2215, 0.1529, 0.0848, 0.05248, 0.0685, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.068, 0.06481, 0.04189, 0.02233, 0.004238, 0.001774, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, ) ,
		"nHad"               :   ( 24.0, 13.0, 4.0, 2.0, 2.0, 3.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 83.0, 34.0, 49.0, 32.0, 18.0, 11.0, 6.0, 2.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.2787, 0.06357, 0.01274, 0.00459, 0.0121, 0.003224, ) ,
		"mcHad"              :   ( 8.52, 4.087, 2.996, 0.6768, 0.1716, 0.04129, 0.005936, 0.001926, ) ,
		"mcTtw"              :   ( 7.751, 3.847, 2.799, 0.6321, 0.1607, 0.03393, 0.004092, 0.001013, ) ,
		"mcMuon"             :   ( 47.09, 28.46, 23.51, 7.306, 2.57, 0.9882, 0.3346, 0.3223, ) ,
		"mcZinv"             :   ( 0.7695, 0.2403, 0.1966, 0.04467, 0.01083, 0.007361, 0.001844, 0.0009131, ) ,
		"mcMumu"             :   ( 1.027, 0.3921, 0.4437, 0.1445, 0.05204, 0.01432, 0.00707, 0.007137, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.4442, 0.3449, 0.3267, 0.1973, 0.09367, 0.07161, 0.03095, 0.02908, ) ,
		"mcMumuErr"          :   ( 0.1023, 0.02528, 0.06065, 0.01542, 0.008, 0.002775, 0.002645, 0.002507, ) ,
		"mcHadErr"           :   ( 0.1799, 0.114, 0.1012, 0.04839, 0.0241, 0.008862, 0.002063, 0.0004697, ) ,
		"mcZinvErr"          :   ( 0.09275, 0.01669, 0.02428, 0.005565, 0.002484, 0.002179, 0.0006615, 0.0002158, ) ,
		"mcTtwErr"           :   ( 0.1541, 0.1128, 0.0982, 0.04807, 0.02398, 0.00859, 0.001954, 0.0004172, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.06385, 0.02145, 0.006035, 0.0005297, 0.008068, 0.0009669, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 8.0, 4.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 48.0, 31.0, 20.0, 9.0, 3.0, 0.0, 1.0, 0.0, ) ,
		"nMumu"              :   ( 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.004085, 0.00422, 0.002011, 0.00103, 0.0005304, 0.0001738, ) ,
		"mcHad"              :   ( 0.8773, 0.3536, 0.3065, 0.2709, 0.154, 0.05864, 0.02171, 0.04311, ) ,
		"mcTtw"              :   ( 0.8693, 0.3508, 0.2916, 0.2687, 0.1534, 0.05752, 0.02134, 0.04286, ) ,
		"mcMuon"             :   ( 3.724, 1.152, 2.072, 1.981, 1.401, 0.7101, 0.3807, 0.5126, ) ,
		"mcZinv"             :   ( 0.007978, 0.002809, 0.01487, 0.002213, 0.0005434, 0.001118, 0.000367, 0.0002528, ) ,
		"mcMumu"             :   ( 0.0187, 0.003006, 0.007429, 0.007389, 0.004227, 0.002791, 0.0007305, 0.001318, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.03584, 0.01919, 0.02918, 0.03589, 0.03645, 0.02323, 0.01695, 0.02237, ) ,
		"mcMumuErr"          :   ( 0.005863, 0.0003963, 0.0007208, 0.0008286, 0.0006641, 0.0007818, 0.0002669, 0.0003658, ) ,
		"mcHadErr"           :   ( 0.01518, 0.009943, 0.01576, 0.0131, 0.01023, 0.006283, 0.004043, 0.007046, ) ,
		"mcZinvErr"          :   ( 0.0007013, 0.0003386, 0.01196, 0.0003397, 0.0001361, 0.0003979, 7.761e-05, 8.568e-05, ) ,
		"mcTtwErr"           :   ( 0.01517, 0.009938, 0.01026, 0.0131, 0.01022, 0.00627, 0.004042, 0.007046, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.001147, 0.001871, 0.0008078, 0.0004525, 0.0001313, 4.093e-05, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 1.0, 2.0, 0.0, 1.0, 2.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcHad"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcTtw"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMuon"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcZinv"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMumu"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMumuErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcHadErr"           :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcZinvErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcTtwErr"           :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)