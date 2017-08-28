#encoding:UTF-8

import urllib
import urllib.request
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.lines as mlines
import numpy as np
import time

data = urllib.request.urlopen('https://stationdata.wunderground.com/cgi-bin/stationdata?iconsize=3&width=2048&height=2048&maxage=3600&format=json&maxstations=100000&rf_filter=1&minlat=38&minlon=-85&maxlat=48&maxlon=-73').read()
record = data.decode('UTF-8')
record = record.replace('},}', '}}')
a = open("/Users/hsw/Desktop/CA_region_rawdata.txt", "w+")
a.write(record)
a.close()

data = json.loads(record)
#print(data)

print(data['conds'])
preprocess = data['conds']

station = []
T = []
lats = []
lons = []

for o in preprocess:
    id = str(o)
    station.append(preprocess[id]['id'])
    T.append(5/9*(float(preprocess[id]['tempf'])-32))
    lats.append(float(preprocess[id]['lat']))
    lons.append(float(preprocess[id]['lon']))

# ============================================ # plot
# ============================================initialize the plot
plt.figure(figsize=(11, 8), dpi=120)
axes = plt.subplot(111)
# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=-87, llcrnrlat=38, urcrnrlon=-73, urcrnrlat=48, \
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

f = open("/Users/hsw/Desktop/CA_region_Tdata.txt", "w+")
f.close()
#draw station point

analyze = ''

for i, j, k, l in zip(x, y, T, station):
    temp = temp+1
    size = size_factor * k / max_T
    if k <= -10.0 and k >= -100.0:
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
    if 35 < k and k <= 100:
        cs6 = map.scatter(i, j, s=15, marker='o', color='#7F0000')

    #if k != 9999:
    #    plt.text(i, j, str(k) + '°C', rotation=rotation, fontsize=10)

    f = open("/Users/hsw/Desktop/CA_region_Tdata.txt", "a+")
    f.write(' Station:'+ l + ' Temperature:' + str(k) + '\n')
    f.close()


title = '多伦多及附近地区气温分布图\n' + '数据更新时间:' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()- 8 * 60 * 60 * 1000)) + 'UTC\n数据来自：wunderground weather, 绘制@Louis_He'
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

save = '/Users/hsw/Desktop/CA_region_Tsample.png'
plt.savefig(save, dpi=120)
