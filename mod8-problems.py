'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''

file1 = open("gardening_tips.txt", "w")
file1.write("Water your plants regularly\n")
file1.write("Give your plants sunlight\n")
file1.write("Must sure the soil is healthy\n")

with open("gardening_tips.txt", "r") as file1:
    for line in file1:
        print(line)
file1.close()

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

with open("hiking_log.txt", "a") as file2:
    while True:
        hike = input("Hike Name (Press 0 to Exit): ")
        if hike == "0":
            break
        miles = input("Miles (Press 0 to Exit): ")
        file2.write(hike + "\t" + miles + "\n")
file2.close()

log = {}
with open("hiking_log.txt", "r") as file2:
    for line in file2:
        stripped_line = line.strip()
        key, val = stripped_line.split("\t")
        log[key] = val

print(log)

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''



'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
file4 = open("poll.txt", "w")
file4.write("yea,nay,nay,nay,yea,yea,yea,nay,yea,nay,nay,yea,yea,nay,yea,nay,yea")
