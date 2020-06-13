import random


MAX_RAND = 999999
N_LABELS = 10000

def main():
	for i in range(N_LABELS):
		rand_value = random.randint(0, MAX_RAND)
		rand_part = pad(rand_value, 6)
		unique_part = pad(i, 4)
		print(rand_part + unique_part)


def pad(number, goal_length):
	number_string = str(number)
	while len(number_string) < goal_length:
		number_string = '0' + number_string
	return number_string

if __name__ == '__main__':
	main()