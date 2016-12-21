__author__ = 'kaihami'
"""
Add Gene_ID to RR_format file
"""

DB_open = open("/home/kaihami/Desktop/Python/RR_Bioinfo/RR_web_scrap_DB2", "r").read().split("\n")
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
"""
DB[k][2] = Taxon
DB[k][3] = CDS
DB[k][5] = genome_ID
"""

RR_open = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/RR_format_Actino", "r").read().split("\n")
RR = []

for line in RR_open:
    a = line.split(",")
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
RR_info = ['taxon', 'bac_name1', 'bac_name2', 'Phylum', 'CDS', 'RR_family', 'Locus_tag']
del RR[0]

fi = "/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/RR_format_Actino2"
to_write = open(fi,"a")
to_write.write("taxon,bac_name1,bac_name2,Phylum,Genome_ID,CDS,RR_family,Locus_tag")
to_write.write("\n")
to_write.close()

All = []
dif = []
a = []
all_genes = []
for line in RR:

    taxon1 = line[0]
    bac_name1 = line[1]
    bac_name2 = line[2]
    phylum = line[3]
    CDS = line[4]
    RR_fun = line[5]
    locus = line[6]
    for ele in DB:
        tmp = []
        taxon2 = ele[2]
        genome_ID = ele[5]

        if taxon1 == taxon2:
            tmp.append(taxon1)
            tmp.append(bac_name1)
            tmp.append(bac_name2)
            tmp.append(phylum)
            tmp.append(genome_ID)
            tmp.append(CDS)
            tmp.append(RR_fun)
            tmp.append(locus)
            for ele in tmp:
                ele_format = str(ele).replace("[","").replace("]","").replace("'","")

                to_write = open(fi,"a")
                to_write.write("%s," % (ele_format))
                to_write.close()
            to_write = open(fi, "a")
            to_write.write("\n")
            to_write.close()