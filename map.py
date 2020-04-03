# -*- coding: utf-8 -*-

#função map servirá para pegar uma função e aplicar a todos os elementos de determinada lista

def dobra(x):
	return x*2;

valor = [1,2,3,4,5,6,7,8,9,10];

dobro = map(dobra, valor);

dobro = list(dobro);
print(dobro);

"""
É possivel também fazer a impressão dos dados com um laço

for d in dobro:
	print (d);
"""