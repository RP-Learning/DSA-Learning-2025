#Asks for your name and birth year
#
#Calculates your current age
#
#Prints:
#"Hello Alice, you are 20 years old in 2025!"

name = input("What is your name : ")
birth_year = int(input("What is your birth year : "))   #input is always String by default, if your input is a number use int()
current_year = 2025
print("Hello",name, ", you are ",current_year - birth_year, "years old in ", current_year)