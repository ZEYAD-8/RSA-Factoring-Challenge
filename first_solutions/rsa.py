#!/usr/bin/python3
import sys

def is_prime(num):
	flag = True
	if num == 2 or num == 3:
		return flag

	for test in range(2, num):
		if num % test == 0:
			flag = False
			break
	
	return flag

def factorize(num):
	for factor_one in range(2, num):
		if not is_prime(factor_one):
			continue

		remainder = num % factor_one
		if remainder != 0:
			continue

		factor_two = int(num / factor_one)
		
		if not is_prime(factor_two):
			continue
		

		return(factor_one, factor_two)
	return (0, 0)


if len(sys.argv) != 2:
	sys.exit(f"Usage: {sys.argv[0]} <filename>")

try:
	with open(sys.argv[1]) as file:
		number = next(file)
		cast_num = int(number)

		factor_one, factor_two = factorize(cast_num)
		if factor_one == 0:
			print("No factors found.")
		else:
			print("{}={}*{}".format(cast_num, factor_two, factor_one))
except:
	pass
