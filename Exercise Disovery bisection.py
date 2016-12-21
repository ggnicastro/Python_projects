# Problem set for discovery machine for a random number

x = 100
low = 0
high = x
res = 50
guessed = False
print "Please think of a number between 0 and 100!"
while not guessed:
	print "Is your number " + str(res) + "?"
	is_your = raw_input("If the guess is too high press (h). If low press (l). Or right press (c) ")
	if is_your == "c":
		guessed = True
	if is_your == "h":
		high = res
	elif is_your == "l":
		low = res
	if is_your != "c" and is_your != "h" and is_your != "l":
		print "Sorry, I did not understand your input."
	res = (low + high) / 2
print "Game over. Your secret number was: " + str(res)
