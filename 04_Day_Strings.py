a = 'Thirty'
b = 'Days'
c = 'of'
d = 'Python'
e = ''
print(a+e+b+e+c+e+d)#1

f = "Coding"
g = 'For'
h = 'All'
company = f+e+g+e+h#2&3
print(company)#4
print(len(company))#5
print(company.upper)#6
print(company.lower)#7
print(company.capitalize)#8
print(company.title)#8
print(company.swapcase)#8
print(company[0:5])#9
print("coding" in company)#10
print(company.find('Coding'))#10
print(company.index('Coding'))#10
print(company.replace('Coding','Python'))#11
word = 'Python for Everyone'
print(word.replace('Everyone','All'))#12
print(company.replace('Python','Coding'))
print(company.split( ))#13
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))#14
print(company[0])#15
print(company[-1])#16
print(company[10])#17

print(item[0] for item in word)#18
print(item[0] for item in company)#19
print(company.index('C'))#20
print(company.index('F'))#21
print("Coding For All People".rfind("l"))#22
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))#23
print(sentence.rindex('because'))#24
phrase = "because because because"
print(sentence.replace(phrase, ""))#25 & 27
print(sentence.find('because'))#26
print(sentence.startswith('Coding'))#28
print(sentence.endswith("Coding"))#29
print('   Coding For All      '.strip())#30
print(f'is 30DaysofPython an identifier? {'30DaysOfPython'.isidentifier}')#31
print('thirty_days_of_python'.isidentifier)#31
print('#'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))#32
print('I am enjoying this challenge.\nI just wonder what is next.')#33
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')#34
#35
radius = 10
area = 3.14 * radius ** 2
print('The area of circle with a radius %d is %.2f meters square.' %(radius, area))
#36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
#bonus
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')


