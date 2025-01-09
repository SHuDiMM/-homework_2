first_string = ['Elon', "Musk", 'Programmer', 'Monitors', 'Variable']
second_string = ['Task', 'Git',  'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_string if len(x)>=5]
second_result = [(x, y) for x in first_string for y in second_string if len(x)==len(y)]
third_result = {x:len(x) for x in first_string+second_string if not len(x)%2}

print(first_result)
print(second_result)
print(third_result)