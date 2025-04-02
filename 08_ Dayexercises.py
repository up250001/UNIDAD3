dog = {}

dog = {'name':'Tito',
       'color':'white and brown',
       'breed':'Beagle',
       'legs':4,
       'age':8}

student = {
    'first_name':'Guillermo',
    'last_name':'Alvarez',
    'gender':'Male',
    'age':19,
    'marital_status':'single',
    'skills':['Python','SQL','HTML','CSS','JS'],
    'country':'Mexico',
    'city':'Aguascalientes',
    'addres':{
        'street':'vallarta Street',
        'zipcode':'20196',}}

print(f'The lenght of the student dictionary is {len(student)}')
print(f'The data type of student skills is {type(student["skills"])}')

student['skills'].append('PHP')
print(student['skills'])

keyList = list(student.keys())
print(keyList)

valList = list(student.values())
print(valList)

studentTuple = student.items()
print(studentTuple)

student.pop('gender')
print(student)

del dog
