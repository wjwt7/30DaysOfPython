# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Exercise level 1
#1
it_companies_length = len(it_companies)
#2
it_companies.add('Twitter')
#3
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])
#4
it_companies.remove('IBM')
#5
#difference between remove and discard is that remove will raise an error if the item does not exist in the set, while discard will not raise an error
