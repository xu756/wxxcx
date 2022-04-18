# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 0011 9:36
# @Author  : xu756
# @File    : rename.py
from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import xlwings as xw
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get("https://graph.baidu.com/pcpage/index?tpl_from=pc")
driver.maximize_window()
imginput = driver.find_element(By.CLASS_NAME, 'graph-d20-search-wrapper-input')

app = xw.App(visible=False, add_book=False)  # 程序可见，只打开不新建工作薄
wb = app.books.open('景明菌形象设计大赛作品收集表（收集结果）.xlsx')  # 打开工作薄
sheets = wb.sheets.active  # 获取当前活动工作薄
# 获取D2单元格超链接的文本
url = sheets.range('D2').hyperlink
imginput.send_keys(url)
sleep(1)
driver.find_element(By.CLASS_NAME, 'graph-d20-search-btn').click()
sleep(5)
# 保存窗口截图
js = "window.scrollTo(0,500);"
driver.execute_script(js)
driver.save_screenshot('baidu_img.png')
sleep(1)
wb.save()
wb.close()
app.quit()
