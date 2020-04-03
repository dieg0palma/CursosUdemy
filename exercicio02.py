# -*- coding: utf-8 -*-

nota1 = float(input("Informe a primeira nota: "));
nota2 = float(input("Informe a segunda nota: "));

media = (nota1 + nota2) / 2;

print("Sua média final é de ", media);
if (media >= 6):
	print("APROVADO");

else:
	print("REPROVADO");