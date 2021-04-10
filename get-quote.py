import random

def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")	#when f is called, the txt file is opend
  quotes = f.readlines()	#readlines reads the lines in the txt file
  f.close()		#the txt file is closed

  last = 13		#defines the last line in the list
  rnd = random.randint(0, last)	#retrieves a random line
  								#between the first and last line

  print(quotes[rnd], end='')

  print(quotes[rnd])

if __name__== "__main__":
  primary()
