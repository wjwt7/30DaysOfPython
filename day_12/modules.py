#Exercise level 1
import random
import string

#1
def generate_random_user_id(length: int = 6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

#2
def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    alphabet = string.ascii_letters + string.digits
    for _ in range(num_ids):
        user_id = ''.join(random.choice(alphabet) for _ in range(num_characters))
        print(user_id)

#3
def rgb_color_gen():
    return f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'

#Exercise level 2
#1
def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        colors.append(color)
    return colors
#2
def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
        colors.append(color)
    return colors
#3
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Invalid color type. Choose 'hexa' or 'rgb'.")

