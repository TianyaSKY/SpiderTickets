# 用于对一段时间内进行爬取
import datetime

import pandas

from sele.api import *

Cookies_MODE = False  # 获取Cookies
To_CSV = True  # 将信息转换为csv输出

if __name__ == '__main__':
    App = CityArrDep()
    App.depCity = '上海'  # 出发地点
    App.arrCity = '北京'  # 到达地点
    for App.date in ['2024-07-14','2024-07-15','2024-07-16','2024-07-17','2024-07-18']:
        App.run()
        App.getInfo()
        infs = App.informations
        if To_CSV:
            file_name = f'data/{App.depCity}To{App.arrCity}In{App.date}：{datetime.datetime.now().strftime("%m-%d %H：%M")}.csv'
            pandas.DataFrame(infs).to_csv(file_name, encoding='gbk')
