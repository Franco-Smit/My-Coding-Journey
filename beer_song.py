import time
word = 'bottles'

#Uncomment the others comments if you're unable to sing at
#extremely high speeds.

for beer_num in range(99, 0, -1):
	print(beer_num, word, "of beer on the wall.")
#	time.sleep(2)
	print(beer_num, word, "of beer.")
#	time.sleep(2)
	print("Take one down")
#	time.sleep(2)
	print("Pass it around")
#	time.sleep(2)

	if beer_num == 1:
		print("No more bottles of beer on the wall.")
	else:
		new_num = beer_num - 1
		if new_num == 1:
			word = "bottle"
	print("Now you have", new_num, word, "of beer on the wall.")
#	time.sleep(2)
print()