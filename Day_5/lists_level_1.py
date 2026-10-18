# Day 5

lst = []
lst_2 = ['Hello', 1, 3.14, 'Python', 190, 'Bye']
print(len(lst_2))
print(f"First item: {lst_2[0]} | Middle item: {lst_2[len(lst_2) // 2]} | Last item: {lst_2[-1]}")

mixed_data_types = ['Tony', 38, 1.83, 'Married', 'Manhattan']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(f"First company: {it_companies[0]} | Middle company: {it_companies[len(it_companies) // 2]} | Last company: {it_companies[-1]}")
it_companies[0] = 'FaceBook'
print(it_companies)
it_companies.insert((len(it_companies) // 2), 'Meta')
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
print('#; '.join(it_companies))
print('IBM' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[::])
print(it_companies[len(it_companies) // 2: (len(it_companies) // 2) + 2])
print(it_companies)
del it_companies[0]
print(it_companies)
del it_companies[len(it_companies) // 2 : (len(it_companies) // 2) + 2]
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)
full_stack = joined_list.copy()
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)