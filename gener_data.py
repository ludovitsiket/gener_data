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


try:
    keys, values, iterator = begin_values()
    min_value, max_value = value_range()
    while iterator <= int(sys.argv[3]):
        keys.append(iterator)
        iterator += 1
        if sys.argv[4] is 'r':
            values.append(round(random.uniform(min_value, max_value)))
        else:
            values.append(random.uniform(min_value, max_value))
    with open('sample_data.txt', 'w') as data_file:
        data_file.write(str(dict(zip(keys, values))))
    print('OK')
except (IndexError, ValueError) as e:
    print(e)
