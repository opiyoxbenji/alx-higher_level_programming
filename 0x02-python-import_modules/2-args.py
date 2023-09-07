#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as cmd_args

    arg_count = len(cmd_args) - 1
    arg_desc = "argument" if arg_count == 1 else "arguments"
    delimiter = "." if arg_count == 0 else ":"

    print("{} {}{}". format(arg_count, arg_desc, delimiter))

    for i in range(1, arg_count + 1):
        print("{}: {}".format(i, cmd_args[i]))
