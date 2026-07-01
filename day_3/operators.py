age = 20
height = 1.74
complex_num = 1 + 2j

#triangle area
base_input = input('Enter base: ')
height_input = input('Enter height: ')
area_of_triangle = 0.5 * float(base_input) * float(height_input)
print('The area of the triangle is: ', area_of_triangle)

#triangle perimeter
side_a_input = input('Enter side a: ')
side_b_input = input('Enter side b: ')
side_c_input = input('Enter side c: ')
perimeter_of_triangle = float(side_a_input) + float(side_b_input) + float(side_c_input)
print('The perimeter of the triangle is: ', perimeter_of_triangle)

#rectangle
length_input = input('Enter length: ')
width_input = input('Enter width: ')
area_of_rectangle = float(length_input) * float(width_input)
perimeter_of_rectangle = 2 * (float(length_input) + float(width_input))

#circle
radius_input = input('Enter radius: ')
area_of_circle = 3.14 * (float(radius_input) ** 2)
circum_of_circle = 2 * 3.14 * float(radius_input)

#slope and intercepts
x = 0  # You can set a value for x or leave it as a variable
y = 2 * x - 2
slope = 2
x_intercept = 1
y_intercept = -2

point1 = (2, 2)
point2 = (6, 10)
slope_between_points = (point2[1] - point1[1]) / (point2[0] - point1[0])
euclidean_distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

#slope comparison
slope == slope_between_points  # True

#which x value gives 0 for y = x^2 + 6x + 9
# Solving x^2 + 6x + 9 = 0
# can rearrange to (x + 3)^2 = 0, which gives x = -3
x_values = [-3]  # The quadratic formula gives x = -3 

#strings
string1 = 'python'
string2 = 'dragon'
string1 == string2  # False
if 'on' in string1 and 'on' in string2:
    print('Both strings contain "on"')  # This will be printed

jargon_sentence = 'I hope this course is not full of jargon.'
if 'jargon' in jargon_sentence:
    print('The word "jargon" is in the sentence.')  # This will be printed

if 'on' not in string1 and 'on' not in string2:
    print('Neither string contains "on"')  # This will not be printed

length_of_python = len(string1)
float_value_python = float(length_of_python)
str_python = str(float_value_python)

#operation checks
#check if number is even in python, use modulus operator, if number % 2 == 0, then it is even, else it is odd

floor_div = 7 // 3  # 2
floor_div == int(2.7)  # True

type('10') == type(10)  # False
int('9.8') == 10 # False, this will raise a ValueError because '9.8' cannot be converted to int directly

#salary user input
hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')
weekly_earnings = float(hours) * float(rate_per_hour)
print('Weekly earnings: ', weekly_earnings)

#year user input
years_lived = input('Enter number of years you have lived: ')
print('You have lived for ', int(years_lived) * 365 * 24 * 60 * 60, ' seconds.')

#display table
print('1\t1\t1\t1\t1')
print('2\t1\t2\t4\t8')
print('3\t1\t3\t9\t27')
print('4\t1\t4\t16\t64')
print('5\t1\t5\t25\t125')
#can also do a for loop but that is later on