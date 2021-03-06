__author__ = 'kaihami'
#!/usr/bin/python
# encoding: utf-8

from scriptLattes import *
from scriptLattes.geradorDePaginasWeb import *
from scriptLattes.util import compararCadeias

class ArtigoEmPeriodico:
	item = None # dado bruto
	idMembro = None
	qualis = None
	qualissimilar = None

	doi = None
	relevante = None
	autores = None
	titulo = None
	revista = None
	volume = None
	paginas = None
	numero = None
	ano = None
	resto = None
	chave = None
	issn = None

	def __init__(self, idMembro, partesDoItem='', doi='', relevante='', complemento=''):
		self.idMembro = set([])
		self.idMembro.add(idMembro)

		self.doi = ''
		self.relevante = ''
		self.autores = ''
		self.titulo = ''
		self.revista = ''
		self.volume = ''
		self.paginas = ''
		self.numero = ''
		self.ano = ''
		self.issn = ''

		if not partesDoItem=='':
			# partesDoItem[0]: Numero (NAO USADO)
			# partesDoItem[1]: Descricao do artigo (DADO BRUTO)
			self.item = partesDoItem[1]
			self.doi = doi
			self.relevante = relevante

			# Dividir o item na suas partes constituintes (autores e o resto)
			partes = self.item.partition(" . ")

			# Verificar quando há um numero de autores > que 25
			if partes[1]=='': # muitos autores (mais de 25) e o lattes insere etal. termina lista com ;
				partes = self.item.partition(" ; ")
				a = partes[0].partition(", et al.") # remocao do et al.
				a = a[0] + a[2] # estes autores nao estao bem separados pois falta ';'
				b = a.replace(', ','*')
				c = b.replace(' ',' ; ')
				self.autores = c.replace('*',', ')
			else:
				self.autores = partes[0].strip()

			# Processando o resto (tudo menos autores)
			partes = partes[2].rpartition(", ")
			self.ano = partes[2].strip().rstrip(".")

			partes = partes[0].rpartition("p. ")
			if partes[1]=='': # se nao existe paginas
				self.paginas = ''
				partes = partes[2]
			else:
				self.paginas = partes[2].strip()
				partes = partes[0]

			partes = partes.rpartition(", n.")
			if partes[1]=='': # se nao existe numero
				self.numero = ''
				partes = partes[2]
			else:
				self.numero = partes[2].strip().rstrip(",")
				partes = partes[0]

			partes = partes.rpartition(", v. ")
			if partes[1]=='': # se nao existe volume
				self.volume = ''
				partes = partes[2]
			else:
				self.volume = partes[2].strip().rstrip(",")
				partes = partes[0]

			p1 = partes.partition(". ")
			p2 = partes.rpartition(". ")
			if len(p1[0])>len(p2[2]):
				self.titulo = p2[0].strip()
				self.revista = p2[2].strip()
			else:
				self.titulo = p1[0].strip()
				self.revista = p1[2].strip()

			self.chave = self.autores # chave de comparação entre os objetos


		# usando os dados complementares (obtidos do div/cvuri)
		nomePeriodicoParte = complemento.split("nomePeriodico=")

		if (len(nomePeriodicoParte)==2):
			self.revista = nomePeriodicoParte[1].strip()

		complementoPartes = complemento.split("&")
		for parametro in complementoPartes:
			partes = parametro.split("=")
			if len(partes)==2:
				parametroNome  = partes[0].strip()
				parametroValor = partes[1].strip()
				if parametroNome=="issn"   : self.issn   = parametroValor
				if parametroNome=="volume" : self.volume = parametroValor
				if parametroNome=="titulo" : self.titulo = parametroValor
				#if parametroNome=="nomePeriodico": self.revista = parametroValor


	def html(self, listaDeMembros):
		s = self.autores + '. <b>' + self.titulo + '</b>. <font color=#330066>' + self.revista + '</font>. '
		s+= 'v. ' + self.volume + ', '  if not self.volume==''  else ''
		s+= 'n. ' + self.numero + ', '  if not self.numero== '' else ''
		s+= 'p. ' + self.paginas + ', ' if not self.paginas=='' else ''
		s+= 'issn: ' + self.issn + ', ' if not self.issn==''    else ''
		s+= str(self.ano) + '.'         if str(self.ano).isdigit() else '.'

		if not self.doi=='':
			s+= ' <a href="'+self.doi+'" target="_blank" style="PADDING-RIGHT:4px;"><img border=0 src="doi.png"></a>'

		s+= menuHTMLdeBuscaPB(self.titulo)
		s+= formataQualis(self.qualis, self.qualissimilar)
		return s


	def ris(self):
		paginas = self.paginas.split('-')
		if len(paginas)<2:
			p1 = self.paginas
			p2 = ''
		else:
			p1 = paginas[0]
			p2 = paginas[1]
		s = '\n'
		s+= '\nTY  - JOUR'
		s+= '\nAU  - '+self.autores
		s+= '\nTI  - '+self.titulo
		s+= '\nJO  - '+self.revista
		s+= '\nVL  - '+self.volume
		s+= '\nIS  - '+self.numero
		s+= '\nSP  - '+p1
		s+= '\nEP  - '+p2
		s+= '\nPY  - '+str(self.ano)
		s+= '\nL2  - '+self.doi
		s+= '\nL3  - '+self.issn
		s+= '\nER  - '
		return s

	def csv(self, nomeCompleto=""):
		if self.qualis==None:
			self.qualis=''
		if self.qualissimilar==None:
			self.qualissimilar=''
		s  = "artigoEmPeriodico\t"
		if nomeCompleto=="": # tratamento grupal
			s +=  str(self.ano) +"\t"+ self.doi +"\t"+ self.titulo +"\t"+ self.revista +"\t"+ self.autores +"\t"+ self.qualis +"\t"+ self.qualissimilar
		else: # tratamento individual
			s += nomeCompleto +"\t"+ str(self.ano) +"\t" + self.doi +"\t"+ self.titulo +"\t"+ self.revista +"\t"+ self.autores +"\t"+ self.qualis +"\t"+ self.qualissimilar
		return s


	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[ARTIGO EM PERIODICO] \n"
		s += "+ID-MEMBRO   : " + str(self.idMembro) + "\n"
		s += "+RELEVANTE   : " + str(self.relevante) + "\n"
		s += "+DOI         : " + self.doi.encode('utf8','replace') + "\n"
		s += "+AUTORES     : " + self.autores.encode('utf8','replace') + "\n"
		s += "+TITULO      : " + self.titulo.encode('utf8','replace') + "\n"
		s += "+REVISTA     : " + self.revista.encode('utf8','replace') + "\n"
		s += "+PAGINAS     : " + self.paginas.encode('utf8','replace') + "\n"
		s += "+VOLUME      : " + self.volume.encode('utf8','replace') + "\n"
		s += "+NUMERO      : " + self.numero.encode('utf8','replace') + "\n"
		s += "+ANO         : " + str(self.ano) + "\n"
		s += "+ISSN        : " + str(self.issn) + "\n"
		s += "+item        : " + self.item.encode('utf8','replace') + "\n"
		return s