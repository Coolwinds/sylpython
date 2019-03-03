#! /usr/bin/python3
import sys

output_dict = {}

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        def handle_data(arg):
            list_arg = arg.split(':')
            output_dict[list_arg[0]] = list_arg[1]
            return output_dict
        handle_data(arg)

    for key in output_dict:
        print('ID:'+ str(key), 'Name:' + output_dict[key])
