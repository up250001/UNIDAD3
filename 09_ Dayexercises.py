age = int(input(f'Enter your age: '))
if age >= 19:
    print(f'You are old enough to drive')
else:
    print(f'You need {19-age} years to drive')

yourAge = int(input("Enter your age: "))
myAge = 19

if myAge > yourAge:
    print(f"I'm {myAge-yourAge} older than you")
elif myAge < yourAge:
    print(f"You're {yourAge-myAge} older than me")
else:
    print(f'We are of the same age ')

n1 = int(input(f"Enter number 1: "))
n2 = int(input(f"Enter number 2: "))

if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 < n2:
    print(f"{n2} is greater than {n1}")
else:
    print(f'The numbers are equal')


score = int(input("Enter your score: "))

if score < 50:
    print(f"Your grade is F")
elif score <= 59 and score >= 50:
    print(f"Your grade is D")
elif score <= 69 and score >= 60:
    print(f"Your grade is C")
elif score <= 89 and score >= 70:
    print(f"Your grade is B")
elif score <= 100 and score >= 90:
    print(f"Your grade is A")
else:
    print(f"Score no valid")


month = input("Enter the current month: ").upper()

if month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
    print(f"The current season is Autumn")

elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
    print(f"The current season is Winter")

elif month == "MARCH" or month == "APRIL" or month == "MAY":
    print(f"The current season is Spring")

elif month == "JUNE" or month == "JULY" or month == "AUGUST":
    print(f"The current season is Summer")

else:
    print(f"Invalid Data")


fruits = ['peach', 'orange', 'mango', 'lemon']
newFruit = input("Enter a fruit: ").lower()

if newFruit in fruits:
    print(f"The {newFruit} it's already in the list: ")
else:
    print(f"Adding the {newFruit}...")
    fruits.append(newFruit)
print(fruits)



person = {
    'first_name': 'Guillermo',
    'last_name': 'Alvarez',
    'age': 19,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'vallarta Street',
        'zipcode': '20196'
    }
}


if 'skills' in person.keys():
    mid = int(len(person['skills'])/2)
    print(person['skills'][mid])
else:
    print(f"'skills' is not on the person")

if 'skills' in person.keys():
    if "Python" in person['skills']:
        print(f"Python is a skill in the diccionary")
    else:
        print(f"Python is not a skill in the diccionary")
else:
    print(f"'skills' is not on the person")


fronDev = ['JavaScript','React']
backDev = ['Node','Python','MongoDB']
fullStack = ['React', 'Node', 'MongoDB']

if person['skills'] == fronDev:
    print(f"He's a front-end developer")
elif person['skills'] == backDev:
    print(f"He's a back-end developer")
elif person['skills'] == fullStack:
    print(f"He's a a fullstack developer")
else:
    print(f"unknown title")



if person['is_marred']:
    status = "He's married"
else:
    status = "He's not married"

print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. {status} ")

