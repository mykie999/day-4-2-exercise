import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# sel = len(names)

# random_name = random.randint(0,sel - 1)
# payer = random_name[sel]

payer = random.choice(names)

print(f"{payer} will pay the bill.")
