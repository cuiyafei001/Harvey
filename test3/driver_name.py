# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print driver.name