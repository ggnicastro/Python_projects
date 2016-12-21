__author__ = 'kaihami'

"""
This script takes information from:
http://www.ncbi.nlm.nih.gov/Complete_Genomes/RRcensus.html

Colecting the following info:

DB[x][y]: x: Key
          y: position 0: Bacteria Name
             postiion 1: Phylum
             position 2: Taxonomy number
             position 3: CDS
             position 4: genome link
             position 5: genome_ID
             position 6: RR_link

Example output: RR_web_scrap_DB2
"""

from bs4 import BeautifulSoup

import requests
import re

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

DB = {}
url = requests.get("http://www.ncbi.nlm.nih.gov/Complete_Genomes/RRcensus.html")

page = url.text #read page
soup = BeautifulSoup(page, "html.parser") #create the soup
url.close()
all_info = soup.find_all("tr") #change limit, use less to test case

all = []


for line_num in xrange(1, len(all_info)): #Phylum genome_link, bac name and RR link and number ok!
    main_page_tmp = []
    position = all_info[line_num]

    for element in position:
        tmp = str(element)
        main_page_tmp.append(tmp)

    #find the phylum
    phy_re = re.findall('<font size="\+1">(.+?)</font>', main_page_tmp[3])
    if len(phy_re) >0:
        phylum = phy_re

    #a more general approach to find genome_link, bacteria name, and the RR link
    if any("center" in s for s in main_page_tmp):

        if len(main_page_tmp) > 43:
            rr_check = re.findall('td align="center"><a href="(.+?)#', main_page_tmp[43])

            rr_num_check = re.findall('><b>(.+?)</b>', main_page_tmp[43])

            rr_link = rr_check
            rr_number = str(rr_num_check).replace("[","").replace("]","").replace("'","").replace(",","")
            rr_final_link = str(rr_check).replace("[","").replace("]","").replace("'","").replace(",","")

            genome_check = re.findall('href="(.+?)">', main_page_tmp[5])
            if len(str(genome_check)) > 3:
                genome_link = genome_check
                genome_id = str(genome_link)[-10:-1]


            bac = (re.findall('">(.+?)</a>', main_page_tmp[3]))
            taxo = re.findall('a href="http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax\.cgi\?id=(.+?)">',main_page_tmp[3])
            bac = [str(element).replace("<i","").replace("/i","").replace(">","").replace("<","") for element in bac]
            bac_name = str(bac).replace("[","").replace("]","").replace("'","").replace(",","")
            info_lst = []
            cds = re.findall('">(.+?)</td', main_page_tmp[7])
            cds_final = str(cds).replace("[","").replace("]","").replace("'","").replace(",","")
            for num in xrange(9, 42,2):
                info = []
                info = re.findall('>(.[0-9]?)</a></td>', main_page_tmp[num])
                if len(info) == 0:
                    info = "0"
                info = str(info).replace("[","").replace("]","").replace("'","").replace(",","")
                info_lst.append(info)
                info_str = str(info_lst).replace("[","").replace("]","").replace("'","") #Distribution of RR by family

            tmp = []
            tmp.append([bac_name])
            tmp.append(phylum)
            tmp.append(taxo)
            tmp.append(cds_final)
            tmp.append(genome_link)
            tmp.append(genome_id)
            tmp.append([rr_final_link])
            DB[len(DB)] = tmp
del DB[len(DB)-1]
RR_links = []
for x in xrange(0,len(DB)):
    a = DB[x][5]
    if a not in RR_links:
        if len(a) >2:
            RR_links.append(a)
tax_lst = []
for x in xrange(0,len(DB)):
    a = DB[x][2]
    tax_lst.append(a)

to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_DB2", "a")
to_write.write("Bacteria,Phylum,Taxon,CDS,Genome_link,Genome_ID,RR_link")
to_write.write("\n")
to_write.close()

for k in DB.keys():
    a = DB[k]
    for ele in a:
        ele_format = str(ele).replace("[","").replace("]","").replace("'","")

        to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_DB2", "a")
        to_write.write("%s," % (ele_format))
        to_write.close()
    to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_DB2", "a")
    to_write.write("\n")
    to_write.close()