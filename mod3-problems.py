#1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = input("Type a word: ")
word2 = word[0:] + " "
repeat = int(input("How many times do you want that word repeated? "))
print(word2 * repeat)
#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("What is your name? ")
age1 = int(input("What is your age? "))
age2 = age1 + 1
age1 = str(age1)
age2 = str(age2)
print("Hello, " + name + "!, You are " + age1 + " years old. Next year, you will be " + age2 + " years old.")
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Type out a whole sentence: ")
word = input("What word in that sentence do you want to find? ")
print(word in sentence)
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word1 = input("Enter a word: ")
first_index = int(input("Select an index position: "))
last_index = int(input("Select another index position: "))
print(word1[first_index] + word1[last_index])
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
combine1 = input("Enter word #1: ")
combine2 = input("Enter word #2: ")
combine3 = input("Enter word #3: ")
list = [combine1,combine2,combine3]
combine_all = "|".join(list)
print(combine_all)
