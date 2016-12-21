__author__ = 'kaihami'
salario = int(raw_input("Qual o seu salario? "))
aumento = float(raw_input("Qual o aumento? "))
aumento_per = aumento/100
novo_salario = aumento_per*salario + salario
print "seu novo salario é:" , novo_salario