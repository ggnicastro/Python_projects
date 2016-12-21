__author__ = 'kaihami'

"""Trim, Check reads, create bowtie index (for bowtie align), align with bowtie,
Sort the sam file, generate Picard Metrics, and finally align with EDGE-Pro"""

import os
#ok
def Trimm_fastq(Sample_path, Sample_name, OUTPUT_DIR, start_trimm = "1" , five_trim = "100"):
    """
    Simple function to Trimm the samples the output file will be trimmed_Sample_name21550
    :param start_trimm: 3' trimm DEFAULT = 1
    :param five_trim: 5' trimm DEFAULT = 100
    :param sample_path: Sample pathway
    :param OUTPUT_DIR: Where to save the output file
    :param Sample_name: Sample name
    """
    os.system("fastx_trimmer -f " + start_trimm + " -l " + five_trim + " -i " + Sample_path +
    " -o " + OUTPUT_DIR + "/trimmed_" + Sample_name + ".fastq")

#ok
def check_reads_count(before_trimm, after_trimm, Sample_name = ""):
    """
    Simple function to check the reads before and after trimm
    :param before_trimm:
    :param after_trimm:
    :param Sample_name:
    """
    print "Reads before trimm", Sample_name
    os.system('grep "@M" ' + before_trimm + " | wc -l")
    print "Reads after trimm", Sample_name
    os.system('grep "@M" ' + after_trimm + " | wc -l")

#ok
def create_bowtie_index(Reference_genome, bowtie_index):
    """
    Function to create the bowtie index
    :param Reference_genome: Reference genome pathway
    :param bowtie_index: Output index pathway
    """
    os.system("bowtie2-build " + Reference_genome + " " + bowtie_index)

#ok
def align_bowtie(bowtie_index, R1_path, R2_path, OUTPUT_PATH, Sample_name = "alignment"):
    """
    Align with bowtie
    :param bowtie_index: bowtie index pathway
    :param R1_path: R1 pathway (trimmed or not)
    :param R2_path: R2 pathway (trimmed or not)
    :param OUTPUT_PATH: Output pathway
    :param Sample_name: Sample name DEFAULT = alignment
    """
    os.system("bowtie2 -X 1000 -t " + bowtie_index +
              " -1 " + R1_path +
              " -2 " + R2_path +
              " -S " + OUTPUT_PATH + "/" + Sample_name + ".sam")

def SortSam(Picard_path, Sample_unsorted, OUTPUT_pathway, Sample_name = ""):
    """
    Sort sam file with Picard tools
    :param Picard_path: Picard tools pathway
    :param Sample_unsorted: Unsorted Sam file pathway
    :param OUTPUT_pathway: Output Sam file pathway
    :param Sample_name: output sample name
    """
    os.system ("java -jar " + Picard_path + "SortSam.jar " +
               "INPUT= " + Sample_unsorted +
               " OUTPUT= " + OUTPUT_pathway + "sorted_" + Sample_name +".sam" +" SO= coordinate")

def Picard_metrics(Picard_path, OUTPUT_Pathway, Sam_sorted_file, Reference_genome, Sample_name = ""):
    """
    Generate some metrics with Picard tools
    :param Picard_path: Picard tools pathway
    :param OUTPUT_Pathway: Output pathway
    :param Sam_sorted_file: Sam sorted file pathway
    :param Reference_genome: Reference genome pathway
    :param Sample_name: Sample name
    """
    os.system("java -jar " + Picard_path + "CollectInsertSizeMetrics.jar " +
              " HISTOGRAM_FILE= " + OUTPUT_Pathway + "/" + "Hist_" + Sample_name +
              " INPUT= " + Sam_sorted_file +
              " OUTPUT= " + OUTPUT_Pathway + "/" + "InsertSize_" + Sample_name +
              " REFERENCE_SEQUENCE= " + Reference_genome)

def Edge_call(Reference_genome, ptt, rnt, R1_file, R2_file, OUTPUT_PATH, M = "500"):
    os.system("./edge.pl -g " + Reference_genome +
              " -p "+ ptt +
              " -r " + rnt +
              " -u " + R1_file +
              " -v " + R2_file +
              " -M " + M
              + " -o " + OUTPUT_PATH)
    print "Finish"


Main_dir = "/home/kaihami/Desktop/RNA-Seq/"

sample1 = "21550-6"
r1_sample1 = "21550-6_R1"
r2_sample1 = "21550-6_R2"
r1_sample_1_path = Main_dir + r1_sample1 + ".fastq"
r2_sample_1_path = Main_dir + r2_sample1 + ".fastq"

sample2 = "26570-6"
r1_sample2 = "26570-6_R1"
r2_sample2 = "26570-6_R2"
r1_sample_2_path = Main_dir + r1_sample2 + ".fastq"
r2_sample_2_path = Main_dir + r2_sample2 + ".fastq"

sample3 = "pJN105-8"
r1_sample3 = "26570-8_R1"
r2_sample3 = "26570-8_R2"
r1_sample_3_path = Main_dir + r1_sample3 + ".fastq"
r2_sample_3_path = Main_dir + r2_sample3 + ".fastq"

sample4 = "pJN105-9"
r1_sample4 = "pJN105-9_R1"
r2_sample4 = "pJN105-9_R2"
r1_sample_4_path = Main_dir + r1_sample4 + ".fastq"
r2_sample_4_path = Main_dir + r2_sample4 + ".fastq"

Trimm_fastq(r1_sample_1_path, r1_sample1, Main_dir)
Trimm_fastq(r2_sample_1_path, r2_sample1, Main_dir)

Trimm_fastq(r1_sample_2_path, r1_sample2, Main_dir)
Trimm_fastq(r2_sample_2_path, r2_sample2, Main_dir)

Trimm_fastq(r1_sample_3_path, r1_sample3, Main_dir)
Trimm_fastq(r2_sample_3_path, r2_sample3, Main_dir)

Trimm_fastq(r1_sample_4_path, r1_sample4, Main_dir)
Trimm_fastq(r2_sample_4_path, r2_sample4, Main_dir)

reference_genome = Main_dir+ "Reference/PA14_reference_genome.fa"
ptt = Main_dir + "Reference/Pseudomonas.ptt"
rnt = Main_dir + "Reference/Pseudomonas.rnt"
output_path = Main_dir + "EDGE-Pro/"

r1_sample11 = "trimmed_21550-6_R1"
r2_sample11 = "trimmed_21550-6_R2"

r1_sample12 = "trimmed_26570-6_R1"
r2_sample12 = "trimmed_26570-6_R2"

r1_sample13 = "trimmed_pJN105-8_R1"
r2_sample13 = "trimmed_pJN105-8_R2"

r1_sample14 = "trimmed_pJN105-9_R1"
r2_sample14 = "trimmed_pJN105-9_R2"

r1_sample_1_path2 = Main_dir + r1_sample11 + ".fastq"
r2_sample_1_path2 = Main_dir + r2_sample11 + ".fastq"

r1_sample_2_path2 = Main_dir + r1_sample12 + ".fastq"
r2_sample_2_path2 = Main_dir + r2_sample12 + ".fastq"

r1_sample_3_path2 = Main_dir + r1_sample13 + ".fastq"
r2_sample_3_path2 = Main_dir + r2_sample13 + ".fastq"

r1_sample_4_path2 = Main_dir + r1_sample14 + ".fastq"
r2_sample_4_path2 = Main_dir + r2_sample14 + ".fastq"

output_path1 = Main_dir + "EDGE-Pro/" + sample1
output_path2 = Main_dir + "EDGE-Pro/" + sample2
output_path3 = Main_dir + "EDGE-Pro/" + sample3
output_path4 = Main_dir + "EDGE-Pro/" + sample4

Edge_call(reference_genome, ptt, rnt, r1_sample_1_path2, r2_sample_1_path2, output_path1, M="400")
Edge_call(reference_genome, ptt, rnt, r1_sample_2_path2, r2_sample_2_path2, output_path2, M="400")
Edge_call(reference_genome, ptt, rnt, r1_sample_3_path2, r2_sample_3_path2, output_path3, M="400")
Edge_call(reference_genome, ptt, rnt, r1_sample_4_path2, r2_sample_4_path2, output_path4, M="400")