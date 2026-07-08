string1 = ['Thirty', 'Days', 'Of', 'Python']
result1 = ' '.join(string1)
print(result1)

string2 = ['Coding', 'For', 'All']
result2 = ' '.join(string2)
print(result2)

company = "Coding For All"
print(company)
print(len(company))
upper_case = company.upper()
print(upper_case)
lower_case = company.lower()
print(lower_case)
capitalized_case = company.capitalize()
print(capitalized_case)
title_case = company.title()
print(title_case)
swap_case = company.swapcase()
print(swap_case)
first_word = company[0:6]
print(first_word)
find_index = company.find('Coding')
print(find_index)
replace_string = company.replace('Coding', 'Python')
print(replace_string)
replace_all_string = company.replace('Coding For All', 'Python For Everyone')
print(replace_all_string)
split_string = company.split()
print(split_string)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(', ')
print(split_companies)

character_index0 = company[0]
print(character_index0)
last_index = company[-1]
print(last_index)
index10 = company[10]
print(index10)
pfe = 'Python For Everyone'
cfa = 'Coding For All'
first_occurence_c = cfa.index('C')
print(first_occurence_c)
first_occurence_f = cfa.index('F')
print(first_occurence_f)
cfap = 'Coding For All People'
last_occurence_l = cfap.rindex('l')
print(last_occurence_l)
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurence_because = sentence.index('because')
print(first_occurence_because)
last_occurence_because = sentence.rindex('because')
print(last_occurence_because)
slice_sentence = sentence[31:54]
print(slice_sentence)
if 'Coding' in company:
    print('Coding is present in the string')
if 'coding' not in company:
    print('coding is not present in the string')
company_space = '   Coding For All   '
stripped_company = company_space.strip()
print(stripped_company)
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
python_library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_library = '# '.join(python_library)
print(joined_library)
paragraph = 'I am enjoying this challenge. \nI just wonder what is next.'
print(paragraph)
table = 'Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(table)
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
