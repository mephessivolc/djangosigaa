import random 

def random_number(amount):
    numbers = "1234567890"
    make_number = ""
    for i in range(amount):
        make_number = make_number + random.choice(numbers)
    
    return make_number

def create_random_strings(amount):
    strings = "abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ"
    make_string = ""
    for i in range(amount):
        make_string = make_string + random.choice(strings)
    
    return make_string