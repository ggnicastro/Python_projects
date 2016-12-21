__author__ = 'kaihami'
"""
Take RR links from the (1) file [RR_web_scrap_RelationalDB]
and find all genes in a link (http://www.ncbi.nlm.nih.gov/Complete_Genomes/SigCensus/RECfirmi2010.html)
and return list with  Taxo_key, Bacteria name, RR subfamily, locus_tag
example of output: (RR_web_scrap_RECfirmi2010)
"""
from bs4 import BeautifulSoup
#from urllib2 import urlopen
import requests
import re
import time

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

DB_open = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_DB1", "r").read().split("\n")
DB = []
for line in DB_open:
    a = line.split(",")
    DB.append(a)
del DB[0]
del DB[-1]
RR_links = []
for x in xrange(0,len(DB)):
    a = DB[x][4]
    if a not in RR_links:
        if len(a) >2:
            RR_links.append(a)

to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_RECfirmi2010","a")
to_write.write("taxo_key, Bacteria, RR Family, Locus_tag")
to_write.write("\n")
to_write.close()

tax_lst = []
for x in xrange(0,len(DB)):
    a = str(DB[x][2]).replace(" ","")
    tax_lst.append(a)
rr_final_link = requests.get("http://www.ncbi.nlm.nih.gov/Complete_Genomes/SigCensus/RECfirmi2010.html")
url2 = rr_final_link.text
rr_soup = BeautifulSoup(url2, "html.parser") #create the soup
rr_final_link.close()

tmp_lst = []
for line in rr_soup:
    if line == "\n":
        pass
    else:
        tmp_lst.append(line)
tmp_lst2 = []
for x in xrange(0, len(tmp_lst)):
    a = str(tmp_lst[x]).split("\n")
    tmp_lst2.append(a)
tmp_lst3 = flatten(tmp_lst2)

info_lst = []
for x in xrange(0,len(tmp_lst3)):
    line = tmp_lst3[x]
    if "<pre><hr>" in line:
        print line
        for y in xrange(x+1, len(tmp_lst3)-1):
            here = tmp_lst3[y]
            info_lst.append(here)

RR_gene_lst = []
test_lst = []
init_list = []
for tax_num in xrange(0, len(tax_lst)):
    taxo = str(tax_lst[tax_num]).replace("[","").replace("]","").replace("'","")
    for y in xrange(0, len(info_lst)):
        info = str(info_lst[y]).replace("[","").replace("]","").replace("'","")
        if '<font size="+1"><b>' in info and "protein" not in info:
            if taxo in info:

                start = y
                init_list.append(start)

init_list.sort()
tax_st_end = []

for x in xrange(0, len(init_list)):
    if x != len(init_list)-1:
        start = init_list[x]
        end = init_list[x+1]
        tmp = []
        tmp.append(start)
        tmp.append(end)
        tax_st_end.append(tmp)
tax_st_end.append([init_list[-1], len(info_lst)-1])

for sta, en in tax_st_end:
    inter = info_lst[sta:en]
    for num in xrange(0, len(inter)):
         c = str(inter[num]).replace("[","").replace("]","").replace("'","")
         #bac name ok!
         if 'size="+1' in c:
            bac = re.findall('">(.+?)</a', c)
            tmp = []
            for ele in bac:
                a = ele.split('>')
                tmp.append(a)
            name_bacterium = tmp[-1]
            name_bacterium = name_bacterium[-1]
            name_bacterium = str(name_bacterium).replace("[","").replace("]","").replace("'","").replace(",",".")
            taxo_key = re.findall('<a name="(.+?)"></a>', c)
            taxo_key = str(taxo_key).replace("[","").replace("]","").replace("'","")
         if "<b>" in c and 'size="+1' not in c:
             RR_fun = re.findall('<b>(.+?)</b', c)
             RR_fun_str = str(RR_fun).replace("[","").replace("]","").replace("'","")
         if "protein" in c:
             test = []
             genes = str(c).split(" ")
             locus_tag = genes[0]
             tmp2 = []
             tmp2.append(taxo_key)
             tmp2.append(name_bacterium)
             tmp2.append(RR_fun_str)
             tmp2.append(locus_tag)
             test.append(tmp2)
             test2 = str(test).replace("[","").replace("]","").replace("'","")
             to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_RECfirmi2010","a")
             to_write.write(test2)
             to_write.write("\n")
             to_write.close()
print "finish"