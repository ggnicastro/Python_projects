
f = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/SRR_infection/deseqFile", "r").read().split("\n")

f_form = []
del f[0]
for line in f:
    s = line.split("\t")
    f_form.append(s)
del f_form[-1]
ff = []
for line in f:
    s = line.split("\t")
    ff.append(s)
dup = []
all = []
for line in f_form:
    gene = line[0]
    print gene
    if gene in all:
        dup.append(gene)
    if gene not in all:
        all.append(gene)

rnts = open("/home/kaihami/Desktop/RNA-Seq/Reference/PAO1_formatted.rnt", "r").read().split("\n")
rnt_l = []
for line in rnts:
    s = line.split("\t")
    if len(s) >4:
        rnt_l.append(s[5])

for line in ff:
    ge = line[0]
    if ge in rnt_l:
        pass
    if ge not in rnt_l:
        with open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/SRR_infection/ribo_dep.txt", "a") as fi:
            fi.write("\t".join(x for x in line))
            fi.write("\n")
