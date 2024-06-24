import datetime

import pandas

from sele.api import *

Cookies_MODE = False  # 获取Cookies
To_CSV = True  # 将信息转换为csv输出

if __name__ == '__main__':
    App = CityArrDep()
    App.depCity = '上海'  # 出发地点
    App.arrCity = '北京'  # 到达地点
    App.date = '2024-07-17'
    if Cookies_MODE:
        print('请登录账号，完成时请手动输入:"q"预估时间: 120s')
        App.getCookies()
        print('已完成操作(可能未正确获取cookies)')
    App.run()
    App.getInfo()
    infs = App.informations
    if To_CSV:
        file_name = f'data/{App.depCity}To{App.arrCity}In{App.date}：{datetime.datetime.now().strftime("%m-%d %H：%M")}.csv'
        pandas.DataFrame(infs).to_csv(file_name, encoding='gbk')
