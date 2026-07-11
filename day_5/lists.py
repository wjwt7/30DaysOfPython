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

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#1
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(min_age)
print(max_age)
#2
ages.append(min_age)
ages.append(max_age)
#3
median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2 
print(median_age)
#4
average_age = sum(ages) / len(ages)
print(average_age)
#5
range_of_ages = max_age - min_age
print(range_of_ages)
#6
compare_min_average = abs(min_age - average_age)
compare_max_average = abs(max_age - average_age)
print(compare_min_average)
print(compare_max_average)
#7
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle_country = countries[len(countries) // 2]
print(middle_country)
len(countries)
print(len(countries))
print('Since it is an odd number of countries, the first half will have 1 more country than the second half.')
first_half_countries = countries[:len(countries) // 2 + 1]
print(first_half_countries)
second_half_countries = countries[len(countries) // 2 + 1:]
print(second_half_countries)
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = countries2
print(china)
print(russia)
print(usa)
print(scandic_countries)