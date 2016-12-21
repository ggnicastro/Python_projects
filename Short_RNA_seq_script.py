__author__ = 'kaihami'

import os

Sample_1 = "PA14_pJN105_2"
Sample_2 = "PA14_21550_2"
Sample_3 = "PA14_26570_2"
Sample_4 = "PA14_BqsR_1"
RNA_path_seq = "/home/kaihami/Desktop/RNA_seq_2_replica"

#reads:
Sample_1_fastq_R1 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-pJN105-2_R1.fastq"
Sample_1_fastq_R2 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-pJN105-2_R2.fastq"

Sample_2_fastq_R1 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-21550-2_R1.fastq"
Sample_2_fastq_R2 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-21550-2_R2.fastq"

Sample_3_fastq_R1 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-26570-2_R1.fastq"
Sample_3_fastq_R2 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-26570-2_R2.fastq"

Sample_4_fastq_R1 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-BqsR-1_R1.fastq"
Sample_4_fastq_R2 = RNA_path_seq + "/" + "Sequence" + "/" + "PA14-BqsR-1_R2.fastq"

#Reference Genome
Ref_gen_path2 = RNA_path_seq + "/" + "Reference"

#Bowtie

bowtie_output = "Pseudomonas"

Ref_gen_path = Ref_gen_path2 + "/" + "PA14_reference_genome.fa"

os.system("bowtie2-build " + Ref_gen_path + " " + Ref_gen_path2 + "/" + bowtie_output)

bowtie_index = Ref_gen_path2 + "/" + bowtie_output


'''
#Trimmer
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_1_fastq_R1 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-pJN105-2_R1.fastq")
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_1_fastq_R2 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-pJN105-2_R2.fastq")
'''
r1_sample_1_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-pJN105-2_R1.fastq"
r2_sample_1_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-pJN105-2_R2.fastq"
'''
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_2_fastq_R1 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-21550-2_R1.fastq")
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_2_fastq_R2 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-21550-2_R2.fastq")
'''
r1_sample_2_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-21550-2_R1.fastq"
r2_sample_2_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-21550-2_R2.fastq"
'''
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_3_fastq_R1 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-26570-2_R1.fastq")
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_3_fastq_R2 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-26570-2_R2.fastq")
'''
r1_sample_3_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-26570-2_R1.fastq"
r2_sample_3_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-26570-2_R2.fastq"
'''
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_4_fastq_R1 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-BqsR-2_R1.fastq")
os.system("fastx_trimmer -f 1 -l " + "100" + " -i " + Sample_4_fastq_R2 + " -o " + RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-BqsR-2_R2.fastq")
'''
r1_sample_4_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-BqsR-2_R1.fastq"
r2_sample_4_path = RNA_path_seq + "/Sequence" + "/trimmed_" + "PA14-BqsR-2_R2.fastq"

#align
Bowtie_path_output = RNA_path_seq + "/Bowtie"
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -1 " + r1_sample_1_path + " -2 " + r2_sample_1_path + " -S " + Bowtie_path_output + "/" + Sample_1 + ".sam")

sample_1_sam_unsorted = Bowtie_path_output +"/"+ Sample_1 + ".sam"
print("Sample 1 done")

os.system("bowtie2 -X 1000 -t " + bowtie_index + " -1 " + r1_sample_2_path + " -2 " + r2_sample_2_path + " -S " + Bowtie_path_output + "/" + Sample_2 + ".sam")

sample_2_sam_unsorted = Bowtie_path_output +"/"+ Sample_2 + ".sam"
print("Sample 2 done")

os.system("bowtie2 -X 1000 -t " + bowtie_index + " -1 " + r1_sample_3_path + " -2 " + r2_sample_3_path + " -S " + Bowtie_path_output + "/" + Sample_3 + ".sam")

sample_3_sam_unsorted = Bowtie_path_output +"/"+ Sample_3 + ".sam"
print("Sample 3 done")

os.system("bowtie2 -X 1000 -t " + bowtie_index + " -1 " + r1_sample_4_path + " -2 " + r2_sample_4_path + " -S " + Bowtie_path_output + "/" + Sample_4 + ".sam")

sample_4_sam_unsorted = Bowtie_path_output +"/"+ Sample_4 + ".sam"
print("Sample 4 done")
#Picard
Picard_path = "/home/kaihami/picard-tools/"
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample_1_sam_unsorted + " OUTPUT= " + Bowtie_path_output + "sorted_" + Sample_1 + ".sam" + " SORT_ORDER=coordinate")
sample_1_sam_sorted = Bowtie_path_output + "/" + "sorted_" + Sample_1 + ".sam"
print("Sort sample 1 done")

os.system("java -Xmx2g -jar " + Picard_path + "/SortSam.jar " + "INPUT= " + sample_2_sam_unsorted + " OUTPUT= " + Bowtie_path_output + "sorted_" + Sample_2 + ".sam" + " SORT_ORDER=coordinate")
sample_2_sam_sorted = Bowtie_path_output + "/" + "sorted_" + Sample_2 + ".sam"
print("Sort sample 2 done")

os.system("java -Xmx2g -jar " + Picard_path + "/SortSam.jar " + "INPUT= " + sample_3_sam_unsorted + " OUTPUT= " + Bowtie_path_output + "sorted_" + Sample_3 + ".sam" + " SORT_ORDER=coordinate")
sample_3_sam_sorted = Bowtie_path_output + "/" + "sorted_" + Sample_3 + ".sam"
print("Sort sample 3 done")

os.system("java -Xmx2g -jar " + Picard_path + "/SortSam.jar " + "INPUT= " + sample_4_sam_unsorted + " OUTPUT= " + Bowtie_path_output + "sorted_" + Sample_4 + ".sam" + " SORT_ORDER=coordinate")
sample_4_sam_sorted = Bowtie_path_output + "/" + "sorted_" + Sample_4 + ".sam"
print("Sort sample 4 done")



####

Bowtie_path_output = RNA_path_seq + "/Bowtie"
Picard_path = "/home/kaihami/picard-tools/"
os.system("java -Xmx2g -jar " + Picard_path + "/SortSam.jar " + "INPUT= " + sample_2_sam_unsorted + " OUTPUT= " + Bowtie_path_output + "sorted_" + Sample_2 + ".sam" + " SORT_ORDER=coordinate")
sample_2_sam_sorted = Bowtie_path_output + "/" + "sorted_" + Sample_2 + ".sam"
print("Sort sample 2 done")

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + Bowtie_path_output +
			"/" + "Hist_" + Sample_1 + " INPUT= " + sample_1_sam_sorted + " OUTPUT= " + Bowtie_path_output + "/" +
			"InsertSize_" + Sample_1 + " REFERENCE_SEQUENCE= " + Ref_gen_path)
print("Picard sample 1 done")

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + Bowtie_path_output +
			"/" + "Hist_" + Sample_2 + " INPUT= " + sample_2_sam_sorted + " OUTPUT= " + Bowtie_path_output + "/" +
			"InsertSize_" + Sample_2 + " REFERENCE_SEQUENCE= " + Ref_gen_path)
print("Picard sample 2 done")

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + Bowtie_path_output +
			"/" + "Hist_" + Sample_3 + " INPUT= " + sample_3_sam_sorted + " OUTPUT= " + Bowtie_path_output + "/" +
			"InsertSize_" + Sample_3 + " REFERENCE_SEQUENCE= " + Ref_gen_path)
print("Picard sample 3 done")

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + Bowtie_path_output +
			"/" + "Hist_" + Sample_4 + " INPUT= " + sample_4_sam_sorted + " OUTPUT= " + Bowtie_path_output + "/" +
			"InsertSize_" + Sample_4 + " REFERENCE_SEQUENCE= " + Ref_gen_path)
print("Picard sample 4 done")
