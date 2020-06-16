'''
Read all the lines in the file holdup.txt
and print them to the screen
'''

FILE_NAME = 'holdup.txt'

def main():
	with open(FILE_NAME) as f:
		for line in f:
			line = line.strip()
			print(line)

if __name__ == '__main__':
	main()