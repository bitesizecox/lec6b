from random import randrange

responses = ["It is certain.", "It is decidedly so.", "Without a doubt!", "Yes, definitely."
			"You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
			"Signs point to yes.", "Reply hazy; try again.", "Ask again later.", "Better not tell you now...",
			"Cannot predict now.", "Concentrate and ask again.", "Ha, don't count on it!", "My reply is no.",
			"My sources say no.", "Outlook not so good...", "Very doubtful."]

# print(len(responses))

def magic8Ball():
	
	question = input("Ask me about your future: ")
	if question[-1] == "?":
		print(responses[randrange(19)])
		play_again = input("Is there anything else you'd like to know? Please respond with yes or no: ").upper()
		if play_again == "YES":
			magic8Ball()
		if play_again == "NO":
			print ("I'm sure you'll seek my wisdom again soon. Goodbye for now.")
		else:
			print("You did not answer as specified so now I'm leaving. Goodbye.")
	else:
		print("Sorry, that's not a valid question...")
		magic8Ball()

	

	# game_over = input("You may respond with yes or no: ")
	# game_over.upper()
	# if game_over == "YES" or "NO":
	# 	if game_over == "NO":
	# 		game = False
	# 	if game_over == "YES":
	# 		game = True

# magic8Ball()

# while True:
#     # main program
#     while True:
#         answer = raw_input('Run again? (y/n): ')
#         if answer in ('y', 'n'):
#             break
#         print 'Invalid input.'
#     if answer == 'y':
#         continue
#     else:
#         print 'Goodbye'
#         break






# question = input("questions: ")
# print(question)
# print(question[-1])
magic8Ball()
# play_again = input("moo yes or no: ").upper()
# if play_again == "YES" or "NO":
# 	if play_again == "NO":
# 		print("butt")
# 	else:
# 		print("monkey")



