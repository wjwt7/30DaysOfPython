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

#Exercise level 2
#1
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.union(B))
print(B.union(A))
#6
print(A.symmetric_difference(B))
#7
del A
del B

#Exercise level 3
#1
age_set = set(age)
length_age_set = len(age_set)
length_age = len(age)
if length_age_set == length_age:
    print("The lengths are equal")
elif length_age_set > length_age:
    print("The length of the set is greater than the length of the list")
else:
    print("The length of the list is greater than the length of the set")
#2
#Explanation of the difference between data types
'''
String: sequence of characters used to represent text
List: ordered collection of items that can be of different data types
Tuple: ordered collection of items that can be of different data types, but is immutable
Set: unordered collection of unique items
'''
#3
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(unique_words)
