__author__ = 'kaihami'
import os

"""Read SRA and convert to Fastq file"""

fastq = "/home/kaihami/sratoolkit.2.4.4-ubuntu64/bin/fastq-dump "
file_path = "/home/kaihami/Desktop/SigX/"
Sample1 = "SRA_SigX_WT1.sra "
Sample2 = "SRA_SigX_WT2.sra "
Sample3 = "SRA_SigX_knockout1.sra "
Sample4 = "SRA_SigX_knockout2.sra "
Sample5 = "SRA_SigX_empty1.sra "
Sample6 = "SRA_SigX_empty2.sra "
Sample7 = "SRA_SigX_over1.sra "
Sample8 = "SRA_SigX_over2.sra "

os.system(fastq + file_path+Sample1 + " -O "+ file_path)
os.system(fastq + file_path+Sample2+ " -O "+ file_path)
os.system(fastq + file_path+Sample3+ " -O "+ file_path)
os.system(fastq + file_path+Sample4+ " -O "+ file_path)
os.system(fastq + file_path+Sample5+ " -O "+ file_path)
os.system(fastq + file_path+Sample6+ " -O "+ file_path)
os.system(fastq + file_path+Sample7+ " -O "+ file_path)
os.system(fastq + file_path+Sample8+ " -O "+ file_path)

"""Align with bowtie2"""

#Build the bowtie index

reference_genome_path = file_path + "Reference/PA14_reference_genome.fa"
bowtie_index = file_path + "Reference/Pseudomonas"
os.system("bowtie2-build " + reference_genome_path + " " + bowtie_index)

#Align with bowtie
bowtie_output = file_path + "Bowtie"
fastq_sample1 = file_path + Sample1.replace("sra", "fastq").replace(" ", "")
fastq_sample2 = file_path + Sample2.replace("sra", "fastq").replace(" ", "")
fastq_sample3 = file_path + Sample3.replace("sra", "fastq").replace(" ", "")
fastq_sample4 = file_path + Sample4.replace("sra", "fastq").replace(" ", "")
fastq_sample5 = file_path + Sample5.replace("sra", "fastq").replace(" ", "")
fastq_sample6 = file_path + Sample6.replace("sra", "fastq").replace(" ", "")
fastq_sample7 = file_path + Sample7.replace("sra", "fastq").replace(" ", "")
fastq_sample8 = file_path + Sample8.replace("sra", "fastq").replace(" ", "")

os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample1+ " -S " + bowtie_output + "/" + Sample1.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample2+ " -S " + bowtie_output + "/" + Sample2.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample3+ " -S " + bowtie_output + "/" + Sample3.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample4+ " -S " + bowtie_output + "/" + Sample4.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample5+ " -S " + bowtie_output + "/" + Sample5.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample6+ " -S " + bowtie_output + "/" + Sample6.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample7+ " -S " + bowtie_output + "/" + Sample7.replace("sra", "sam").replace(" ", ""))
os.system("bowtie2 -X 1000 -t " + bowtie_index + " -U "+ fastq_sample8+ " -S " + bowtie_output + "/" + Sample8.replace("sra", "sam").replace(" ", ""))

"""Picard"""
unsorted_sample1 = bowtie_output + "/" + Sample1.replace("sra", "sam").replace(" ", "")
unsorted_sample2 = bowtie_output + "/" + Sample2.replace("sra", "sam").replace(" ", "")
unsorted_sample3 = bowtie_output + "/" + Sample3.replace("sra", "sam").replace(" ", "")
unsorted_sample4 = bowtie_output + "/" + Sample4.replace("sra", "sam").replace(" ", "")
unsorted_sample5 = bowtie_output + "/" + Sample5.replace("sra", "sam").replace(" ", "")
unsorted_sample6 = bowtie_output + "/" + Sample6.replace("sra", "sam").replace(" ", "")
unsorted_sample7 = bowtie_output + "/" + Sample7.replace("sra", "sam").replace(" ", "")
unsorted_sample8 = bowtie_output + "/" + Sample8.replace("sra", "sam").replace(" ", "")

Picard_path = "/home/kaihami/picard-tools-1.119/"
#Sort files
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample1 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample1.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample2 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample2.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample3 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample3.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample4 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample4.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample5 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample5.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample6 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample6.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample7 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample7.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + unsorted_sample8 + " OUTPUT= " + bowtie_output +"/" + "sorted_"+  Sample8.replace("sra", "sam").replace(" ", "") + " SORT_ORDER=coordinate")

#Create and collect insert size metric

sorted_sample1 = bowtie_output +"/" + "sorted_"+  Sample1.replace("sra", "sam").replace(" ", "")
sorted_sample2 = bowtie_output +"/" + "sorted_"+  Sample2.replace("sra", "sam").replace(" ", "")
sorted_sample3 = bowtie_output +"/" + "sorted_"+  Sample3.replace("sra", "sam").replace(" ", "")
sorted_sample4 = bowtie_output +"/" + "sorted_"+  Sample4.replace("sra", "sam").replace(" ", "")
sorted_sample5 = bowtie_output +"/" + "sorted_"+  Sample5.replace("sra", "sam").replace(" ", "")
sorted_sample6 = bowtie_output +"/" + "sorted_"+  Sample6.replace("sra", "sam").replace(" ", "")
sorted_sample7 = bowtie_output +"/" + "sorted_"+  Sample7.replace("sra", "sam").replace(" ", "")
sorted_sample8 = bowtie_output +"/" + "sorted_"+  Sample8.replace("sra", "sam").replace(" ", "")

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample1.replace("sra", "").replace(" ", "").replace(".","") +
 " INPUT= " + sorted_sample1 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample1.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path + " ASSUME_SORTED= False")

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample2.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample2 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample2.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample3.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample3 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample3.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample4.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample4 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample4.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample5.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample5 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample5.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample6.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample6 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample6.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample7.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample7 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample7.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)

os.system("java -Xmx2g -jar " + Picard_path + "CollectInsertSizeMetrics.jar "" HISTOGRAM_FILE= " + bowtie_output + "/" + "Hist_" + Sample8.replace("sra", "").replace(" ", "").replace(".","")  +
 " INPUT= " + sorted_sample8 + " OUTPUT= " + bowtie_output +"/" + "InsertSize_" + Sample8.replace("sra", "").replace(" ", "").replace(".","")  + " REFERENCE_SEQUENCE= " + reference_genome_path)
