import os
bowtie_index = "/home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas"
sample_1 = "PA14-pJN105_1"
sample_2 = "PA14-21550_1"
sample_3 = "PA14-26570_1"
RNA_path_seq = "/home/kaihami/Desktop/PA14_1analise/Bowtie/"
ref_gen_path = "/home/kaihami/Desktop/PA14_1analise/Reference/PA14_reference_genome.fa"

Picard_path = "/home/kaihami/picard-tools-1.122/"




sample_1_sam_sorted = RNA_path_seq + "sorted_" + sample_1 + ".sam"

sample_2_sam_sorted = RNA_path_seq + "sorted_" + sample_2 + ".sam"

sample_3_sam_sorted = RNA_path_seq + "sorted_" + sample_3 + ".sam"


os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= Hist_" + sample_1 + " INPUT= " + sample_1_sam_sorted + " OUTPUT= " + RNA_path_seq + "/" + "InsertSize_" + sample_1 + " REFERENCE_SEQUENCE= " + ref_gen_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= Hist_" + sample_2 + " INPUT= " + sample_2_sam_sorted + " OUTPUT= " + RNA_path_seq + "/" + "InsertSize_" + sample_2 + " REFERENCE_SEQUENCE= " + ref_gen_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= Hist_" + sample_3 + " INPUT= " + sample_3_sam_sorted + " OUTPUT= " + RNA_path_seq + "/" + "InsertSize_" + sample_3 + " REFERENCE_SEQUENCE= " + ref_gen_path)
 
