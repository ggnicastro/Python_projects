__author__ = 'kaihami'
"""
Using a batch-CDD search file find the REC domain in the FASTA file formatted
return a file with:  Taxon,Bacteria,Bacteria2,Phylym,Genome_ID,CDS,
                    RR_class,Locus_tag,UID,Fasta,Hit,Start,End,E_val,
                    Short,REC_sequence"
"""

#Working with hit data: generate a list with ID, Hit_type, Start, end, e_val, and domain name
hit_data = "/home/kaihami/Desktop/RR_files/NarL_hitdata.txt"
save_path = "/home/kaihami/Desktop/RR_files/Final_NarL/RR_NarL.txt"
fasta_file = "/home/kaihami/Desktop/RR_files/Fasta/FASTA_NarL/All_NarL.txt"
with open(save_path, "a") as f:
    f.write("Taxon,Bacteria,Bacteria2,Phylym,Genome_ID,CDS,RR_class,Locus_tag,UID,Fasta,Hit,Start,End,E_val,Short,REC_sequence")
    f.write("\n")

open_hit = open(hit_data, "r").read().split("\n")

hit = []

for line in open_hit:
    if line.startswith("#"):
        pass
    else:
        if len(line.split("\t")) > 2:
            hit.append(line.split("\t"))

hit_format = []

for x in xrange(0, len(hit)):
    try:
        query = hit[x][0].split()[2].replace(">","")
    except:
        query = hit[x][0]
    Hit_type = hit[x][1]
    start = hit[x][3]
    end = hit[x][4]
    e_val = hit[x][5]
    short_name = hit[x][8]
    tmp = []
    tmp.extend((query, Hit_type, start, end, e_val, short_name))
    hit_format.append(tmp)
del hit_format[0]

#work with the fasta_formatted file


print "Opening"
Open_fasta = open(fasta_file, "r").read().split("\n")
RR = []
for line in Open_fasta:
    if len(line.split(","))>2:
        RR.append(line.split(","))
REC = []
HTHs = ["HTH_LUXR", "FixJ", "OmpR", "GerE","fixJ","CsgD", "LuxR_C_like", "PRK10651",
        "FhlA","PRK10403", "zf-C3HC4", "zf-C2H2", "zf-H2C2_2", "HTH_AsnC-type",
        "HTH_11","HTH_29","HTH_AraC","HTH_IclR","MarR_2","Sigma70_r2", "Sigma54_activat",
        "HTH_8","LytTR", "HTH_ARSR"]
print "RR"
for ele in RR:
    Taxon = ele[0]
    Bacteria = ele[1]
    Bacteria2 = ele[2]
    Phylym = ele[3]
    Genome_ID = ele[4]
    CDS = ele[5]
    RR_class = ele[6]
    Locus_tag = ele[7]
    UID = ele[8]
    Fasta = ele[9]
    for x in xrange(0, len(hit_format)):
        Q2 = hit_format[x][0]
        Hit = hit_format[x][1]
        Start = hit_format[x][2]
        End = hit_format[x][3]
        E_val = hit_format[x][4]
        Short = hit_format[x][5]
        if Locus_tag == Q2 and Hit.lower() == "specific" and Short in HTHs:
            print "Enter"
            RR_slice = Fasta[int(Start):int(End)]
            tmp = []
            tmp.extend((Taxon, Bacteria, Bacteria2, Phylym, Genome_ID, CDS, RR_class, Locus_tag, UID, Fasta, Hit, Start, End, E_val, Short, RR_slice))
            REC.append(tmp)
print "Finish"
dup = []
dup2 = []
for ele in REC:
    tmp = []
    locus = ele[7]
    st = ele[12]
    tmp.extend((locus, st))
    if tmp not in dup:
        dup.append(tmp)
        with open(save_path, 'a') as f:
            for pos in xrange(0, len(ele)):
                if pos != (len(ele)-1):
                    f.write(ele[pos])
                    f.write(",")
                else:
                    f.write(ele[pos])
            f.write("\n")
    else:
        dup2.append(ele)

print "finish"
#Save it: RR_list:    Taxonomy, Bacteria, Bacteria2, Phylum, Genome_ID, CDS, RR_Class, Locus_tag, UID_nuber, Fasta\
#         hit_format: query, Hit_type, start, end, e_val, short_name
h_d = []

for ele in hit_format:
    Hit = ele[1]
    fun = ele[-1]
    if fun not in h_d:
        h_d.append(fun)

