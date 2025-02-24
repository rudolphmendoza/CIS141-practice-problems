'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
    Test: letter (2), bye (1), by (0)
    Input: string (input)
    Output: integer; number of vowels in string
    Function body: vowels; vowel counter (vowel_counter); for-if statement to count the number of vowels in word; return function to cycle through the whole word
'''
def count_vowels(input):
    vowels = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    vowel_counter = 0
    for characters in input:
        if characters in vowels:
            vowel_counter += 1
    return vowel_counter

print(count_vowels("letter")) # 2
print(count_vowels("bye")) # 1
print(count_vowels("by")) # 0

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
    Test: kayak (True), lemons (False), Kayak (True)
    Input: string (s)
    Output: boolean
    Function body: lowercase s, flip s and save to new variable (flipped_s), and then compare s & flipped_s
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return (lower_s == flipped_s)

print(is_palindrome("lemons")) # False
print(is_palindrome("kayak")) # True
print(is_palindrome("Kayak")) # True

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
    Test: water vs. fire (super effective), fire vs. water (not very effective), electric vs. grass (neutral)
    Input: string (attack, defender)
    Output: boolean
    Function body: define function for attacker and defender; have if statement for water vs fire, fire vs water, electric vs. grass
'''
def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"

print(type_advantage("Water", "Fire"))      # "Super Effective"
print(type_advantage("Fire", "Water"))      # "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # "Neutral"

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
    Test: age 10; age 30 with vehicle; age 30 without vehicle; age 70 with vehicle; age 70 without vehicle
    Input: integer, string (age, vehicle)
    Output: string, boolean
    Function body: determines if age falls within different parameters; if rider has a vehicle or not
'''
def ferry_fare(age, vehicle):
    has_vehicle = vehicle.lower()
    if age <= 18:
        return "Free"
    if age >= 65:
        if has_vehicle == "yes":
            return "$15"
        else:
            return "$5"
    else:
        if has_vehicle == "yes":
            return "$20"
        else:
            return "$10"

print(ferry_fare(10, "no"))     # Free
print(ferry_fare(30, "yes"))    # $20
print(ferry_fare(30, "No"))     # $10
print(ferry_fare(70, "Yes"))    # $15
print(ferry_fare(70, "NO"))     # $5

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
    Test: 50 xp, 150 xp, 250 xp
    Input: integer (experience)
    Output: string
    Function body: determines where experience falls within different parameters
'''

def level_up(experience):
    if experience < 100:
        return "Level 1"
    elif experience < 200:
        return "Level 2"
    else:
        return "Level 3"

print(level_up(50))     # Level 1
print(level_up(150))    # Level 2
print(level_up(250))    # Level 3
