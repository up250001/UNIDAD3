first_name = 'Guillermo'     
last_name = 'Alvarez' 
full_name = 'Guillermo Alvarez Cardenas'      
country = 'Mexico'         
city='Aguascalientes'            
age = 19    
year = 2025
is_married = False            



print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type (age))
print(type(year))
print(type(is_married))



print(len(first_name))
print(len(last_name))

num_one=5
num_two=4
variable_total=(num_one + num_two)
variable_diff=(num_one - num_two)
viariable_product=(num_one*num_two)
variable_division=(num_one/num_two)
variable_remainder=(num_two % num_one)
variable_exp=(num_one**num_two)
variable_floor_division=(num_one//num_two)
area_circle=print((3.1416*30*30))

radio_of_circle=float(input('ingrese la medida del radio'))
area_of_circle=(radio_of_circle*radio_of_circle*3.1416)
print(area_of_circle)

circunferencia_circulo=float(2*radio_of_circle*3.1416)
print(circunferencia_circulo)

nombre=input('ingrese su nombre')
apellido=input('ingrese su apellido')
pais=input('ingrese su paais')
edad=input('ingrese su edad')

first_name, last_name, country, age, is_married = 'Guillermo', 'Alvarez', 'Mexico', 19, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)