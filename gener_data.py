import random
import sys


def begin_values():
    keys = []
    values = []
    iterator = 0
    return(keys, values, iterator)


def value_range():
    min_v = float(sys.argv[1])
    max_v = float(sys.argv[2])
    return(min_v, max_v)


def write_data(keys, values):
    with open('sample_data.txt', 'w') as data_file:
        data_file.write(str(dict(zip(keys, values))))
    print('OK')


def decision(iterator, keys, values, min_value, max_value):
    while iterator <= int(sys.argv[3]):
        keys.append(iterator)
        iterator += 1
        if sys.argv[4] == 'r':
            values.append(round(random.uniform(min_value, max_value)))
        elif sys. argv[4] == 'n':
            values.append(random.uniform(min_value, max_value))
        else:
            print('Example: python3 gener_data.py 1 7 15 r')
            sys.exit()
    return(keys, values)


def main():
    try:
        keys, values, iterator = begin_values()
        min_value, max_value = value_range()
        keys, values = decision(iterator, keys, values, min_value, max_value)
        write_data(keys, values)
    except (IndexError, ValueError) as e:
        print(e)
        print('Example: python3 gener_data.py 1 7 15 r')


main()
