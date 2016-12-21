__author__ = 'kaihami'
RR_open = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/RR_format_gamma", "r").read().split("\n")

to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/Total_RR/RR_total_gamma","a")
to_write.write("ActR,AmiR,CDS,CheB,CheV,FimX,HisK,LytR,NarL,NtrC,OmpR,Other,PvrR,REC_only,RpfG,RssB,WspR,AraC,Bacteria,Phylum,taxon")
to_write.write("\n")
to_write.close()

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
del RR[0]
bac_dict = {}
RR_dict = {}
for line in RR:
    bac_name = line[1]
    fun = line[-2]
    taxon = line[0]
    CDS = line[-3]
    phylum = line[3]
    if bac_name not in bac_dict.keys():
        bac_dict[bac_name] = {}
    if fun not in bac_dict[bac_name].keys():
        bac_dict[bac_name][fun] = 0
    if fun in bac_dict[bac_name].keys():
        bac_dict[bac_name][fun] +=1
    bac_dict[bac_name]["CDS"] = CDS
    bac_dict[bac_name]["phylum"] = phylum
    bac_dict[bac_name]["taxon"] = taxon


options = ["REConly","OmpRfamily(REC-wHTH)",
           "NarLfamily(REC-HTH)", "NtrCfamily(REC-AAA-Fis)",
           "LytRfamily(REC-LytTR)","ActRfamily(REC-Fis)",
           "YesNfamily(REC-HTH_AraC)","AmiRfamily(REC-ANTAR)",
           "WspRfamily(REC-GGDEF)","FimXfamily(REC-GGDEF-EAL)",
           "PvrRfamily(REC-EAL)","RpfGfamily(REC-HD-GYP)",
           "HybridHisK","RssBfamily(REC-PP2C)","CheBfamily(REC-CheB)",
           "CheVfamily(CheW-REC)", "Other", "taxon", "CDS", "phylum" ]
all_dict = {}
for ke, rr in bac_dict.items():
    all_dict[ke] ={}
    for rr_k, rr_n in bac_dict[ke].items():
        rr_class = str(rr_k)
        for ele in options:
            ele_s = str(ele)
            if ele_s in rr_class:
                all_dict[ke][rr_k] = rr_n
        if rr_k not in all_dict[ke].keys():
            if "Other" not in all_dict[ke].keys():
                all_dict[ke]["Other"] = 0
            all_dict[ke]["Other"] += rr_n

for opt in options:
    for key in all_dict.keys():
        if opt not in all_dict[key].keys():
            all_dict[key][opt] = 0
final_lst = []
for key in all_dict.keys():
    tmp = []
    for k, n in all_dict[key].items():
        rr_fun = k
        rr_num = n
        bac_name = key
        for x in xrange(0, len(options)):
            tmp2 = []
            if rr_fun == options[x]:
                tmp2.append([rr_fun, rr_num])
                tmp.append(tmp2)

    tmp.append([["bac",bac_name]])
    final_lst.append(tmp)

for ele in final_lst:
    ele.sort()

for line in final_lst:
    tmp = []
    for ele in line:
        write = ele[0][1]
        tmp.append(write)
    before = str(tmp).replace("[","").replace("]","").replace("'","")
    to_write = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/Total_RR/RR_total_gamma","a")
    to_write.write(before)
    to_write.write("\n")
    to_write.close()

