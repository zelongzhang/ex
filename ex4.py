def print_triangular_numbers(num):
	for n in range(1,num+1):
		print(n,'		',int(n*(n+1)/2))


def num_digits(n):
	count=0
	while n!=0:
		count = count+1
		n=abs(n//10)
	if count==0:
		return count+1
	else:
		return count



while True:
	print_triangular_numbers(int(input('Enter how many triangular numbers to be printed\n')))
	print(num_digits(int(input('Enter a number for its digits to be counted\n'))))
