#encoding:UTF-8

import urllib
import urllib.request
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.lines as mlines
import numpy as np

station1 = '50136,50246,50247,50349,50353,50425,50431,50434,50445,50468,50514,50526,50525,50548,50527,50557,50564,50566,50639,50647,50632,50646,50655,50656,50674,50658,50659,50673,50739,50742,50727,50745,50741,50749,50750,50756,50755,50758,50772,50775,50776,50778,50767,50774,50779,50787,50788,50832,50838,50834,50844,50854,50853,50850,50851,50852,50862,50858,50871,50873,50880,50884,50892,50867,50879,50859,50861,50877,50878,50888,50913,50936,50949,50939,50948,50940,50924,50934,50928,50945,50946,50956,50955,50953,50954,50950,50964,50965,50973,50971,50978,50987,50983,50985,50963,50958,50962,50960,50968,50979,51059,51068,51053,51060,51076,51087,51133,51145,51137,51186,51243,51238,51232,51241,51334,51330,51328,51329,51356,51357,51365,51359,51369,51368,51352,51353,51367,51378,51377,51379,51437,51431,51434,51435,51436,51433,51430,51438,51465,51470,51463,51477,51482,51467,51542,51571,51568,51581,51567,51573,51559,51633,51642,51627,51639,51629,51628,51636,51644,51656,51655,51707,51704,51705,51708,51717,51716,51722,51730,51711,51720,51747,51765,51777,51802,51810,51811,51826,51828,51804,51815,51814,51818,51827,51829,51839,51855,51886,51931,52101,52118,52203,52378,52424,52436,52447,52515,52532,52533,52546,52557,52643,52602,52652,52656,52661,52657,52674,52681,52679,52713,52745,52754,52765,52797,52784,52818,52833,52836,52855,52863,52869,52868,52874,52877,52889,52866,52895,52876,52885,52862,52881,52884,52896,52943,52955,52957,52968,52981,52983,52984,52986,52963,52978,52972,52988,52980,52982,52998,52985,52993,53068,53083,53149,53231,53289,53276,53337,53343,53348,53357,53385,53391,53392,53399,53367,53368,53362,53397,53420,53419,53446,53475,53488,53490,53472,53491,53463,53480,53478,53487,53486,53483,53484,53498,53492,53499,53518,53512,53513,53502,53522,53533,53519,53547,53574,53577,53576,53579,53584,53588,53582,53594,53575,53562,53567,53565,53573,53564,53580,53578,53585,53593,53599,53590,53596,53617,53618,53612,53644,53614,53610,53615,53619,53646,53611,53651,53658,53662,53669,53673,53682,53680,53690,53685,53689,53688,53697,53666,53678,53687,53664,53660,53665,53663,53659,53694,53676,53691,53692,53693,53698,53695,53699,53696,53704,53705,53732,53738,53740,53748,53723,53725,53735,53751,53753,53750,53756,53754,53757,53764,53773,53769,53776,53778,53775,53780,53787,53792,53799,53789,53796,53767,53777,53768,53770,53760,53784,53759,53783,53763,53782,53781,53791,53772,53785,53788,53786,53774,53794,53771,53795,53798,53790,53806,53817,53829,53841,53845,53848,53810,53821,53832,53853,53850,53852,53857,53854,53856,53864,53871,53872,53877,53873,53883,53874,53875,53896,53893,53899,53868,53886,53866,53861,53862,53863,53888,53860,53885,53859,53879,53865,53869,53878,53882,53880,53891,53890,53889,53892'
station2 = '53898,53897,53884,53895,53894,53906,53903,53908,53923,53929,53930,53934,53941,53942,53946,53916,53928,53917,53935,53945,53947,53914,53925,53931,53913,53924,53927,53937,53926,53948,53949,53944,53938,53956,53955,53953,53957,53959,53950,53967,53964,53972,53970,53978,53983,53979,53985,53993,53996,53994,53968,53961,53966,53954,53986,53987,53965,53997,53963,53958,53962,53988,53973,53975,53974,53980,53981,53976,53982,53989,53984,53995,53992,53991,53998,54024,54041,54027,54049,54031,54039,54063,54065,54072,54080,54092,54093,54069,54096,54076,54064,54098,54094,54099,54102,54115,54134,54113,54135,54132,54142,54156,54154,54157,54181,54187,54164,54186,54161,54195,54165,54171,54172,54204,54244,54243,54218,54236,54214,54245,54249,54237,54252,54254,54260,54273,54274,54286,54291,54259,54285,54267,54266,54261,54263,54276,54290,54293,54292,54284,54304,54323,54332,54335,54336,54349,54347,54319,54316,54324,54320,54301,54348,54311,54308,54330,54318,54338,54327,54328,54331,54333,54334,54337,54339,54342,54345,54346,54371,54374,54386,54353,54362,54363,54377,54365,54398,54405,54404,54408,54401,54406,54416,54420,54431,54424,54432,54437,54430,54419,54438,54436,54423,54425,54434,54429,54439,54428,54449,54453,54452,54472,54471,54474,54454,54493,54499,54494,54455,54475,54497,54486,54470,54502,54506,54503,54507,54511,54520,54526,54522,54533,54523,54540,54528,54518,54538,54517,54512,54505,54510,54515,54521,54525,54534,54532,54539,54529,54519,54531,54541,54563,54569,54596,54568,54584,54590,54579,54594,54606,54602,54601,54604,54605,54608,54614,54621,54624,54631,54636,54619,54616,54617,54618,54628,54603,54607,54610,54609,54633,54611,54615,54622,54613,54612,54620,54627,54626,54632,54640,54644,54662,54660,54704,54706,54707,54703,54708,54711,54705,54710,54719,54724,54700,54732,54729,54730,54727,54716,54726,54717,54715,54701,54725,54744,54736,54712,54702,54714,54709,54718,54722,54713,54723,54731,54728,54734,54737,54738,54749,54753,54755,54752,54751,54764,54765,54776,54778,54777,54766,54774,54801,54805,54800,54802,54812,54803,54807,54804,54827,54832,54824,54834,54830,54831,54829,54848,54837,54820,54814,54819,54828,54849,54844,54815,54808,54810,54811,54809,54818,54816,54806,54821,54825,54817,54836,54835,54842,54822,54841,54846,54843,54823,54833,54855,54852,54853,54857,54851,54871,54863,54861,54904,54909,54900,54907,54902,54903,54910,54901,54922,54925,54927,54929,54920,54940,54938,54939,54943,54945,54914,54905,54921,54912,54915,54908,54923,54916,54932,54918,54911,54917,54936,54913,54935,54919,55125,55248,55294,55279,55299,55325,55357,55437,55472,55493,55574,55572,55597,55593,55569,55585,55578,55591,55655,55696,55664,55680,55690,55773,56016,56021,56038,56033,56046,56045,56029,56018,56071,56074'
station3 = '56091,56080,56096,56065,56082,56094,56081,56067,56084,56095,56093,56092,56079,56106,56109,56125,56128,56137,56144,56116,56147,56146,56158,56151,56152,56167,56168,56173,56178,56182,56183,56196,56193,56194,56199,56195,56192,56164,56190,56172,56171,56185,56180,56184,56188,56186,56198,56197,56189,56202,56223,56227,56228,56247,56251,56273,56272,56276,56289,56281,56295,56296,56287,56267,56280,56288,56257,56263,56278,56279,56284,56285,56291,56297,56286,56298,56290,56308,56307,56312,56301,56342,56317,56331,56319,56357,56371,56374,56373,56382,56387,56381,56396,56390,56385,56389,56391,56378,56376,56386,56395,56383,56393,56384,56394,56399,56434,56443,56441,56444,56459,56474,56478,56483,56485,56491,56497,56498,56475,56462,56473,56490,56487,56480,56496,56489,56494,56493,56479,56492,56499,56548,56533,56543,56565,56584,56578,56585,56582,56592,56595,56567,56586,56596,56569,56575,56580,56593,56594,56598,56641,56646,56645,56649,56652,56664,56670,56673,56669,56674,56684,56666,56651,56665,56671,56675,56654,56688,56691,56693,56697,56746,56748,56739,56742,56745,56756,56752,56755,56757,56751,56763,56775,56768,56777,56785,56788,56793,56792,56767,56766,56761,56764,56774,56772,56778,56782,56781,56790,56838,56836,56841,56839,56849,56835,56840,56842,56846,56843,56856,56863,56867,56873,56875,56872,56876,56882,56871,56878,56851,56854,56862,56870,56880,56869,56879,56881,56883,56885,56886,56889,56891,56898,56946,56949,56944,56948,56952,56950,56954,56951,56958,56976,56969,56987,56986,56984,56996,56978,56970,56975,56992,56985,56994,56959,56962,56991,56966,56961,56973,56982,56977,56989,56995,57007,57006,57008,57002,57001,57012,57021,57022,57032,57027,57029,57030,57036,57042,57049,57020,57041,57003,57043,57004,57014,57011,57026,57023,57016,57031,57045,57024,57034,57025,57033,57040,57028,57039,57047,57038,57044,57048,57035,57055,57057,57051,57053,57052,57056,57054,57061,57074,57086,57077,57076,57083,57070,57088,57099,57098,57090,57095,57063,57079,57065,57067,57066,57078,57085,57075,57081,57072,57071,57060,57096,57094,57091,57087,57082,57089,57080,57093,57105,57106,57102,57119,57128,57144,57140,57134,57132,57113,57127,57126,57110,57111,57129,57124,57137,57123,57143,57153,57154,57155,57176,57187,57177,57179,57182,57185,57180,57183,57169,57189,57184,57178,57156,57162,57173,57181,57175,57188,57194,57186,57193,57191,57192,57197,57198,57196,57195,57204,57211,57217,57232,57231,57237,57242,57247,57216,57238,57206,57213,57208,57249,57233,57248,57245,57256,57257,57251,57259,57253,57260,57274,57268,57279,57285,57281,57295,57290,57294,57299,57271,57254,57261,57265,57273,57293,57292,57296,57297,57298,57304,57307,57303,57308,57309,57324,57329,57338,57317,57306,57318,57315,57313,57314,57326,57320,57333'
station4 = '57339,57343,57345,57348,57359,57355,57370,57378,57388,57399,57395,57396,57368,57362,57385,57377,57358,57361,57363,57381,57387,57389,57398,57402,57401,57405,57414,57413,57426,57425,57439,57447,57417,57416,57407,57437,57409,57408,57445,57415,57411,57420,57432,57438,57453,57461,57458,57469,57477,57481,57482,57486,57496,57499,57498,57465,57485,57460,57462,57464,57466,57475,57483,57476,57489,57493,57492,57494,57491,57507,57503,57505,57506,57502,57508,57513,57511,57537,57540,57545,57517,57516,57510,57512,57514,57520,57525,57509,57523,57544,57541,57543,57562,57565,57574,57571,57577,57583,57598,57581,57558,57589,57554,57575,57566,57564,57573,57585,57582,57584,57590,57595,57586,57604,57600,57605,57606,57612,57608,57623,57634,57635,57640,57642,57646,57647,57603,57633,57614,57609,57636,57637,57643,57649,57625,57657,57655,57662,57669,57673,57674,57682,57698,57699,57663,57678,57696,57661,57658,57666,57671,57680,57679,57688,57694,57713,57710,57707,57719,57723,57734,57732,57722,57744,57729,57736,57740,57741,57717,57735,57712,57714,57720,57742,57718,57731,57708,57728,57739,57743,57749,57737,57738,57745,57754,57752,57763,57758,57769,57774,57768,57761,57773,57760,57771,57779,57796,57799,57798,57762,57780,57766,57767,57776,57772,57778,57777,57781,57786,57793,57792,57789,57803,57805,57806,57800,57807,57808,57809,57821,57827,57829,57841,57846,57844,57816,57828,57818,57837,57811,57813,57814,57822,57824,57825,57832,57834,57835,57839,57840,57842,57845,57853,57851,57857,57860,57865,57871,57872,57874,57881,57887,57891,57894,57895,57866,57868,57867,57886,57896,57876,57859,57870,57875,57899,57889,57882,57900,57907,57906,57902,57903,57908,57923,57914,57926,57941,57916,57927,57949,57905,57910,57909,57912,57913,57911,57915,57922,57921,57932,57936,57942,57948,57947,57956,57955,57957,57954,57972,57973,57964,57962,57975,57960,57985,57988,57992,57993,57989,57981,57996,57976,57990,57991,57971,57978,57994,57969,57966,57974,57965,57995,58001,58002,58007,58006,58005,58004,58003,58012,58021,58024,58032,58020,58027,58036,58034,58045,58047,58017,58016,58025,58022,58011,58015,58008,58013,58026,58030,58040,58048,58035,58038,58044,58049,58102,58100,58107,58101,58104,58118,58126,58122,58125,58128,58130,58131,58139,58148,58146,58117,58147,58129,58109,58108,58114,58111,58116,58113,58135,58132,58138,58127,58141,58140,58143,58150,58158,58154,58202,58205,58203,58208,58221,58236,58243,58240,58242,58238,58244,58241,58212,58210,58207,58214,58224,58215,58235,58223,58225,58230,58220,58247,58222,58246,58245,58234,58249,58255,58251,58248,58250,58257,58268,58269,58254,58264,58259,58306,58301,58319,58316,58323,58327,58329,58341,58344,58340,58346,58317,58320,58334,58342,58349,58311,58314,58330,58326,58321,58335'
station5 = '58331,58337,58339,58343,58338,58345,58336,58353,58352,58351,58354,58356,58360,58359,58377,58366,58367,58370,58362,58361,58365,58369,58404,58401,58409,58414,58421,58420,58427,58432,58433,58436,58442,58446,58448,58419,58418,58416,58417,58428,58407,58437,58402,58408,58415,58424,58429,58426,58431,58435,58441,58438,58443,58449,58455,58456,58453,58451,58454,58457,58452,58450,58472,58468,58467,58458,58461,58463,58460,58462,58464,58459,58484,58507,58506,58502,58501,58500,58503,58530,58529,58542,58548,58544,58527,58509,58512,58510,58514,58508,58517,58520,58537,58534,58543,58523,58549,58546,58547,58553,58556,58555,58557,58550,58566,58568,58567,58558,58563,58559,58565,58562,58570,58605,58606,58600,58608,58620,58622,58632,58624,58627,58637,58647,58634,58618,58619,58616,58615,58609,58633,58601,58644,58612,58614,58625,58642,58635,58623,58631,58646,58602,58643,58626,58629,58654,58652,58657,58656,58659,58664,58693,58665,58667,58658,58706,58705,58701,58704,58713,58734,58731,58724,58744,58737,58745,58746,58710,58718,58712,58707,58715,58719,58714,58736,58730,58725,58735,58742,58747,58749,58748,58754,58760,58752,58750,58806,58819,58813,58821,58834,58837,58823,58839,58843,58848,58818,58804,58846,58836,58844,58814,58820,58824,58826,58822,58845,58828,58847,58906,58907,58903,58905,58911,58921,58923,58929,58935,58932,58936,58938,58946,58918,58927,58917,58912,58944,58928,58926,58933,58934,58941,58942,59007,59004,59001,59022,59025,59034,59031,59038,59045,59046,59017,59015,59027,59037,59012,59023,59021,59033,59041,59047,59053,59052,59057,59055,59051,59063,59061,59075,59071,59091,59092,59088,59093,59096,59094,59058,59064,59065,59072,59059,59074,59090,59082,59081,59087,59099,59097,59107,59106,59102,59113,59114,59129,59132,59137,59126,59125,59134,59109,59122,59116,59130,59127,59124,59133,59131,59205,59211,59215,59209,59229,59230,59228,59237,59242,59241,59238,59235,59213,59218,59224,59227,59246,59249,59256,59255,59254,59265,59269,59280,59279,59284,59285,59288,59293,59294,59266,59268,59264,59276,59270,59271,59290,59289,59297,59306,59304,59303,59313,59318,59321,59320,59324,59316,59315,59312,59310,59317,59319,59322,59314,59419,59426,59421,59435,59427,59441,59417,59431,59425,59429,59446,59449,59448,59432,59451,59456,59452,59453,59457,59454,59475,59478,59493,59492,59476,59477,59462,59469,59471,59470,59485,59488,59487,59502,59501,59500,59640,59632,59644,59631,59626,59635,59654,59650,59658,59656,59663,59653,59655,59659,59664,59754,59750,59758,59838,59845,59842,59849,59848,59843,59847,59856,59851,59854,59855,59940,59941,59945,59954,59951'

station = []
code = []
codeinfile = []
province = []
time = []
T = []
date1 = ''
date2 = ''
forecastupdatetime = ''
day1day = []
day1dayweather = []
day1night = []
day2day = []
day2dayweather = []
day2night = []
lons = []
lats = []
author = ''
save = '/Users/hsw/Desktop/T_sample.png'
save2 = '/Users/hsw/Desktop/TF1_sample.png'
save3 = '/Users/hsw/Desktop/TF2_sample.png'
save4 = '/Users/hsw/Desktop/F1_sample.png'
save5 = '/Users/hsw/Desktop/F2_sample.png'

def getstationdata(list):
    data = urllib.request.urlopen('http://www.nmc.cn/f/rest/weather/' + list).read()
    record = data.decode('UTF-8')
    data = json.loads(record)
    print(data)

    for i in range(0,len(data)):
        station.append(data[i]['station']['city'])
        province.append(data[i]['station']['province'])
        code.append(data[i]['station']['code'])
        time.append(data[i]['publish_time'])
        T.append(data[i]['temperature'])
        day1day.append(float(data[i]['detail'][0]['day']['weather']['temperature']))
        day1night.append(data[i]['detail'][0]['night'])
        day2day.append(float(data[i]['detail'][1]['day']['weather']['temperature']))
        day2night.append(data[i]['detail'][1]['night'])

        day1dayweather.append(int(data[i]['detail'][0]['day']['weather']['img']))
        day2dayweather.append(int(data[i]['detail'][1]['day']['weather']['img']))
    global date1
    global date2
    global forecastupdatetime
    date1 = data[0]['detail'][0]['date']
    date2 = data[0]['detail'][1]['date']
    forecastupdatetime = data[0]['detail'][0]['pt']

def readinfofile():
    # ============================================# input time
    #inittime = input("Enter Init time:(YYYYMMDDHH)");
    author = input("author(can remain blank):");
    if author == '':
        author = '绘图：华师大二附中气象服务中心  数据：中央气象台'
    # ============================================# read data
    file = "/Users/hsw/Desktop/stations.txt"
    fh = open(file)
    for line in fh:
        info = line.split()
        code = info[0]
        codeinfile.append(code)
        lat = float(info[3][:-1])
        if info[2][-1] == 'S': lat = -lat
        lats.append(lat)
        lon = float(info[4][:-1])
        if info[3][-1] == 'W': lon = -lon + 360.0
        lons.append(lon)
    return author

author=readinfofile()
getstationdata(station1)
getstationdata(station2)
getstationdata(station3)
getstationdata(station4)
getstationdata(station5)
print('station', station)
print('time', time)
print('T', T)


# ============================================initialize the plot
plt.figure(figsize=(13, 9), dpi=80)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=70, llcrnrlat=15, urcrnrlon=135, urcrnrlat=55, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='l', projection='merc', \
              lat_0=40., lon_0=-20., lat_ts=20.)
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#87CEFA')#689CD2
# draw lat/lon grid lines every 30 degrees.

#map.drawmeridians(np.arange(0, 360, 10))
map.drawmeridians(np.arange(0, 360, 10),labels=[0,0,0,1],fontsize=10)
#map.drawparallels(np.arange(-90, 90, 10))
map.drawparallels(np.arange(-90, 90, 10),labels=[1,0,0,0],fontsize=10)

# Fill continent wit a different color
map.fillcontinents(color='#FFFFFF', lake_color='#87CEFA', zorder=0)

# ============================================draw the stations and data
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons, lats)
max_T = max(T)
# Plot each city in a loop.
# Set some parameters
size_factor = 100.0
x_offset = 20.0
y_offset = -20.0
rotation = 0
temp=0

f = open("/Users/hsw/Desktop/realTdata.txt", "w+")
f.close()
#draw station point
for i, j, k, l, m, n, p in zip(x, y, T, station, province, code, codeinfile):
    temp = temp+1
    size = size_factor * k / max_T
    if k <= -10.0:
        cs1 = map.scatter(i, j, s=15, marker='o', color='#00008F')
    if -10 < k and k <= -5:
        cs2 = map.scatter(i, j, s=15, marker='o', color='#00009F')
    if -5 < k and k <= 0:
        cs3 = map.scatter(i, j, s=15, marker='o', color='#0000FF')
    if 0 < k and k <= 5:
        cs4 = map.scatter(i, j, s=15, marker='o', color='#006FFF')
    if 5 < k and k <= 10:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00BFFF')
    if 10 <= k and k <= 15:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00FFFF')
    if 15 <= k and k <= 20:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#4FFFAF')
    if 20 <= k and k <= 25:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#7FF77F')
    if 25 <= k and k <= 30:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFFF00')
    if 30 <= k and k <= 35:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFBF00')
    if 35 <= k and k <= 40:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF6F00')
    if 40 <= k and k <= 45:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF0000')
    if 45 < k and k != 9999:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#7F0000')
    if l == '上海' or l == '北京' or l == '重庆' or l == '石家庄' or l == '郑州' or l == '武汉' or l == '长沙' or l == '南京' \
            or (l == '南昌' and m == '江西省') or l == '沈阳' or l == '长春' or l == '哈尔滨' or l == '西安' or l == '太原' or l == '济南' or l == '成都' \
            or l == '西宁' or l == '合肥' or l == '海口' or l == '广州' or l == '贵阳' or l == '兰州' or l == '昆明' \
            or l == '拉萨' or l == '银川' or l == '南宁' or l == '乌鲁木齐' or l == '呼和浩特':
        plt.text(i + 20, j - 20, l + '\n' + str(k) + '°', rotation=rotation, fontsize=10)
    if l == '天津' or l == '杭州':
        plt.text(i + 20, j - 100020, l + '\n' + str(k) + '°', rotation=rotation, fontsize=10)
    #print('Original_code:', p, 'Data:', n, l, '实时气温:', str(k), '°')
    f = open("/Users/hsw/Desktop/realTdata.txt", "a+")
    f.write('Original_code:'+ p + ' Data:' + n + ' ' + l + ' 实时气温:' + str(k) + '°\n')
    f.close()


title = '全国实时气温分布图（自动站）\n' + '数据更新时间:' + time[0] + '\n' + author

# ============================================#define legends
a = mlines.Line2D([], [], color='#7F0000', marker='o',
                          markersize=5, label='>45°C',ls='')
b = mlines.Line2D([], [], color='#FF0000', marker='o',
                          markersize=5, label='40~45°C',ls='')
c = mlines.Line2D([], [], color='#FF6F00', marker='o',
                          markersize=5, label='35~40°C',ls='')
d = mlines.Line2D([], [], color='#FFBF00', marker='o',
                          markersize=5, label='30~35°C',ls='')
e = mlines.Line2D([], [], color='#FFFF00', marker='o',
                          markersize=5, label='25~30°C',ls='')
f = mlines.Line2D([], [], color='#7FF77F', marker='o',
                          markersize=5, label='20~25°C',ls='')
g = mlines.Line2D([], [], color='#4FFFAF', marker='o',
                          markersize=5, label='15~20°C',ls='')
h = mlines.Line2D([], [], color='#00FFFF', marker='o',
                          markersize=5, label='10~15°C',ls='')
i = mlines.Line2D([], [], color='#00BFFF', marker='o',
                          markersize=5, label='5~10°C',ls='')
j = mlines.Line2D([], [], color='#006FFF', marker='o',
                          markersize=5, label='0~5°C',ls='')
k = mlines.Line2D([], [], color='#0000FF', marker='o',
                          markersize=5, label='-5~0°C',ls='')
l = mlines.Line2D([], [], color='#00009F', marker='o',
                          markersize=5, label='-10~-5°C',ls='')
m = mlines.Line2D([], [], color='#00008F', marker='o',
                          markersize=5, label='<-10°C',ls='')
plt.legend(handles=[a, b, c, d, e, f, g, h, i, j, k, l, m])
plt.title(title)

# plt.show()
plt.savefig(save, dpi=100)
plt.show()

# ============================================
# ============================================
# ============================================
# ============================================
# ============================================DRAW SECOND PLOT
# ============================================
# ============================================
# ============================================
# ============================================initialize the plot
plt.figure(figsize=(13, 9), dpi=80)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=70, llcrnrlat=15, urcrnrlon=135, urcrnrlat=55, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='l', projection='merc', \
              lat_0=40., lon_0=-20., lat_ts=20.)
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#87CEFA')#689CD2
# draw lat/lon grid lines every 30 degrees.

#map.drawmeridians(np.arange(0, 360, 10))
map.drawmeridians(np.arange(0, 360, 10),labels=[0,0,0,1],fontsize=10)
#map.drawparallels(np.arange(-90, 90, 10))
map.drawparallels(np.arange(-90, 90, 10),labels=[1,0,0,0],fontsize=10)

# Fill continent wit a different color
map.fillcontinents(color='#FFFFFF', lake_color='#87CEFA', zorder=0)

# ============================================draw the stations and data
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons, lats)
max_T = max(day1day)
# Plot each city in a loop.
# Set some parameters
size_factor = 100.0
x_offset = 20.0
y_offset = -20.0
rotation = 0
temp=0

f = open("/Users/hsw/Desktop/forecastTdata.txt", "w+")
f.close()
#draw station point
for i, j, k, l, m, n, p in zip(x, y, day1day, station, province, code, codeinfile):
    temp = temp+1
    if k <= -10.0:
        cs1 = map.scatter(i, j, s=15, marker='o', color='#00008F')
    if -10 < k and k <= -5:
        cs2 = map.scatter(i, j, s=15, marker='o', color='#00009F')
    if -5 < k and k <= 0:
        cs3 = map.scatter(i, j, s=15, marker='o', color='#0000FF')
    if 0 < k and k <= 5:
        cs4 = map.scatter(i, j, s=15, marker='o', color='#006FFF')
    if 5 < k and k <= 10:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00BFFF')
    if 10 <= k and k <= 15:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00FFFF')
    if 15 <= k and k <= 20:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#4FFFAF')
    if 20 <= k and k <= 25:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#7FF77F')
    if 25 <= k and k <= 30:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFFF00')
    if 30 <= k and k <= 35:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFBF00')
    if 35 <= k and k <= 40:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF6F00')
    if 40 <= k and k <= 45:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF0000')
    if 45 < k and k != 9999:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#7F0000')
    if l == '上海' or l == '北京' or l == '重庆' or l == '石家庄' or l == '郑州' or l == '武汉' or l == '长沙' or l == '南京' \
            or (l == '南昌' and m == '江西省') or l == '沈阳' or l == '长春' or l == '哈尔滨' or l == '西安' or l == '太原' or l == '济南' or l == '成都' \
            or l == '西宁' or l == '合肥' or l == '海口' or l == '广州' or l == '贵阳' or l == '兰州' or l == '昆明' \
            or l == '拉萨' or l == '银川' or l == '南宁' or l == '乌鲁木齐' or l == '呼和浩特':
        plt.text(i + 20, j - 20, l + '\n' + str(k) + '°', rotation=rotation, fontsize=10)
    if l == '天津' or l == '杭州':
        plt.text(i + 20, j - 100020, l + '\n' + str(k) + '°', rotation=rotation, fontsize=10)
    #print('Original_code:', p, 'Data:', n, l, '实时气温:', str(k), '°')
    f = open("/Users/hsw/Desktop/forecastTdata.txt", "a+")
    f.write('Original_code:'+ p + ' Data:' + date1 + ' 预报最高气温:' + str(k) + '°\n')
    f.close()


title = date1 + '全国最高气温预报图\n' + '预报时间:' + forecastupdatetime + '\n' + author

# ============================================#define legends
a = mlines.Line2D([], [], color='#7F0000', marker='o',
                          markersize=5, label='>45°C',ls='')
b = mlines.Line2D([], [], color='#FF0000', marker='o',
                          markersize=5, label='40~45°C',ls='')
c = mlines.Line2D([], [], color='#FF6F00', marker='o',
                          markersize=5, label='35~40°C',ls='')
d = mlines.Line2D([], [], color='#FFBF00', marker='o',
                          markersize=5, label='30~35°C',ls='')
e = mlines.Line2D([], [], color='#FFFF00', marker='o',
                          markersize=5, label='25~30°C',ls='')
f = mlines.Line2D([], [], color='#7FF77F', marker='o',
                          markersize=5, label='20~25°C',ls='')
g = mlines.Line2D([], [], color='#4FFFAF', marker='o',
                          markersize=5, label='15~20°C',ls='')
h = mlines.Line2D([], [], color='#00FFFF', marker='o',
                          markersize=5, label='10~15°C',ls='')
i = mlines.Line2D([], [], color='#00BFFF', marker='o',
                          markersize=5, label='5~10°C',ls='')
j = mlines.Line2D([], [], color='#006FFF', marker='o',
                          markersize=5, label='0~5°C',ls='')
k = mlines.Line2D([], [], color='#0000FF', marker='o',
                          markersize=5, label='-5~0°C',ls='')
l = mlines.Line2D([], [], color='#00009F', marker='o',
                          markersize=5, label='-10~-5°C',ls='')
m = mlines.Line2D([], [], color='#00008F', marker='o',
                          markersize=5, label='<-10°C',ls='')
plt.legend(handles=[a, b, c, d, e, f, g, h, i, j, k, l, m])
plt.title(title)

# plt.show()
plt.savefig(save2, dpi=100)
plt.show()

# ============================================
# ============================================
# ============================================
# ============================================
# ============================================DRAW THIRD PLOT
# ============================================
# ============================================
# ============================================
# ============================================initialize the plot
plt.figure(figsize=(13, 9), dpi=80)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=70, llcrnrlat=15, urcrnrlon=135, urcrnrlat=55, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='l', projection='merc', \
              lat_0=40., lon_0=-20., lat_ts=20.)
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#87CEFA')#689CD2
# draw lat/lon grid lines every 30 degrees.

#map.drawmeridians(np.arange(0, 360, 10))
map.drawmeridians(np.arange(0, 360, 10),labels=[0,0,0,1],fontsize=10)
#map.drawparallels(np.arange(-90, 90, 10))
map.drawparallels(np.arange(-90, 90, 10),labels=[1,0,0,0],fontsize=10)

# Fill continent wit a different color
map.fillcontinents(color='#FFFFFF', lake_color='#87CEFA', zorder=0)

# ============================================draw the stations and data
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons, lats)
max_T = max(day1day)
# Plot each city in a loop.
# Set some parameters
size_factor = 100.0
x_offset = 20.0
y_offset = -20.0
rotation = 0
temp=0

#draw station point
for i, j, k, l, m, n, p in zip(x, y, day2day, station, province, code, codeinfile):
    temp = temp+1
    if k <= -10.0:
        cs1 = map.scatter(i, j, s=15, marker='o', color='#00008F')
    if -10 < k and k <= -5:
        cs2 = map.scatter(i, j, s=15, marker='o', color='#00009F')
    if -5 < k and k <= 0:
        cs3 = map.scatter(i, j, s=15, marker='o', color='#0000FF')
    if 0 < k and k <= 5:
        cs4 = map.scatter(i, j, s=15, marker='o', color='#006FFF')
    if 5 < k and k <= 10:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00BFFF')
    if 10 <= k and k <= 15:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00FFFF')
    if 15 <= k and k <= 20:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#4FFFAF')
    if 20 <= k and k <= 25:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#7FF77F')
    if 25 <= k and k <= 30:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFFF00')
    if 30 <= k and k <= 35:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFBF00')
    if 35 <= k and k <= 40:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF6F00')
    if 40 <= k and k <= 45:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF0000')
    if 45 < k and k != 9999:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#7F0000')
    if l == '上海' or l == '北京' or l == '重庆' or l == '石家庄' or l == '郑州' or l == '武汉' or l == '长沙' or l == '南京' \
            or (l == '南昌' and m == '江西省') or l == '沈阳' or l == '长春' or l == '哈尔滨' or l == '西安' or l == '太原' or l == '济南' or l == '成都' \
            or l == '西宁' or l == '合肥' or l == '海口' or l == '广州' or l == '贵阳' or l == '兰州' or l == '昆明' \
            or l == '拉萨' or l == '银川' or l == '南宁' or l == '乌鲁木齐' or l == '呼和浩特':
        plt.text(i + 20, j - 20, l + '\n' + str(k) + '°', rotation=rotation, fontsize=10)
    if l == '天津' or l == '杭州':
        plt.text(i + 20, j - 100020, l + '\n' + str(k) + '°', rotation=rotation, fontsize=10)
    #print('Original_code:', p, 'Data:', n, l, '实时气温:', str(k), '°')
    f = open("/Users/hsw/Desktop/forecastTdata.txt", "a+")
    f.write('Original_code:'+ p + ' Data:' + date2 + ' 预报最高气温:' + str(k) + '°\n')
    f.close()


title = date2 + '全国最高气温预报图\n' + '预报时间:' + forecastupdatetime + '\n' + author

# ============================================#define legends
a = mlines.Line2D([], [], color='#7F0000', marker='o',
                          markersize=5, label='>45°C',ls='')
b = mlines.Line2D([], [], color='#FF0000', marker='o',
                          markersize=5, label='40~45°C',ls='')
c = mlines.Line2D([], [], color='#FF6F00', marker='o',
                          markersize=5, label='35~40°C',ls='')
d = mlines.Line2D([], [], color='#FFBF00', marker='o',
                          markersize=5, label='30~35°C',ls='')
e = mlines.Line2D([], [], color='#FFFF00', marker='o',
                          markersize=5, label='25~30°C',ls='')
f = mlines.Line2D([], [], color='#7FF77F', marker='o',
                          markersize=5, label='20~25°C',ls='')
g = mlines.Line2D([], [], color='#4FFFAF', marker='o',
                          markersize=5, label='15~20°C',ls='')
h = mlines.Line2D([], [], color='#00FFFF', marker='o',
                          markersize=5, label='10~15°C',ls='')
i = mlines.Line2D([], [], color='#00BFFF', marker='o',
                          markersize=5, label='5~10°C',ls='')
j = mlines.Line2D([], [], color='#006FFF', marker='o',
                          markersize=5, label='0~5°C',ls='')
k = mlines.Line2D([], [], color='#0000FF', marker='o',
                          markersize=5, label='-5~0°C',ls='')
l = mlines.Line2D([], [], color='#00009F', marker='o',
                          markersize=5, label='-10~-5°C',ls='')
m = mlines.Line2D([], [], color='#00008F', marker='o',
                          markersize=5, label='<-10°C',ls='')
plt.legend(handles=[a, b, c, d, e, f, g, h, i, j, k, l, m])
plt.title(title)

# plt.show()
plt.savefig(save3, dpi=100)
plt.show()


# ============================================
# ============================================
# ============================================
# ============================================
# ============================================DRAW FORTH PLOT
# ============================================
# ============================================
# ============================================
# ============================================initialize the plot
plt.figure(figsize=(13, 9), dpi=80)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=70, llcrnrlat=15, urcrnrlon=135, urcrnrlat=55, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='l', projection='merc', \
              lat_0=40., lon_0=-20., lat_ts=20.)
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#87CEFA')#689CD2
# draw lat/lon grid lines every 30 degrees.

#map.drawmeridians(np.arange(0, 360, 10))
map.drawmeridians(np.arange(0, 360, 10),labels=[0,0,0,1],fontsize=10)
#map.drawparallels(np.arange(-90, 90, 10))
map.drawparallels(np.arange(-90, 90, 10),labels=[1,0,0,0],fontsize=10)

# Fill continent wit a different color
map.fillcontinents(color='#FFFFFF', lake_color='#87CEFA', zorder=0)

# ============================================draw the stations and data
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons, lats)
# Plot each city in a loop.
# Set some parameters
size_factor = 100.0
x_offset = 20.0
y_offset = -20.0
rotation = 0
temp=0

#draw station point
for i, j, k, l, m, n, p in zip(x, y, day1dayweather, station, province, code, codeinfile):
    temp = temp+1
    if k == 0:
        cs1 = map.scatter(i, j, s=15, marker='o', color='#FF7F00')
    if k == 1:
        cs2 = map.scatter(i, j, s=15, marker='o', color='#FFE600')
    if k == 2:
        cs3 = map.scatter(i, j, s=15, marker='o', color='#969696')
    if k == 4:
        cs4 = map.scatter(i, j, s=15, marker='o', color='#FA0000')
    if k == 6:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF69B4')
    if k == 3 or k == 7:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#96F278')
    if k == 8 or k == 21 or k == 32:
        cs7 = map.scatter(i, j, s=15, marker='o', color='#56A708')
    if k == 9 or k == 22:
        cs8 = map.scatter(i, j, s=15, marker='o', color='#62B8FB')
    if k == 10 or k == 19 or k == 23:
        cs9 = map.scatter(i, j, s=15, marker='o', color='#244AFC')
    if k == 11 or k == 24:
        cs10 = map.scatter(i, j, s=15, marker='o', color='#E45EFB')
    if k == 12 or k ==25:
        cs11 = map.scatter(i, j, s=15, marker='o', color='#8B0000')
    if k == 5 or k == 13 or k ==14:
        cs12 = map.scatter(i, j, s=15, marker='o', color='#D3D3D3')
    if k == 15 or k == 26 or k == 33:
        cs13 = map.scatter(i, j, s=15, marker='o', color='#A9A9A9')
    if k == 16 or k == 27:
        cs14 = map.scatter(i, j, s=15, marker='o', color='#808080')
    if k == 17 or k == 28:
        cs15 = map.scatter(i, j, s=15, marker='o', color='#000000')
    if k == 18 or k == 20 or k == 29 or k == 30 or k == 31:
        cs15 = map.scatter(i, j, s=15, marker='o', color='#FFD700')
    if l == '上海' or l == '北京' or l == '重庆' or l == '石家庄' or l == '郑州' or l == '武汉' or l == '长沙' or l == '南京' \
            or (l == '南昌' and m == '江西省') or l == '沈阳' or l == '长春' or l == '哈尔滨' or l == '西安' or l == '太原' or l == '济南' or l == '成都' \
            or l == '西宁' or l == '合肥' or l == '海口' or l == '广州' or l == '贵阳' or l == '兰州' or l == '昆明' \
            or l == '拉萨' or l == '银川' or l == '南宁' or l == '乌鲁木齐' or l == '呼和浩特':
        plt.text(i + 20, j - 20, l, rotation=rotation, fontsize=10)
    if l == '天津' or l == '杭州':
        plt.text(i + 20, j - 100020, l, rotation=rotation, fontsize=10)
    #print('Original_code:', p, 'Data:', n, l, '实时气温:', str(k), '°')
    f = open("/Users/hsw/Desktop/forecastTdata.txt", "a+")
    f.write('Original_code:'+ p + ' Data:' + date1 + ' 预报天气现象代码:' + str(k) + '°\n')
    f.close()


title = date1 + '白天全国天气现象预报图\n' + '预报时间:' + forecastupdatetime + '\n' + author

# ============================================#define legends
a = mlines.Line2D([], [], color='#FF7F00', marker='o',
                          markersize=5, label='晴天',ls='')
b = mlines.Line2D([], [], color='#FFE600', marker='o',
                          markersize=5, label='多云',ls='')
c = mlines.Line2D([], [], color='#969696', marker='o',
                          markersize=5, label='阴天',ls='')
d = mlines.Line2D([], [], color='#FA0000', marker='o',
                          markersize=5, label='雷阵雨',ls='')
e = mlines.Line2D([], [], color='#FF69B4', marker='o',
                          markersize=5, label='雨夹雪',ls='')
f = mlines.Line2D([], [], color='#96F278', marker='o',
                          markersize=5, label='小雨',ls='')
g = mlines.Line2D([], [], color='#56A708', marker='o',
                          markersize=5, label='中雨',ls='')
h = mlines.Line2D([], [], color='#62B8FB', marker='o',
                          markersize=5, label='大雨',ls='')
i = mlines.Line2D([], [], color='#244AFC', marker='o',
                          markersize=5, label='暴雨',ls='')
j = mlines.Line2D([], [], color='#E45EFB', marker='o',
                          markersize=5, label='大暴雨',ls='')
k = mlines.Line2D([], [], color='#8B0000', marker='o',
                          markersize=5, label='特大暴雨',ls='')
l = mlines.Line2D([], [], color='#D3D3D3', marker='o',
                          markersize=5, label='小雪',ls='')
m = mlines.Line2D([], [], color='#A9A9A9', marker='o',
                          markersize=5, label='中雪',ls='')
n = mlines.Line2D([], [], color='#808080', marker='o',
                          markersize=5, label='大雪',ls='')
o = mlines.Line2D([], [], color='#000000', marker='o',
                          markersize=5, label='暴雪',ls='')
p = mlines.Line2D([], [], color='#FFD700', marker='o',
                          markersize=5, label='雾、霾、沙尘',ls='')
plt.legend(handles=[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p])
plt.title(title)

# plt.show()
plt.savefig(save4, dpi=100)
plt.show()

# ============================================
# ============================================
# ============================================
# ============================================
# ============================================DRAW FIFTH PLOT
# ============================================
# ============================================
# ============================================
# ============================================initialize the plot
plt.figure(figsize=(13, 9), dpi=80)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=70, llcrnrlat=15, urcrnrlon=135, urcrnrlat=55, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='l', projection='merc', \
              lat_0=40., lon_0=-20., lat_ts=20.)
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#87CEFA')#689CD2
# draw lat/lon grid lines every 30 degrees.

#map.drawmeridians(np.arange(0, 360, 10))
map.drawmeridians(np.arange(0, 360, 10),labels=[0,0,0,1],fontsize=10)
#map.drawparallels(np.arange(-90, 90, 10))
map.drawparallels(np.arange(-90, 90, 10),labels=[1,0,0,0],fontsize=10)

# Fill continent wit a different color
map.fillcontinents(color='#FFFFFF', lake_color='#87CEFA', zorder=0)

# ============================================draw the stations and data
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons, lats)
# Plot each city in a loop.
# Set some parameters
size_factor = 100.0
x_offset = 20.0
y_offset = -20.0
rotation = 0
temp=0

#draw station point
for i, j, k, l, m, n, p in zip(x, y, day2dayweather, station, province, code, codeinfile):
    temp = temp+1
    if k == 0:
        cs1 = map.scatter(i, j, s=15, marker='o', color='#FF7F00')
    if k == 1:
        cs2 = map.scatter(i, j, s=15, marker='o', color='#FFE600')
    if k == 2:
        cs3 = map.scatter(i, j, s=15, marker='o', color='#969696')
    if k == 4:
        cs4 = map.scatter(i, j, s=15, marker='o', color='#FA0000')
    if k == 6:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF69B4')
    if k == 3 or k == 7:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#96F278')
    if k == 8 or k == 21 or k == 32:
        cs7 = map.scatter(i, j, s=15, marker='o', color='#56A708')
    if k == 9 or k == 22:
        cs8 = map.scatter(i, j, s=15, marker='o', color='#62B8FB')
    if k == 10 or k == 19 or k == 23:
        cs9 = map.scatter(i, j, s=15, marker='o', color='#244AFC')
    if k == 11 or k == 24:
        cs10 = map.scatter(i, j, s=15, marker='o', color='#E45EFB')
    if k == 12 or k ==25:
        cs11 = map.scatter(i, j, s=15, marker='o', color='#8B0000')
    if k == 5 or k == 13 or k ==14:
        cs12 = map.scatter(i, j, s=15, marker='o', color='#D3D3D3')
    if k == 15 or k == 26 or k == 33:
        cs13 = map.scatter(i, j, s=15, marker='o', color='#A9A9A9')
    if k == 16 or k == 27:
        cs14 = map.scatter(i, j, s=15, marker='o', color='#808080')
    if k == 17 or k == 28:
        cs15 = map.scatter(i, j, s=15, marker='o', color='#000000')
    if k == 18 or k == 20 or k == 29 or k == 30 or k == 31:
        cs15 = map.scatter(i, j, s=15, marker='o', color='#FFD700')
    if l == '上海' or l == '北京' or l == '重庆' or l == '石家庄' or l == '郑州' or l == '武汉' or l == '长沙' or l == '南京' \
            or (l == '南昌' and m == '江西省') or l == '沈阳' or l == '长春' or l == '哈尔滨' or l == '西安' or l == '太原' or l == '济南' or l == '成都' \
            or l == '西宁' or l == '合肥' or l == '海口' or l == '广州' or l == '贵阳' or l == '兰州' or l == '昆明' \
            or l == '拉萨' or l == '银川' or l == '南宁' or l == '乌鲁木齐' or l == '呼和浩特':
        plt.text(i + 20, j - 20, l, rotation=rotation, fontsize=10)
    if l == '天津' or l == '杭州':
        plt.text(i + 20, j - 100020, l, rotation=rotation, fontsize=10)
    #print('Original_code:', p, 'Data:', n, l, '实时气温:', str(k), '°')
    f = open("/Users/hsw/Desktop/forecastTdata.txt", "a+")
    f.write('Original_code:'+ p + ' Data:' + date2 + ' 预报天气现象代码:' + str(k) + '°\n')
    f.close()


title = date2 + '白天全国天气现象预报图\n' + '预报时间:' + forecastupdatetime + '\n' + author

# ============================================#define legends
a = mlines.Line2D([], [], color='#FF7F00', marker='o',
                          markersize=5, label='晴天',ls='')
b = mlines.Line2D([], [], color='#FFE600', marker='o',
                          markersize=5, label='多云',ls='')
c = mlines.Line2D([], [], color='#969696', marker='o',
                          markersize=5, label='阴天',ls='')
d = mlines.Line2D([], [], color='#FA0000', marker='o',
                          markersize=5, label='雷阵雨',ls='')
e = mlines.Line2D([], [], color='#FF69B4', marker='o',
                          markersize=5, label='雨夹雪',ls='')
f = mlines.Line2D([], [], color='#96F278', marker='o',
                          markersize=5, label='小雨',ls='')
g = mlines.Line2D([], [], color='#56A708', marker='o',
                          markersize=5, label='中雨',ls='')
h = mlines.Line2D([], [], color='#62B8FB', marker='o',
                          markersize=5, label='大雨',ls='')
i = mlines.Line2D([], [], color='#244AFC', marker='o',
                          markersize=5, label='暴雨',ls='')
j = mlines.Line2D([], [], color='#E45EFB', marker='o',
                          markersize=5, label='大暴雨',ls='')
k = mlines.Line2D([], [], color='#8B0000', marker='o',
                          markersize=5, label='特大暴雨',ls='')
l = mlines.Line2D([], [], color='#D3D3D3', marker='o',
                          markersize=5, label='小雪',ls='')
m = mlines.Line2D([], [], color='#A9A9A9', marker='o',
                          markersize=5, label='中雪',ls='')
n = mlines.Line2D([], [], color='#808080', marker='o',
                          markersize=5, label='大雪',ls='')
o = mlines.Line2D([], [], color='#000000', marker='o',
                          markersize=5, label='暴雪',ls='')
p = mlines.Line2D([], [], color='#FFD700', marker='o',
                          markersize=5, label='雾、霾、沙尘',ls='')
plt.legend(handles=[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p])
plt.title(title)

# plt.show()
plt.savefig(save5, dpi=100)
plt.show()


