# -*- coding: utf-8 -*-

#função zip

num = [1,2,3,4,5];
bichos = ["gato", "foca", "lince", "urso", "lobo"];
subordem = ["feliformia", "não se aplica", "feliformia", "caniformia", "caniformia"]; 
for numero, nome, tipo in zip(num,bichos,subordem):
	print("Nº", "Nome", "SubOrdem");
	print(numero, nome, tipo);
	print("                      ")