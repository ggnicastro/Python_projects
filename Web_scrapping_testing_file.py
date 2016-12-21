__author__ = 'kaihami'
import bs4
from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
import re
import time
"""
url = urlopen('http://www.pseudomonas.com/getAnnotation.do?locusID=PA14_00830')
page = url.read()
soup = BeautifulSoup(page)
"""
#gene name

def scale(max_value, dict_ipt):
    max_scale = max_value/20
    lst = []
    scale_dict = {}
    for number in range(1,max_scale+1):
        if number%5 == 0 or number == max_value:
            tmp = number*20
            tmp2 = str(tmp) + " - |"
            lst.append(tmp2)
        else:
            tmp = "      |"
            lst.append(tmp)
    for i, v in enumerate(lst, start = 1):
        scale_dict[i] = v

    point_dict = {}
    for k, value in dict_ipt.items():
        point_dict[k] = value/20

    for value in point_dict.values():
        for k, v in scale_dict.items():
            if value <= 0:
                scale_dict[k] = v + "   "
            else:
                for x in range(1, value+1):
                    if k <= x:
                        scale_dict[k] = v + "** "
                    else:
                        scale_dict[k] = v + "   "
    tmp = []
    for value in scale_dict.values():
        tmp.append(value)
    final = tmp[::-1]
    return final




def base_scale(dict_ipt):
    base = len(dict_ipt.keys())
    tmp = ""
    for number in range(0, base+1):
        if number == 0:
            tmp = "   0 -+-"
        else:
            tmp += "-+-"
    return tmp
def legend(dict_ipt):
    base = len(dict_ipt.keys())
    tmp = ""
    for number in range(0, base+1):
        if number == 0:
            tmp  = "       "
        else:
            tmp += str(number) + "  "
    return tmp
def show(max_scale=400, dict_ipt=dict_len):
    tmp = scale(max_scale, dict_ipt)
    tmp.append(base_scale(dict_ipt))
    tmp.append(legend(dict_ipt))
    for line in tmp:
        print line


dict_len = {1:16, 2:267,3:267, 4:169, 5:140, 6:20}
show(m)