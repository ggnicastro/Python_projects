__author__ = 'kaihami'
#!python

"""First step, trimm the samples, and use Picard tools to see the insert size"""

import os
import argparse
"""
Inputs: Sample Names
        paired or single end
        reads 1
        reads 2
        reference genome
        ptt
        rnt
        Trim(?)
        Picard
"""
text = """
\n
MANDATORY FILES:
________________
-g --genome: fasta file containing bacterial genome.
-p --ptt:    ptt file with coordinates of coding genes, in Genbank format.
-r --rnt:    rnt file with coordinates of rRNAs and tRNAs, in Genbank format.
-s --sample: Sample name separated by space with fastq file of reads.
             In paired-end library put the second read file after the first read file.
             Single-end: sample_1 read_1 sample_2 read_1 ...
             Paired-end: sample_1 read_1 read_2 sample_2 read_1 read_2 ...

OPTIONAL FILES/PARAMETERS:
__________________________
-T --Trim: Trim samples in 3' and or 5' [Default = no]
           <[start] [end]> (e.g. 1 100) ==> will trimm sample from base 0 to 100 in fastq file
--Picard:  Generate insert size metrics (only for paired-end library) (Choices: yes/no)
           [Default = no]
-Project:  Directory name to save output results [Default = Results]
-m minimum insert size in paired-end
-M maximum insert size in paired-end
-threads: number of threads
-w window: It is an integer specifying the window size close to
           overlapping region used to approximate the coverage of a gene close to the overlapping
           region in order to distrbute the coverage of the overlapping region between two overlapping genes. Default: 100.
-i untranslated region Default = 40
-c minimum coverage: It is an integer specifying the minimum average coverage of gene for gene to be considered expressed.
            Coverage lower than specified is assumed to be noise and gene is considered to not be expressed. Default: 3.
-n count type: It is 0 or 1 specifying how to count reads that map to multiple places.
               0 denotes giving a partial count to each place where the read maps.
               1 denotes picking randomly one of the places where the read maps and assigning full count to that one place. Default: 0.

"""
parser = argparse.ArgumentParser(
                                 usage = "python iBRA.py <-g genome> <-p ptt_file> <-rnt rnt_file> <-s Sample_name_1 read_1 read_2 Sample_name_2 read_1...>",
                                 add_help= False,
                                 formatter_class = argparse.RawDescriptionHelpFormatter,
                                 description = text
                                )

parser.add_argument('-s', '--sample', nargs = '+', required = True,
                    help=argparse.SUPPRESS)

parser.add_argument('-t', '--type', default = "paired",
                    choices = ["paired", "single", "p", "s"],
                    help=argparse.SUPPRESS)

parser.add_argument('-g', '--genome', required = True,
                    help=argparse.SUPPRESS)

parser.add_argument('-p', '--ptt', required = True,
                    help=argparse.SUPPRESS)

parser.add_argument('-r', '--rnt', required = True,
                    help=argparse.SUPPRESS)

parser.add_argument('-T', '--Trim', default = 'no', nargs = '+',
                    help=argparse.SUPPRESS)
parser.add_argument('--Picard', default = 'no', choices = ['yes', 'no'],
                    help=argparse.SUPPRESS)
parser.add_argument('-Project', default = "Results",
                    help=argparse.SUPPRESS)
parser.add_argument('-m', '--minimum', default= "0",
                    help = argparse.SUPPRESS)
parser.add_argument('-M', '--maximum', default = "500",
                    help = argparse.SUPPRESS)
parser.add_argument('-threads', default= "1",
                    help = argparse.SUPPRESS)
parser.add_argument('-w', default= "100",
                    help = argparse.SUPPRESS)
parser.add_argument('-i', default = "40",
                    help = argparse.SUPPRESS)
parser.add_argument('-c', default = "3",
                    help = argparse.SUPPRESS)
parser.add_argument('-n', default="0",
                    help = argparse.SUPPRESS)
parser.add_argument('-h', '--help',action = "help",
                    help=argparse.SUPPRESS)

args = parser.parse_args()

#Samples ok!
def Samples(args, Type):
    """
    get sample name and fastq files
    ok
    """
    single_end = ["single", "s"]
    paired_end = ["paired", "p"]
    if Type in single_end:
        samples = args.sample
        my_samples = [samples[x:x+2] for x in xrange(0, len(samples), 2)]
        return my_samples
    if Type in paired_end:
        samples = args.sample
        my_samples = [samples[x:x+3] for x in xrange(0, len(samples), 3)]
        return my_samples

def Trimm_fastq(read, sample_name, OUTPUT_DIR, Trim):
    print "Trimming sample %s" % sample_name
    start_trim = str(Trim[0])
    end_trim = str(Trim[1])
    print ("fastx_trimmer -f " + start_trim + " -l " + end_trim + " -i " + read + " -o " + OUTPUT_DIR)
    os.system("fastx_trimmer -f " + start_trim + " -l " + end_trim + " -i " + read +
    " -o " + OUTPUT_DIR)
    print "%s Trimmed" % sample_name

def check_reads_count(before_trimm):
    """
    Simple function to check the reads before and after trimm
    :param before_trimm:
    :param after_trimm:
    :param Sample_name:
    """
    total = os.system('grep "@M" ' + before_trimm + " | wc -l")
    print total

def SortSam(Sample_unsorted, OUTPUT_pathway):
    """
    Sort sam file with Picard tools
    :param Picard_path: Picard tools pathway
    :param Sample_unsorted: Unsorted Sam file pathway
    :param OUTPUT_pathway: Output Sam file pathway
    :param Sample_name: output sample name
    """
    sample = "_sorted" + ".sam"
    Output = OUTPUT_pathway + sample
    os.system ("java -jar " + "./SortSam.jar " +
               "INPUT= " + Sample_unsorted +
               " OUTPUT= " + OUTPUT_pathway + sample +" SO= coordinate")
    return Output

def Picard_metrics(OUTPUT_Pathway, Sam_sorted_file, Reference_genome, Sample_name = ""):
    """
    Generate some metrics with Picard tools
    :param Picard_path: Picard tools pathway
    :param OUTPUT_Pathway: Output pathway
    :param Sam_sorted_file: Sam sorted file pathway
    :param Reference_genome: Reference genome pathway
    :param Sample_name: Sample name
    """
    os.system("java -jar " + "./CollectInsertSizeMetrics.jar " +
              " HISTOGRAM_FILE= " + OUTPUT_Pathway + "/" + "Hist_" + Sample_name +
              " INPUT= " + Sam_sorted_file +
              " OUTPUT= " + OUTPUT_Pathway + "/" + "InsertSize_" + Sample_name +
              " REFERENCE_SEQUENCE= " + Reference_genome)

def Edge_call2(Reference_genome, ptt, rnt, R1_file, R2_file, OUTPUT_PATH, M, m, t,w,i,n,c):
    os.system("/home/kaihami/EDGE_pro_v1.3.1/edge.pl -g " + Reference_genome +
              " -p "+ ptt +
              " -r " + rnt +
              " -u " + R1_file +
              " -v " + R2_file +
              " -M " + M +
              " -m " + m +
              " -t " + t +
              " -w " + w +
              " -i " + i +
              " -n " + n +
              " -c " + c +
              " -o " + OUTPUT_PATH)

def MakeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

path = os.getcwd()

sequencing_type = args.type

Trim = args.Trim
ptt = args.ptt
rnt = args.rnt
genome = args.genome
minimum = args.minimum
maximum = args.maximum
threads = args.threads
window = args.w
i = args.i
c = args.c
n = args.n

project = args.Project
#make project directory
project_dir = os.path.join(path, project) #/usr/path/project

MakeDir(project_dir)

if len(Trim) >1:
    Trim_dir = os.path.join(project_dir, "trimmed_samples")
    MakeDir(Trim_dir) #Create a trimmed samples dir

edge_pro_dir = os.path.join(project_dir, "EDGE-PRO")
MakeDir(edge_pro_dir) #/path/project/EDGE-PRO

Type = args.type

Picard = args.Picard

samples = Samples(args, Type)
log = []
for sample in samples: #only paired-end

    sample_name, read_1, read_2 = sample[0], sample[1], sample[2]
    print sample, sample_name, read_1, read_2

    if len(Trim) >1:
        trim_r1 = "trimmed_"+sample_name+"_R1.fastq"
        r_1 = os.path.join(Trim_dir, trim_r1)

        trim_r2 = "trimmed_"+sample_name+"_R2.fastq"
        r_2 = os.path.join(Trim_dir, trim_r2)

        Trimm_fastq(read_1, sample_name, r_1, Trim)
        Trimm_fastq(read_2, sample_name, r_2, Trim)

        edge_pro_output = os.path.join(edge_pro_dir, sample_name) #/path/project/EDGE-PRO/sample_name

        edge_pro_output_final = os.path.join(edge_pro_output, sample_name)

        MakeDir(edge_pro_output)

        print ""
        print genome, ptt, rnt, r_1, r_2, edge_pro_output_final, maximum, minimum, threads, window, i, n,c
        print ""
        Edge_call2(genome, ptt, rnt, r_1, r_2, edge_pro_output_final, maximum, minimum, threads, window, i, n,c) #ok por enquanto

        if Picard == "yes" or Picard == "y":
            Picard_path = os.path.join(project_dir, "Picard") #path errado... colocar do projeto
            MakeDir(Picard_path)

            aligned_sample = sample_name+".alignments"
            aligned_pathway = os.path.join(edge_pro_output, aligned_sample)

            Picard_sample_path = os.path.join(Picard_path, sample_name)
            MakeDir(Picard_sample_path)

            log.append(["Picard_sample_path", Picard_sample_path])

            Sort_Path = os.path.join(Picard_sample_path, sample_name)
            log.append(["Sort_Path", Sort_Path])
            sorted_file = SortSam(aligned_pathway, Sort_Path)
            log.append(["Sorted_file", sorted_file])
            Picard_metrics(Sort_Path, sorted_file, genome, Sample_name = sample_name)

print ""
print ""
print "_"*40
for line in log:
    print line
#python iBRA.py

#python iBRA.py -g /home/kaihami/Desktop/RNA-Seq/Reference/PA14_reference_genome.fa -p /home/kaihami/Desktop/RNA-Seq/Reference/Pseudomonas.ptt -r /home/kaihami/Desktop/RNA-Seq/Reference/Pseudomonas.rnt -s 46810 46810-1_R1.fastq 46810-1_R2.fastq  --Picard yes -Project test2 -T 1 20

"""
Picard_metrics(OUTPUT_Pathway, Sam_sorted_file, Reference_genome, Sample_name = ""):

    os.system("java -jar " + "./CollectInsertSizeMetrics.jar " +
              " HISTOGRAM_FILE= " + OUTPUT_Pathway + "/" + "Hist_" + Sample_name +
              " INPUT= " + Sam_sorted_file +
              " OUTPUT= " + OUTPUT_Pathway + "/" + "InsertSize_" + Sample_name +
              " REFERENCE_SEQUENCE= " + Reference_genome)
                  """