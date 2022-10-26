from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import csv
import re
import time


class HomeLinkSpider(object):
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.data = list()
        self.path = "浦东_三房_500_800万.csv"
        self.url = "https://sh.lianjia.com/ershoufang/pudong/a3p5/"

    def get_max_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            a = soup.select('div[class="page-box house-lst-page-box"]')
            # 使用eval是字符串转化为字典格式
            max_page = eval(a[0].attrs["page-data"])["totalPage"]
            return max_page
        else:
            print("请求失败 status:{}".format(response.status_code))
            return None

    def parse_page(self):
        max_page = self.get_max_page()
        for i in range(1, max_page + 1):
            url = 'https://sh.lianjia.com/ershoufang/pudong/pg{}a3p5/'.format(i)
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            ul = soup.find_all("ul", class_="sellListContent")
            li_list = ul[0].select("li")
            for li in li_list:
                detail = dict()
                detail['title'] = li.select('div[class="title"]')[0].get_text()

                #  2室1厅 | 74.14平米 | 南 | 精装 | 高楼层(共6层) | 1999年建 | 板楼
                house_info = li.select('div[class="houseInfo"]')[0].get_text()
                house_info_list = house_info.split(" | ")

                detail['bedroom'] = house_info_list[0]
                detail['area'] = house_info_list[1]
                detail['direction'] = house_info_list[2]

                floor_pattern = re.compile(r'\d{1,2}')
                # 从字符串任意位置匹配
                match1 = re.search(floor_pattern, house_info_list[4])
                if match1:
                    detail['floor'] = match1.group()
                else:
                    detail['floor'] = "未知"

                # 匹配年份
                year_pattern = re.compile(r'\d{4}')
                match2 = re.search(year_pattern, house_info_list[5])
                if match2:
                    detail['year'] = match2.group()
                else:
                    detail['year'] = "未知"

                # 文兰小区 - 塘桥， 提取小区名和哈快
                position_info = li.select('div[class="positionInfo"]')[0].get_text().split(' - ')
                detail['house'] = position_info[0]
                detail['location'] = position_info[1]

                # 650万，匹配650
                price_pattern = re.compile(r'\d+')
                total_price = li.select('div[class="totalPrice"]')[0].get_text()
                detail['total_price'] = re.search(price_pattern, total_price).group()

                # 单价64182元/平米， 匹配64182
                unit_price = li.select('div[class="unitPrice"]')[0].get_text()
                detail['unit_price'] = re.search(price_pattern, unit_price).group()
                self.data.append(detail)

    def write_csv_file(self):
        head = ["标题", "小区", "房厅", "面积", "朝向", "楼层", "年份",
                "位置", "总价(万)", "单价(元/平方米)"]
        keys = ["title", "house", "bedroom", "area", "direction",
                "floor", "year", "location",
                "total_price", "unit_price"]

        try:
            with open(self.path, 'w', newline='', encoding='utf_8_sig') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                if head is not None:
                    writer.writerow(head)
                for item in self.data:
                    row_data = []
                    for k in keys:
                        row_data.append(item[k])
                        # print(row_data)
                    writer.writerow(row_data)
                print("Write a CSV file to path %s Successful." % self.path)
        except Exception as e:
            print("Fail to write CSV to path: %s, Case: %s" % (self.path, e))


if __name__ == '__main__':
    start = time.time()
    home_link_spider = HomeLinkSpider()
    home_link_spider.parse_page()
    home_link_spider.write_csv_file()
    end = time.time()
    print("耗时：{}秒".format(end - start))
