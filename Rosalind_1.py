__author__ = 'kaihami'
from Bio import Entrez

Entrez.email ="kaihami@gmail.com"

handle = Entrez.esearch(db = "nucleotide", term = "Cerithidea[organism] and 2000/03/18:2009/11/22[MDAT]")
record = Entrez.read(handle)
record["Count"]