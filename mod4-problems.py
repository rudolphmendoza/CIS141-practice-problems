#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
# Determine the Number of Rows
# 2 possibilities for A
# 2 possibilities for B
# 2 x 2 combinations of A & B = 4
# Create Table Columns
# A B   (A AND B)   (NOT B)     OR (NOT B)      (A AND B) OR (NOT B)
# Enumerate All Possible (A, B) Combinations
# A B   (A AND B)   (NOT B)     OR (NOT B)      (A AND B) OR (NOT B)
# T T
# T F
# F T
# F F
# Fill Each Row with Sub-Expression Results
# A B   (A AND B)   (NOT B)     (A AND B) OR (NOT B)
# T T   T           F           T
# T F   F           T           T
# F T   F           F           F
# F F   F           F           F
#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
sensor = int(input("What number is the sensor threshold at? "))
if sensor <= 7:
    print("Headlights On")
else:
    print("Headlights Off")
#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
money = int(input("How much left is in your account? $"))
print(money <= 99)
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("How old are you? "))
if age >=18:
    print("You are allowed to watch R-rated movies")
elif age >=13:
    print("You are allowed to watch PG-13 movies")
else:
    print("You are only allowed to watch G-rated movies")
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
order = int(input("Order Total: $"))
if order >= 50:
    print("Total Cost is $", order, "+ Free Shipping")
else:
    print("Total Cost with a $5 Shipping Fee is $", order + 5)
