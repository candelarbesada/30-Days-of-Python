# Day 9 - Level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person.keys():
    print(f'Middle skill: {person['skills'][len(person['skills'])//2]}')
    if 'Python' in person['skills']:
        print('Python is in skills')
    else:
        print('Python is not in skills')
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        if len(person['skills']) == 2:
            print('He is a front end developer')
        else:
            print('He is a fullstack developer')
    else:
        print('He is a back end developer')

if person['is_married'] is True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
