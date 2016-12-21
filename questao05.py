__author__ = 'kaihami'
preco = int(raw_input("Informe o preço da mercadoria. "))
desconto = float(raw_input("Informe o desconto. "))
desconto = desconto/100
preco_novo = preco - (preco*desconto)
desconto_total = preco*desconto
print "Valor com desconto", preco_novo
print "Valor total de desconto", desconto_total

lista1 = [10,10,20,100,30]
lista2 = []
for i in lista1:
   if i not in lista2:
      lista2.append(i)
a = sorted(list(set(lista1)))
a = 1
b = []
b.append(a)