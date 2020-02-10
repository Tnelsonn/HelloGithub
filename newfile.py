#three data types

#string

phrase = input("enter string")
print("you said" + phrase)
print(f"you said {phrase}")

someFloat = float(input("Enter a float: "))
print("You entered float: " + str(someFloat))
print(f"You entered float: {someFloat}")

someInt = float(input("enter an int: "))
print("You entered int: " + str(someInt))
print(f"You entered int: {someInt}")

print(f"Do python inline, like this : {someFloat} * {someInt} = {someFloat * someInt}")
