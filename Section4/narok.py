BRIGHTNESS_THRESHOLD = 153

import simpleimage from SimpleImage

def main():
	for pixel in image:
			average = (pixel.red + pixel.green + pixel.blue) // 3
			# see if this pixel is "sufficiently" green
			if pixel.green >= average * INTENSITY_THRESHOLD:
					# if so, overwrite pixel in original image with corresponding
					# pixel from the back image.
					x = pixel.x
					y = pixel.y
					image.set_pixel(x, y, back.get_pixel(x, y))
			return image



if __name__ == '__main__':
    main()
