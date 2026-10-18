# Day 4

single_str = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(single_str)

items = ['Coding', 'For', 'All']
single_str2 = ' '.join(items)
print(single_str2)


company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip('Coding'))
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))

string = 'Python For Everyone'
print(string.replace('Everyone', 'All'))

print(company.split(' '))

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(","))

print(company[0])
print(len(company) - 1)
print(company[10])


print(company.index('C'))
print(company.index('F'))
company_2 = 'Coding For All People'
print(company_2.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
print(sentence.replace('because ', ''))

print(company.startswith('Coding'))
print(company.endswith('coding'))

company_3 = ' Coding For All '
print(company_3.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())


python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki')

print(f'radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is {int(3.14 * (10 ** 2))} meters square.')

print(f'8 + 6 = {8+6}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8 ** 6 = {8**6}')