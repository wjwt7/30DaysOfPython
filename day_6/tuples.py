#Exercise 1: Level 1
#1
empty_tuple = ()
#2
brothers = ('Bro', 'bruh', 'brother')
sisters = ('sister', 'shi')
#3
siblings = brothers + sisters
print(siblings)
#4
print(len(siblings))
#5
family_members = siblings + ('Father', 'Mother')
print(family_members)

#Exercise: Level 2
#1
bro1, bro2, bro3, sis1, sis2, father, mother = family_members
print(bro1, bro2, bro3, sis1, sis2, father, mother)
#2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('Milk', 'Meat', 'Butter', 'Yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#4
middle_item = food_stuff_lt[len(food_stuff_lt) // 2]
print(middle_item)
#5
first_three = food_stuff_lt[:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)