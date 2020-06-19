import json

START = 'tressider'

def main():
	data = json.load(open('adventure.json'))
	play_game(data)

def play_game(data):
	print('Welcome to the Stanford Adventure Game:\n')
	curr_room = START
	while True:
		room_data = data[curr_room]
		print_room_description(room_data)
		move = input('Your move: ')
		curr_room = room_data['moves'][move]

def print_room_description(room_data):
	print('')
	print(room_data['text'])
	print('Your options are:')
	for move_key in room_data['moves']:
		move_target = room_data['moves'][move_key]
		print("'" +move_key + "' to go to " + move_target)

if __name__ == '__main__':
	main()