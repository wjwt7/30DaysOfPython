# Day 2: 30 Days of python programming
#Level 1
first_name = 'Wilson'  # string
last_name = 'Truong'   # string
full_name = 'Wilson Truong'
country = 'Canada'
city = 'Montreal'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True
height, weight = 1.75, 68.0

#Level 2
type(first_name)  # string
type(last_name)   # string
type(full_name)   # string
type(country)     # string
type(city)        # string
type(age)         # int
type(year)        # int
type(is_married)  # bool
type(is_true)     # bool
type(is_light_on) # bool
type(height)      # float
type(weight)      # float
len(first_name)  # 6
len(last_name)   # 6
len(first_name) == len(last_name)  # True
num_one = 5
num_two = 4
total = num_one + num_two  # 9
diff = num_one - num_two  # 1
product = num_one * num_two  # 20
division = num_one / num_two  # 1.25
remainder = num_one % num_two  # 1
exp = num_one ** num_two  # 625
floor_division = num_one // num_two  # 1
area_of_circle = 3.14 * (30 ** 2)  # 2826.0
circum_of_circle = 2 * 3.14 * 30  # 188.4
user_radius = input('Enter radius: ')
area_of_circle = 3.14 * (float(user_radius) ** 2)
user_first_name, user_last_name, user_country, user_age = input('Enter your first name, last name, country and age separated by commas: ').split(',')

