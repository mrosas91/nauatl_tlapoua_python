#!/usr/bin/env python3
from numeral_to_text import *

def ask():
	numeral = int(input('¿Qué número deseas nombrar?:'))
	print(numeral_to_text(numeral, True))

while 1==1:
	ask()
