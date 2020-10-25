# Egyptian Algorithm
import math

def egyptianFraction(nr, dr):

	print("Єгипетський Дріб представлений як {0}/{1} є: ".format(nr, dr), end="\n")
	ef = []
	while nr != 0:
		x = math.ceil(dr / nr)
		ef.append(x)
		nr = x * nr - dr
		dr = dr * x

	for i in range(len(ef)):
		if i != len(ef) - 1:
			print(" 1/{0} +" .
					format(ef[i]), end = " ")
		else:
			print(" 1/{0}" .
					format(ef[i]), end = " ")

egyptianFraction(5, 18)