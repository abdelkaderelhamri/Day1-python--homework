
## Exercise #1
#<p>Accept two user ages as inputs and give us the difference between them. (The Answer should always be a positive output)</p>
user1_age = int(input("how old are you?"))
user2_age = int(input("how old are you?"))
difference= abs(user1_age-user2_age)
print(difference)


#Exercise2:
#Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.
noun="GMU"
adjective="good"
verb="is"
print(f"{noun} {verb} a {adjective} school")



#Exercise #3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age=int(input("how old are you?"))
if age <18:
   print("kids")
elif 18<age<65:
    print("adult")
else :
    print("Senior")

# Exercise #4
# Take in a number from a user input output the number squared.


age=int(input("how old are you?"))
square=age**2
print(square)

# ​
# Exercise #5
# Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False

word = "panini"     # variable declared

if len(word)>5:
    print("True")
elif len(word)<5:
     print("False")
else:
    print(f"the lenght of {word} is {len(word)}")


#word1="panini"
# word2 = "bulbasaur"
# word3 = "pie"
# word4 = "dolphin"
# word5 = "dog"
#word = "dog"

# putting the code above in a function that can be called when needed.
def variable_len(word):
  if len(word)>5:
    print("True")
  elif len(word)<5:
    print("False")
  else:
    print(f"the lenght of {word} is {len(word)}")
variable_len("dog")