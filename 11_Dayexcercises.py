import math


def add_two_numbers(n1,n2):
    sum = n1 + n2
    return sum


def circle_area(r):
    area = math.pi*r**2
    return area


def add_all_nums(nums):
    sum = 0
    if type(nums) == list:
        for num in nums:
            if type(num) == int:
                sum += num
            else:
                return f"One element in the list is not a number"
    else:
        if type(nums) == int:
                return
        else:
            return f"One element in the list is not a number"
    return sum


def temperatureCF(cel):
    far = (cel * 9/5) + 32
    return far


def check_season(month):
    if month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
        return f"The current season is Autumn"

    elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
        return f"The current season is Winter"

    elif month == "MARCH" or month == "APRIL" or month == "MAY":
        return f"The current season is Spring"

    elif month == "JUNE" or month == "JULY" or month == "AUGUST":
        return f"The current season is Summer"
    else:
        return f"Invalid Data"
    

def calculate_slope(x1,x2,y1,y2):
    slope = (y2+y1)/(x2-x1)
    return slope


def solve_quadratic_eqn(a,b,c):
    if b**2 - 4*a*c >= 0:
        sol1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        sol2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    else:
        return "The ecuation don't have any real solution"
    return sol1, sol2


def print_list(lis):
    if type(lis) == list:
        for i in lis:
            print(i)
    else:
        return f"{lis} is not a list"
    

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  
        reversed_arr.append(arr[i])
    return reversed_arr


capItems = []
def capitalize_list_items(li):
    if type(li) == list:
        for l in li:
            x = l.capitalize()
            capItems.append(x)
    else:
        return f"{li} is not a list"
    return capItems


fruits = ["apple", "banana", "cherry"]
def add_item(li,item):
    li.append(item)
    return li


def remove_item(li,item):
    if item in li:
        li.remove(item)
    else:
        return f"{item} is not in the list"
    return li


def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum


sumOdd = 0
def sum_of_odds(num):
    for i in range(num+1):
        if i % 2 != 0:
            sumOdd += i
    return sumOdd


sumEven = 0
def sum_of_even(num):
    for i in range(num+1):
        if i % 2 == 0:
            sumEven += i
    return sumEven


import math


def evens_and_odds(num):
    numOdd = 0
    numEven = 0
    if num <= 0:
        return "The number isn't positive"
    else:
        for i in range(num+1):
            if i % 2 == 0:
                numEven += 1
            elif i % 2 != 0:
                numOdd += 1
        return numOdd,numEven
    

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


def is_empty(var):
    return not bool(var)


def calculate_mean(num):
    return sum(num) / len(num) if num else None

def calculate_median(num):
    sorted_numbers = sorted(num)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def calculate_mode(num):
    frequency = {}
    max_freq = 0
    modes = []

    for n in num:
        frequency[n] = frequency.get(n, 0) + 1
        max_freq = max(max_freq, frequency[n])

    for n, freq in frequency.items():
        if freq == max_freq:
            modes.append(n)

    return modes if len(modes) > 1 else modes[0]

def calculate_range(num):
    return max(num) - min(num)

def calculate_variance(num):
    mean = calculate_mean(num)
    return sum((x - mean) ** 2 for x in num) / len(num)

def calculate_std(num):
    return math.sqrt(calculate_variance(num))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def check_if_repeat(lst):
    return not len(lst) == len(set(lst))


def all_same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst) if lst else True


def is_valid_variable(name):
    return name.isidentifier()


