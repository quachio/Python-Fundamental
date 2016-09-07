def print_scores(num):

	print("Score and Grades")

	scores = []
	for i in range(0, num):
		scores.append(int(input(str(i + 1) + ". Enter score: ")))

	for score in scores:
		if 60 <= score <= 69:
			print("Score: {}; Grade is D".format(score))
		elif 70 <= score <= 79:
			print("Score: {}; Grade is C".format(score))
		elif 80 <= score <= 89:
			print("Score: {}; Grade is B".format(score))
		elif 90 <= score <= 100:
			print("Score: {}; Grade is A".format(score))
		else:
			print("Score: {}; Grade is F".format(score))

	print("End of the program. Bye!")

print_scores(10)


