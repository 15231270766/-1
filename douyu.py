# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Douyu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def parse_data(self):
        time.sleep(3)
        self.driver.execute_script('scrollTo(0,1000000)')
        room_list = self.driver.find_elements(By.XPATH, '//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        print(len(room_list))

        data_list = []
        # 遍历房间列表，从没一个房间节点中获取数据
        for room in room_list:
            temp = {}

            temp['title'] = room.find_elements(By.XPATH, './a[1]/div[2]/div[1]/h3')[0].text
            temp['type'] = room.find_elements(By.XPATH, './a[1]/div[2]/div[1]/span')[0].text
            temp['owner'] = room.find_elements(By.XPATH, './a[1]/div[2]/div[2]/h2')[0].text
            temp['num'] = room.find_elements(By.XPATH, './a[1]/div[2]/div[2]/span')[0].text
            # temp['pic'] = room.find_elements(By.XPATH, './a[1]/div[1]/div[1]/picture/source[1]')
            data_list.append(temp)

        return data_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        # url
        # driver
        # get

        self.driver.get(self.url)
        while True:
            # parse
            data_list = self.parse_data()

            # save
            self.save_data(data_list)

            # next
            try:
                # self.driver.execute_script('scrollTo(0,1000000)')
                el_next = self.driver.find_elements(By.XPATH, '//*[contains(text(),"下一页")]')
                el_next[0].click()
            except:
                break


if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
