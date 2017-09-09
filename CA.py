#-*- coding:utf8 -*-
import sys
sys.path.append('/usr/lib/python3/dist-packages/matplotlib/externals/')

import matplotlib
matplotlib.use('Agg')

from xml.parsers.expat import ParserCreate
import xml.etree.ElementTree as et
import requests
import time
import os
import json
import urllib
import urllib.request
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from PIL import Image,ImageDraw,ImageFont

from matplotlib.font_manager import FontProperties
#chinese_font = FontProperties(fname='/home/weather/hsefz_server/program_font/simhei.ttf')

emaillist = []

def getweather():
    url = 'http://dd.weather.gc.ca/citypage_weather/xml/ON/s0000458_e.xml'
    xml = (requests.get(url).text)
    #print(xml)
    root = et.fromstring(xml)

    current = et.Element("CURRENT")
    hourly = et.Element("HOURLY")
    forecast = et.Element("FORECAST")
    yesterday = et.Element("YESTERDAY")
    info = et.Element("INFO")

    for child in root:  # layer two
        #print(child.tag, child.attrib, child.text)  # <om:Observation> #
        if child.tag == 'currentConditions':
            current.append(child)
        if child.tag == 'forecastGroup':
            forecast.append(child)
        if child.tag == 'hourlyForecastGroup':
            hourly.append(child)
        if child.tag == 'yesterdayConditions':
            yesterday.append(child)

    # ============================================ # process weather forecast data
    info = ''
    weather = []
    time = []
    count = 0

    for subforecast in forecast:
        #print(subforecast.tag, subforecast.attrib, subforecast.text)
        for sub in subforecast:
            #print(subforecast.tag, subforecast.attrib, subforecast.text)
            count = count + 1
            for i in sub:
                if count == 1 and i.tag == 'textSummary':
                    info = i.text
                    #print(info+'\n')
                if count >=4:
                    #print(i.tag, i.attrib, i.text)
                    if i.tag == 'textSummary':
                        weather.append(i.text)
                    if i.tag == 'period':
                        time.append(i.text)

    result = ''
    for i in range(0, len(weather)):
        if i == 0:
            result = result + 'Weather Forecast for Toronto\nissued by Environment Canada at ' + info + '\n\n'
            result = result + 'Next 24 Hours Forecast\n'
        if i == 2:
            result = result + '\nMedium Range Forecast\n'
        result = result + time[i] + ': ' + weather[i] + '\n\n'

    result = result + '\n\n***********************\nThis Message Was Sent Directly From Server\n<PLEASE DO NOT REPLY!>'
    print(result)

    f = open("/home/weather/hsefz_server/weather_map/mailtext/CAtext.txt", "w+")
    f.write(result)
    f.close()

def getemaillist():
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] GET EMAIL LIST')
    global emaillist
    file = "/home/weather/hsefz_server/secret/CAmailto.txt"
    fh = open(file)
    for line in fh:
        info = line.split()
        emailaddress = info[0]
        emaillist.append(emailaddress)
        print('target_email: '+emailaddress)
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] GET EMAIL LIST COMPLETE')

def sendemail():
    global emaillist
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] SEND EMAIL START')
    for i in emaillist:
        os.system('mutt -s "Toronto_Weather" -- ' + i + ' < mailtext/CAtext.txt')
        print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] EMAIL TO ' + i + ' SEND COMPLETE')
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] ALL EMAILS WERE SENT COMPLETE')

def timer(n):
    ''''' 
    每n秒执行一次 
    '''
    while True:
        print ('[' + time.strftime('%Y-%m-%d %X',time.localtime()) + '] CYCLE START')
        getweather()  # 此处为要执行的任务
        sendemail()
        time.sleep(n)
        print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] PROGRAM SLEEP')

print ('[' + time.strftime('%Y-%m-%d %X',time.localtime()) + '] PROGRAM START')
getemaillist()
timer(43195)
'''
# ============================================ # process weather data
weather = []
MSL = []
vis = []
T= []
dew = []
hum = []
ws = []
wd = []
gust = []
C = []
WC = []

count = 0
for s in stations:
    #print(s.tag, s.attrib, s.text)#<om:result>
    for d in s:
        count = count + 1
        for data in d:
            if count != 1:
                #print(data.tag, data.attrib, data.text)#station weather data
                record = str(data.attrib)
                record = record.replace("'",'"')
                data = json.loads(record)
                #print(data['name']+' '+data['value'])
                if data['name'] == 'present_weather':
                    weather.append(data['value'])
                if data['name'] == 'mean_sea_level':
                    if data['value'] != '':
                        MSL.append(float(data['value']))
                    else:
                        MSL.append(float('9999'))
                if data['name'] == 'horizontal_visibility':
                    if data['value'] != '':
                        vis.append(float(data['value']))
                    else:
                        vis.append(float('9999'))
                if data['name'] == 'air_temperature':
                    if data['value'] != '':
                        T.append(float(data['value']))
                    else:
                        T.append(float('9999'))
                if data['name'] == 'dew_point':
                    if data['value'] != '':
                        dew.append(float(data['value']))
                    else:
                        dew.append(float('9999'))
                if data['name'] == 'relative_humidity':
                    if data['value'] != '':
                        hum.append(float(data['value']))
                    else:
                        hum.append(float('9999'))
                if data['name'] == 'wind_speed':
                    if data['value'] != '':
                        ws.append(float(data['value']))
                    else:
                        ws.append(float('9999'))
                if data['name'] == 'wind_direction':
                    wd.append(data['value'])
                if data['name'] == 'wind_gust_speed':
                    if data['value'] != '':
                        gust.append(float(data['value']))
                    else:
                        gust.append(float('9999'))
                if data['name'] == 'total_cloud_cover':
                    C.append(data['value'])
                if data['name'] == 'wind_chill':
                    WC.append(data['value'])

# ============================================ # process station info
stationname = []
lats = []
lons = []
CA_id = []
CSN = []
WMO = []

count = 0
for s in info:
    count = count + 1
    for station in s:
        #print(station.tag, station.attrib, station.text)
        for detail in station:
            #print(detail.tag, detail.attrib, detail.text)
            for stationinfo in detail:
                if detail.tag == '{http://dms.ec.gc.ca/schema/point-observation/2.1}identification-elements' and count != 1:
                    #print(stationinfo.tag, stationinfo.attrib, stationinfo.text)
                    record = str(stationinfo.attrib)
                    record = record.replace("'", '"')
                    record = record.replace('Int"l', "Int'l")
                    data = json.loads(record)
                    if data['name'] == 'station_name':
                        stationname.append(data['value'])
                    if data['name'] == 'latitude':
                        lats.append(float(data['value']))
                    if data['name'] == 'longitude':
                        lons.append(float(data['value']))
                    if data['name'] == 'transport_canada_id':
                        CA_id.append(data['value'])
                    if data['name'] == 'climate_station_number':
                        CSN.append(data['value'])
                    if data['name'] == 'wmo_station_number':
                        WMO.append(data['value'])

# ============================================ # plot
# ============================================initialize the plot
plt.figure(figsize=(11, 8), dpi=120)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=-98, llcrnrlat=40, urcrnrlon=-70, urcrnrlat=58, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='i', projection='merc', \
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
map.fillcontinents(color='#FFFFFF', lake_color='#EEEEEE', zorder=0)

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

f = open("/Users/hsw/Desktop/CA_Tdata.txt", "w+")
f.close()
#draw station point

analyze = ''

for i, j, k, l, m in zip(x, y, T, stationname, WMO):
    temp = temp+1
    size = size_factor * k / max_T
    if k <= -10.0:
        cs1 = map.scatter(i, j, s=15, marker='o', color='#00008F')
    if -10 < k and k <= -5:
        cs2 = map.scatter(i, j, s=15, marker='o', color='#00009F')
    if -5 < k and k <= -2:
        cs3 = map.scatter(i, j, s=15, marker='o', color='#0000FF')
    if -2 < k and k <= 2:
        cs4 = map.scatter(i, j, s=15, marker='o', color='#006FFF')
    if 2 < k and k <= 6:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00BFFF')
    if 6 <= k and k <= 10:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#00FFFF')
    if 10 <= k and k <= 14:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#4FFFAF')
    if 14 <= k and k <= 18:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#7FF77F')
    if 18 <= k and k <= 22:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFFF00')
    if 22 <= k and k <= 26:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FFBF00')
    if 26 <= k and k <= 30:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF6F00')
    if 30 <= k and k <= 35:
        cs5 = map.scatter(i, j, s=15, marker='o', color='#FF0000')
    if 35 < k and k != 9999:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#7F0000')

    #if k != 9999:
    #    plt.text(i, j, str(k) + '°C', rotation=rotation, fontsize=10)

    f = open("/Users/hsw/Desktop/CA_Tdata.txt", "a+")
    f.write('WMO_code:' + m + ' Station:'+ l + ' Temperature:' + str(k) + '\n')
    f.close()


title = '加拿大安大略省气温分布图\n' + '数据更新时间:T' + time + 'UTC\n数据来自：Environment Canada, 绘制@Louis_He'
# ============================================#define legends
a = mlines.Line2D([], [], color='#7F0000', marker='o',
                              markersize=5, label='>35°C',ls='')
b = mlines.Line2D([], [], color='#FF0000', marker='o',
                              markersize=5, label='>30°C',ls='')
c = mlines.Line2D([], [], color='#FF6F00', marker='o',
                              markersize=5, label='26~30°C',ls='')
d = mlines.Line2D([], [], color='#FFBF00', marker='o',
                          markersize=5, label='22~26°C',ls='')
e = mlines.Line2D([], [], color='#FFFF00', marker='o',
                          markersize=5, label='18~22°C',ls='')
f = mlines.Line2D([], [], color='#7FF77F', marker='o',
                          markersize=5, label='14~18°C',ls='')
g = mlines.Line2D([], [], color='#4FFFAF', marker='o',
                          markersize=5, label='10~14°C',ls='')
h = mlines.Line2D([], [], color='#00FFFF', marker='o',
                          markersize=5, label='6~10°C',ls='')
i = mlines.Line2D([], [], color='#00BFFF', marker='o',
                          markersize=5, label='2~6°C',ls='')
j = mlines.Line2D([], [], color='#006FFF', marker='o',
                          markersize=5, label='-2~2°C',ls='')
k = mlines.Line2D([], [], color='#0000FF', marker='o',
                          markersize=5, label='-5~-2°C',ls='')
l = mlines.Line2D([], [], color='#00009F', marker='o',
                          markersize=5, label='-10~-5°C',ls='')
m = mlines.Line2D([], [], color='#00008F', marker='o',
                          markersize=5, label='<-10°C',ls='')
plt.legend(handles=[b, c, d, e, f, g, h, i, j, k, l, m])
plt.title(title)

save = '/Users/hsw/Desktop/CA_Tsample.png'
plt.savefig(save, dpi=120)

# ============================================#plot station data on graph
im = Image.open("/Users/hsw/Desktop/CA_Tsample.png")
draw = ImageDraw.Draw(im)
ttFont = ImageFont.truetype ("AppleSDGothicNeo.ttc", 16)

draw.text ((10, 115), 'Weather Station List + Temperature(°C):', fill=(255,0,0), font=ttFont)

for i in range(1, len(stationname)):
    if (stationname[i]=="Toronto Downtown"):
        draw.text ((10, 145), stationname[i] +'\t\t'+ str(T[i])+'°C', fill=(255,0,0), font=ttFont)
    if (stationname[i]=="Toronto City Centre Airport"):
        draw.text ((10, 165), stationname[i] +'\t\t'+ str(T[i])+'°C', fill=(255,0,0), font=ttFont)
    if (stationname[i]=="Toronto Pearson Int'l Airport"):
        draw.text ((10, 185), stationname[i] +'\t\t'+ str(T[i])+'°C', fill=(255,0,0), font=ttFont)
    if (stationname[i]=="Toronto Buttonville Municipal Airport"):
        draw.text ((10, 205), 'Buttonville Municipal Airport\t\t'+ str(T[i])+'°C', fill=(255,0,0), font=ttFont)

im.show()
im.save('/Users/hsw/Desktop/CA_Tsample.png')
'''