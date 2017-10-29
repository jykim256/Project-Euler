n = 600851475143


def factor(n):
	for i in range(2,round(n**0.5) + 1):
		if n % i == 0:
			print('factor:',i)
			print('n:',n)
			print('n/i:',n//i,end='\n\n')
			factor(n // i)
	print('DONE')

factor(n)
