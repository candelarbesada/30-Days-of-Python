# Day 8

dog = {}
dog['name'] = 'Coco'
dog['breed'] = 'Puddle'
dog['legs'] = 4
dog['age'] = 9

student = {
    'first_name': 'Candela',
    'last_name': 'Rodriguez',
    'gender': 'F',
    'age': 23,
    'marital_status': 'Single',
    'skills': ['Python', 'AI', 'Data', 'C', 'Java'],
    'country': 'Spain',
    'city': 'Pontevedra',
    'address': '12th Street'
}

print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('LLMs')
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())
del student['skills']
print(student)
del dog