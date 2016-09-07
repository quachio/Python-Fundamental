def draw_stars():
	# x = [4, 6, 1, 3, 7, 25]
	x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
	for i in x:
		stars = ''

		if(str(i).isdigit()):
			for star in range(0, i):
				stars = stars + '*'
		else:
			for star in range(0, len(i)):
				stars = stars + str(i[0]).lower()

		print(stars)


draw_stars()
