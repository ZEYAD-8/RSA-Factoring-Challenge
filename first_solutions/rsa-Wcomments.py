#!/usr/bin/python3

import sys

def is_prime(num):
	print(f"is_prime: num is [{num}]")
	flag = True
	if num == 2 or num == 3:
		print("is_prime: num is 2 or 3")
		return flag

	for test in range(2, num):
		if num % test == 0:
			print(f"is_prime: num is divisable by {test}")

			flag = False
			break
	
	print(f"is_prime: returning {flag}")
	return flag

def factorize(num):
	for factor_one in range(2, num):
		print(f"factorize: NEW iteration. factor_one is [{factor_one}]")
		if not is_prime(factor_one):
			continue

		print(f"factorize: factor_one [{factor_one}] is prime")

		remainder = num % factor_one
		print(f"factorize: remainder is [{remainder}]")
		if remainder != 0:
			continue

		print(f"factorize: num [{num}] is divisible by factor_one [{factor_one}]")

		factor_two = int(num / factor_one)
		
		if not is_prime(factor_two):
			continue
		
		print(f"factorize: factor_one is [{factor_one}] and factor_two is [{factor_two}]")

		return(factor_one, factor_two)
	print("factorize: next line is\t\treturn (0, 0)")
	return (0, 0)


if len(sys.argv) != 2:
	sys.exit(f"Usage: {sys.argv[0]} <filename>")

try:
	with open(sys.argv[1]) as file:
		number = next(file)

		print(f"main: number is [{number}]")

		cast_num = int(number)
		print(f"main: casted number is [{number}]")

		factor_one, factor_two = factorize(cast_num)
		print(f"main: returned from factorize and the factors are [{factor_one}] and [{factor_two}]")
		if factor_one == 0:
			print("No factors found.")
		else:
			print("{}={}*{}".format(cast_num, factor_two, factor_one))
except:
	pass
