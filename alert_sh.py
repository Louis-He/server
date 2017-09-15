#encoding:UTF-8
import sys
sys.path.append('/usr/lib/python3/dist-packages/matplotlib/externals/')

import matplotlib
matplotlib.use('Agg')

import os
import urllib
import urllib.request
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.patches import Polygon
import numpy as np
import time

from matplotlib.font_manager import FontProperties
chinese_font = FontProperties(fname='/home/weather/hsefz_server/program_font/simhei.ttf')

fqcolor = []
notify = False
latestwarn = []
emaillist = []
alarmflag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def getalarm():
    global notify
    global latestwarn
    global alarmflag
    global shanghai
    global chongming
    global baoshan
    global jiading
    global qingpu
    global songjiang
    global minhang
    global pudong
    global jinshan
    global fengxian
    global latestwarn

    #http://182.254.214.114/wxapp/jsondata/fqwarnlist.js
    # ============================================get realtime alerts
    data = urllib.request.urlopen('http://182.254.214.114/wxapp/jsondata/fqwarnlist.js').read()
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] RAW DATA INPUT COMPLETE')

    record = data.decode('UTF-8')
    #print('DEBUG PURPOSE: ',record)
    record=record.replace('[市预警发布中心]','「市预警发布中心」')

    fqwarn = record[record.index('=[')+1:record.index(']')+1]
    record = record[record.index(']')+1:len(record)]
    #print(fqwarn)

    fqwarnhistory = record[record.index('=[')+1:record.index(']')+1]
    record = record[record.index(']')+1:len(record)]
    #print(fqwarnhistory)

    warn = record[record.index('var warns=[')+len('var warns='):record.index(']')+1]
    #print(warn)

    regionwarn = json.loads(fqwarn)
    citywarn = json.loads(warn)

    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] RAW DATA JSON ANALYSIS COMPLETE')
    # ============================================analyze district warning

    warninfo = []
    alarmflag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    shanghai = []
    chongming = []
    baoshan = []
    jiading = []
    qingpu = []
    songjiang = []
    minhang = []
    pudong = []
    jinshan = []
    fengxian = []

    for o in regionwarn:
        if o['yjfbdw']=='崇明区气象台':
            chongming.append(o['name'])
        if o['yjfbdw']=='宝山区气象台':
            baoshan.append(o['name'])
        if o['yjfbdw']=='嘉定区气象台':
            jiading.append(o['name'])
        if o['yjfbdw']=='青浦区气象台':
            qingpu.append(o['name'])
        if o['yjfbdw']=='松江区气象台':
            songjiang.append(o['name'])
        if o['yjfbdw']=='闵行区气象台':
            minhang.append(o['name'])
        if o['yjfbdw']=='浦东新区气象台':
            pudong.append(o['name'])
        if o['yjfbdw']=='金山区气象台':
            jinshan.append(o['name'])
        if o['yjfbdw']=='奉贤区气象台':
            fengxian.append(o['name'])
        if '台风' in o['name']:
            alarmflag[0] = 1
        if '暴雨' in o['name']:
            alarmflag[1] = 1
        if '暴雪' in o['name']:
            alarmflag[2] = 1
        if '寒潮' in o['name']:
            alarmflag[3] = 1
        if '大风' in o['name']:
            alarmflag[4] = 1
        if '沙尘暴' in o['name']:
            alarmflag[5] = 1
        if '高温' in o['name']:
            alarmflag[6] = 1
        if '干旱' in o['name']:
            alarmflag[7] = 1
        if '雷电' in o['name']:
            alarmflag[8] = 1
        if '冰雹' in o['name']:
            alarmflag[9] = 1
        if '霜冻' in o['name']:
            alarmflag[10] = 1
        if '大雾' in o['name']:
            alarmflag[11] = 1
        if '霾' in o['name']:
            alarmflag[12] = 1
        if '道路结冰' in o['name']:
            alarmflag[13] = 1


    for o in citywarn:
        shanghai.append(o['name'])
        warninfo.append(o['htmlword'])


    def analyzecolor(warnlist):
        global fqcolor
        global shanghai
        global chongming
        global baoshan
        global jiading
        global qingpu
        global songjiang
        global minhang
        global pudong
        global jinshan
        global fengxian
        global latestwarn
        #print(warnlist)
        max = 0
        for i in warnlist:
            if '蓝色' in i and max == 0:
                max = 1
            if '黄色' in i and max <= 1:
                max = 2
            if '橙色' in i and max <= 2:
                max = 3
            if '红色' in i and max <= 3:
                max = 4
            #print(i, max)
        fqcolor.append(max)

    fqcolor = []
    analyzecolor(shanghai)
    analyzecolor(chongming)
    analyzecolor(baoshan)
    analyzecolor(jiading)
    analyzecolor(qingpu)
    analyzecolor(songjiang)
    analyzecolor(minhang)
    analyzecolor(pudong)
    analyzecolor(jinshan)
    analyzecolor(fengxian)

    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] DATA ANALYSIS COMPLETE')

    for i in range(0,len(shanghai)):
        if i > len(latestwarn)-1 or shanghai[i] != latestwarn[i]:
            notify = True

    latestwarn = shanghai

    f = open("/home/weather/hsefz_server/weather_map/mailtext/text.txt", "w+")
    f.close()

    for i in range(0,len(shanghai)):
        f = open("/home/weather/hsefz_server/weather_map/mailtext/text.txt", "a+")
        f.write('[市预警发布中心]上海市中心气象台发布'+shanghai[0]+'预警信号：\n'+warninfo[0]+'\n\n')
        f.close()

    f = open("/home/weather/hsefz_server/weather_map/mailtext/text.txt", "a+")
    f.write('###################################\n'
            '这封邮件由华师大二附中气象服务中心服务器自动发出,<请不要回复！>\nThis email was directly sent from HSEFZ Meteorological Service Center,<PLEASE DO NOT RESPOND!>')
    f.close()
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] TEXT FILE COMPLETE')


    if notify:
        print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] ALARM CONDITION UPDATE! ALARMS SHOWED BELOW:')
        print(shanghai)
        plot()
        sendemail()

    notify = False
    #print(fqcolor)

def plot():
    global fqcolor
    # ============================================initialize the plot
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] INITIALIZE THE PLOT')
    plt.figure(figsize=(5, 6), dpi=120)
    axes = plt.subplot(111)

    # set up map projection with
    # use low resolution coastlines.
    map = Basemap(llcrnrlon=120.8, llcrnrlat=30.5, urcrnrlon=122.2, urcrnrlat=32, \
                  rsphere=(6378137.00, 6356752.3142), \
                  resolution='l', projection='merc', \
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
    #map.fillcontinents(color='#DDDDDD', lake_color='#87CEFA', zorder=0)

    shp_info = map.readshapefile('/home/weather/hsefz_server/weather_map/shanghai_shp/Shanghai_county','shanghai',drawbounds=False)
    for info, shp in zip(map.shanghai_info, map.shanghai):
        proid = info['NAME_3']
        if proid == 'Shanghai' and fqcolor[0]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Shanghai' and fqcolor[0]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Shanghai' and fqcolor[0]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Shanghai' and fqcolor[0]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Shanghai' and fqcolor[0]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Chongming' and fqcolor[1]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Chongming' and fqcolor[1]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Chongming' and fqcolor[1]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Chongming' and fqcolor[1]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Chongming' and fqcolor[1]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Baoshan' and fqcolor[2]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Baoshan' and fqcolor[2]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Baoshan' and fqcolor[2]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Baoshan' and fqcolor[2]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Baoshan' and fqcolor[2]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Jiading' and fqcolor[3]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jiading' and fqcolor[3]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jiading' and fqcolor[3]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jiading' and fqcolor[3]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jiading' and fqcolor[3]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Qingpu' and fqcolor[4]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Qingpu' and fqcolor[4]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Qingpu' and fqcolor[4]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Qingpu' and fqcolor[4]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Qingpu' and fqcolor[4]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Songjiang' and fqcolor[5]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Songjiang' and fqcolor[5]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Songjiang' and fqcolor[5]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Songjiang' and fqcolor[5]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Songjiang' and fqcolor[5]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Minhang' and fqcolor[6]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Minhang' and fqcolor[6]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Minhang' and fqcolor[6]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Minhang' and fqcolor[6]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Minhang' and fqcolor[6]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Pudong' and fqcolor[7]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Pudong' and fqcolor[7]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Pudong' and fqcolor[7]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Pudong' and fqcolor[7]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Pudong' and fqcolor[7]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Nanhui' and fqcolor[7]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Nanhui' and fqcolor[7]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Nanhui' and fqcolor[7]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Nanhui' and fqcolor[7]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Nanhui' and fqcolor[7]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Jinshan' and fqcolor[8]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jinshan' and fqcolor[8]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jinshan' and fqcolor[8]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jinshan' and fqcolor[8]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Jinshan' and fqcolor[8]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

        if proid == 'Fengxian' and fqcolor[9]==0:
            poly = Polygon(shp,facecolor='w',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Fengxian' and fqcolor[9]==1:
            poly = Polygon(shp,facecolor='blue',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Fengxian' and fqcolor[9]==2:
            poly = Polygon(shp,facecolor='yellow',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Fengxian' and fqcolor[9]==3:
            poly = Polygon(shp,facecolor='orange',edgecolor='b', lw=0.2)
            axes.add_patch(poly)
        if proid == 'Fengxian' and fqcolor[9]==4:
            poly = Polygon(shp,facecolor='red',edgecolor='b', lw=0.2)
            axes.add_patch(poly)

    plt.text(65507.8, 139347, '崇明区', fontsize=9,fontproperties=chinese_font)
    plt.text(38152.6, 105400, '嘉定区', fontsize=9,fontproperties=chinese_font)
    plt.text(57268.3, 110344, '宝山区', fontsize=9,fontproperties=chinese_font)
    plt.text(14093.3, 72112.2, '青浦区', fontsize=9,fontproperties=chinese_font)
    plt.text(60230.3, 89250.4, '中心城区', fontsize=9,fontproperties=chinese_font)
    plt.text(84293.9, 76385.5, '浦东新区', fontsize=9,fontproperties=chinese_font)
    plt.text(36175.1, 61236.1, '松江区', fontsize=9,fontproperties=chinese_font)
    plt.text(60564.1, 73101, '闵行区', fontsize=9,fontproperties=chinese_font)
    plt.text(38811.8, 39813.3, '金山区', fontsize=9,fontproperties=chinese_font)
    plt.text(68803.6, 49700.7, '奉贤区', fontsize=9,fontproperties=chinese_font)
    #map.readshapefile(shapefile='/Users/hsw/Downloads/shanghai_shp/Shanghai_county',name='1', drawbounds=True, linewidth=0.5, color='red', default_encoding='UTF-8')

    plt.title('上海市实时分区预警信号分布图\n最搞预警信号级别落区\n' + '更新时间:' + time.strftime('%Y年%m月%d日 %H时%M分%S秒',time.localtime(time.time())),fontproperties=chinese_font)
    plt.savefig('/home/weather/hsefz_server/weather_map/diagrams/alert.png',dpi=100)
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] PLOT COMPLETE')

def getemaillist():
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] GET EMAIL LIST')
    global emaillist
    file = "/home/weather/hsefz_server/secret/mailto.txt"
    fh = open(file)
    for line in fh:
        info = line.split()
        emailaddress = info[0]
        emaillist.append(emailaddress)
        print('target_email: '+emailaddress)
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] GET EMAIL LIST COMPLETE')

def sendemail():
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] SEND EMAIL START')
    global emaillist
    for i in emaillist:
        os.system('mutt -s "预警信号_WeatherALARM" -a diagrams/alert.png -- '+i+' < mailtext/text.txt')
        print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] EMAIL TO '+i+' SEND COMPLETE')
    print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] ALL EMAILS WERE SENT COMPLETE')

def timer(n):
    ''''' 
    每n秒执行一次 
    '''
    while True:
        print ('[' + time.strftime('%Y-%m-%d %X',time.localtime()) + '] CYCLE START')
        getalarm()  # 此处为要执行的任务
        time.sleep(n)
        print('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + '] PROGRAM SLEEP')

print ('[' + time.strftime('%Y-%m-%d %X',time.localtime()) + '] PROGRAM START')
getemaillist()
timer(120)