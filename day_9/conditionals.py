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

#Exercise level 2
#1
score = int(input("Enter your score: "))
if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")

#2
month = input("Enter the month: ").lower()
if month in ["september", "october", "november"]:
    print("The season is Autumn.")
elif month in ["december", "january", "february"]:
    print("The season is Winter.")
elif month in ["march", "april", "may"]:
    print("The season is Spring.")
else:
    print("The season is Summer.")

#3
fruits = ["banana", "orange", "mango", "lemon"]
new_fruit = input("Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print(fruits)

#Exercise level 3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    middle_skill = person['skills'][len(person['skills']) // 2]
    print(f"The middle skill is: {middle_skill}")
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    if set(skill.lower() for skill in person['skills']) == {'javascript', 'react'}:
        print('He is a front end developer.')
    if set(skill.lower() for skill in person['skills']) == {'node', 'python', 'mongodb'}:
        print('He is a backend developer.')
    if set(skill.lower() for skill in person['skills']) == {'react', 'node', 'mongodb'}:
        print('He is a fullstack developer.')
    else:
        print('Unknown title.')

