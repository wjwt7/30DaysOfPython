#Level 1
#1
empty_list = []
#2
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
print(fruits)
#3
length = len(fruits)
print(length)
#4
first_fruit = fruits[0]
print(first_fruit)
middle_fruit = fruits[length // 2]
print(middle_fruit)
last_fruit = fruits[-1]
print(last_fruit)

#5
mixed_data_types = ['Wilson', 20, 1.75, False, 'Canada']
print(mixed_data_types)

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
first_company = it_companies[0]
print(first_company)
middle_company = it_companies[len(it_companies) // 2]
print(middle_company)
last_company = it_companies[-1]
print(last_company)
#10
it_companies[0] = 'Meta'
print(it_companies)
#11
it_companies.append('Twitter')
print(it_companies)
#12
it_companies.insert(3, 'Netflix')
print(it_companies)
#13
upper_case_companies = [company.upper() for company in it_companies]
print(upper_case_companies)
#14
joined_companies = '#; '.join(it_companies)
print(joined_companies)
#15
netflix_exist = 'Netflix' in it_companies
print(netflix_exist)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
sliced_first_three = it_companies[3:]
print(sliced_first_three)
#19
sliced_last_three = it_companies[:-3]
print(sliced_last_three)
#20
sliced_middle_companies = it_companies[3:6]
print(sliced_middle_companies)
#21
remove_first_company = it_companies.pop(0)
print(remove_first_company)
#22
remove_middle_company = it_companies.pop(len(it_companies) // 2)
print(remove_middle_company)
#23
remove_last_company = it_companies.pop(-1)
print(remove_last_company)
#24
remove_all_companies = it_companies.clear()
print(remove_all_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)
#27
full_stack = joined_list.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)