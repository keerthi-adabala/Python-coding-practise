start_choice = input("Let's start Rock- Paper. Scissor game? ")


while(start_choice == "y"):
	user1 = input("Enter your choice R/P/S: ")
	user2 = input("Enter your choice R/P/S: ")
	
	if user1 == "r" and user2 == "p":
		print(user1, "won")
	elif user1 == "p" and user2 == "s":
		print(user1, "won")
	elif user1 == "s" and user2 == "r":
		print(user1, "won")
	
	elif user2 == "r" and user1 == "p":
		print(user2, "won")
	elif user2 == "p" and user1 == "s":
		print(user2, "won")
	elif user2 == "s" and user1 == "r":
		print(user2, "won")
		
	elif user2 == "r" and user1 == "r":
		print("Same input, Game Draw")
	elif user2 == "p" and user1 == "p":
		print("Same input, Game Draw")
	elif user2 == "s" and user1 == "s":
		print("Same input, Game Draw")
		
	else:
		print("Invalid input. please enter values r/p/s.")
		
	choice = input("Want to play another game? ")
	start_choice = choice
		
	
	


