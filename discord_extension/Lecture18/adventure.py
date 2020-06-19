import json

'''
Allows the user to navigate around a (text based) world.
Data comes from adventure.json
'''
START = 'tresidder'

def main():
	data = json.load(open('adventure.json'))
	play_game(data)

def play_game(data):
	print('Welcome to the Stanford Adventure Game:\n')
	# TODO: your code here
	print(data)


if __name__ == '__main__':
	main()