# -*- coding: utf-8 -*-

#função filter servirá para pegar uma dada condição, a ser populada em outra lista

num = [1,2,3,4,5,6,7,8,9,10];

#O que se busca aqui é retornar os números pares:

def pares(i):
	if i % 2 == 0:
		return i

numPar = filter(pares, num);
print(list(numPar));