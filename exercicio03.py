# -*- coding: utf-8 -*-

from math import sqrt;

a = int(input("Informe o valor de A: "));
b = int(input("Informe o valor de B: "));
c = int(input("Informe o valor de C: "));

delta = (((b*b) -4 ) * a) * c;
raiz = sqrt(delta);

x1 = (-b + raiz) / 2 * a;
x2 = (-b - raiz) / 2 * a;

print("O valor de x¹ é de ", x1);

print("O valor de x² é de ", x2);
