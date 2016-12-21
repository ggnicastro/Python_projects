'''
Simple program for pseudomonas site web scraping
Using BeautifulSoup and Regular expression (re)
It will write a text file. The first line is the header and the following lines are the results.
You have to have 2 txt files, one with the gene list and the second to save the results.
Created by Kaihami 12/09/2014.
'''

#Import
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import time


#Open file

gene_file_path = "/home/kaihami/Desktop/Python/gene.txt"
# test file gene_file = open('/home/kaihami/Desktop/Python/gene.txt', 'r').read().split('\n')
gene_file = open(gene_file_path, 'r').read().split('\n')

#write first line in file
first_line = "Gene_Number", "Gene_Name", "Mutant_Number", "Entrez",\
			 "Upstream_500bp", "Coding_Sequence", "Downstream_500bp",\
			 "Protein_Sequence", "Operon", "Strand"

appendFile = open('/home/kaihami/Desktop/Python/Web_scrap2.txt', 'a')

before_write = (str(first_line).replace("'",'').replace("[", "").replace("]", "").replace(" ",""))
before_write2 = before_write[1:-1]
appendFile.write(str(before_write2))
appendFile.write('\n')
appendFile.close()
i = 0
print "Please wait..."

All_initial_time = []
All_final_time = []
All_elapsed_time = []
for line in gene_file:
	try:
		initial_time = time.time()
		All_initial_time.append(initial_time)
		url = urlopen('http://www.pseudomonas.com/getAnnotation.do?locusID='+line)
		page = url.read()
		soup = BeautifulSoup(page)

		#Finding gene number
		Locus_tag = soup.find(colspan='1').get_text()
		Locus_tag_formatted = str(Locus_tag).replace(' ', '').replace('\r','').replace('\n','')
		Locus_tag_formatted2 = '=HYPERLINK("http://pseudomonas.com/getAnnotation.do?locusID='\
							   + Locus_tag_formatted + '";"' + Locus_tag_formatted + '")'

		#Gene name
		gene = soup.find_all("td")
		gene_name = str(gene).replace("  ", "")
		gene_list =[]
		x = re.findall('<td class="rightcol">\r\n(.+?)\xc2\xa0\r\n</td>', gene_name)
		gene_list.append(x)
		a = str(gene_list).replace("[", "").replace("]","").replace("'",""). replace(" ","").split(",")
		if len(a) >=2:
			gene_list2 = a[1]
			gene_format = str(gene_list2).replace("'","")
		else:
			gene_format = "-"

		#mutant Available
		NR_mutant = soup.find_all("td", align="left", nowrap="" )
		NR_mutant2 = str(NR_mutant).replace("  ", "").split(",")

		NR_list = []
		for line in NR_mutant2:
			NR_list.append(line)
		NR_list2 = []
		#for child in NR_mutant2:
			#NR_list2.append(child)

		for element in NR_list:
			x = re.findall("<strong>PA14NR</strong>: (.+?)<br>", element)
			if len(x) != 0:
				NR_list2 = "Yes"
				NR_mutant_formatted = NR_mutant_formatted = '=HYPERLINK("http://ausubellab.mgh.harvard.edu/cgi-bin/pa14\
				/search.cgi?submittedForm=SEARCH_ALL_FIELDS&searchType=SEARCH_ALL_FIELDS&allFields=\
				{PA14_number}\
				&btnSearch=Search&radioExactOrContain=EXACT&radioAllOrAny=ALL&radioWholeOrNR=WHOLE&minBitScore=\
				&maxBitScore=&minBitScoreSep=&maxBitScoreSep=";"' + NR_list2 + '")'
				NR_mutant_formatted = NR_mutant_formatted.format(PA14_number = Locus_tag_formatted)
				break
		if len(NR_list2) == 0:
			NR_list2 = "No"
			NR_mutant_formatted = NR_list2
		#Entrez Code
		Entrez = soup.find_all("a")
		Entrez_list =[]
		Entrez2 = str(Entrez).replace("  ", "").split(",")
		for line in Entrez2:
			Entrez_list.append(line)
		Entrez_list2 = []
		for element in Entrez_list:
			if "entrez" in element and not "NC" in element:
				x = re.findall('<a href="(.+?)" target="_blank">', element)
				Entrez_list2.append(x)
		Entrez_html = str(Entrez_list2).replace("[", "").replace("]", "").replace("'","")
		Entrez_id = re.findall("list_uids=(.+?)'", str(Entrez_list2))
		Entrez_id_forma = str(Entrez_id).replace("[","").replace("]","").replace("'","")
		print Entrez_id_forma

		Entrez_link = "=" + "HYPERLINK" + "(" + '"' + Entrez_html + '"' + ";" + '"' + Entrez_id_forma + '"' + ")"
		print Entrez_link
		#Sequence upstream, coding region, downstream and protein sequence.
		sequence_find = soup.find_all("td")
		sequence_str = str(sequence_find).replace("  ", "")
		sequence_list = re.findall('<font face="Courier New, Courier, monospace">\r\n(.+?)\n', sequence_str)
		try:
			upstream = sequence_list[0].replace("<br>", "").replace("</br>", "").replace("</font>", "").replace("</r>", "")
			coding = sequence_list[1].replace("<br>", "").replace("</br>", "").replace("</font>", "").replace("</r>", "")
			downstream = sequence_list[2].replace("<br>", "").replace("</br>", "").replace("</font>", "").replace("</r>", "")
			protein = sequence_list[3].replace("<br>", "").replace("</br>", "").replace("</font>", "").replace("</r>", "")
		except IndexError:
			protein = "Error"
		#Is operon?
		operon = soup.find_all("td")
		operon2 = str(operon).replace("  ", "").split(",")
		operon_genes = []
		for element in operon2:
			x = re.findall('<span><a href="getAnnotation\.do\?locusID=(.+?)"', element)
			if len(str(x)) >= 4:
				operon_genes.append(x)
		while len(operon_genes) > 1:
			operon_genes.pop(1)
		operon_form = ""
		operon_form = str(operon_genes).replace(",", ";").replace(" ", "")
		if len(operon_form) < 3:
			operon_form = "no"
		find_strand = soup.find_all("td")
		find_strand2 = str(find_strand).replace("  ", "").split(",")
		tmp = []
		for line in find_strand2:
			if "strand" in line:
				tmp.append(line)
		for line in tmp:
			if "+" in line:
				strand = "+"
			else:
				strand = "-"
		#Saving file, Locus number, Product name, COG function, ...
		web_scrap = Locus_tag_formatted2, gene_format,\
					NR_mutant_formatted, Entrez_link,\
					upstream, coding, downstream,\
					protein, operon_form, strand

		appendFile = open('/home/kaihami/Desktop/Python/Web_scrap2.txt', 'a')
		before_write = (str(web_scrap).replace("'",'').replace("[", "").replace("]", "")).replace(" ", "")
		before_write2 = before_write[1:-1]
		appendFile.write(str(before_write2))
		appendFile.write('\n')
		appendFile.close()
		i += 1
		left = len(gene_file) - i
		print (str(left) + " genes left!")

		final_time = time.time()
		All_final_time.append(final_time)
		elapsed_time = final_time - initial_time

		All_elapsed_time.append(elapsed_time)



	except (NameError, TypeError,AttributeError):
		Locus_tag = ''
print "Finish!"
Avg_time = sum(All_elapsed_time)/len(All_elapsed_time)
max_time = max(All_elapsed_time)
print "Average time", "%.3f" %Avg_time
print "Max time", "%.3f" %max_time

