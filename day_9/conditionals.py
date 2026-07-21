#Exercise level 1
#1
my_age = int(input("Enter your age: "))
if my_age >= 18:
    print("You are old enough to drive.")
else:
    age_left = 18 - my_age
    print(f"You need {age_left} more years to learn to drive.")

#2
my_age = 20
your_age = int(input("Enter your age: "))
age_difference = abs(my_age - your_age)
if my_age > your_age:
    if age_difference == 1:
        print(f"I am {age_difference} year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
elif my_age < your_age:
    if age_difference == 1:
        print(f"You are {age_difference} year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
else:
    print("We are the same age.")

#3
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}.")
else:
    print(f"{number_one} is smaller than {number_two}.")


