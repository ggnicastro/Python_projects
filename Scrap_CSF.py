__author__ = 'kaihami'
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

import time

url = "http://www.cienciasemfronteiras.gov.br/web/csf/bolsistas-pelo-mundo"

xp_next_page = '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[11]/ul/li[5]/a'
driver = webdriver.Firefox()
b = driver.get(url)
next_page = driver.find_element_by_xpath(xp_next_page)
xp_lista_uni = "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]"
time.sleep(300)
info = driver.find_element_by_xpath(xp_lista_uni)

#link = '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div['+x+']/a[1]' #x 1->10
link = '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/a[1]' #x 1->10
move_to = driver.find_element_by_xpath(link)
webdriver.ActionChains(driver).move_to_element(move_to).click(move_to).perform()
time.sleep(20)

xp_todos_bolsistas = '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div[4]/div/div[2]/div/div/div/ul/div[2]/a[2]'

todos_bolsistas = driver.find_element_by_xpath(xp_todos_bolsistas)
webdriver.ActionChains(driver).move_to_element(todos_bolsistas).click(todos_bolsistas).perform()

xp_bolsistas = '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div'
bolsistas = driver.find_elements_by_xpath(xp_bolsistas)
for bolsista in bolsistas:
    a = [x.encode('utf-8') for x in bolsista.text.split('\n')]
#set vigencia
for ele in a:
    if 'Vig\xc3\xaancia' in ele:
        print ele

##################
#get lattes
lates = bolsistas[0].find_elements_by_tag_name('a')
lates[0].get_attribute('href')
for cur in lates:
    b = cur.get_attribute('href')
    if 'visualizacv' in b:
        print b
xp_close_lattes = '/html/body/div[2]/div[1]/div[1]/span[2]/span/button'
close_lattes = driver.find_element_by_xpath(xp_close_lattes)
webdriver.ActionChains(driver).move_to_element(close_lattes).click(close_lattes).perform()

