#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://sh.xsjedu.org/")
time.sleep(1)

# 将display 的值设置成 none 就可以去除返个弹窗了
js = 'document.getElementById("doyoo_mon_inner").style.display="none";'
driver.execute_script(js)
