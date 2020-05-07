
from simpleimage import SimpleImage


BRIGHTNESS_THRESHOLD = 153


DEFAULT_FILE = 'images/simba-sq.jpg'


def main():
	# Get file and load image
	filename = get_file()
	image = SimpleImage(filename)

	# Show the original simba
	original_simba = SimpleImage(filename)
	original_simba.show()

	# Show simba with the narok filter
	narok_simba = apply_narok(filename)
	narok_simba.show()


def apply_narok(filename):
	image = SimpleImage(filename)
	for pixel in image:
		average = (pixel.red + pixel.green + pixel.blue) // 3
		# see if this pixel is "bright"
		if average > BRIGHTNESS_THRESHOLD:
				# if so, make pixel greyscale
			pixel.red = average
			pixel.green = average
			pixel.blue = average
	return image


def get_file():
	# Read image file path from user, or use the default file
	filename = input('Enter image file (or press enter): ')
	if filename == '':
		filename = DEFAULT_FILE
	return filename


if __name__ == '__main__':
	main()
