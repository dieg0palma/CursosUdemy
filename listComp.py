# -*- coding: utf-8 -*-

#isso pode ser feito, através de uma linha com o list comprehension

#list comprehension

x = [1,2,3,4,5];
quadrado = [i**2 for i in x];
impares = [i for i in x if i%2==1]

"""for i in x:
	quadrado.append(i**2);
"""

print(x);
print(quadrado);
print(impares);