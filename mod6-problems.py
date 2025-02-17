#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers.
#Print the resulting sum.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for even in numbers:
    if even % 2 == 0:
        sum += even
print("The Sum is: ", sum)

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list,
#and then print the count.
words = ["Olympic", "College", "Olympic", "Rangers", "Olympic", "Peninsula"]
counter = 0
for word in words:
    if word == "Olympic":
        counter += 1
print("The word \"Olympic\" is used", counter, "time(s)")

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters.
#Print the resulting filtered list.
characters = ["Hi", "Bye", "Go", "Stop", "Yes", "No"]
three = []
for character in characters:
    if len(character) <= 2:
        continue
    else:
       three.append(character)
print("The words with 3 or more characters are:", three)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative,
#then print both counts.
posnegnumbers = [8, 22, -4, -40, 3, -8, 15, 32]
pos_count = 0
neg_count = 0
for posnegnumber in posnegnumbers:
    if posnegnumber >= 1:
        pos_count += 1
    else:
        neg_count += 1
print("Postive Number Count: ", pos_count)
print("Negative Number Count: ", neg_count)

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element
#in the original list. Print the new list.
square_numbers = []
for number in numbers:
    square_numbers.append(number * number)
print(square_numbers)
