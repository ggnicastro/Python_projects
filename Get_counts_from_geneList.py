__author__ = 'kaihami'


gene_list = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550/gene_list", "r").read().split("\n")

to_extract = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550/counts_21550_pJN105.csv", "r").read().split("\n")
to_extract2 = []
for line in to_extract:
    tmp = line.split(",")
    to_extract2.append(tmp)

test = []
aa = []

fi = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550/counts_21550_pJN105_p005.csv", "a")
fi.close()
for line in to_extract2:
    for getgene in gene_list:
        if getgene in line:
            aa.append(line)
        else:
            continue


for line in aa:
    fi = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550/counts_21550_pJN105_p005.csv", "a")
    fi.write(str(line).replace("'","").replace("[","").replace("]","").replace(",","\t"))
    fi.write("\n")
    fi.close()