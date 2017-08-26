#encoding:UTF-8

import urllib
import urllib.request
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.lines as mlines
import numpy as np

# ============================================initialize the plot
plt.figure(figsize=(5, 6), dpi=120)
axes = plt.subplot(111)

# set up map projection with
# use low resolution coastlines.
map = Basemap(llcrnrlon=120.8, llcrnrlat=30.5, urcrnrlon=122.2, urcrnrlat=32, \
              rsphere=(6378137.00, 6356752.3142), \
              resolution='h', projection='merc', \
              lat_0=40., lon_0=-20., lat_ts=20.)

# draw coastlines, country boundaries, fill continents.
#map.drawcoastlines(linewidth=0.25)
#map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#DDDDDD')#689CD2
# draw lat/lon grid lines every 30 degrees.

#map.drawmeridians(np.arange(0, 360, 10))
map.drawmeridians(np.arange(0, 360, 10),labels=[0,0,0,1],fontsize=10)
#map.drawparallels(np.arange(-90, 90, 10))
map.drawparallels(np.arange(-90, 90, 10),labels=[1,0,0,0],fontsize=10)

# Fill continent wit a different color
map.fillcontinents(color='#DDDDDD', lake_color='#87CEFA', zorder=0)

map.readshapefile(shapefile='/Users/hsw/Downloads/shanghai_shp/Shanghai_county',name='1', drawbounds=True, linewidth=0.5, color='red', default_encoding='UTF-8')

plt.title('上海市实时分区预警信号分布图')
plt.show()