#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = [chars for chars in my_string if chars not in 'cC']
    new_string = ''.join(filtered_chars)
    return new_string
