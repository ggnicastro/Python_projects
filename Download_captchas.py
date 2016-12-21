__author__ = 'kaihami'
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
import re
import urllib
import time
"""
Script to automate downloa captchas from lattes platform
"""


url = 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4711245P4'
driver = webdriver.Firefox()
b = driver.get(url)
dir_name = "/home/kaihami/Desktop/Python/Captcha_images/Training_data/original/"
for x in xrange(3000,4000):
    if 3000<=x<3250:
        img_xp = '/html/body/form/div/div/div/div/div/div/div/div[3]/img'

        img = driver.find_element_by_xpath(img_xp)

        src = img.get_attribute('src')
        img.get_attribute('id')
        save_path = dir_name+'3000_3250/'
        urllib.urlretrieve(src, save_path+"captcha"+str(x)+".png")

        #refresh
        refresh_xp = '/html/body/form/div/div/div/div/div/div/div/div[4]/a[1]'
        move_to = driver.find_element_by_xpath(refresh_xp)
        webdriver.ActionChains(driver).move_to_element(move_to).click(move_to).perform()
        time.sleep(0.5)
        print "Left: " + str(4000-x-1)
    if 3250<=x<3500:
        img_xp = '/html/body/form/div/div/div/div/div/div/div/div[3]/img'

        img = driver.find_element_by_xpath(img_xp)

        src = img.get_attribute('src')
        img.get_attribute('id')
        save_path = dir_name+'3250_3500/'
        urllib.urlretrieve(src, save_path+"captcha"+str(x)+".png")

        #refresh
        refresh_xp = '/html/body/form/div/div/div/div/div/div/div/div[4]/a[1]'
        move_to = driver.find_element_by_xpath(refresh_xp)
        webdriver.ActionChains(driver).move_to_element(move_to).click(move_to).perform()
        time.sleep(0.5)
        print "Left: " + str(4000-x-1)
    if 3500<=x<3750:
        img_xp = '/html/body/form/div/div/div/div/div/div/div/div[3]/img'

        img = driver.find_element_by_xpath(img_xp)

        src = img.get_attribute('src')
        img.get_attribute('id')
        save_path = dir_name+'3500_3750/'
        urllib.urlretrieve(src, save_path+"captcha"+str(x)+".png")

        #refresh
        refresh_xp = '/html/body/form/div/div/div/div/div/div/div/div[4]/a[1]'
        move_to = driver.find_element_by_xpath(refresh_xp)
        webdriver.ActionChains(driver).move_to_element(move_to).click(move_to).perform()
        time.sleep(0.5)
        print "Left: " + str(4000-x-1)
    if 3750<=x<4000:
        img_xp = '/html/body/form/div/div/div/div/div/div/div/div[3]/img'

        img = driver.find_element_by_xpath(img_xp)

        src = img.get_attribute('src')
        img.get_attribute('id')
        save_path = dir_name+'3750_4000/'
        urllib.urlretrieve(src, save_path+"captcha"+str(x)+".png")

        #refresh
        refresh_xp = '/html/body/form/div/div/div/div/div/div/div/div[4]/a[1]'
        move_to = driver.find_element_by_xpath(refresh_xp)
        webdriver.ActionChains(driver).move_to_element(move_to).click(move_to).perform()
        time.sleep(0.5)
        print "Left: " + str(4000-x-1)
print "Finish"