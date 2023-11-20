#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except TypeError:
        print("Error: BOth inputs should be integers")
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
