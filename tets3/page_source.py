# _*_ coding: UTF-8 _*_
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/cyfyywfc/")

# 使用selenium提供的page_source方法获取页面源码
page = driver.page_source
print page