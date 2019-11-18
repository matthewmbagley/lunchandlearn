# This function asks the user for their name and facvorite food
def question():
	# Variable holding a string
	welcome_message = "Welcome to Hallmarklabs' Lunch and Learn!"
	subject = "Let's talk about your favorite food!"

	print(welcome_message)
	print(subject)

	# Asks the user for their questions and assign their respose to variable
	user_name = input("What is your name? ")
	favorite_food = input("What is your favorite food? ")

	# Conditional Logic
	if favorite_food == "Chocolate":
		print("Hey " + user_name + ", we both like Chocolate!")
	else:
		print("Oh, sorry! I don't like " + favorite_food + ", " + user_name)

# Call the function question()
question()
