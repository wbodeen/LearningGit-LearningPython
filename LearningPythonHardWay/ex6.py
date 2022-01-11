types_of_people = 10 #variable with a string
x = f"There are {types_of_people} types of people." #variable definition as a formatted string with another string inside it

binary = "binary" #a string
do_not = "don't" #string
y = f"Those who know {binary} and those who {do_not}." #string with 2 strings inside

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False #Not actually a string?
joke_evaluation = "Isn't that joke so funny?! {}" #string with an evaluation in the end?

print(joke_evaluation.format(hilarious)) #printing a variable including the additional string. I'm not sure why the {} is there atm.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
