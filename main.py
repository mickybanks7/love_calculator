# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_combine = name1 + name2
names = name_combine.lower()

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

add_true = t + r + u + e

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

add_love = l + o + v + e

add_both = int(str(add_true) + str(add_love))

if add_both < 10 or add_both > 90:
  print(f'Your score is {add_both}, you go together like coke and mentors')
elif add_both >= 40 and add_both <= 50:
  print(f'Your score is {add_both}, you are alright together')
else:
  print(f'Your score is {add_both}')


