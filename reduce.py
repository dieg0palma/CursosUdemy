# -*- coding: utf-8 -*-
from functools import reduce

#função reduce recebe uma lista e retorna um único valor para ela

def soma(x,y):
	return x+y;

fi = [1,1,2,3,5,8]

soma = reduce(soma, fi);
print(soma);