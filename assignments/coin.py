import random


def coin_toss(attempts):
	head = 0
	tail = 0
	for i in range(0, attempts):
		if round(random.random()) == 0:
			head += 1
			print("Attempt #{:<4}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i + 1, head, tail))
		else:
			tail += 1
			print("Attempt #{:<4}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i + 1, head, tail))


coin_toss(10)