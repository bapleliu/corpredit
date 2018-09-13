# -*- coding: utf-8 -*-
"""
@Date     :2018/04/18
@Author   : Yosef
@Software :anaconda3
"""

import time
import random
import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

import cv2
import numpy as np
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

import requests
from hashlib import md5
from lxml import etree
from copyheaders import headers_raw_to_dict


if __name__=='__main__':
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get('http://www.baidu.com/')
    inputElement = driver.find_element_by_id('kw')  # 获取输入框
    searchButton = driver.find_element_by_id('su')  # 获取搜索按钮

    inputElement.send_keys("Python")  # 输入框输入"Python"
    searchButton.click()  # 搜索
    
    

