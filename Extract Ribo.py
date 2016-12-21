__author__ = 'kaihami'
ribo_file = open("/home/kaihami/Desktop/RNA-Seq/Reference/Ribo_genes", "r").read().split("\n")

to_extract = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/deseqFile", "r").read().split("\n")
to_extract2 = []
for line in to_extract:
    tmp = line.split("\t")
    to_extract2.append(tmp)

test = []
len(ribo_file)
aa = []

fi = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/deseqFile_ribodepleted", "a")
fi.close()
for line in to_extract2:
    for remove in ribo_file:
        if remove in line:
            break
    else:
        test.append(line)

for line in test:
    fi = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/deseqFile_ribodepleted", "a")
    fi.write(str(line).replace("'","").replace("[","").replace("]","").replace(",","\t"))
    fi.write("\n")
    fi.close()
