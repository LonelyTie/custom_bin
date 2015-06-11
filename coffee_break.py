#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import random
import time
from sys import stdout

def main():
	while 42:
		coffee = random.randint(0, 100000)
		if coffee == 42:
			sys.exit("COFFEE TIME!")
		else :

			print "%029s" % bin(coffee)

		time.sleep(0.1)

if __name__ == "__main__":
	main()
