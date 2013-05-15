import collections

def graphBlackLists() :
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(list)

    out["ExpectedUpperLimit_-1_Sigma"].update({"T1": [(1150,425), (1100,300), (1100,350), (1100,375), (875, 550),
                                                      (825, 600), (850,600), (875,600), (800,550), (750,550), (950,525),
                                                      (1000,525), (1050, 500), (925,550),
                                                      ],
                                               "T2": [(950,175), (925,100), (875,300), (550,375), (575,350),(600,350),
                                                      (525,350), (650,375), (675,400), (825,325), (775,375),
                                                      ],
                                               "T2bb":[(450,250), (500,275), (550,275), (575,275), (600,275), (750,50), (650,250),
                                                       ],
                                               "T2tt":[(340,70), (320,60), (310,50), (390,110), (390,90), (380,90), (370,90),
                                                       (400,100), (420,120), (430,110), (450,110), (480,120), (490,110),
                                                       (520,110), (530,110), (530,130), (560,70), (560,90), (570,70), (570,50),
                                                       (590,30), (590,10), (570,0), (360,90), (460,130), (470,130), (520,130),
                                                       (570,80),
                                                       ],
                                               "T1bbbb":[(1225,100), (900,675), (1000,725), (950,725), (875,675), (925,700),
                                                         (1025,750), (1050,750), (1100,700), (1150,650), (1125,725),
                                                         (1200,650),
                                                         ],
                                               "T1tttt":[(475,125), (425,50), (525,125), (650,225), (725,300),
                                                         (750,300), (800,350), (825,350), (875,400), (925,400),
                                                         (950,425), (1100,400), (1000,425), (1050,425),
                                                         ],
                                               })
    out["ExpectedUpperLimit"].update({"T1": [(1000,525),(1075,400), (725,500), (700,525), (950,525),
                                             (875,550), (825,550), (900,525), (800,525), (775,525),
                                             ],
                                      "T2":[(500,300), (600,325), (575,325), (550,325), (725,325), (700,350), (750,325),
                                            (800,300), (850,225), (475,300),
                                            ],
                                      "T2bb": [(700,150), (675,200), (650,150), (600,250), (425,250), (450,225),
                                               (525,225), (550,250), (500,250), (625,250),
                                               ],
                                      "T2tt": [(530,70), (520,60), (500,60), (490,60), (490,100), (480,80),
                                               (460,70), (460,90), (490,80), (310,50), (400,90), (420,100),
                                               (380,80), (340,60), (360,80), (370,80), (410,100), (430,100),
                                               ],
                                      "T1bbbb":[(1125,625), (850,650), (925,675), (900,675), (975,700), (825,650),
                                                (1100,700), (1200,575),
                                                ],
                                       "T1tttt":[(1075,250), (525,100), (425,50), (650,225), (750,300), (800,325),
                                                 (950,375), (1000,375), (925,400), (1025,400), (850,375), (1075,325)
                                                 ],
                                      })
    out["ExpectedUpperLimit_+1_Sigma"].update({"T1": [(1000,450), (700,475), (775,500), (725,500), (700,525),
                                                      (950,450), (800,525), (850,525), (875,500), (925,475),
                                                      ],
                                               "T2": [(450,275), (550,275), (625,300), (525,275), (500,275), (575,300),
                                                      (675,325), (700,300), (750,275),
                                                      ],
                                               "T2bb": [(400,200), (525,200), (650, 25), (575,175),
                                                        ],
                                               "T2tt":[(350,0), (420,10), (430,10), (440,30), (430,40), (360,10),
                                                       (370,30), (390,30), (420,40),
                                                       ],
                                               "T1bbbb": [(1225,500), (1200,150), (825,600), (800,625), (850,650),
                                                          (975,650), (925,650), (900,650), (1050,650), (1150,550),
                                                          ],
                                               "T1tttt":[(1025,300), (525,100),(475,100),(425,50),(550,150),
                                                         (675,225),(750,275),(800,300),(850,350),
                                                         ],
                                               })

    out["UpperLimit"].update({"T1": [(675,500), (650,475), (900,450), (850,475), (950,425), (800,475),
                                     ],
                              "T2": [(575,300),(575,350),(450,275),(525,300), (475,275),
                                     (600,325), (525,325), (700,350), (625,350),
                                     ],
                              "T2bb": [(650,125), (400,200), (575,225),
                                       ],
                              "T1bbbb":[(825,625), (1150,550), (1050,650), (900,650), #(850,650),
                                        (950,700), (875,650), (925,675), (1075,650),
                                        ],
                              "T1tttt":[(500,125), (550,125), (625,225), (650,225), (700,225), (725,275),
                                        (800,300), (850,325), (600,200), (975,350), (425, 50), (400,50), (375,25),
                                        ],
                              })

    out["UpperLimit_-1_Sigma"].update({"T1": [(700,475), (675,475), (625,450), (875,425),
                                              ],
                                       "T2": [(575,300), (525,275), (675,325), (500,275), (600,325), (450,275),
                                              ],
                                       "T2bb": [(425,200), (500,225), (400,200), (525,200),
                                                ],
                                       "T1bbbb":[(800,625), (825,600), (975,625), (1000,650), (875,650), (1050,550),
                                                 ],
                                       "T1tttt":[(875,275), (775,275), (825,325), (850,300), (925,300), (625,175),
                                                 (650,225), (700,225), (750,275), (575,125), (525,100), (475,100),
                                                 (400, 50), (425, 50),
                                                 ],
                                       })
    out["UpperLimit_+1_Sigma"].update({"T1": [(700,475), (675,500), (1050,250), (750,475), (775,475), (925,475), (950,475),
                                              ],
                                       "T2": [(500,300), (550,325), (600,350), (625,350), (650,375), (725,350),
                                              ],
                                       "T2bb":[(450,225), (425,225), (525,225), (600,225),
                                               ],
                                       "T2tt":[(340,10),
                                               ],
                                       "T1bbbb":[(1225,450), (1025,725), (850,650), (900,675), (925,700),
                                                 (1075,700), (1100,650),
                                                 ],
                                       "T1tttt":[(1050,50), (525,100), (475,125), (425,50), (400,50),
                                                 (675,225), (700,275), (625,225), (750,275), (825,325), (775,325),
                                                 (1025,375), (850,350), (550,150),
                                                 ],
                                       })

    out["UpperLimit"].update({"T1tttt_ichep" : [ (850,200) ]})
    out["UpperLimit_-1_Sigma"].update({"T1tttt_ichep" : [ (450,50) ]})

    return out

def graphReplacePoints():
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(dict)

    out["ExpectedUpperLimit_-1_Sigma"].update({"T1": {(1075,500):(1075,487.5),
                                                      (1125,350):(1125,300),
                                                      (1100,  0):(1120,0),
                                                      },
                                               "T2": {(900,175):(895,175),
                                                      (850,300):(860,300),
                                                      (875,250):(880,250),
                                                      (800,350):(800,360),
                                                      (750,375):(750,372),
                                                      },
                                               "T2bb":{(525,300):(525,287.5),
                                                       (725,125):(725, 50),
                                                       (725,  0):(730,  0  ),
                                                       (700,175):(705, 175),
                                                       (675,225):(675, 235),
                                                       },
                                               "T2tt":{(330,80):(330,75),
                                                       (350,90):(350,88),
                                                       (380,110):(380,100),
                                                       (580,20):(580,0),
                                                       (580,50):(575,40),
                                                       },
                                               "T1bbbb":{(1250,450):(1237.5,450),
                                                         (1250,325):(1237.5,325),
                                                         (1250,275):(1237.5,275),
                                                         (1200,  0):(1220,    0),
                                                         (1075,725):(1075,  730),
                                                         (1225,625):(1225, 550),
                                                         },
                                               "T1tttt":{(1125,200):(1126,200),
                                                         (1100,325):(1110,325),
                                                         (1075,425):(1075,400),
                                                         (675,250):(675,255),
                                                         (850,375):(850,380),
                                                         (400,50):(400,45),
                                                         },
                                               })
    out["ExpectedUpperLimit"].update({"T1": {(850,525):(850,550),
                                             (1050,0):(1072.5,0),
                                             (750,525):(750,537.5),
                                             },
                                      "T2": {(825,325):(825,265),

                                             (875,  0):(865,  0),
                                             (875, 50):(865, 50),
                                             (875,100):(860,100),
                                             (875,150):(855,150),
                                             },
                                      "T2bb": {(575,275):(575,255),
                                               (700,75):(685,75),
                                               (700,25):(687,25),
                                               (675, 0):(687.5, 0),
                                               },
                                      "T2tt":{(510, 0):(515, 0),
                                              (520,50):(513,50),
                                              (350,70):(350,75),
                                              (440,110):(440,100),
                                              },
                                      "T1bbbb":{(950,700):(950,692.5),
                                                (1225,500):(1213,450),
                                                (1225,200):(1211,300),
                                                (1225,150):(1208,200),
                                                (1225,100):(1205,100),
                                                },
                                      "T1tttt":{(1100,100):(1080,100),
                                                (1100,250):(1090,200),
                                                (1075,  0):(1070,  0),
                                                (975,400):(975,387.5),
                                                (725,300):(725,285),
                                                (625,225):(625,215),
                                                (500,125):(500,115),
                                                (600,200):(600,190),
                                                (575,175):(575,165),
                                                (700,275):(700,265),
                                                (775,325):(775,315),
                                                (400,50):(400,45),
                                                },
                                      })
    out["ExpectedUpperLimit_+1_Sigma"].update({"T1": {(750,525):(750,512.5),
                                                      (675,500):(687.5,500),
                                                      (1050,275):(1037.5,275),
                                                      (1050,200):(1037.5,200),
                                                      (1050,100):(1037.5,100),
                                                      (1025,  0):(1032,    0),
                                                      (1025,375):(1030,350),
                                                      (1000,400):(1012.5,400),
                                                      },
                                               "T2":{(600,325):(600,320),
                                                     (650,325):(650,320),
                                                     (825, 75):(820, 75),
                                                     (775,250):(780,250),
                                                     },
                                               "T2bb": {(550,200):(555,205),
                                                        (500,225):(500,220),
                                                        (600,200):(600,175),
                                                        (625,75):(637.5,75),
                                                        },
                                               "T2tt": {(340,30):(335,0),
                                                        (380,20):(380,25),
                                                        (350,20):(350,15),
                                                        (410,20):(410,32),
                                                        (430,30):(430,34),
                                                        (440,20):(438,25),
                                                        (440, 0):(441, 0),
                                                        },
                                               "T1bbbb": {(950,675):(950,667.5),
                                                          (1175,400):(1175,300),
                                                          (1125,550):(1135,550),
                                                          (1175,225):(1170,225),
                                                          (1150,  0):(1162.5,0),
                                                          (1075,650):(1080,640),
                                                          },
                                               "T1tttt":{(1025,0):(1020,0),
                                                         (1025,250):(1025,175),
                                                         (400,50):(400,45),
                                                         },
                                               })
    out["UpperLimit"].update({"T1": {#(950,425):(950,437.5),
                                     (975,425):(980,375),
                                     #(875,475):(874,467.5),
                                     (1000,350):(1000,225),
                                     (925,450):(935,455),
                                     },
                              "T2": {(800,200):(795,150),
                                     },
                              "T2bb":{(625,125):(632,125),
                                      (650,50): (647,50),
                                      (425,225):(425,224),
                                      (550,225):(550,224),
                                      },
                              "T1bbbb":{(1175,225):(1167.5,225),
                                        (1175,275):(1167.5,275),
                                        (1175,325):(1167.5,325),
                                        (1175,350):(1167.5,350),
                                        (1175,400):(1167.5,400),
                                        (1150,500):(1160, 475),
                                        (1125,550):(1135,550),
                                        },
                              "T1tttt":{(1025,250):(1025,175),
                                        (1025,75):(1020,75),
                                        (1000, 0):(1010, 0),

                                        (525,100):(525,125),
                                        (475,100):(487.5,100),
                                        (675,225):(650,218),
                                        (750,275):(730,275),
                                        (575,175):(575,165),
                                        },
                              })
    
    out["UpperLimit_-1_Sigma"].update({"T1":{(950,325):(950,275),
                                             (850,450):(850,448),
                                             },
                                       "T2":{(775,100):(770,100),
                                             (625,325):(610,325),
                                             (550,300):(550,310)
                                             },
                                       "T2bb":{(600,125):(590,125),
                                               (575,175):(575,185),
                                               (450,225):(450,212.5),
                                               (475,225):(475,212.5),
                                               (550,200):(560,200),
                                               },
                                       "T1bbbb":{(1125,175): (1120,175),
                                                 (1125,100): (1115,100),
                                                 (1100,  0): (1112.5,0),
                                                 (1125,400): (1125,300),
                                                 (1025,625): (1025,600),
                                                 (850, 625): (850,637.5),
                                                 },
                                       "T1tttt":{(975,200):(973,200),
                                                 (975,100):(968,100),
                                                 (950,  0):(960,  0),
                                                 (600,175):(610,175),
                                                 (675,225):(675,220),
                                                 (550,125):(550,128)
                                                 },
                                       })

    out["UpperLimit_+1_Sigma"].update({"T1":{(1025,400):(1025,325),
                                             },
                                       "T2":{(825,200):(817.5,175),
                                             (475,300):(485,300),
                                             },
                                       "T2bb":{(475,250):(475,245),
                                               (500,250):(500,245),
                                               (550,250):(550,245),
                                               (575,250):(575,242),
                                               (675,75):(670,70),
                                               },
                                       "T1bbbb":{(950,700):(935,700),
                                                 (1200,525):(1200,400),
                                                 (1200,100):(1195,100),
                                                 (1200, 50):(1192.5, 50),
                                                 (1200, 25):(1190, 25),
                                                 (1175,  0):(1187.5,  0),
                                                 },
                                       "T1tttt":{(1050,  0):(1055,  0),
                                                 (1075,175):(1060,75),
                                                 (1075,225):(1070,175),
                                                 (1075,250):(1070,220),
                                                 (1050,300):(1050,310),
                                                 (800,325):(790,325),
                                                 (725,275):(715,275),
                                                 (650,225):(640,225),
                                                 (500,125):(500,120),
                                                 (575,175):(575,178),
                                                 },
                                       })

    return out

def graphAdditionalPoints():
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(list)

    return out