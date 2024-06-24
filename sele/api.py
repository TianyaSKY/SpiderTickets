from selenium.webdriver.common.by import By

from sele import *

depCity = ''
arrCity = ''
date = '2024-07-07'


class CityArrDep:
    def __init__(self):
        self.depCity = depCity
        self.arrCity = arrCity
        self.date = date
        self.informations = []  # 存储一日的航班信息
        """
        dep_time:出发时间
        from_ellipsis:出发航站楼
        company1:航空公司
        longtake:时长
        arr_time:到达时间
        to_ellipsis:到达航站楼
        price:价格
        """

    def getCookies(self):

        driver.get('https://m.flight.qunar.com/')
        while input() != 'q':
            continue
        with open('data/cookies.txt', 'w') as f:
            # 将cookies保存为json格式
            f.write(json.dumps(driver.get_cookies()))
        driver.close()

    def run(self):
        try:
            url = get_airplane(depCity=self.depCity, arrCity=self.arrCity, Date=self.date)  # 输入
            login(url)
        except Exception as e:
            print()

    def getInfo(self):
        blocks = driver.find_elements(by=By.CLASS_NAME, value='list-row')  # 每个信息块，包括所有信息
        for block in blocks:
            dep_time = block.find_element(by=By.CLASS_NAME, value='from-time').text
            from_ellipsis = block.find_element(by=By.CLASS_NAME, value='from-place').text
            company1 = block.find_element(by=By.CLASS_NAME, value='company1').text
            longtake = block.find_element(by=By.CLASS_NAME, value='time-info').text
            arr_time = block.find_element(by=By.CLASS_NAME, value='to-time').text
            to_ellipsis = block.find_element(by=By.CLASS_NAME, value='to-place').text
            price = block.find_element(by=By.CLASS_NAME, value='price1').text
            self.informations.append({'dep_time': dep_time,
                                      'from_ellipsis': from_ellipsis,
                                      'company1': company1,
                                      'longtake': longtake,
                                      'arr_time': arr_time,
                                      'to_ellipsis': to_ellipsis,
                                      'price': price,
                                      'dep_place': self.depCity,
                                      'arr_place': self.arrCity,
                                      'date': self.date,
                                      })
