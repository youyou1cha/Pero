from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Edge(executable_path=r"C:\Users\wwa\wo\msedgedriver.exe")
browser.get("https://www.bilibili.com/")
# driver.findElement(By.className("className"));
browser.find_element(By.CLASS_NAME,"nav-search-input").send_keys("selenium")
# browser.find_element_by_id("su").click()
# sleep(1)
#
# # 1.定位一组元素
# elements = browser.find_elements_by_xpath('//div/h3/a')
# print(type(elements))
#
# # 2.循环遍历出每一条搜索结果的标题
# for t in elements:
#     print(t.text)
#     element = browser.find_element_by_link_text(t.text)
#     element.click()
#     sleep(3)
#
# browser.quit()
