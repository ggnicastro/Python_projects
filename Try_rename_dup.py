__author__ = 'kaihami'
""" Rename dup locus"""

fi = "/home/kaihami/Desktop/RR_files/Final_REC/dup/Others_REC.txt.txt"
save_path = "/home/kaihami/Desktop/RR_files/Final_REC/Others_REC_DupRemoved.txt"
fi_open = open(fi, "r").read().split("\n")

dup_tot = []

for line in fi_open:
    if len(line) >2:
        dup_tot.append(line)

fi_rec = "/home/kaihami/Desktop/RR_files/Final_REC/dup/old/Others_REC.txt"
fi_rec_open = open(fi_rec, "r").read().split("\n")
fi_rec_tot = []

for line in fi_rec_open:
    lsplit = line.split(",")
    if len(lsplit) >2:
        fi_rec_tot.append(lsplit)
x =1
dup_dic = {}
for ele in fi_rec_tot:
    locus = ele[7]
    start =  ele[11]
    if locus in dup_tot:
        x+=1
        print locus
        if locus in dup_dic.keys():
            dup_dic[locus].append(start)
        if locus not in dup_dic.keys():
            dup_dic[locus] = [start]
def sort_dic(dic):
    final = {}
    for k, v in dic.items():
        tmp = []
        for val in v:
            tmp.append(int(val))
        tmp.sort()
        final[k] = tmp
    return final
reorder = sort_dic(dup_dic)

for ele in fi_rec_tot:
    Taxon = ele[0]
    Bacteria = ele[1]
    Bacteria2 = ele[2]
    Phylum = ele[3]
    Genome = ele[4]
    CDS = ele[5]
    RR_Class = ele[6]
    locus = ele[7]
    uid = ele[8]
    Fasta = ele[9]
    Hit = ele[10]
    start =  ele[11]
    end = ele[12]
    E_val = ele[13]
    Short = ele[14]
    REC_seq = ele[15]
    if locus in reorder.keys():
        Start_int = int(start)
        for x in xrange(0, len(reorder[locus])):
            if Start_int == int(reorder[locus][x]):
                tmp = []
                Locus_mod = locus + "_" + str(x+1)
                tmp.extend((Taxon, Bacteria, Bacteria2, Phylum, Genome, CDS, RR_Class, Locus_mod, uid, Fasta, Hit, start, end, E_val, Short, REC_seq))
                with open(save_path, 'a') as f:
                    for pos in xrange(0, len(tmp)):
                        if pos != (len(tmp)-1):
                            f.write(tmp[pos])
                            f.write(",")
                        else:
                            f.write(tmp[pos])
                    f.write("\n")
    else:
        tmp = []
        tmp.extend((Taxon, Bacteria, Bacteria2, Phylum, Genome, CDS, RR_Class, locus, uid, Fasta, Hit, start, end, E_val,Short, REC_seq))
        with open(save_path, 'a') as f:
            for pos in xrange(0, len(tmp)):
                if pos != (len(tmp)-1):
                    f.write(tmp[pos])
                    f.write(",")
                else:
                    f.write(tmp[pos])
            f.write("\n")
print "finish"
