#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


numero = input("Digite numero positivo: ")
for i in range(int(numero)):
	if(i%2!=0):
		print("Numero Impar: " + str(i))


