__author__ = 'kaihami'

"""Merge data from RR_Web_scrap_DB and RR_web_scrap_x_cur"""
DB_open = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_DB1", "r").read().split("\n")
DB = []
for line in DB_open:
    a = line.split(",")
    tmp = []
    for x in xrange(0,(len(a))):
        if x == 0:
            b = a[x]
            tmp.append(b)
        if x != 0:
            b = a[x].replace(" ", "")
            tmp.append(b)

    DB.append(tmp)
del DB[0]
del DB[-1]
RR_open = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_web_scrap_RECOthers_cur", "r").read().split("\n")
RR = []

for line in RR_open:
    a = line.split("\t")
    tmp = []
    for x in xrange(0,(len(a))):
        if x == 1:
            b = a[x].lstrip()
            tmp.append(b)
        if x != 1:
            b = a[x].replace(" ", "")
            tmp.append(b)
    if len(tmp) > 1:
        RR.append(tmp)
del RR[0]

to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_format_Others","a")
to_write.write("taxon,bac_name1,bac_name2,Phylum,CDS,RR_family,Locus_tag")
to_write.write("\n")
to_write.close()

All = []
dif = []
a = []
all_genes = []
for line in RR:
    taxon1 = line[0]
    bac_name1 = line[1]
    RR_fun = line[2]
    locus = line[3]
    for ele in DB:
        tmp = []
        bac_name2 = ele[0]
        phylum = ele[1]
        taxon2 = ele[2]
        CDS = ele[-1]
        if taxon1 == taxon2:
            tmp.append(taxon1)
            tmp.append(bac_name1)
            tmp.append(bac_name2)
            tmp.append(phylum)
            tmp.append(CDS)
            tmp.append(RR_fun)
            tmp.append(locus)
            All.append(tmp)
            to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_format_Others","a")
            test2 = str(tmp).replace("[","").replace("]","").replace("'","")
            to_write.write(test2)
            to_write.write("\n")
            to_write.close()

def dup(lst):
    a = []
    for line in lst:
        gene = line[3]
        all_genes = []
        for ele in a:
            genes = ele[-1]
            all_genes.append(genes)
        if gene not in all_genes:
            a.append(line)
        print "going"
    return a
