import sys

def factorize(num):

	for factor_one in range(2, num):
		if num % factor_one != 0:
			continue
		factor_two = int(num / factor_one)
		return(factor_one, factor_two)
	return (0, 0)


if len(sys.argv) != 2:
	sys.exit(f"Usage: {sys.argv[0]} <filename>")

try:
	with open(sys.argv[1]) as file:
		numbers = file.readlines()

		for num in numbers:
			cast_num = int(num)
			factor_one, factor_two = factorize(cast_num)
			if factor_one == 0:
				print("No factors found.")
				continue
			print("{}={}*{}".format(cast_num, factor_two, factor_one))
except:
	pass
