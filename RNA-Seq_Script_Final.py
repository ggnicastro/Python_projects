__author__ = 'kaihami'

"""First step, trimm the samples, and use Picard tools to see the insert size"""

import os
#ok
def Trimm_fastq(Sample_path, Sample_name, OUTPUT_DIR, start_trimm = "1" , five_trim = "100"):
    """
    Simple function to Trimm the samples the output file will be trimmed_Sample_name
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

#Dir pathway
Main_dir = "/home/kaihami/Desktop/RNA-Seq/"

#Sample names
sample1 = "pJN105-10"
sample2 = "46810-1"
sample3 = "46810-2"
sample4 = "46810-3"

#Raw Samples names
r1_sample1 = "pJN105-10_R1"
r2_sample1 = "pJN105-10_R2"
r1_sample2 = "46810-1_R1"
r2_sample2 = "46810-1_R2"
r1_sample3 = "46810-2_R1"
r2_sample3 = "46810-2_R2"
r1_sample4 = "46810-3_R1"
r2_sample4 = "46810-3_R2"
#Raw Samples pathways
r1_sample_1_path = Main_dir + r1_sample1 + ".fastq"
r2_sample_1_path = Main_dir + r2_sample1 + ".fastq"
r1_sample_2_path = Main_dir + r1_sample2 + ".fastq"
r2_sample_2_path = Main_dir + r2_sample2 + ".fastq"
r1_sample_3_path = Main_dir + r1_sample3 + ".fastq"
r2_sample_3_path = Main_dir + r2_sample3 + ".fastq"
r1_sample_4_path = Main_dir + r1_sample4 + ".fastq"
r2_sample_4_path = Main_dir + r2_sample4 + ".fastq"


#Trimm_fastq(r1_sample_1_path, r1_sample1, Main_dir)
Trimm_fastq(r1_sample_1_path, r1_sample1, Main_dir)
Trimm_fastq(r2_sample_1_path, r2_sample1, Main_dir)
Trimm_fastq(r1_sample_2_path, r1_sample2, Main_dir)
Trimm_fastq(r2_sample_2_path, r2_sample2, Main_dir)
Trimm_fastq(r1_sample_3_path, r1_sample3, Main_dir)
Trimm_fastq(r2_sample_3_path, r2_sample3, Main_dir)
Trimm_fastq(r1_sample_4_path, r1_sample4, Main_dir)
Trimm_fastq(r2_sample_4_path, r2_sample4, Main_dir)


r1_sample1_trimmed = Main_dir + "trimmed_" + r1_sample1 + ".fastq"
r2_sample1_trimmed = Main_dir + "trimmed_" + r2_sample1 + ".fastq"

r1_sample2_trimmed = Main_dir + "trimmed_" + r1_sample2 + ".fastq"
r2_sample2_trimmed = Main_dir + "trimmed_" + r2_sample2 + ".fastq"

r1_sample3_trimmed = Main_dir + "trimmed_" + r1_sample3 + ".fastq"
r2_sample3_trimmed = Main_dir + "trimmed_" + r2_sample3 + ".fastq"

r1_sample4_trimmed = Main_dir + "trimmed_" + r1_sample4 + ".fastq"
r2_sample4_trimmed = Main_dir + "trimmed_" + r2_sample4 + ".fastq"

#check_reads_count(r1_sample_1_path, r1_sample1_trimmed, sample1)
#Bowtie2
Reference_genome_path = Main_dir + "Reference/"
Reference_genome = Reference_genome_path +"PA14_reference_genome.fa"
bowtie_index = Reference_genome_path + "Pseudomonas"

create_bowtie_index(Reference_genome, bowtie_index)

bowtie_output = Main_dir + "Bowtie/"

align_bowtie(bowtie_index, r1_sample1_trimmed, r2_sample1_trimmed, bowtie_output, Sample_name = sample1)
align_bowtie(bowtie_index, r1_sample2_trimmed, r2_sample2_trimmed, bowtie_output, Sample_name = sample2)
align_bowtie(bowtie_index, r1_sample3_trimmed, r2_sample3_trimmed, bowtie_output, Sample_name = sample3)
align_bowtie(bowtie_index, r1_sample4_trimmed, r2_sample4_trimmed, bowtie_output, Sample_name = sample4)

#Sort the sam file SortSam(Picard_path, Sample_unsorted, OUTPUT_pathway, Sample_name = "")
sample1_unsorted = bowtie_output + sample1 + ".sam"
sample2_unsorted = bowtie_output + sample2 + ".sam"
sample3_unsorted = bowtie_output + sample3 + ".sam"
sample4_unsorted = bowtie_output + sample4 + ".sam"

Picard_path = "/home/kaihami/picard-tools-1.119/"
SortSam(Picard_path, sample1_unsorted, bowtie_output, Sample_name=sample1)
SortSam(Picard_path, sample2_unsorted, bowtie_output, Sample_name=sample2)
SortSam(Picard_path, sample3_unsorted, bowtie_output, Sample_name=sample3)
SortSam(Picard_path, sample4_unsorted, bowtie_output, Sample_name=sample4)

sample1_sorted = bowtie_output + "sorted_" +sample1 + ".sam"
sample2_sorted = bowtie_output + "sorted_" +sample2 + ".sam"
sample3_sorted = bowtie_output + "sorted_" +sample3 + ".sam"
sample4_sorted = bowtie_output + "sorted_" +sample4 + ".sam"

#Picard Metrics
Picard_metrics(Picard_path, bowtie_output, sample1_sorted, Reference_genome, Sample_name= sample1)
Picard_metrics(Picard_path, bowtie_output, sample2_sorted, Reference_genome, Sample_name= sample2)
Picard_metrics(Picard_path, bowtie_output, sample3_sorted, Reference_genome, Sample_name= sample3)
Picard_metrics(Picard_path, bowtie_output, sample4_sorted, Reference_genome, Sample_name= sample4)

#EDGE-Pro

