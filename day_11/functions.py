#exercise level 1
#1
def add_two_numbers(num1, num2):
    return num1 + num2
#2
def area_of_circle(radius):
    pi = 3.14
    return pi * radius ** 2
#3
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise ValueError("All arguments must be numbers.")
    return total
#4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#5
def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        raise ValueError("Invalid month name.")
#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for vertical lines.")
    return (y2 - y1) / (x2 - x1)
#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
#8
def print_list(lst):
    for item in lst:
        print(item)
#9
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst
#10
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.capitalize())
    return capitalized_lst
#11
def add_item(lst, item):
    lst.append(item)
    return lst
#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
#13
def sum_of_numbers(num):
    for i in range(num + 1):
        total_sum += i
    return total_sum
#14
def sum_of_odds(num):
    odd_sum = 0
    for i in range(sum + 1):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum
#15
def sum_of_evens(num):
    even_sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even_sum += i
    return even_sum

#Exercise level 2
#1
def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
#2
def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
#3
def is_empty(param):
    return len(param) == 0
#4
def calculate_mean(*args):
    total_sum = 0
    count = 0
    for num in args:
        if isinstance(num, (int, float)):
            total_sum += num
            count += 1
    if count == 0:
        raise ValueError("At least one number is required to calculate the mean.")
    return total_sum / count
def calculate_median(*args):
    sorted_args = sorted(args)
    n = len(sorted_args)
    if n == 0:
        raise ValueError("At least one number is required to calculate the median.")
    mid = n // 2
    if n % 2 == 0:
        return (sorted_args[mid - 1] + sorted_args[mid]) / 2
    else:
        return sorted_args[mid]
def calculate_mode(*args):
    frequency = {}
    for num in args:
        if isinstance(num, (int, float)):
            frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values(), default=0)
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes
def calculate_range(*args):
    if not args:
        raise ValueError("At least one number is required to calculate the range.")
    return max(args) - min(args)
def calculate_variance(*args):
    mean = calculate_mean(*args)
    variance = sum((num - mean) ** 2 for num in args) / len(args)
    return variance
def calculate_std(*args):
    variance = calculate_variance(*args)
    return variance ** 0.5
#5
def greet(name="Guest"):
    print(f"Hello, {name}!")
#6
def show_args(**args):
    formatted_args = ', '.join(f"{key}: {value}" for key, value in args.items())
    print(f"Received: {formatted_args}")