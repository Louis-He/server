# weather_map server version


Using the data from National Meteorological Center of CMA to plot the realtime weather map(Temperature), and future two days Temperature and weather Forecast. Other charts will be added to this project in the future:

'getData.py' is used to plot realtime and forecast graphs.


Using the data from Shanghai Meteorological Bureau to plot realtime alarm:

'alert_sh.py' is used to plot realtime alerts in Shanghai every districts(Graph shows the higest level of alarm).

# 天气图server版

通过使用中国气象局中央气象台的数据绘出中国地区的实时气温分布图，未来两天气温和天气现象预报：

'getData.py' 是用来绘制实况和未来天气预报。


通过使用上海市气象局的实时预警信息绘制上海市预警信号分布：

'alert_sh.py' 是用来绘制上海市实况分区预警信号。


# !IMPORTANT NOTE!
1. This python file can be successfully operataing on Ubuntu Server 14.04LTS. It has not been tested on other platforms.

2. This python file use Python3 with JSON, Basemap, matplotlib and numpy.

3. Folder 'shanghai_shp' contains shape file for Shanghai, it is needed in 'alert_sh.py'.

4. THE PATH OF GRAPHS AND REQUIRED FILES NEEDS TO BE CHANGED BEFORE RUNING!

Credit @Louis_He

# ！重要事项！
1. 本python文件可以在Ubuntu Server 14.04LTS系统上成功运行，但还没有在别的系统上进行测试。

2. 本文件使用python3编写，使用插件JSON, Basemap, matplotlib和numpy。

3. 'shanghai_shp'文件夹包含了上海地区的shape地理信息文件，在'alert_sh.py'中需要使用。

4. 在使用所有程序前，请检查Python文件中各种图片保存和所需文件的地址并修改！


版权所有： Louis_He



Update Date: Sept, 1st, 2017

最近一次更新时间：2017年9月1日
