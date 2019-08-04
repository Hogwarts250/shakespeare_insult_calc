import ast, json
import math, random

def shakespearean_insult_gen():
    insults = []
    
    with open("shakespearean_insults.json") as f:
        reader = json.load(f)
        for insult in reader:
            insults.append(insult)
    
    rand_num = random.randint(0, len(insults) - 1)

    return insults[rand_num]

def sqrt_or_insult(user_input):
    try:
        num = float(user_input)

        return(math.sqrt(num))
    
    except ValueError:
        return(shakespearean_insult_gen())

"""
while True:
    user_input = input()

    if user_input == "end":
        break

    print(str(sqrt_or_insult(user_input)) + "\n")
"""