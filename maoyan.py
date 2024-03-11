# # coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class MaoYan(object):
    def __init__(self):
        # 初始化创建url
        self.url = 'https://piaofang.maoyan.com/dashboard'

    def parse_data(self, url):
        # '''
        # 解析页面
        # 返回[{'电影名','票房'}]列表
        # '''
        # 创建浏览器对象 谷歌
        driver = webdriver.Chrome()
        # 操作浏览器对象
        driver.get(url)
        time.sleep(2)
        # 电影名
        name_list = driver.find_elements(
            By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]/div/div[2]/p[1]')
        # 票房
        pf_list = driver.find_elements(
            By.XPATH,
            '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]/div/div[2]/p[2]/span[last()]'
        )
        # 创建数据列表
        data_list = []

        for i in range(len(name_list)):
            # 字典接收数据
            data = {'name': name_list[i].text, 'pf': pf_list[i].text}
            # 字典列表
            data_list.append(data)

        return data_list

    def save_data(self, data_list):
        # 读取并展示数据
        for data in data_list:
            print(data)

    def run(self):
        # 运行原始的数据
        url = self.url
        data_list = self.parse_data(url)
        self.save_data(data_list)


if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.run()
