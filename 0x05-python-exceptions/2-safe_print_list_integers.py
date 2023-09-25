#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            for item in my_list[:x]:
                if isinstance(item, int):
                    print("{:d}".format(item), end="")
                    count += 1
            print()
        except (ValueError, TypeError):
            pass
        return count

    print()
    return count
