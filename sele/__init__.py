import json
import time
from urllib.parse import urlencode

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://m.flight.qunar.com/ncs/page/flightlist?'

options = Options()
# 隐藏 正在受到自动软件的控制 这几个字
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

# 修改 webdriver 值
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})


def get_airplane(depCity, arrCity, Date):
    poly_data = {'depCity': depCity,
                 'arrCity': arrCity,
                 'goDate': Date,
                 'from': 'touch_index_search',
                 'child': 0,
                 'baby': 0,
                 'cabinType': 0,
                 }
    encoded_data = urlencode(poly_data)
    driver.get(url + encoded_data)
    return url + encoded_data


def login(url):
    driver.get(url)
    time.sleep(6)
    driver.delete_all_cookies()
    with open('../data/cookies.txt', 'r') as f:
        # 使用json读取cookies
        cookies_list = json.load(f)
        for cookie in cookies_list:
            cookie['domain'] = '.qunar.com'  # 区别在这儿
            driver.add_cookie(cookie)
    driver.get(url)
    driver.refresh()
    time.sleep(5)


if __name__ == '__main__':
    url_ad = get_airplane('上海', '北京')
    login(url_ad)
