__author__ = 'kaihami'
__author__ = 'kaihami'
###
###Pseudomonas aeruginosa PAO1-VE13 genome. - 1..6265484
###76 RNAs
###Location	Strand	Length	PID	Gene	Synonym	Code	COG	Product


gff = open("/home/kaihami/Desktop/RNA-Seq/Reference/Pseudomonas_aeruginosa_PAO1_107.gff", "r").read().split("\n")
del gff[-1]
del gff[0:3]

gff_format = []

for line in gff:
    ele = line.split("\t")
    gff_format.append(ele)

gff_info = []
ptts = []
for info in gff_format:
    gene = info[2]
    if gene == "gene":
        start = info[3]
        end = info[4]

        location = start+".."+end

        length = str((((int(end) - (int(start)-1)))-3)/3)
        strand = info[6]
        features = info[-1].split(";")
        for feature in features:
            if "Alias=" in feature:
                locus = feature.replace("Alias=","")
            if "name=" in feature:
                gene_id = feature.replace("name=", "")
        PID = "553895034"
        #Location OK	Strand OK	Length OK	PID OK	Gene -	Synonym OK	Code -	COG -	Product OK
        table_code = "-"
        table_COG = "-"
        table_product = "-"
        tog = []
        tog.extend([location, strand, length, PID, gene_id, locus, table_code, table_COG, table_product])
        ptts.append(tog)
with open("/home/kaihami/Desktop/RNA-Seq/Reference/PAO1_formatted.ptt", "a") as f:
    f.write("Pseudomonas aeruginosa PAO1. - 1..6264404")
    f.write("\n")
    f.write("5696 proteins")
    f.write("\n")
    f.write("Location	Strand	Length	PID	Gene	Synonym	Code	COG	Product")
    f.write("\n")

for ptt in ptts:
    with open("/home/kaihami/Desktop/RNA-Seq/Reference/PAO1_formatted.ptt", "a") as f:
        s = "\t".join(x for x in ptt)
        f.write(s)
        f.write("\n")
#gff_format: chromossome PseudoCAP gene/cds/etc start end . strand  features
#rnt format: Location	Strand	Length	PID	Gene	Synonym	Code	COG	Product
## 298816..298892	-/+	77	553895034	-	N297_270	-	-	Arg tRNA

