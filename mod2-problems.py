# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
num1 = int(input("Give me one number: "))
num2 = int(input("Give me another number: "))
print(num1, " + ", num2, " = ", num1+num2)
print(num1, " - ", num2, " = ", num1-num2)
print(num1, " x ", num2, " = ", num1*num2)
print(num1, " ÷ ", num2, " = ", num1/num2)
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
len1 = int(input("What is the length of the 1st side?: "))
len2 = int(input("What is the length of the 2nd side?: "))
len3 = int(input("What is the length of the 3rd side?: "))
semip = 1/2 * (len1 + len2 + len3)
area = (math.sqrt(semip * (semip - len1) * (semip - len2) * (semip - len3)))
print("The area of this triangle is ", area)
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
stat1 = int(input("Give me the 1st number: "))
stat2 = int(input("Give me the 2nd number: "))
stat3 = int(input("Give me the 3rd number: "))
stat4 = int(input("Give me the 4th number: "))
stat5 = int(input("Give me the 5th number: "))
total = stat1+stat2+stat3+stat4+stat5
print ("The total is ", total)
average = ((stat1 + stat2 + stat3 + stat4 + stat5)/5)
print ("The average is ", average)
minimum = min(stat1, stat2, stat3, stat4, stat5)
print ("The minimum is ", minimum)
maximum = max(stat1, stat2, stat3, stat4, stat5)
print ("The maximum is ", maximum)
range = maximum - minimum
print ("The range is ", range)
