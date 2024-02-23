# Final Project CS 115 Python
# Francine Vo 01253035

# Create functions that does the calculations
def addition(list):
  i = 0
  sum = 0
  while i < len(list):
    sum += list[i]
    i+=1
  return sum

def subtraction(list):
  i = 1
  diff = list[0]
  while i < len(list):
    diff -= list[i]
    i+=1
  return diff

def multiplication(list):
  i = 1
  total = list[0]
  while i < len(list):
    total *= list[i]
    i+=1
  return total

def division(list):
  i = 1
  answer = list[0]
  while i < len(list):
    answer /= list[i]
    i+=1
  return answer

# Create and print header
headerlist = ["|************************|",
              "|**Francine's Calculator*|",
              "|************************|",
              "| 1 |    Addition (+)    |",
              "| 2 |  Subtraction (-)   |",
              "| 3 | Multiplication (*) |",
              "| 4 |    Division (/)    |",
              "|************************|"]
for x in headerlist:
  print(x)

# Create loop so the user can do multiple calculations if needed
looper = 'N'
while True:
  choice = int(input("Please enter your choice (1/2/3/4): "))
  if (choice > 4 or choice <= 0): # Account for invalid inputs
    print("Please pick either 1, 2, 3, or 4.")
    break # Exit loop if invalid input

  amount = int(input("How many numbers will you input? "))
  list = []
  i = 0
  while i < amount:
    num = float(input("Enter number "))
    list.append(num)
    i += 1

# Use if statements to apply functions for appropriate choice number
  if (choice == 1):
    print("The sum is", addition(list))
  if (choice == 2):
    print("The difference is", subtraction(list))
  if (choice == 3):
    print("The total is", multiplication(list))
  if (choice == 4):
    print("The answer is", division(list))

# Prompt the user to decide whether or not they want to calculate again
  word = input("Go again? Y/N ")
  if word.upper() == looper:
    break # Exit loop if the user inputs N or n
