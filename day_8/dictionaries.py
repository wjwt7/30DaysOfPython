#Exercise
#1
dog = {}
#2
dog['name'] = 'Buddy'
dog['breed'] = 'Beagle'
dog['legs'] = 4
dog['age'] = 5
#3
student = {}
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Male'
student['age'] = 20
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'Java', 'C++']
student['country'] = 'USA'
student['city'] = 'New York'
student['address'] = {'street': '123 Main St', 'zip_code': '10001'}
#4
print(len(student))
#5
print(student['skills'])
print(type(student['skills']))
#6
student['skills'].append('JavaScript')
print(student['skills'])
#7
print(student.keys())
#8
print(student.values())
#9
student_items = student.items()
#10
del student['marital_status']
#11
del dog