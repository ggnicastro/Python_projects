__author__ = 'kaihami'
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import cv2
import urllib
import time
from collections import OrderedDict
#set dir
os.chdir("/home/kaihami/Desktop/Python/Captcha_images/")

def solve_captcha(url, dir_name = os.getcwd()):
    b = driver.get(url)

    time.sleep(1.5)

    print "Initializing"
    captcha_img_path = os.path.join(dir_name, "captcha_to_solve.png")

    driver.save_screenshot(captcha_img_path)
    ###transform captcha

    #image = dir_name+"captcha_to_solve"+".png"
    img_print = cv2.imread(captcha_img_path,0)
    img = img_print[287:336, 363:649]
    ret,thresh = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
    save_image_path = os.path.join(dir_name,"captcha_bw.png")
    mid = (len(thresh[0])/2)
    img_crop = thresh[:,28:mid+12]
    cv2.imwrite(save_image_path, img_crop)

    ###Run tesseract
    os.system("tesseract " + save_image_path +" output -l captcha")
    output = open("output.txt", "r").read().replace("\n", "")
    output = output.replace(" ","").replace("'","").replace(".","").replace("'","").replace("_","").replace(",","").replace("E","F")
    print "Try: ", str(x)
    print output

    time.sleep(3)

    ### fill
    captcha_form = "/html/body/form/div/div/div/div/div/div/div/input"
    fill_path = driver.find_element_by_xpath(captcha_form)
    try:
        fill_path.send_keys(output)
        fill_path.send_keys(Keys.RETURN)
    #refresh page
    except:
        fill_path.send_keys("aa")
        fill_path.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        t = "/html/body/div[3]"
        ok = driver.find_element_by_xpath(t)
        captcha = False

        print "Passed"
        return "Passed"
    except:
        pass
    ##########################################################

#open page

driver = webdriver.Firefox()

url = 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4793616Z4'

b = driver.get(url)

###Get Captcha
captcha = True
x = 0
#for captcha in captcha_lattes
while captcha:
    x+=1
    a = solve_captcha(url)
    if a == "Passed":
        #extract lattes
        captcha = False

from bs4 import BeautifulSoup
import re

html = driver.page_source
Letter_ID = driver.current_url
Letter_ID = re.findall("id=(.+?)$", Letter_ID)[0]

soup = BeautifulSoup(html)
Number_ID = soup.find_all("div",{"class" : "layout-cell layout-cell-12 data-cell"})
wraps = soup.find_all("div", {"class": "title-wrapper"})
#   wrap[0]
#   wrap[1]
x = 0

#ok
def Nome_prod(soup):
    """
    Return researcher name and productivity
    """
    h = soup.find("h2", {"class":"nome"})
    nome = re.findall('tabindex="0">(.+?)<br', str(h))[0]
    bolsista_prod = re.findall('bold">(.+?)<', str(h))[0]
    return nome, bolsista_prod
#ok
def identificador(soup):
    """
    Return Lattes ID (number)
    """
    ID = soup.find("li")
    ID_num = re.findall('lattes.cnpq.br/(.+?)<', str(ID))[0]
    return ID_num
#ok
def citation_name(soup):
    a = soup.find_all("div", {"class": "title-wrapper"})
    for e in a:
        if 'Nome em citações bibliográficas' in str(e):
            names = re.findall('class="layout-cell-pad-5">(.+?)</div>', str(e))[1]
            name = names.split(";")
            break
    return name
#ok
def academic_form(soup):
    sub_filter = soup.find_all("div", {"class": "title-wrapper"})
    for e in sub_filter:
        if "FormacaoAcademicaTitulacao" in str(e):
            print str(e)
            local = e.find_all('div', {"class": "layout-cell-pad-5"})

            l = []
            for b in local:
                tmp = []
                #Forma
                if "layout-cell-pad-5 text-align-right" not in str(b):
                    s = re.findall('div class="layout-cell-pad-5">(.+?)\.', str(b))
                    tmp.append(s)
                #year
                if "layout-cell-pad-5 text-align-right" in str(b):
                    year = re.findall('<b>(.+?)</b>', str(b))
                    tmp.append(year)
                l.append(tmp)
            break
    return l
#ok
def postdocs(soup):
    sub_filter = soup.find_all("div", {"class": "title-wrapper"})
    for e in sub_filter:
        if "FormacaoAcademicaPosDoutorado" in str(e):

            local = e.find_all('div', {"class": "layout-cell-pad-5"})

            forms = []
            years = []
            for b in local:
                tmp = []
                #Forma
                if "layout-cell-pad-5 text-align-right" not in str(b):
                    s = re.findall('div class="layout-cell-pad-5">(.+?)\.' , str(b))[0]
                    whe = re.findall('class="clear"(.+?)\.' , str(b))
                    forms.append([s, whe])
                #

                #year
                if "layout-cell-pad-5 text-align-right" in str(b):
                    year = re.findall('<b>(.+?)</b>', str(b))[0]
                    years.append(year)
            infos = zip(years, forms)
    try:
        return infos
    except:
        infos = []
        return infos
#ok
def prof_atu(soup):
    """

    :param soup:
    :return: Atuacao Profissional
    """
    sub_filter = soup.find_all("div", {"class": "title-wrapper"})
    for e in sub_filter:

        if "AtuacaoProfissional" in str(e):
            a = str(e).split("\n")
            infos = OrderedDict()
            l = []
            for i, it in enumerate(a):
                if 'class="inst_back"' in it:
                    l.append(i)
            s_t = []
            for x in xrange(0, len(l)):
                if x == 0:
                    start = l[x]
                if x != 0:
                    end = l[x]
                    s_t.append([start, end])
                    start = end
                if x == len(l)-1:
                    s_t.append([start, len(a)])

            for s, e in s_t:
                vinc = ""
                year = ""
                for y in xrange(s, e):
                    #uni
                    if 'class="inst_back"' in a[y]:
                        university = a[y+1]
                        infos[university] = OrderedDict()

                    #get year
                    if 'div class="layout-cell-pad-5 text-align-right' in a[y]:
                        if 'Vínculo institucional' not in a[y+1] and\
                                'class="clear"' not in a[y+1] and\
                                'Outras informações' not in a[y+1] and\
                                'Atividades' not in a[y+1]:
                            year = a[y+1]

                                #tmp_y.append(year)

                    if 'div class="layout-cell layout-cell-9"' in a[y]:
                        if 'div class="layout-cell-pad-5"' in a[y+1] and\
                                        'class="clear"' not in a[y+1]:
                            vinc = a[y+1]
                    if len(vinc) > 0 and len(year) >0:
                        if vinc not in infos[university].keys():
                            infos[university][vinc] = year
    try:
        return infos
    except:
        infos = []
        return infos

a = academic_form(soup)