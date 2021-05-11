import random
import sys


def begin_values():
    return([], [], 0)


def value_range():
    return(float(sys.argv[1]), float(sys.argv[2]))


def write_data(keys, values):
    with open('sample_data.txt', 'w') as data_file:
        data_file.write(str(dict(zip(keys, values))))
    print('OK')


def help_syntax():
    print('Syntax: gener_data.py [minimum] [maximum] [number of values] [r/n]')
    print('[r] - round values to integer')
    print('[n] - not round values to integer')
    print('Example: python3 gener_data.py 1 7 15 r')


def decision(iterator, keys, values, min_value, max_value):
    while iterator <= int(sys.argv[3]):
        keys.append(iterator)
        iterator += 1
        if sys.argv[4] == 'r':
            values.append(round(random.uniform(min_value, max_value)))
        elif sys. argv[4] == 'n':
            values.append(random.uniform(min_value, max_value))
        else:
            help_syntax()
    return(keys, values)


def main():
    try:
        keys, values, iterator = begin_values()
        min_value, max_value = value_range()
        keys, values = decision(iterator, keys, values, min_value, max_value)
        write_data(keys, values)
    except (IndexError, ValueError) as e:
        print(e)
        help_syntax()


main()
